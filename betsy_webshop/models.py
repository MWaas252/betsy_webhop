# Models go here

import peewee

db = peewee.SqliteDatabase("Betsy.db")

class BaseModel(peewee.Model):
    class Meta:
        database = db

class User (BaseModel):
    name = peewee.CharField(max_length=255)
    address = peewee.CharField(max_length=255)
    billing_info = peewee.CharField(max_length=255)

class Product(BaseModel): 
    name = peewee.CharField(unique=True, max_length=255) 
    description = peewee.TextField()  # Corrected typo from 'discription' to 'description'
    price_per_unit = peewee.DecimalField(max_digits=10, decimal_places=2)
    quantity = peewee.IntegerField()
 

class Tag(BaseModel):
    name = peewee.CharField(unique=True, max_length=255)

class Transaction(BaseModel):
    buyer = peewee.ForeignKeyField (User)
    product = peewee.ForeignKeyField (Product)
    quantity = peewee.IntegerField()

# Create tables if they do not exist
def initialize_database():
    with db:
        db.create_tables([User, Product, Tag, Transaction])         

# Call initialize_database() function to create tables when the application starts

initialize_database()