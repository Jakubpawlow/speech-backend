FROM python:3.9-slim

WORKDIR /app

# instalacja wymaganych zależności systemowych
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "speech-backend.app:app", "--host", "0.0.0.0", "--port", "7860"]
