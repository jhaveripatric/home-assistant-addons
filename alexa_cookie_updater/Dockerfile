ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

# Install Python and the requests package
RUN apk add --no-cache python3 py3-pip py3-requests

# Copy the Python script into the container
COPY extract_alexa_cookie.py /app/extract_alexa_cookie.py

# Make sure the entrypoint uses s6-overlay
ENTRYPOINT [ "/init" ]

# Run the Python script via s6-overlay
CMD ["python3", "/app/extract_alexa_cookie.py"]
