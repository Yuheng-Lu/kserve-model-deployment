# Use Python as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install curl and any required system dependencies
RUN apt-get update && apt-get install -y curl && apt-get clean

# Copy the application code
COPY app.py /app/app.py

# Install required Python packages
RUN pip install --no-cache-dir streamlit requests

# Expose the Streamlit default port
EXPOSE 8502

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8502", "--server.enableCORS=false", "--server.enableXsrfProtection=false"]
