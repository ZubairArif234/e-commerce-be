import mongoengine as me

class Product(me.Document):
    name = me.StringField(required=True)
    desc = me.StringField(required=True)
    price = me.StringField(required=True)
    discount = me.IntField(default=0)
    shades = me.ListField()
    sizes = me.ListField()
    thumbnailImg = me.StringField()
    # additionalImg = me.DictField()