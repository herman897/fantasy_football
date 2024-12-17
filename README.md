# Fantasy Football Advisor

Hello! Welcome to our fantasy football app which contains a fantasy football player comparison tool (ff report) and a fantasy football web app.

## Setup

Create and activate a virtual environment (first time only):

```sh
conda create -n ff-env python=3.10
```

Activate the environment (whenever revisiting):

```sh
conda activate ff-env
```

Install packages:
```sh
pip install -r requirements.txt
```

[Obtain an API Key](https://rapidapi.com/tank01/api/tank01-nfl-live-in-game-real-time-statistics-nfl) from Tank01's NFL Live In-Game Real Time Statistics NFL, available for free (1,000 requests per month). Simply sign up for an account on Nokia's Rapid API Marketplace, and subscribe under the free tier to Tank01's API. 

Next, create your own ".env" file in your repository folder and add your own Tank01 Rapid API Key and Host follows:

```sh
# this is the ".env" file (which is ignored from version control via the .gitignore file)

x_rapidapi_host="____________"
x_rapidapi_key="____________"
```

## Usage 

Run the ff report:

```sh
python -m app.ff
```

Run the web app:

(then view in the browser your [local host](http://127.0.0.1:5000/), please find instructions on navigating the web app on its home page)

```sh
flask run
```

## Testing

Run tests:

```sh
pytest
```



