#!/usr/bin/env python3
'''
list all
'''


def insert_school(mongo_collection, **kwargs):
    '''
    lists all documents
    '''
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
