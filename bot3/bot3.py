
import config
import telebot


bot=telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=["text"])
def repeat_allMessages(message):

    print("message.chat.id=",message.chat.id)

    bot.send_message(config.Chanel_2, message.text)


if __name__=='__main__':
    bot.infinity_polling()
