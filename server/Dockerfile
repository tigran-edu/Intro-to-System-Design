FROM python:3.10

WORKDIR /system/server

COPY server.py .

RUN pip install "fastapi[all]"
RUN pip install redis

ENTRYPOINT ["uvicorn", "server:app", "--reload", "--host", "0.0.0.0"]