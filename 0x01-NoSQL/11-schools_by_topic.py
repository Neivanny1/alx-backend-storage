#!/usr/bin/env python3
'''
Python function that returns the
list of school having a specific topic
'''


def schools_by_topic(mongo_collection, topic):
    """
    Retrieving list of matching items
    """
    results = mongo_collection.find({"topics": topic})
    return [result for result in results]
