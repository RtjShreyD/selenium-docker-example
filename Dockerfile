FROM python:3.9

WORKDIR /usr/src/app

# Install dependencies
RUN apt-get update \
    && apt-get install -y wget curl unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install the latest version of Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Download and install Chromedriver with the specified version
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.94/linux64/chromedriver-linux64.zip
RUN unzip /tmp/chromedriver.zip -d /usr/local/bin/

# set display port to avoid crash
ENV DISPLAY=:99

COPY main.py .
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
