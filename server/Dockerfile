FROM python:3.10

WORKDIR /system/server

RUN pip install "fastapi[all]"
RUN pip install redis

COPY server.py .

ENTRYPOINT ["uvicorn", "server:app", "--reload", "--host", "0.0.0.0"]