from mongoengine import Document, StringField,\
                        connect, GeoPointField,\
                        DateTimeField, DecimalField,\
                        ObjectIdField, BooleanField, EmbeddedDocumentListField,\
                        EmbeddedDocument,PointField

import connect_db

class Tweet(Document):
    tweet_id  = StringField(required=True)
    text     = StringField(required=True)
    analyzed = BooleanField(default=False)

Tweet(tweet_id='123',text='Wuddup').save()