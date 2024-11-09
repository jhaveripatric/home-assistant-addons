ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

# Install Python and dependencies
RUN apk add --no-cache python3 py3-pip && \
    pip3 install --no-cache-dir requests

# Copy the Python script into the container
COPY extract_alexa_cookie.py /app/extract_alexa_cookie.py

# Run the Python script when the container starts
CMD ["python3", "/app/extract_alexa_cookie.py"]
