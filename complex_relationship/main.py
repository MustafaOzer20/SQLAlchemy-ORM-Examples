from database import Session
from models import (
    Address,
    Customer,
    Order,
    OrderItem
)

def order_to_access_all():
    session = Session()

    orders = session.query(Order).all()

    for order in orders:
        items = []
        for item in order.order_items:
            items.append(item.product_name)
        print({
            "order_items": items,
            "Customer_Name": order.customer.name,
            "Delivery_City": order.customer.delivery_address.city,
            "Delivery_Postal_Code": order.customer.delivery_address.postal_code
        })

    session.close()

def address_to_customer():
    session = Session()

    address = session.query(Address).all()

    for adres in address:
        customer = ""
        address_type = ""
        if adres.delivery_customer:
            customer:Customer = adres.delivery_customer[0]
            address_type = "delivery"
        else:
            customer:Customer = adres.billing_customer[0]
            address_type = "billing"
        
        print({
            "customer": customer.name,
            "address_type": address_type,
            "postal_code": adres.postal_code,
            "city": adres.city,
            "street": adres.street
        })

    session.close()

def main():
    order_to_access_all()
    print(50*"-")
    address_to_customer()

if __name__ == "__main__":
    main()