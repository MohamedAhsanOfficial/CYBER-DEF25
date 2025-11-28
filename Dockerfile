FROM python:3.9-slim

WORKDIR /app

# Copy dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy model + inference script
COPY model.pkl .
COPY inference.py .

# Prepare directories
RUN mkdir -p /input/logs /output

CMD ["python3", "inference.py"]
