#!/usr/bin/env python3
'''
Python script that provides some stats
about Nginx logs stored in MongoDB
'''
from pymongo import MongoClient


METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def analyse_nginx_logs(mongo_collection, option=None):
    """
    Getting stats about Nginx logs sotred in MongoDB
    """
    if option:
        count = mongo_collection.count_documents({"method": option})
        print(f"\t{option}: {count}")
    else:
        total_logs = mongo_collection.count_documents({})
        print(f"{total_logs} logs")
        print("Methods:")
        for method in METHODS:
            count = mongo_collection.count_documents({"method": method})
            print(f"\t{method}: {count}")
        rgm = {"method": "GET", "path": "/status"}
        status_check = mongo_collection.count_documents(rgm)
        print(f"GET /status: {status_check}")


if __name__ == "__main__":
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    log_stats(nginx_collection)
