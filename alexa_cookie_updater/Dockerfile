ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

# Install Python and the requests package directly via Alpine's package manager
RUN apk add --no-cache python3 py3-requests

# Copy the Python script into the container
COPY extract_alexa_cookie.py /app/extract_alexa_cookie.py

# Set the working directory
WORKDIR /app

# Run the Python script when the container starts
CMD ["python3", "/app/extract_alexa_cookie.py"]
