import logging
import os
from datetime import datetime
import sys
reload(sys)  # Reload does the trick!
from src.models import Locusdbentity, Referencedbentity, Dbentity, Reservedname, \
    LocusReferences, ArchLocuschange, Source, Locusnote, LocusnoteReference
from scripts.loading.database_session import get_session

__author__ = 'sweng66'

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

# CREATED_BY = os.environ['DEFAULT_USER']

def standardize_name(infile, logfile):

    nex_session = get_session()

    name_to_locus_id = dict([(x.systematic_name, x.dbentity_id) for x in nex_session.query(Locusdbentity).all()])
    pmid_to_reference = dict([(x.pmid, x.dbentity_id) for x in nex_session.query(Referencedbentity).all()])
    reference_id_to_pub_status = dict([(x.dbentity_id, x.publication_status) for x in nex_session.query(Referencedbentity).all()])
    gene_to_created_by = dict([(x.display_name, x.created_by) for x in nex_session.query(Reservedname).all()])
    sgd = nex_session.query(Source).filter_by(display_name='SGD').one_or_none()
    source_id = sgd.source_id
    
    locus_id_gene_to_note_id = {}
    for x in nex_session.query(Locusnote).filter_by(note_class='Locus', note_type='Name').all():
        gene = x.note.replace("<b>Name:</b> ", "")
        locus_id_gene_to_note_id[(x.locus_id, gene)] = x.note_id

    # log.info("Fixing...\n") 

    fw = open(logfile, "w")    
    f = open(infile)

    unique_papers = []

    for line in f:
        pieces = line.strip().split("\t")
        if pieces[0] == 'ORF':
            continue
        orf_name = pieces[0]
        gene_name = pieces[1]

        # if gene_name in ['MIY1', 'MCO13', 'COI1', 'CCW22', 'NRE1']:
        #    continue

        created_by = gene_to_created_by.get(gene_name)

        if created_by is None:
            print "The gene name: ", gene_name, " is not in Reservedname table."
            continue

        pmid_4_gene_name = None
        pmid_4_name_desc = None
        if pieces[2]:
            pmid_4_gene_name = int(pieces[2]) 
        name_desc = pieces[3].replace('"', '')
        if pieces[4]:
            pmid_4_name_desc = int(pieces[4])
        # date_standardized = reformat_date(pieces[5])
        date_standardized = pieces[5]

        locus_id = name_to_locus_id[orf_name]       
        if pmid_4_gene_name and pmid_4_gene_name not in pmid_to_reference:
            print "The pmid:", pmid_4_gene_name, " is not in the database."
        if pmid_4_name_desc and pmid_4_name_desc not in pmid_to_reference:
            print "The pmid:", pmid_4_name_desc, " is not in the database."
            
        # 1. update dbentity.display_name = gene_name in the file
        update_dbentity(nex_session, fw, locus_id, gene_name)
       
        # 2. update locusdbentity.gene_name = gene_name in the file 
        # 3. update locusdbentity.name_description = name_description in the file 
        update_locusdbentity(nex_session, fw, locus_id, gene_name, name_desc)

        # 4.1 Delete the old row in LOCUS_REFERENCE table reference_class = 'name_description' 
        delete_locus_reference(nex_session, fw, locus_id, 'name_description')

        # 4.2 Add rows to LOCUS_REFERENCE where reference_class = 'gene_name' and 'name_description'
        insert_locus_reference(nex_session, fw, locus_id, 
                               pmid_to_reference.get(pmid_4_gene_name), 
                               'gene_name', source_id, created_by,
                               date_standardized) 

        if name_desc and pmid_4_name_desc:
            insert_locus_reference(nex_session, fw,locus_id,
                                   pmid_to_reference.get(pmid_4_name_desc),
                                   'name_description', source_id, created_by, 
                                   date_standardized)

        # 5. Update ARCH_LOCUSCHANGE.date_name_standardized = date_standardized in the file
        #    for the given locus_id, with change_type = 'Gene name' and new_value = [NEW GENE NAME] 
        update_arch_locuschange(nex_session, fw, locus_id, gene_name, date_standardized)
            
        # 6. Delete the row from RESERVEDNAME
        delete_reservedname_row(nex_session, fw, gene_name)
    
        # 7. update the papers in the locusnote to point to new papers in LOCUSNOTE_REFERENCE
        note_id = locus_id_gene_to_note_id.get((locus_id, gene_name))
        if note_id is None:
            print "No note for gene_name: ", gene_name
            continue

        delete_old_locusnote_reference(nex_session, fw, note_id, gene_name)

        insert_locusnote_reference(nex_session, fw, note_id, pmid_to_reference.get(pmid_4_gene_name), 
                                   source_id, created_by, date_standardized)
        
        
    # nex_session.rollback()
    nex_session.commit()

    fw.close()
    f.close()


def delete_locus_reference(nex_session, fw, locus_id, reference_class):

    x = nex_session.query(LocusReferences).filter_by(locus_id=locus_id, reference_class=reference_class).one_or_none()
    nex_session.delete(x)

    fw.write("Old locus_reference row for locus_id = " + str(locus_id) + " has been deleted\n")

def delete_reservedname_row(nex_session, fw, gene_name):
    
    x = nex_session.query(Reservedname).filter_by(display_name=gene_name).one_or_none()
    nex_session.delete(x)

    fw.write("The reservedname row for " + gene_name + " has been deleted\n")


def update_arch_locuschange(nex_session, fw, locus_id, gene_name, date_standardized):

    x = nex_session.query(ArchLocuschange).filter_by(dbentity_id=locus_id, change_type='Gene name', new_value=gene_name).one_or_none()
    if x is None:
        return
    x.date_name_standardized = date_standardized
    nex_session.add(x)

    fw.write("The date_name_standardized for dbentity_id = " + str(locus_id) + " and new_value=" + gene_name + " is set to: " + date_standardized + "\n")

def delete_old_locusnote_reference(nex_session, fw, note_id, gene_name):

    x = nex_session.query(LocusnoteReference).filter_by(note_id=note_id).one_or_none()

    if x is None:
        print "No papers for note_id: ", note_id, " and gene: ", gene_name
        return

    nex_session.delete(x)

    fw.write("The old paper for gene = " + gene_name + " and note_id = " + str(note_id) + " has been deleted.\n")


def insert_locusnote_reference(nex_session, fw, note_id, reference_id, source_id, created_by, date_standardized):
    
    if reference_id is None:
        return

    x = LocusnoteReference(note_id = note_id,
                           reference_id = reference_id,
                           source_id = source_id,
                           created_by = created_by,
                           date_created = date_standardized)

    nex_session.add(x)

    fw.write("Insert Locusnote_reference row for note_id = " + str(note_id) + ", reference_id = " + str(reference_id) + ", created_by = " + created_by + ", date_created = " + date_standardized + "\n")


def insert_locus_reference(nex_session, fw, locus_id, reference_id, reference_class, source_id, created_by, date_standardized):
    
    if reference_id is None:
        return

    x = LocusReferences(locus_id = locus_id,
                        reference_id = reference_id,
                        reference_class = reference_class,
                        source_id = source_id,
                        created_by = created_by,
                        date_created = date_standardized)

    nex_session.add(x)

    fw.write("Insert Locus_reference row for locus_id = " + str(locus_id) + ", reference_id = " + str(reference_id) + ", reference_class = " + reference_class + ", created_by = " + created_by + ", date_created = " + date_standardized + "\n")
 

def update_locusdbentity(nex_session, fw, locus_id, gene_name, name_desc):

    x = nex_session.query(Locusdbentity).filter_by(dbentity_id=locus_id).one_or_none()
    if x is None:
        return
    x.gene_name = gene_name
    if name_desc:
        x.name_description = name_desc
    nex_session.add(x)

    fw.write("Update locusdbentity.gene_name for dbentity_id=" + str(locus_id) + " to: " + gene_name + "\n")
    if name_desc:
        fw.write("Update locusdbentity.name_description for dbentity_id=" + str(locus_id) + " to: " + name_desc + "\n")


def update_dbentity(nex_session, fw, locus_id, gene_name):
    
    x = nex_session.query(Dbentity).filter_by(dbentity_id=locus_id).one_or_none()
    if x is None:
        return
    x.display_name = gene_name
    nex_session.add(x)

    fw.write("Update dbentity.display_name for dbentity_id=" + str(locus_id) + " to: " + gene_name + "\n")


def reformat_date(this_date):

    if this_date == "":
        return

    dates = this_date.split("/")
    if len(dates) <3:
        print "BAD DATE:", this_date
        return
    month = dates[0]
    day= dates[1]
    year = dates[2]
    if len(year) == 2 and year.startswith('9'):
        year = "19" + year
    elif len(year) == 2 and (year.startswith('0') or year.startswith('1')):
        year = '20' + year
    elif len(year) == 2:
        print "WRONG YEAR"
        return 
    if len(month) == 1:
        month ="0" + month
    if len(day) == 1:
        day = "0" + day

    return year + "-" + month + "-" + day


if __name__ == '__main__':

    infile = None
    if len(sys.argv) >= 2:
         infile = sys.argv[1]
    else:
        print "Usage:         python standardizeReservedName.py datafile"
        print "Usage example: python standardizeReservedName.py scripts/loading/locus/data/reservedNames2standardize110817.txt"
        exit()
    
    logfile = "scripts/loading/locus/logs/standardizeReservedName.log"
    
    standardize_name(infile, logfile)
                                                  
