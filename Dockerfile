FROM python:3.9.17-slim-bullseye

# Prevent interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Update and install required packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends git curl ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN python3 -m pip install --upgrade pip

# Copy project files
COPY . /app/
WORKDIR /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make start.sh executable
RUN chmod +x start.sh

# Start the app Fixed Via @SourabhProfessor
CMD ["bash", "start.sh"]
