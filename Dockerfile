# Python image to use.
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# copy the requirements file used for dependencies
COPY requirements.txt .

ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
# ENV PORT 5000
# ENV HOST 0.0.0.0

# Install any needed packages specified in requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# Copy the rest of the working directory contents into the container at /app
COPY . /app


# Run app.py when the container launches
CMD exec gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 app:app