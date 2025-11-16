FROM python:3.11-slim

WORKDIR /app

# Copia os arquivos necessários
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY bot.py .

# Executa o bot
CMD ["python", "bot.py"]
