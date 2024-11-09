ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

# Copy a basic script to test s6-overlay behavior
COPY test_script.sh /app/test_script.sh
RUN chmod +x /app/test_script.sh

# Use s6-overlay entrypoint
ENTRYPOINT [ "/init" ]

# Execute a minimal command to check for s6-overlay issues
CMD ["/app/test_script.sh"]
