FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# O código fonte não é copiado aqui para forçar o uso do bind mount no Compose
EXPOSE 5000

CMD ["python", "app.py"]
