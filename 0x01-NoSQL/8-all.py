#!/usr/bin/env python3
'''
list all
'''


def list_all(mongo_collection):
    '''
    lists all documents
    '''
    return [doc for doc in mongo_collection.find()]
