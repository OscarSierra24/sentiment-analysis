from mongoengine import Document, StringField,\
                        connect, GeoPointField,\
                        DateTimeField, DecimalField,\
                        ObjectIdField, BooleanField, EmbeddedDocumentListField,\
                        EmbeddedDocument,PointField

class Tweet(Document):
    id       = StringField(required=True)
    text     = StringField(required=True)
    analyzed = BooleanField(default=False)