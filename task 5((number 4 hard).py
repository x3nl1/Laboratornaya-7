from sqlalchemy import create_engine, Column, Integer, String, Index
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    category = Column(String)
    
    __table_args__ = (
        Index('idx_product_name', 'name'),
        Index('idx_product_category', 'category')
    )

def demonstrate_indexes():
    engine = create_engine('sqlite:///shop.db')
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    products = [
        Product(name="Ноутбук", price=50000, category="Электроника"),
        Product(name="Смартфон", price=30000, category="Электроника"),
        Product(name="Книга", price=500, category="Литература")
    ]
    
    session.add_all(products)
    session.commit()
    
    electronic_items = session.query(Product).filter_by(category="Электроника").all()
    
    print("Электроника в магазине:")
    for item in electronic_items:
        print(f"{item.name} - {item.price} руб.")
    
    session.close()

if __name__ == "__main__":
    demonstrate_indexes()
