import ptbot
import random



def read_secrets():
    with open("./secrets/telegram_token.txt", "r") as file:
        return file.readlines()


def choose():
    answes = ("да", "нет", "это возможно")
    choice = random.choice(answes)
    message = f"Думаю, {choice}"
    bot.send_message(TG_CHAT_ID, message)
    
if __name__ == "__main__":
    
    secrets_list = read_secrets()
    TG_TOKEN = secrets_list[0].rstrip()
    TG_CHAT_ID = secrets_list[1].rstrip()

    bot = ptbot.Bot(TG_TOKEN)
    choose()
    choose()
    



