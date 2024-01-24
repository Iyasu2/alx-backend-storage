'''
this is the module
'''
import requests
import time
from functools import wraps


def count_access(url):
    '''
    a function
    '''
    def decorator(func):
        '''
        another function
        '''
        @wraps(func)
        def wrapper(*args, **kwargs):
            '''
            another one
            '''
            count_key = f"count:{url}"
            count = int(redis.get(count_key) or 0)
            count += 1
            redis.set(count_key, count, ex=10)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@count_access("http://slowwly.robertomurray.co.uk")
def get_page(url):
    '''
    last function
    '''
    response = requests.get(url)
    return response.text
