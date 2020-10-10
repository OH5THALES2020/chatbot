# Thales Ocean Hackathon 2020

## Prerequisites

- python 3.6.8 or greater
- python3 venv module should be installed

## Installation

```sh
# clone this repository
git clone

# create a virtualenv
python3 -m venv .venv

# install python requirements
source .venv/bin/activate
pip install -r requirements.txt
```

## Executing the webserver

```sh
python3 hackathon_2020/main_entry.py
```

## Exposing webserver over https with ngrok

```sh
# download ngrok from here https://ngrok.com/download

# then

$NGROK_INSTALL_DIR/ngrok http http://localhost:8456
```
