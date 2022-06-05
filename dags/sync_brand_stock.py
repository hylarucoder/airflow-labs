import random
import json
import pendulum

from airflow import DAG, XComArg, models
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from airflow.decorators import dag, task
import time

def rand_exc():
    if random.randint(0,10) < 1:
        raise Exception()

def rand_sleep():
    time.sleep(random.randint(0,10))

@task
def load_urls():
    return [
        "https://www.baidu.com",
        "https://www.baidu.com",
        "https://www.baidu.com",
        "https://www.baidu.com",
        "https://www.baidu.com",
        "https://www.baidu.com",
        "https://www.baidu.com",
        "https://www.baidu.com",
        "https://www.baidu.com",
    ]

@task()
def crawl_url(url: str):
    rand_exc()
    rand_sleep()
    print(f"do crawl {url}")
    print(f"do backup {url}")
    return {
        "url": url,
        "batch_no": "tt",
    }


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


with models.DAG(
    dag_id="定期同步品牌库存plus",
    schedule_interval=None,
    start_date=days_ago(1),
    tags=['etl', 'Ecommence'],
) as dag:
    urls_args = load_urls()
    response = crawl_url.expand(url=urls_args)
    results = parse_url.expand(url=urls_args)
    # apply_result.expand(result=results)
