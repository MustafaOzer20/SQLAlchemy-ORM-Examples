from models import (
    Address,
    Customer,
    Order,
    OrderItem
)
from database import Session, Base, engine

# create db or tables
Base.metadata.create_all(engine) 

session = Session()

# Birinci müşteri ve adresler
delivery_address = Address(street="123 Main St", city="Anytown", postal_code="12345")
billing_address = Address(street="456 Elm St", city="Anytown", postal_code="54321")
customer1 = Customer(name="John Doe", delivery_address=delivery_address, billing_address=billing_address)

# İkinci müşteri ve adresler
delivery_address2 = Address(street="789 Oak St", city="Othertown", postal_code="67890")
billing_address2 = Address(street="321 Pine St", city="Othertown", postal_code="09876")
customer2 = Customer(name="Jane Smith", delivery_address=delivery_address2, billing_address=billing_address2)

# Üçüncü müşteri ve adresler
delivery_address3 = Address(street="111 Cedar St", city="Anothertown", postal_code="13579")
billing_address3 = Address(street="222 Maple St", city="Anothertown", postal_code="24680")
customer3 = Customer(name="Bob Johnson", delivery_address=delivery_address3, billing_address=billing_address3)

# Dördüncü müşteri ve adresler
delivery_address4 = Address(street="444 Walnut St", city="Yetanothertown", postal_code="11223")
billing_address4 = Address(street="555 Birch St", city="Yetanothertown", postal_code="33445")
customer4 = Customer(name="Emily Davis", delivery_address=delivery_address4, billing_address=billing_address4)

# Siparişler

order1 = Order(order_number="12345", customer=customer1)
order_item1 = OrderItem(product_name="Product 1", quantity=2, order=order1)
order_item2 = OrderItem(product_name="Product 2", quantity=1, order=order1)
order_item3 = OrderItem(product_name="Product 3", quantity=3, order=order1)

order2 = Order(order_number="54321", customer=customer2)
order_item4 = OrderItem(product_name="Product 4", quantity=3, order=order2)

order3 = Order(order_number="98765", customer=customer3)
order_item5 = OrderItem(product_name="Product 5", quantity=2, order=order3)
order_item6 = OrderItem(product_name="Product 6", quantity=2, order=order3)

order4 = Order(order_number="13579", customer=customer4)
order_item7 = OrderItem(product_name="Product 7", quantity=1, order=order4)
order_item8 = OrderItem(product_name="Product 8", quantity=3, order=order4)
order_item9 = OrderItem(product_name="Product 9", quantity=3, order=order4)
order_item10 = OrderItem(product_name="Product 10", quantity=3, order=order4)

# Örnek verileri ekle
session.add_all([
    delivery_address, billing_address, customer1,
    delivery_address2, billing_address2, customer2,
    delivery_address3, billing_address3, customer3,
    delivery_address4, billing_address4, customer4,
    order1, order_item1, order_item2, order_item3,
    order2, order_item4,
    order3, order_item5, order_item6,
    order4, order_item7, order_item8, order_item9, order_item10
])

session.commit()
session.close()