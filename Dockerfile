# 1. Base Image
FROM python:3.12-slim

# 2. Setup Workspace
WORKDIR /app

# 3. Install Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy Code
COPY . .

# 5. EXPOSE THE PORT
# This tells Docker: "I plan to listen on port 8000"
EXPOSE 8000

# 6. START THE SERVER
# --host 0.0.0.0 is MANDATORY for Docker. 
# It lets the container accept connections from outside (your Mac).
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]