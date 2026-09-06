# Use lightweight official Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files
COPY . .

# Expose port 5000 for Flask
EXPOSE 5000

# Set Flask entrypoint environment variable
ENV FLASK_APP=flask_app.py

# Force Flask to bind to 0.0.0.0 on launch
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]