# Use official Python 3.11 base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Copy the rest of the application
COPY . .

# Expose Flask/Gunicorn port
EXPOSE 5000

# Run with Gunicorn (production server)
# Format: gunicorn --bind 0.0.0.0:5000 <module>:<app_instance>
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "routes:app"]