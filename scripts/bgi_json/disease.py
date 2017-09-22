from src.models import DBSession, Base, Colleague, ColleagueLocus, Dbentity, Locusdbentity, LocusUrl, LocusAlias, Dnasequenceannotation, So, Locussummary, Phenotypeannotation, PhenotypeannotationCond, Phenotype, Goannotation, Go, Goslimannotation, Goslim, Apo, Straindbentity, Strainsummary, Reservedname, GoAlias, Goannotation, Referencedbentity, Referencedocument, Referenceauthor, ReferenceAlias, Chebi
from sqlalchemy import create_engine, and_
import os
import json
import re
import time
import sys
from datetime import datetime
import dateutil.parser as parser
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput


def txtJson():
    temp_data = []
    with open(
            './scripts/bgi_json/data_dump/disease/disease_2.json') as data_file:

        content = json.load(data_file)
    for item in content:
        if(item[10] != "Inferred"):
            obj = {
                "DOid": "",
                "taxonId": "",
                "objectRelation": {
                    "associationType": "",
                    "objectType": ""
                },
                "objectId": "",
                "dateAssigned": "",
                "dataProvider": "SGD",
                "with": [],
                "evidence": {
                    "evidenceCode": [],
                    "publication": {
                        "pubMedId": ""
                    }
                }
            }

            obj["DOid"] = item[6]
            obj["taxonId"] = item[0]
            obj["objectRelation"]["associationType"] = item[5]
            obj["objectRelation"]["objectType"] = item[1]
            obj["objectId"] = item[2]
            obj["dateAssigned"] = str(
                datetime.strptime(str(item[10]), "%Y%m%d")
                .isoformat()) + "-07:00"
            obj["dataProvider"] = item[11]
            obj["with"].append(str(item[7]))
            obj["evidence"]["evidenceCode"] = item[8].split(",")

            obj["evidence"]["publication"]["pubMedId"] = item[9]
            temp_data.append(obj)

    dProduced = datetime.now().isoformat()
    data_obj = {
        "data": json.dumps(temp_data, ensure_ascii=False),
        "metaData": {
            "dateProduced": dProduced,
            "dataProvider": "SGD"
        }
    }
    with open('./scripts/bgi_json/data_dump/disease/new_obj.json', 'w+') as res_file:
        res_file.write(data_obj)
if __name__ == '__main__':
    txtJson()
