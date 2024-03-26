#!/usr/bin/env python3
'''
Python function that lists all documents in a collection
'''


def list_all(mongo_collection):
    """
    List all documents in the collection mongo_collection
    """
    documents = mongo_collection.find()
    if documents.count() == 0:
        return []
    return documents
