#1. Base Image
FROM python:3.9-slim

#2. Working directory
WORKDIR /app

#3. Install Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#4. Copy Application Code
COPY . .

#5. Expose Port
EXPOSE 5000

#6. Run command and start flask application directly
CMD ["python", "app.py"]