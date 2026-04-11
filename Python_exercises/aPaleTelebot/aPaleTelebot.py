import json
import telebot


def send_mensagem(texto, chat):
    bot.send_message(chat.id, texto, "HTML")


secrets = {}
with open(f"./secrets.json") as secrets:
    secrets = json.load(secrets)
apiKey = secrets["telebotApiKey"]

bot = telebot.TeleBot(apiKey)



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Saudações meu rei!\n")

@bot.message_handler(commands=['luan'])
def send_welcome(message):
    bot.reply_to(message, "bunda\nfurry gay\nlmao")

@bot.message_handler(func=lambda message: message.text.lower() == "bunda")
def bunda(message):
    send_mensagem("bunda", message.chat)

@bot.message_handler(func=lambda message:  "bunda" in message.text.lower())
def bunda(message):
    send_mensagem("[texto irrelevante] bunda [texto irrelevante]", message.chat)

@bot.message_handler(func=lambda mensagem: True)
def nao_reconhecido(mensagem):
    send_mensagem('Me mande "bunda" que eu irei te responder!', mensagem.chat)


bot.infinity_polling()