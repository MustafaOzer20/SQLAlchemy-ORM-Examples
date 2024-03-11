from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite veritabanı motorunu oluşturuyoruz
engine = create_engine('sqlite:///complex_relationship.sqlite3')# create_engine('sqlite:///db.sqlite3', echo=True)

# Oturum oluşturucuyu tanımlıyoruz
Session = sessionmaker(bind=engine)

# SQLAlchemy'nin Base sınıfını kullanarak tablolarımızı temsil edecek Base sınıfını tanımlıyoruz.
Base = declarative_base()
