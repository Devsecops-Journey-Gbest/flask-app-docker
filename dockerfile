# Use Python base image
FROM python:slim

# Set work directory
WORKDIR /app

# Copy files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose Flask port
EXPOSE 8080

# Start the app
CMD ["python", "app.py"]