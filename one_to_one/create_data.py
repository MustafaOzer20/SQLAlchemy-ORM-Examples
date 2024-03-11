from models import (
    User,
    Profile
)
from database import Session, Base, engine



# create db or tables
Base.metadata.create_all(engine) 

session = Session()

# Kullanıcı ve profilleri oluştur
user1 = User(name='John')
profile1 = Profile(address='123 Main St', user=user1)

user2 = User(name='Alice')
profile2 = Profile(address='456 Elm St', user=user2)

# Oturuma ekle ve değişiklikleri kaydet
session.add_all([user1, profile1, user2, profile2])
session.commit()

# Oturumu kapat
session.close()