#!/bin/bash

# Fix timezone (msg_id sync)
export TZ=Asia/Kolkata
date

# Optional: try time sync (only if Render allows)
which ntpdate && ntpdate -u time.google.com || true

# Clone repo
if [ -z "$UPSTREAM_REPO" ]; then
  echo "Cloning main Repository"
  git clone https://github.com/TG-V4MP1R3/Alexa-V2.git Alexa-V2
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO"
  git clone "$UPSTREAM_REPO" Alexa-V2
fi

cd Alexa-V2

# Fix deps
pip install setuptools==65.5.1
pip install dnspython==2.4.2
pip install -U -r requirements.txt

# Run bot
echo "Starting Alexa-v2....🔥"
python3 bot.py

# Install all other requirements
pip install -U -r requirements.txt

# Safety flag for time sync (Pyrogram edge case)
export PYROGRAM_TIME_FIX=1

echo "Starting Alexa-v2....🔥"
python3 bot.py
