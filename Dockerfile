# Use a lightweight Python 3.9 base image
FROM python:3.9-alpine AS build-stage

# Set the working directory inside the container
WORKDIR /home/data

# Set environment variables to avoid creating __pycache__ directories
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache \
    build-base \
    libffi-dev \
    musl-dev \
    gcc \
    python3-dev \
    postgresql-dev \
    && rm -rf /var/cache/apk/*


FROM python:3.9-alpine

# Set environment variables again for final stage
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /home/data

# Install runtime dependencies (only for final stage)
RUN apk add --no-cache \
    libffi \
    musl \
    postgresql-libs \
    && rm -rf /var/cache/apk/*

# Copy files from the build stage, including installed Python packages
COPY --from=build-stage /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=build-stage /usr/local/bin /usr/local/bin

# Copy specific files to /home/data directory
COPY AlwaysRememberUsThisWay.txt IF.txt scripts.py /home/data/

# Create output directory
RUN mkdir -p /home/data/output

# Expose port 8000 (optional, depending on your application)
EXPOSE 8000

# Command to run your application
CMD ["python", "scripts.py"]
