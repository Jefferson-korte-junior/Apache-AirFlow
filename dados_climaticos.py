from airflow import DAG
import pendulum
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.macros import ds_add
from os.path import join 
import pandas as pd
import os


with DAG(
    "dados_climaticos",
    start_date=pendulum.datetime(2025, 5, 26, tz="UTC"),
    schedule_interval='0 0 * * 1',
    catchup=False
) as dag: 

    tarefa_1 = BashOperator(
        task_id='cria_pasta',
        bash_command='mkdir -p "/home/jeffinho345/Documents/airflowalura/semana={{ data_interval_end.strftime("%Y-%m-%d") }}/"'
    )

    def extrai_dados(data_interval_end):
        city = "boston" 
        key = "FCEBUQSX974B4B58F2X9QFMLW"

        url = (
            f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
            f"{city}/{data_interval_end}/{ds_add(data_interval_end, 7)}?unitGroup=metric&include=days&key={key}&contentType=csv"
        )

        file_path = f"/home/jeffinho345/Documents/airflowalura/semana={data_interval_end}/"
        os.makedirs(file_path, exist_ok=True)

        dados = pd.read_csv(url)

        dados.to_csv(file_path + "dados_bruto.csv")
        dados[["datetime", "tempmin", "temp", "tempmax"]].to_csv(file_path + "temperatura.csv", index=False)
        dados[["datetime", "description", "icon"]].to_csv(file_path + "condicoes.csv", index=False)

    tarefa_2 = PythonOperator(
        task_id='extrai_dados',
        python_callable=extrai_dados,
        op_kwargs={'data_interval_end': '{{ data_interval_end.strftime("%Y-%m-%d") }}'}
    )

    tarefa_1 >> tarefa_2
