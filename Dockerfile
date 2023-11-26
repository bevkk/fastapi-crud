FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN rm -rf Dockerfile
RUN rm -rf README.md

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
