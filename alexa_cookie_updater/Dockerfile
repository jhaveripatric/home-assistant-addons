ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

# Install Python and necessary dependencies
RUN apk add --no-cache python3 py3-pip

# Copy the Python script into the container
COPY extract_alexa_cookie.py /app/extract_alexa_cookie.py

# Set up Home Assistant’s add-on service control (s6-overlay)
# Entrypoint must be /init for s6-overlay to manage services properly
ENTRYPOINT [ "/init" ]

# Run the Python script on container start
CMD ["python3", "/app/extract_alexa_cookie.py"]
