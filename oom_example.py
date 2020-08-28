from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator


YESTERDAY = datetime.combine(
    datetime.today() - timedelta(days=1), datetime.min.time())

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': YESTERDAY,
}

def oom():
  print 'OOM Prologue'
  strings = ['a']
  while True:
    strings.append(strings[-1] + strings[-1])
  print 'OOM Epilogue'


with DAG('oom_example', catchup=False, default_args=default_args) as dag:
  PythonOperator(task_id='oom_python', python_callable=oom)
