#!/bin/bash

# Fix timezone issue (Telegram msg_id error)
export TZ=UTC
date

# Clone the repo
if [ -z "$UPSTREAM_REPO" ]
then
  echo "Cloning main Repository"
  git clone https://github.com/TG-V4MP1R3/Alexa-V2.git Alexa-V2
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO"
  git clone "$UPSTREAM_REPO" Alexa-V2
fi

cd Alexa-V2

# Install necessary dependencies
pip install setuptools==65.5.1
pip install dnspython==2.4.2

# Install all other requirements
pip install -U -r requirements.txt

# Safety flag for time sync (Pyrogram edge case)
export PYROGRAM_TIME_FIX=1

echo "Starting Alexa-v2....🔥"
python3 bot.py
