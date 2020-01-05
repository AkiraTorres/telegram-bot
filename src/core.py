from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

#from conf.settings import TELEGRAM_TOKEN, HTTP_CATS_URL
TELEGRAM_TOKEN = "917350378:AAFJiETmnzcBXKU0mnJ6BTMx9QvER5P3S7k"
HTTP_CATS_URL = "https://http.cat/"
HTTP_DOGS_URL = "https://httpstatusdogs.com/"
def start(bot, update):
    response_message = "=^._.^="
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def http_cats(bot, update, args):
    bot.sendPhoto(
        chat_id=update.message.chat_id,
        photo=HTTP_CATS_URL + args[0]
    )

def http_dogs(bot, update, args):
    bot.sendPhoto(
        chat_id=update.message.chat_id,
        photo=HTTP_DOGS_URL + args[0]
    )

def unknown(bot, update):
    response_message = "Meow? =^._.^="
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )

def help(bot, update):
    responde_message = "Type '/help' to show this message.\
                        \nType '/http [http-code-error]' to receive the corresponding cat image.\
                        \nType '/dogs [http-code-error]' to receive the corresponding dog image."
    bot.send_message(
        chat_id=update.message.chat_id,
        text=responde_message
    )



def main():
    updater = Updater(token=TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        CommandHandler('start', start)
    )
    dispatcher.add_handler(
        CommandHandler('http', http_cats, pass_args=True)
    )
    dispatcher.add_handler(
        CommandHandler('dogs', http_dogs, pass_args=True)
    )
    dispatcher.add_handler(
        CommandHandler('help', help)
    )
    dispatcher.add_handler(
        MessageHandler(Filters.command, unknown)
    )

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()