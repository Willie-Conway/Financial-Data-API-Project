# backend/Dockerfile
FROM python:3.10-slim  

# Set working directory
WORKDIR /app

# Install system dependencies (for packages like psycopg2, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and setuptools for better package handling
RUN pip install --upgrade pip setuptools

# Copy only requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Set entrypoint and default command
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

