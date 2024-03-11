from models import (
    Category,
    Product
)
from database import Session, Base, engine


Base.metadata.create_all(engine)

# Oturumu oluştur
session = Session()

# Ürünler ve kategoriler oluştur
product1 = Product(name='Laptop')
product2 = Product(name='Smartphone')

category1 = Category(name='Electronics')
category2 = Category(name='Computers')

# Ürünler ve kategoriler arasındaki ilişkiyi belirle
product1.categories.append(category1)
product1.categories.append(category2)
product2.categories.append(category1)

# Oturuma ekle ve değişiklikleri kaydet
session.add_all([product1, product2, category1, category2])
session.commit()

# Oturumu kapat
session.close()