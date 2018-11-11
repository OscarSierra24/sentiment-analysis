from mongoengine import connect
import settings
import os


user       = os.environ['DB_USER']
password   = os.environ['DB_PASS']

uri        = f'mongodb://{user}:{password}@ds151383.mlab.com:51383/proyect_bases'

#Database connection
try:
        connect(db='tweet-analysis',
                username=user,
                password=password,
                host=uri)
except Exception as e:
        print(e)

#Crash if not connected