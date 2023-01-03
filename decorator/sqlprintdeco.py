# Implement a retry decorator that takes can be used to initiate retries 
# for a database connection if an exception occurs.It should take as parameters
# the number of retries and delay between each retry .

import time 
import logging 
from functools import wraps 
from mysql.connector import MySQLConnection 

def retry(retry_count, delay):
    def retry_decorator(func):
        wraps(func)
        def func_wrapper(*args,**kwargs):
            result=None
            last_exception=[]
            
            for _ in range(retry_count):
                try:
                    result=func(*args,**kwargs)
                    if result: return result
                except Exception as e:
                    last_exception.append(e)
                
                time.sleep(delay)
                
            if last_exception:
                for _ in last_exception:
                    logging.exception("An exception occured")
                    
        return func_wrapper
    return retry_decorator

@retry(retry_count=3, delay=1)
def demo_db_connect():
    conn=MySQLConnection(user='myuser', password='mypass', host='localhost', database='mydb')
    with conn.cursor() as c:
        
    # """
    
    # Perform whatever database task
    # """
    return True 

    
                    
                    