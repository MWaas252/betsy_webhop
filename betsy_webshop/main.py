from peewee import fn
from fuzzywuzzy import fuzz  # import fuzzywuzzy
from betsy_webshop.models import User, Product, Tag, Transaction
from betsy_webshop.models import db

__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

# Check database connection
try:
    db.connect()
    print("Database connection established successfully.")
except Exception as e:
    print("Error connecting to the database:", e)


def search(term):
    """Search for products based on term.
    Searching for 'sweater' should yield all products that have the word 'sweater' in the name.
    This search should be case-insensitive.
    """
    results = (Product
               .select()
               .where(
                   (fn.lower(Product.name).contains(term.lower())) |
                   (fn.lower(Product.description).contains(term.lower()))
                ))
                
    # Fuzzy search to account for spelling mistakes
    fuzzy_results =[]
    for product in results:
        name_score = fuzz.partial_ratio(term.lower(), product.name.lower())
        # Check if product has description attribute
        if hasattr(product, 'discription'):
            desc_score = fuzz.partial_ratio(term.lower(), product.description.lower())
        else: 
            desc_score = 0    
        avg_score = (name_score + desc_score) /2
        fuzzy_results.append((product, avg_score))

    #Sort the results by fuzzy score
    fuzzy_results.sort(key=lambda x: x[1], reverse=True)

    return [result[0] for result in fuzzy_results]

def list_user_products(user_id):
    """View the products of a given user."""
    user = User.get_or_none(User.id == user_id)
    if user:
        return user.product_set
    else:
        return[]
    
def list_products_per_tag(tag_id):
    """View all products for given tag."""
    tag = Tag.get_or_none(Tag.id == tag_id)
    if tag:
        return tag.product_set
    else:
        return []

def add_product_to_catalog(user_id, product_data):
    """Add a product to a user."""
    user = User.get_or_none(User.id == user_id)
    if user:
        product = Product.create(**product_data)
        user.product_set.add(product)
        return product
    else:
        return None    


def update_stock(product_id, new_quantity):
    """Update the stock quantity of a product"""
    product = Product.get_or_none(Product.id == product_id)
    if product:
        product.quantity = new_quantity
        product.save()
        return product
    else:
        return None


def purchase_product(product_id, buyer_id, quantity):
    """Handle a purchase between a buyer and a seller for a given product."""
    product = Product.get_or_none(Product.id == product_id)
    buyer = User.get_or_none(User.id == buyer_id)
    if product and buyer and product.quantity >= quantity:
        transaction = Transaction.create(buyer=buyer, product=product, quantity=quantity)
        product.quantity -= quantity
        product.save()
        return transaction
    else:
        return None


def remove_product(product_id):
    """"Remove a product from a user"""
    product = Product.get_or_none(Product.id == product_id)
    if product:
        product.delete_instance()
        return True
    else:
        return False


"""Explanation:
Search(term): Searches for products based on a term in the product name or description.
List_user_products(user_id): Lists all products of a given user.
List_products_per_tag(tag_id): Lists all products associated with a given tag.
Add_product_to_catalog(user_id, product_data): Adds a product to a user's catalog.
Update_stock(product_id, new_quantity): Updates the stock quantity of a product.
Purchase_product(product_id, buyer_id, quantity): Handles a purchase between a buyer and a seller for a given product.
Remove_product(product_id): Removes a product from the database.
"""

# This block of code will be executed when you run main.py directly 
if __name__ == "__main__":
    # You can put your test code or any other code that you want to execute here
    pass