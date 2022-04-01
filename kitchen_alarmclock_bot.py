import pytimeparse

import ptbot


def read_secrets():
    with open("./secrets/telegram_token.txt", "r") as file:
        return file.readlines()


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix) 


def notify_progress(secs_left, chat_id, message_id, total_delay):
    progress_bar = render_progressbar(total_delay, total_delay-secs_left)
    bot.update_message(chat_id, message_id, f"Осталось {secs_left} секунд\n{progress_bar}")
    if secs_left == 0:
        bot.send_message(chat_id, "Время вышло")


def execute_after_secs_specified(chat_id, message):
    delay = pytimeparse.parse(message)
    if delay is None:
        message = "Некорректный формат времени задержки таймера"
        bot.send_message(chat_id, message)
    else:
        message_id = bot.send_message(chat_id, "Запуск таймера")
        bot.create_countdown(delay, notify_progress, chat_id=chat_id, message_id=message_id, total_delay=delay)


if __name__ == "__main__":
    secrets_list = read_secrets()
    TG_TOKEN = secrets_list[0].rstrip()

    bot = ptbot.Bot(TG_TOKEN)
    bot.reply_on_message(execute_after_secs_specified)
    bot.run_bot()
