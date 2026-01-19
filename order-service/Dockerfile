# 1. Lightweight Python base image
FROM python:3.11-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy dependencies first (cache optimization)
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy application code
COPY app.py .

# 6. Expose service port
EXPOSE 5001

# 7. Run the application
CMD ["python", "app.py"]
