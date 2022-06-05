import random
import json
import pendulum

from airflow import models
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from airflow.decorators import dag, task
import time

def rand_exc():
    if random.randint(0,10) < 3:
        raise Exception()

def rand_sleep():
    time.sleep(random.randint(0,10))

@dag(
    dag_id="定期同步品牌库存",
    schedule_interval=None,
    start_date=days_ago(1),
    tags=['etl', 'Ecommence'],
)
def BrandRefreshStock():

    @task
    def load_url():
        rand_exc()
        rand_sleep()
        return "https://www.baidu.com"

    @task()
    def crawl_url(url: str):
        rand_exc()
        rand_sleep()
        print(f"do crawl {url}")
        return {
            "url": url,
            "stock": 1,
        }

    @task()
    def backup_url(url: str):
        rand_exc()
        rand_sleep()
        print(f"do backup {url}")

    @task()
    def parse_url(url: str):
        rand_exc()
        rand_sleep()
        print(f"do parse {url}")

    @task()
    def apply_result(result: dict):
        rand_exc()
        rand_sleep()
        print(f"Total order value is: {result}")

    url = load_url()
    crawl_url(url)
    backup_url(url)
    parse_url(url)
    apply_result(url)

brand_refresh_dag = BrandRefreshStock()
