from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker

# conexão local - MySQL
#engine = create_engine("mysql+mysqldb://root:@localhost:3306/maternidade")

# conexão supabase - PostgreSQL
engine = create_engine("postgresql://maternidade_api_service_user:PuabHcKcf0qJX9K3ISuUjoxjqlmEKus9@dpg-cs9f15jqf0us739fdso0-a.oregon-postgres.render.com/maternidade_api_service")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  
Base = declarative_base()

def get_db():     
    db = SessionLocal()     
    try:         
        yield db     
    finally:
        db.close()