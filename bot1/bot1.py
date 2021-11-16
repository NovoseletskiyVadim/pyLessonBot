

import config
import telebot


bot=telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=["text"])
def repeat_allMessages(message):

    bot.send_message(config.GrID, message.text)


if __name__=='__main__':
    bot.infinity_polling()
