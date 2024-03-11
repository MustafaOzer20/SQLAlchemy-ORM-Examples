from models import (
    Category,
    Product
)
from database import Session

def category_to_product():
    session = Session()

    category = session.query(Category).filter_by(name="Electronics").first()
    products = category.products

    print("Products in Electronics category:")
    for product in products:
        print(product.name)

    
    session.close()

def product_to_category():
    session = Session()
    """
    electronics_products = session.query(Product).filter(Product.categories.any(name='Electronics')).all()
    print("Products in Electronics category:")
    for product in electronics_products:
        print(product.name)
    """

    product = session.query(Product).filter_by(name="Laptop").first()
    print("List of Laptop Categories:")
    for category in product.categories:
        print(category.name)

    session.close()

def main():
    category_to_product()
    print(50*"-")
    product_to_category()


if __name__ == "__main__":
    main()