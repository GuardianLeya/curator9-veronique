import telebot
bot = telebot.TeleBot('6810377813:AAHBdWlT05IaWtj3vWd6WNiUKOfIMUDe-W0')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет:) Напиши /morning , если ты только что проснулся; напиши /night , если ты ложишься спать; напиши /niceday , и у тебя будет хороший день)', parse_mode='Markdown')

@bot.message_handler(commands=['morning'])
def main(message):
    bot.send_message(message.chat.id, 'Доброе утро:)', parse_mode='Markdown')
    
@bot.message_handler(commands=['night'])
def main(message):
    bot.send_message(message.chat.id, 'Спокойной ночи:)', parse_mode='Markdown')
    
@bot.message_handler(commands=['niceday'])
def main(message):
    bot.send_message(message.chat.id, '[Желаю хорошего дня:)](https://pozdravok.com/pozdravleniya/lyubov/dobroe-utro/khoroshego-dnya/proza.htm)', parse_mode='Markdown')
    
bot.infinity_polling()
