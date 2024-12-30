# Use Python slim base image
FROM python:3-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Expose Flask app port
EXPOSE ${FLASK_PORT}

# Command to run the Flask app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.run:app"]
