# Blog Title generator API

This project sets up a speaker diarization API using **Django** and **llama 3.2 1b instruct**. Follow the instructions below to set up the environment, run the Django server, and test the API with a sample `curl` command.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [Setting Up Conda Environment](#setting-up-conda-environment)
  - [Running the Django Application](#running-the-django-application)
- [Testing the title API](#testing-the-title-api)
  - [Using `curl` for Testing](#using-curl-for-testing)

---

## Prerequisites

- **Python 3.8 or higher** (Ensure your system is using a compatible version)
- **Conda**: Used for managing the environment.
- **`curl`**: Used to test the API with an audio file.

---

## Setup Instructions

### Setting Up Conda Environment

 1. **Clone the Repository**:
   ```bash
   git clone https://github.com/anushka0415/NLP_blog_title
   cd speaker-diarization
   ```

1. **Create the Conda Environment**:
   - Ensure the `environment.yml` file is in the root folder (same level as `manage.py`).
   - Run the following command to create the environment:
     ```bash
     conda env create -f environment.yml
     ```

2. **Activate the Conda Environment**:
   - After the environment is created, activate it:
     ```bash
     conda activate llama_env
     ```

## Running the Django Application
### Start the Django Development Server:

  - Once the environment is set up, start the server with:
```bash
python manage.py runserver

```

 - The server will start at `http://127.0.0.1:8000/`.
 - You should see the Django app running locally.

## Testing the blog title API
### Using curl for Testing
- Test the API Endpoint:

- To test the title generator API, send a POST request with an audio file using `curl`:
```bash
curl -X POST http://127.0.0.1:8000/generate/ \
     -H "Content-Type: application/json" \
     -d '{"text": "a captivating story about adventure"}'

```
- Replace `a captivating story about adventure` with the actual text for which you want to test.
- Expected Response:
     - The response will be a JSON file containing the title results in `generated_titles` folder.
