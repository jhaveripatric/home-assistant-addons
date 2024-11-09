FROM python:3.12-alpine

ENV LANG C.UTF-8

# Copy the Python script into the container
COPY extract_alexa_cookie.py /app/extract_alexa_cookie.py

# Set the working directory
WORKDIR /app

# Install any necessary dependencies
RUN apk add --no-cache python3 py3-requests

# Run the Python script directly on container start
CMD ["python3", "/app/extract_alexa_cookie.py"]
