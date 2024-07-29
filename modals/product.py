import mongoengine as me

class Product(me.Document):
    name = me.StringField(required=True)
    desc = me.StringField(required=True)
    price = me.StringField(required=True)
    discount = me.IntField(default=0)
    shades = me.DictField()
    sizes = me.DictField()
    # thumbnailImg = me.ImageField(required=True, size=(800, 600, True))
    additionalImg = me.DictField()