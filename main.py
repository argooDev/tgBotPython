import telebot

#tg bot api
bot = telebot.TeleBot(
    '6528279192:AAHSAdlKazDMFEfkBNyJW1EJBDSDp7N2wK8'
)

#this function allows to start bot

@bot.message_handler(
    #here we can set command, when called, the function below will work
    # You can add as many square brackets as you like
    commands=['start']
)
def main(message):
    bot.send_message(message.chat.id,'Hello')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,'Help info')
    # Also we can add several parameter : parse_html. Who allows format text in html





#Allow infinity use bot, he can works Always
bot.polling(none_stop=True)