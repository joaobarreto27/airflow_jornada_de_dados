FROM astrocrpublic.azurecr.io/runtime:3.0-9
RUN pip install -r requirements.txt
ENV PYTHONPATH="/usr/local/airflow/include:${PYTHONPATH}"