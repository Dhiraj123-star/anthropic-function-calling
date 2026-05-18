FROM python:3.13-slim

# prevent Python buffering
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt . 

RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Start application
CMD ["uvicorn","app:app","--host","0.0.0.0","--port","8000"]