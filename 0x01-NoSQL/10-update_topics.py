#!/usr/bin/env python3
'''
list all
'''


def update_topics(mongo_collection, name, topics):
    '''
    lists all documents
    '''
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
