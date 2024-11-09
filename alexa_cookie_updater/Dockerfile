ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

# Install Python
RUN apk add --no-cache python3 py3-pip

# Copy the Python script into the container
COPY extract_alexa_cookie.py /app/extract_alexa_cookie.py

# Set the command to run the Python script with the environment variable
CMD ["python3", "/app/extract_alexa_cookie.py"]
