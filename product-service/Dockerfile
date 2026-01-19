# 1. Use lightweight Python base image
FROM python:3.11-slim

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy dependency file first (layer optimization)
COPY requirements.txt .

# 4. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy application code
COPY app.py .

# 6. Expose application port
EXPOSE 5000

# 7. Command to run the app
CMD ["python", "app.py"]
