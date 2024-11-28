FROM python:3.12.7-slim
WORKDIR /app
RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev \
    libmariadb-dev-compat \
    pkg-config \
    && apt-get clean
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
ENV FLASK_APP=main.py
ENV FLASK_ENV=development
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
