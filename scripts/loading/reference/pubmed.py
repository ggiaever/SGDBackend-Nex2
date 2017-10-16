from Bio import Entrez
from urllib import urlopen
import sys
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')
sys.path.insert(0, '../')
from config import EMAIL

__author__ = 'sweng66'

Entrez.email = EMAIL
    
def get_abstract(pmid):

    handle = Entrez.efetch(db="pubmed", id=pmid, rettype='abstract')
    record = Entrez.read(handle)
    paper = record['PubmedArticle'][0]
    abstractText = ""
    article = paper['MedlineCitation']['Article']
    if article.get('Abstract'):
        for abstract in article['Abstract']['AbstractText']:
            if abstractText != "":
                abstractText = abstractText + "<p>"
            abstractText = abstractText + abstract

    return abstractText

def get_abstracts(pmid_list):

    handle = Entrez.efetch(db="pubmed", id=pmid_list, rettype='abstract')
    record = Entrez.read(handle)

    abstracts = []
    for paper in record['PubmedArticle']:
        abstractText = ""
        article = paper['MedlineCitation']['Article']
        if article.get('Abstract'):
            for abstract in article['Abstract']['AbstractText']:
                if abstractText != "":
                    abstractText = abstractText + "<p>"
                abstractText = abstractText + abstract
        pmid = int(paper['MedlineCitation']['PMID'])
        abstracts.append((pmid, abstractText))

    return abstracts


def get_pubmed_esummary(pmid_list):

    handle = Entrez.esummary(db="pubmed", id=pmid_list) 
    records = Entrez.read(handle)
    return records


def get_pubmed_record(pmid_list):

    handle = Entrez.efetch(db="pubmed", id=pmid_list, rettype='Medline', retmode='text')
    records_txt = handle.read()
    return records_txt.split("\n\n")

    # handle = Entrez.efetch(db="pubmed", id=pmid_list, rettype='Medline', retmode='xml') 
    # records = Entrez.read(handle)
    # print records
    # return records

def get_pubmed_record_from_xml(pmid_list):

    handle = Entrez.efetch(db="pubmed", id=pmid_list, rettype='xml')
    record = Entrez.read(handle)

    data = []
    for paper in record['PubmedArticle']:    
        entry = {}
        entry['pmid'] = int(paper['MedlineCitation']['PMID'])
        article = paper['MedlineCitation']['Article']
        
        journal = article['Journal']
        # entry['issn'] = journal.get('ISSN') 
        entry['journal_abbrev'] = journal.get('ISOAbbreviation')
        entry['journal_title'] = journal.get('Title')
        if journal.get('JournalIssue'):
            entry['issue'] = journal['JournalIssue'].get('Issue')
            entry['volume'] = journal['JournalIssue'].get('Volume')
            if journal['JournalIssue'].get('PubDate'):
                entry['year'] = journal['JournalIssue']['PubDate'].get('Year')
        entry['title'] = article.get('ArticleTitle')
        if paper['MedlineCitation'].get('DateRevised'):
            dateRevised = paper['MedlineCitation']['DateRevised']
            entry['date_revised'] = dateRevised['Year'] + "-" + dateRevised['Month'] + "-" + dateRevised['Day']  
            
        if article.get('Pagination'):
            entry['page'] = article['Pagination'].get('MedlinePgn')
        
        if article.get('PublicationTypeList'):
            types = []
            for type in article['PublicationTypeList']:
                types.append(str(type))
            entry['pubtypes'] = types
        
        if article.get('AuthorList'):
            authors = []
            for author in article['AuthorList']:
                if author.get('LastName') is None or author.get('Initials') is None:
                    continue
                authors.append(author['LastName'] + " " + author['Initials'])
            entry['authors'] = authors
        
        if paper['PubmedData'].get('PublicationStatus'):
            entry['publication_status'] = paper['PubmedData'].get('PublicationStatus')

        if paper['PubmedData'].get('ArticleIdList'):
            for item in paper['PubmedData'].get('ArticleIdList'):
                if item.attributes.get('IdType') is not None and item.attributes.get('IdType') == 'pmc':
                    entry['pmc'] = str(item)
                if item.attributes.get('IdType') is not None and item.attributes.get('IdType') == 'doi':
                    entry['doi'] = str(item)
        
        print entry, "\n"

        data.append(entry)
        
    return data
        
    
def get_author_etc(author_list):

    if author_list is None or len(author_list) == 0:
        return ""

    author_et_al = ""

    if len(author_list) == 1:
        author_et_al = author_list[0]
    elif len(author_list) == 2:
        author_et_al = " and ".join(author_list)
    else:
        author_et_al = author_list[0] + ", et al."

    return author_et_al


def set_cite(title, author_list, year, journal, volume, issue, pages):

    author_etc = get_author_etc(author_list)

    citation_data = {
            'title': title,
            'authors': author_etc,
            'year': year,
            'journal': journal,
            'volume': volume,
            'issue': issue,
            'pages': pages }
    citation = "{authors} ({year}) {title} {journal}".format(**citation_data)
    if volume and issue and pages:
        citation += " {volume}({issue}):{pages}".format(**citation_data)
    elif volume and issue:
        citation += " {volume}({issue})".format(**citation_data)
    elif volume and pages:
        citation += " {volume}:{pages}".format(**citation_data)
    elif volume:
        citation += " {volume}".format(**citation_data)
    elif pages:
        citation += " {pages}".format(**citation_data)
    return citation

def get_pmid_list(terms, retmax, day):

    pmid_list_all = []
    for term in terms:
        results = search(term+'[tw]', retmax, day)
        pmid_list = results['IdList']
        for pmid in pmid_list:
            if pmid not in pmid_list_all:
                pmid_list_all.append(pmid)
    return pmid_list_all

def search(query, retmax, day):

    handle = Entrez.esearch(db='pubmed',
                            sort='relevance',
                            reldate=day,
                            datetype='edat',
                            retmax=retmax,
                            retmode='xml',
                            term=query)
    results = Entrez.read(handle)
    return results

