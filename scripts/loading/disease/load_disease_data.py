import csv
import os
import logging
from src.models import DBSession, Dbentity, Disease, Diseaseannotation, Diseasesupportingevidence, Eco, Ro, Referencedbentity, Source, Taxonomy
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker, scoped_session
from zope.sqlalchemy import ZopeTransactionExtension
import transaction
import traceback
import sys

'''
    Process a TSV file of disease annotation
    example
        $ source dev_variables.sh && CREATED_BY=STACIA INPUT_FILE_NAME=/Users/kkarra/Dev/SGDBackend-Nex2/scripts/loading/disease/disease_associationSGD1.0.1.txt  python scripts/loading/disease/load_disease_data.py
'''

INPUT_FILE_NAME = os.environ.get('INPUT_FILE_NAME')
NEX2_URI = os.environ.get('NEX2_URI')
CREATED_BY = os.environ.get('CREATED_BY')
ANNOTATION_TYPE = 'manually curated'

logging.basicConfig(level=logging.INFO)

def upload_db(obj, row_num):

    try:
        temp_engine = create_engine(NEX2_URI)
        session_factory = sessionmaker(bind=temp_engine, extension=ZopeTransactionExtension(), expire_on_commit=False)
        db_session = scoped_session(session_factory)
        # see if already exists, if not create
        disease_id = db_session.query(Disease.disease_id).filter(Disease.doid == obj['doid']).one_or_none()[0]
        if disease_id:
            try:
                tax_id = db_session.query(Taxonomy.taxonomy_id).filter(Taxonomy.taxid==obj['taxon']).one_or_none()[0]
                print tax_id
                ref_id = db_session.query(Referencedbentity.dbentity_id).filter(Referencedbentity.pmid == obj['pmid']).one_or_none()[0]
                print ref_id
                ro_id = db_session.query(Ro.ro_id).filter(Ro.display_name == obj['association']).one_or_none()[0]
                print ro_id
                #eco_id = db_session.query(Eco.eco_id).filter(Eco.display_name == obj['evidence_code']).one_or_none()[0]
                #print eco_id
                dbentity_id = db_session.query(Dbentity.dbentity_id).filter(Dbentity.sgdid == obj['sgdid']).one_or_none()[0]
                print dbentity_id
                source_id = db_session.query(Source.source_id).filter(Source.display_name == obj['source']).one_or_none()[0]
                print source_id
            except TypeError:
                logging.error('invalid do id or eco id in row ' + str(row_num) +  ' ' + str(disease_id) + ' ' + str(eco_id))
                return
            new_daf_row = Diseaseannotation(
                dbentity_id=dbentity_id,
                source_id=source_id,
                taxonomy_id=tax_id,
                reference_id=ref_id,
                disease_id=disease_id,
                eco_id=236220,
                annotation_type=ANNOTATION_TYPE,
                association_type=ro_id,
                created_by=CREATED_BY,
                date_assigned = obj['date_assigned']
            )
            db_session.add(new_daf_row)
            transaction.commit()
            db_session.flush()

        logging.info('finished ' + obj['sgdid'] + ', line ' + str(row_num))
    except:
        logging.error('error with ' + obj['sgdid']+ ' in row ' + str(row_num))
        traceback.print_exc()
        db_session.rollback()
        db_session.close()

def load_csv_disease_dbentities():
    engine = create_engine(NEX2_URI, pool_recycle=3600)
    DBSession.configure(bind=engine)

    o = open(INPUT_FILE_NAME,'rU')
    reader = csv.reader(o, delimiter='\t')
    for i, val in enumerate(reader):
        if i > 0:
            if val[0] == '':
                logging.info('Found a blank value, DONE!')
                return
            codes = val[16].strip().split(",")
            print codes[0]
            obj = {
                'taxon': val[0].strip().replace("taxon:","TAX:"),
                'sgdid': val[2].strip().replace("SGD:", ""),
                'symbol': val[3].strip(),
                'association': val[8].strip(),
                'doid': val[10].strip(),
                'with': val[11].strip(),
                'evidence_code': codes[0],
                'pmid': val[18].strip().replace("PMID:", ""),
                'date_assigned': val[19].strip(),
                'source': val[20]
            }
            upload_db(obj, i)
            sys.exit()

if __name__ == '__main__':
    load_csv_disease_dbentities()
