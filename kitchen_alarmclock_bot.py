from tokenize import String
import ptbot



def read_secrets():
    with open("./secrets/telegram_token.txt", "r") as file:
        return file.readlines()

if __name__ == "__main__":
    secrets_list = read_secrets()
    TG_TOKEN = secrets_list[0].rstrip()
    TG_CHAT_ID = secrets_list[1].rstrip()
    print(TG_TOKEN, TG_CHAT_ID, sep="\n")
    bot = ptbot.Bot(TG_TOKEN)
    bot.send_message(TG_CHAT_ID, "Бот запущен")