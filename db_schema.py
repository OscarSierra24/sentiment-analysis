from mongoengine import Document, StringField,\
                        connect, GeoPointField,\
                        DateTimeField, DecimalField,\
                        ObjectIdField, BooleanField, EmbeddedDocumentListField,\
                        EmbeddedDocument,PointField
from datetime import datetime
class Tweet(Document):
    tweet_id = StringField(required=True)
    text     = StringField(required=True)
    analyzed = BooleanField(default=True)
    sentiment= DecimalField(required=True)
    retrieved= DateTimeField(default=datetime.now)
    topic    = StringField(required=True)