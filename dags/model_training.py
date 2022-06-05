import random

from airflow import models
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago

# old way

with models.DAG(
        dag_id="modal training",
        description="模型",
        start_date=days_ago(1),
        schedule_interval="@daily",
        tags=['ETL', 'example3'],

) as dag:
    fetch_weather_forecast = DummyOperator(task_id="获取天气预报数据", dag=dag)
    fetch_sales_data = DummyOperator(task_id="获取销售额数据", dag=dag)
    clean_forecast_data = DummyOperator(task_id="清理天气预报数据", dag=dag)
    clean_sales_data = DummyOperator(task_id="清理销售额数据", dag=dag)
    join_datasets = DummyOperator(task_id="合并数据集合", dag=dag)
    train_ml_model = DummyOperator(task_id="训练模型", dag=dag)
    deploy_ml_model = DummyOperator(task_id="部署模型", dag=dag)

    fetch_weather_forecast >> clean_forecast_data
    fetch_sales_data >> clean_sales_data
    [clean_forecast_data, clean_sales_data] >> join_datasets
    join_datasets >> train_ml_model >> deploy_ml_model
