FROM nikolaik/python-nodejs:python3.10-nodejs20

RUN apt-get update && \
    apt-get install -y curl gnupg ffmpeg git && \
    curl -fsSL https://deb.nodesource.com/setup_19.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . /app/
WORKDIR /app/

RUN python3 -m pip install --upgrade pip
RUN pip3 install --no-cache-dir -U -r requirements.txt \
    && python3 -m pip install -U --pre "yt-dlp[default]"

CMD ["bash", "start"]
