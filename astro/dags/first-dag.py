from airflow.decorators import dag, task
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.utils.dates import days_ago


@dag(
    dag_id="first-dag",
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

    extract() >> transform() >> load()


my_dag()
