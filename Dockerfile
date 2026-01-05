# Base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy dependency file first (for layer caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Default command: run tests
CMD ["pytest", "-v"]