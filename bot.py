from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random
import logging
import os
import datetime 


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

PORT = int(os.environ.get('PORT', 80))

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
HEROKUURL = os.getenv('HEROKU_URL')
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

responses = [
    "Ich weiß dass dir folgendes gefallen wird ",
    "Dein heutiges Geschenk: ",
    "Moment...Gibt es etwa jeden Tag das selbe? bestimmt nicht!!! aber heute schon ",
    "Herzlichen Glückwunsch, du erhälst ",
    "Du musst trotzdem jeden Tag dein Tuerchen offenen um das Finale geschenk zu erhalten. Aber heute wird es ",
    "Zur Feier des heutigen Tages schenke ich dir ",
    "Frohlocke! Heute gibts ",
    "Hoffe es ist noch nicht genug hiervon im Haus. Denn es gibt mehr ",
    "Its dangerous to go alone. Take this: ",
    "Welch herzhafter Tag für ein herzhaftes Stück ",
    "Gepriesen sei der ",
    "Von mir, für dich ",
    "Ach wie schön. Es ist ",
    "Ach toll! Heute gibt es ",
    "Wie schön wäre jetzt ein Stück ",
    "Von ganzem Herzem ",
    "Was du schon immer wolltest ",
    "Was wäre jetzt besser als ",
    "Du warst artig dieses Jahr! du erhälst ",
    "Warst du etwa doch unartig? denn heute gib es ",
    "Wir nähern uns dem Höhepunkt der Weihnachtszeit. Daher gibt es heute "
]

item = "Knoblauch!"




# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    # Send a message when the command /start is issued
    update.message.reply_text('Hallo! ich habe einen einzigartigen Adventskalender für dich gebastelt')


def tuer(update, context):
    
    day = datetime.datetime.today().day
    if day > len(responses):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Glückwunsch, du hast das Ende erreicht! Heute kein Knoblauch für dich. Aber dafür frohe Weihnachten!!")
    response = responses[day] + "..." + item
    # send message
    #context.bot.send_message(chat_id=update.effective_chat.id, text=response)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('image.png', "rb"), caption=response)

# linking the /random command with the function random() 
day_handler = CommandHandler('tuer', tuer)
dispatcher.add_handler(day_handler)


updater.start_webhook(
        listen="0.0.0.0",
        port=int(PORT),
        url_path=TOKEN,
        webhook_url='https://pollyadventskalender.herokuapp.com/' + TOKEN
    )

updater.idle()