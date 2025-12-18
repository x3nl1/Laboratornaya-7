from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    employees = relationship("Employee", back_populates="department")

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    department_id = Column(Integer, ForeignKey('departments.id'))
    department = relationship("Department", back_populates="employees")

def setup_relationship():
    engine = create_engine('sqlite:///company.db')
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    it_department = Department(name="IT отдел")
    hr_department = Department(name="HR отдел")
    
    employee1 = Employee(name="Алексей", department=it_department)
    employee2 = Employee(name="Ольга", department=hr_department)
    
    session.add_all([it_department, hr_department, employee1, employee2])
    session.commit()
    
    result = session.query(Department).all()
    for dept in result:
        print(f"Отдел: {dept.name}")
        for emp in dept.employees:
            print(f"  - {emp.name}")
    
    session.close()

if __name__ == "__main__":
    setup_relationship()
