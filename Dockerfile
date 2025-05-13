FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y gcc iputils-ping default-libmysqlclient-dev pkg-config &&\
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy your code
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
