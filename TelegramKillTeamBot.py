import telebot, os, Token

PATH = os.path.abspath(__file__ + "/.." + "/..")

bot = telebot.TeleBot("5858840614:AAERIbuBD7PPgDrXjChzTe2q8ZvpzzI-jqE")
question_list = []
owner_id = 1109954939


#main commands
@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message,"Привет! Я - оффициальный бот KillTeam. Написан лично создателем. Чтобы узнать что я умею напиши: /help")


@bot.message_handler(commands=["discord"])
def discord(message):
    bot.reply_to(message,'[KillTeam Discord](https://discord.gg/sPUSqXFt9f)', parse_mode='MarkdownV2')


@bot.message_handler(commands=["help"])
def help(message):
    bot.reply_to(message, "Вот что я умею:\n1./discord - получение ссылки на оффициальный дискорд сервер\n2./questiontoadm - Вы можете задать вопрос к администрации бота. Оффтоп - бан на 2 часа.")


