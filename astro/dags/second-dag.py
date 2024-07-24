from airflow.decorators import dag, task
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.utils.dates import days_ago


@dag(
    dag_id="second-dag",
    schedule_interval="0 0 * * *",
    start_date=days_ago(1),
    catchup=False,
    tags=["example"],
)
def my_dag():
    @task
    def extract():
        print("Extracting data...")

    @task
    def transform():
        print("Transforming data...")

    @task()
    def load():
        print("Loading data...")

    spark_submit_task = SparkSubmitOperator(
        task_id="spark_submit_task",
        application="/usr/local/airflow/include/my-spark.py",
        conn_id="spark_default",
        conf={
            "spark.master": "spark://spark-master1:7077",
            "spark.submit.deployMode": "client",
        },
    )

    extract() >> transform() >> load() >> spark_submit_task


my_dag()
