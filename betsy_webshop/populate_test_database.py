from models import User, Product, Tag, Transaction

def populate_test_database():
    # Create users
    user1 = User.create(name='John Doe', address='123 Main St', billing_info='Card ending in 1234')
    user2 = User.create(name='Jane Smith', address='456 Elm St', billing_info='Card ending in 5678')

    # Create tags
    tag1 = Tag.create(name='Clothing')
    tag2 = Tag.create(name='Electronics')
    tag3 = Tag.create(name='Home')

    # Create products
    product1 = Product.create(name='Sweater', description='Warm and cozy sweater', price_per_unit=29.99, quantity=50)
    product1.tags.add(tag1)

    product2 = Product.create(name='Smartphone', description='Latest smartphone model', price_per_unit=799.99, quantity=20)
    product2.tags.add(tag2)

    product3 = Product.create(name='Coffee Maker', description='Espresso machine', price_per_unit=149.99, quantity=10)
    product3.tags.add(tag3)

    populate_test_database()
    
