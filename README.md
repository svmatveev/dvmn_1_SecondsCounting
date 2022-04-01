# Seconds timer

[Devman](https://dvmn.org/modules/meeting-python/lesson/timer-in-telegram) Task 5 implementation of Python introduction module.

This is a simple cooking-helper telegram bot.
Supporting features:
- Cooking timer


**Prerequisites**
---
Telegram bot should be registered using @BotFather. Api-token should be found.

Telegram bot api-roken should be stored at "secrets" folder inside "telegram_token.txt" file. So, the path to api key should be resolved by "./secrets/telegram_token.txt" path from "kitchen_alarmclock_bot.py" script file.

Python3 should be installed

Additional modules required:
- pytimeparse==1.1.8
- telegram==0.0.1
- [ptbot.py](https://gist.github.com/dvmn-tasks/e603319227656c63e486831bf4673f26) Should be inside the folder where "kitchen_alarmclock_bot.py" is placed. ([ptbot.py docs](https://dvmn.org/encyclopedia/modules/ptbot_docs/))

Dependencies can be solved by running:
```
pip install -r requirements.txt
``` 

**Usage**
---
1. You can join newly-created bot using Telegram
2. Run kitchen_alarmclock_bot.py from command line:
```
$ python3 kitchen_alarmclock_bot.py
```
3. Send */start* command
4. Now you can send the time you want to countdown

**Authors**
---
[Sergey M](mailto:svmatveev1988@yandex.ru)

**License**
---
This project is licensed under the MIT License - see the LICENSE.md file for details