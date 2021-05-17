import random

from airflow import models
from airflow.models.baseoperator import chain
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago


def _generate_feedback_tasks(merchant_id=None):
    print("----> merchant_id", merchant_id)
    if random.randint(0, 1):
        raise Exception("just a simple error")


def _crawl_by_date(merchant_id=None, date=None):
    print("----> merchant_id, --->date", merchant_id, date)


with models.DAG(
        dag_id="美团点评数据定期同步2",
        schedule_interval=None,
        start_date=days_ago(1),
        tags=['ETL', '美团', 'example3'],
) as dag:
    group_op = BashOperator(
        task_id="批量同步点评数据",
        bash_command="echo summary"
    )
    # Create
    for i in range(20):
        merchant_id = str(i).zfill(4)
        check_auth_by_merchant = BashOperator(
            task_id=f"检查商家_{merchant_id}_登陆凭证",
            bash_command="echo 1"
        )
        group_op >> check_auth_by_merchant
        generate_feedback_tasks = PythonOperator(
            task_id=f"生成商家_{merchant_id}_任务",
            python_callable=_generate_feedback_tasks,
            # op_kwargs={
            #     "merchant_id": merchant_id
            # }

        )
        check_auth_by_merchant >> generate_feedback_tasks
        for date in range(40):
            _no = str(date).zfill(4)
            crawl_by_date = PythonOperator(
                task_id=f"爬取商家_{merchant_id}_日期_{_no}_任务",
                python_callable=_crawl_by_date, op_kwargs={
                    # merchant_id: merchant_id,
                    # date: _no,
                }
            )
            check_auth_by_merchant >> crawl_by_date
