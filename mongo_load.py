from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import pymongo
import certifi
import os
import sys
import json

load_dotenv()
Url=os.getenv("MONGO_DB_URL")
ca=certifi.where()
class Network_Data_Extractor:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    def csv_to_json_converter(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    def insert_data_mongo(self,records,database,collections):
        try:
            self.database=database
            self.collections=collections
            self.records=records
            self.mongoclient=pymongo.MongoClient(Url)
            self.database=self.mongoclient[self.database]
            self.collections=self.database[self.collections]
            self.collections.insert_many(self.records)
            return (len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e,sys)
if __name__=="__main__":
    fp="Network_Data/phisingData.csv"
    database1="Aishik"
    collection="NetworkData"
    networkobj=Network_Data_Extractor()
    records=networkobj.csv_to_json_converter(file_path=fp)
    records_no=networkobj.insert_data_mongo(records,database=database1,collections=collection)
    print(records_no)