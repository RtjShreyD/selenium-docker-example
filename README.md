# Selenium Python Application Dockerization

This example project demonstrates the process of dockerizing a Selenium Python application along with the compatible Chromedriver.

## Project Overview

The project is a simple Selenium Python script that scrapes Wikipedia search results. The script prompts the user for a search query, opens Wikipedia, performs the search, and retrieves the first two paragraphs of text from the search result.

The `main.py` script also serves as an example of on how we can use the Selenium Python script in headless/non-headless mode with/without docker.

The Dockerfile in this project serves as an example to dockerise a selenium based project. 

## Dockerization Steps

Follow these steps to dockerize the Selenium Python application:

### Step 1: Clone the Repository

```bash
git clone git@github.com:RtjShreyD/selenium-docker-example.git
cd selenium-docker-example
```

### Step 2: Build the Docker Image

```bash
docker build -t seleniumDockerised .
```

### Step 3: Run the Docker Container

```bash
docker run -it --rm seleniumDockerised
```

This command starts the container in interactive mode and removes it after execution.

### Step 4: Enter Search Query

Once the container is running, enter your Wikipedia search query as prompted.

### Step 5: View Results

The script will execute the search, retrieve the first two paragraphs of text, and display them.

## Chromedriver Compatibility

If the provided Dockerfile fails to download the correct Chromedriver version for the latest Chrome version, you can find compatible Chromedriver executable download links from [ChromeDriver - WebDriver for Chrome](https://googlechromelabs.github.io/chrome-for-testing/). In such a case, replace the Chromedriver download link in the Dockerfile with the actual download link.

```bash
RUN wget -O /tmp/chromedriver.zip https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.94/linux64/chromedriver-linux64.zip

# Link in this line needs to be replaced in Dockerfile
```

Note: Ensure compatibility by matching the Chrome and Chromedriver versions.

Feel free to modify and extend this project based on your specific requirements.

Happy Dockerizing!
