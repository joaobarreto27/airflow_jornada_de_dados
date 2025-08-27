from airflow.decorators import dag, task #type:ignore

from datetime import datetime
from time import sleep


@dag(
    dag_id="minha_primeira_dag",
    description="minha etl braba",
    schedule="* * * * *",
    start_date=datetime(2025, 8, 26),
    catchup=False
)
def pipeline():

    @task
    def primeira_atividade():
        print("Primeira atividade iniciada! - Hello World")
        sleep(2)

    @task
    def segunda_atividade():
        print("Segunda atividade iniciada! - Hello World")
        sleep(2)

    @task
    def terceira_atividade():
        print("Terceira atividade iniciada! - Hello World")
        sleep(2)

    @task
    def quarta_atividade():
        print("Pipeline encerrada")
        sleep(2)

    t1 = primeira_atividade()
    t2 = segunda_atividade()
    t3 = terceira_atividade()
    t4 = quarta_atividade()

    t1 >> t2 >> t3 >> t4


# instanciando a DAG para o Airflow reconhecer
dag = pipeline()