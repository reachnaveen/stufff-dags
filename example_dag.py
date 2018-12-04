from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2018, 12, 1, 10, 00, 00),
    'concurrency': 1,
    'retries': 1
}

dag = DAG('example', default_args=default_args, schedule_interval=timedelta(seconds=120))

task1 = BashOperator(task_id='task1', bash_command='echo "Hi!!"', dag=dag)