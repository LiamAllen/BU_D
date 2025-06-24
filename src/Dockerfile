#python runtime as parent image 
FROM python:3.12-slim

#working directory
WORKDIR /app

#copy requirements.txt
COPY . /app
#install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

#command to run the application
CMD ["python", "main.py"]