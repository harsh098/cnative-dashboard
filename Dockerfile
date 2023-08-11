FROM python:3.10.12-slim as base-img

RUN mkdir app
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

FROM base-img
WORKDIR /app

COPY . /app/
EXPOSE 3000

ENTRYPOINT [ "python", "app.py"]


