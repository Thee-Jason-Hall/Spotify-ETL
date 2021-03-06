import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

from spotify_etl import run_spotify_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.datetime(2021, 6, 17),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes=1)
}

dag = DAG(
    'spotify_dag',
    default_args=default_args,
    description='SpotifyDAG with ETL',
    schedule_interval=datetime.timedelta(days=1),
)

def just_a_function():
    print("Service ON")

run_etl = PythonOperator(
    task_id='whole_spotify_etl',
    python_callable=run_spotify_etl,
    dag=dag,
)

run_etl