from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
sys.path.append('/opt/airflow/scripts')

from extract import extract_data
from transform import transform_data
from load import load_data

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 3, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "covid_pipeline",
    default_args=default_args,
    description="COVID-19 Data Pipeline",
    schedule_interval="0 * * * *",  # Runs every hour
    catchup=False
)

extract_task = PythonOperator(task_id="extract", python_callable=extract_data, dag=dag)
transform_task = PythonOperator(task_id="transform", python_callable=transform_data, dag=dag)
load_task = PythonOperator(task_id="load", python_callable=load_data, dag=dag)

extract_task >> transform_task >> load_task
