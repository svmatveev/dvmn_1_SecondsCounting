from asyncio.windows_events import NULL
import pytimeparse

import ptbot


bot = NULL


def getBot():
    if bot == NULL:
        with open("./secrets/telegram_token.txt", "r") as file:
            secrets_list =  file.readlines()
            telegram_token = secrets_list[0].rstrip()
        bot = ptbot.Bot(telegram_token)
    return bot


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix) 


def notify_progress(secs_left, chat_id, message_id, total_delay):
    progress_bar = render_progressbar(total_delay, total_delay-secs_left)
    getBot().update_message(chat_id, message_id, f"Осталось {secs_left} секунд\n{progress_bar}")
    if secs_left == 0:
        bot.send_message(chat_id, "Время вышло")


def execute_with_period_set_in_mesage(chat_id, message):
    delay = pytimeparse.parse(message)
    if delay is None:
        message = "Некорректный формат времени задержки таймера"
        getBot().send_message(chat_id, message)
    else:
        message_id = bot.send_message(chat_id, "Запуск таймера")
        getBot().create_countdown(delay, notify_progress, chat_id=chat_id, message_id=message_id, total_delay=delay)


def main():
    getBot().reply_on_message(execute_with_period_set_in_mesage)
    getBot().run_bot()


if __name__ == "__main__":
    main()
