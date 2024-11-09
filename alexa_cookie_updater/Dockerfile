FROM python:3.12-alpine

# Set environment variables
ENV LANG C.UTF-8

# Copy the Python script into the container
COPY extract_alexa_cookie.py /app/extract_alexa_cookie.py

# Set the working directory
WORKDIR /app

# Install any necessary dependencies
RUN apk add --no-cache python3 py3-pip && \
    pip3 install --no-cache-dir requests

# Run the Python script on container start
CMD ["python3", "/app/extract_alexa_cookie.py"]
