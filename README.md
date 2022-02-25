# Introduction

This is a proof of concept for an anonymous chat.  
You can find strangers to talk through the program.

## Usage

Requires Python3 (It's tested on python 3.7.3)

1. Clone this project to your server side.
    > git clone https://github.com/keoy7am/chat_match_telegram_bot.git
2. Install python dependencies with pip
    > pip3 install -r requirements.txt

3. Setting up your bot config
    Config File Path:
    > bot_poc/config.py

    The following are the configs you need to adjust:
    - BOT_API_KEY
        > "1234567890:ABCDEFGHIJKKKKKKKKKK" (example)  
        > If you don't have token,check [here](https://core.telegram.org/bots).

    - BOT_HOOK_URL
        > "https://Domainnnnnnnnnnnnn/hook" (example)  
        __Note: Your protocol must be https!__

    _Please put your bot token and webhook callback uri in the file._

## Supported forwarding message types

- text
- photo
- video
- document
- animation
- voice
- sticker
- video_note

## TODO List

- Decoupling data access layer
  - The program is depend on the Redis database for chat pairing data access now.
If you abstract the data access behavior,  
You can support the use of other databases.  
- Implement something to prevent resource competition  
  - When the number of users is large,  
There may be a situation where a queue is matched to different people.  
- Globalization
  - Match by user's language
  - Reply based on user's language (Default:English)
- New Features
  - Add gender selection