from sqlalchemy import create_engine

# create engine
engine = create_engine("postgresql+pygresql://airflow:airflow@host:5432/airflow")
