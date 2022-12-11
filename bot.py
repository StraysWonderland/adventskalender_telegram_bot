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

# Text message leading to the item reveal. These can be send in random order
responses = [
    #Day 0 - so wont get drafted currently
    "Ich weiß dass dir folgendes gefallen wird ",
    "Dein heutiges Geschenk: ",
    "Herzlichen Glückwunsch, du erhälst ",
    "Du musst trotzdem jeden Tag dein Tuerchen offenen um das Finale geschenk zu erhalten. Aber heute wird es ",
    "Moment...Gibt es etwa jeden Tag das selbe? bestimmt nicht!!! aber heute schon ",
    "Zur Feier des heutigen Tages schenke ich dir ",
    "Frohlocke! Heute gibts ",
    "Hoffe es ist noch nicht genug hiervon im Haus. Denn es gibt mehr ",
    "Davon kannst du definitiv nicht genug haben: ",
    "Welch herzhafter Tag für ein herzhaftes Stück ",
    "Its dangerous to go alone. Take this: ",
    "Damit du im nächsten Jahr auch mal ans mittlere Regal kommst: ",
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
    "Wir nähern uns dem Höhepunkt der Weihnachtszeit. Daher gibt es heute ", #Day 21
    "",
    "",
    "Der Finale Tag!" # Day 24
]

# the items to reveal. send these in progressing order based on current day.
items = [
    "Knoblauch!", #Day 0 - so wont get drafted currently
    "Knoblauch!", # Day 1
    "Knoblauch!", # Day 2
    "Knoblauch!", # Day 3
    "Knoblauch!", # Day 4
    "Ein schönes Glas Senf!",
    "Doch wieder Knoblauch!",
    "Anti-Aging-Creme!!",
    "Butter!",
    "Eine saftige Packung Dosenravioli!",
    "Knoblauch!",
    "Eine ganze Palette Fruchtzwerge!",
    "Knoblauch!",
    "Knoblauch!",
    "Knoblauch!",
    "Knoblauch!",
    "Knoblauch!",
    "Knoblauch!",
    "Knoblauch!",
    "Knoblauch!",
    "Knoblauch!",
    "Knoblauch!",
    "Knoblauch!",
    "Knoblauch!",
    "Knoblauch!" # Day 24 - this should be the "best" gift
]

item_url = [
    "https://aux.iconspalace.com/uploads/10997651451607759607.png", # garlic
    "https://aux.iconspalace.com/uploads/10997651451607759607.png", # garlic
    "https://aux.iconspalace.com/uploads/10997651451607759607.png", # garlic
    "https://aux.iconspalace.com/uploads/10997651451607759607.png", # garlic
    "https://aux.iconspalace.com/uploads/10997651451607759607.png", # garlic
    "https://ih1.redbubble.net/image.828904801.5611/st,small,507x507-pad,600x600,f8f8f8.u4.jpg", # mustard
    "https://aux.iconspalace.com/uploads/10997651451607759607.png", # garlic
    "https://emojigraph.org/media/apple/lotion-bottle_1f9f4.png", # creme emojie
    "https://cdn.mdr.de/nachrichten/welt/osteuropa/land-leute/butter-inflation-preise-102-resimage_v-variantSmall1x1_w-256.jpg?version=115", #butter
    "https://media.istockphoto.com/photos/canned-ravioli-picture-id459388797?k=6&m=459388797&s=170667a&w=0&h=uOIFeqQGyWsaKvCYpQRTO_o9IOsTXi63ofjJf9LyQ1A=", # ravioli
    "https://aux.iconspalace.com/uploads/10997651451607759607.png", # garlic
    "https://www.darello.com/web/image/product.template/9882/image_256", # fruchtzwerge
    "https://aux.iconspalace.com/uploads/10997651451607759607.png", # garlic
    "https://aux.iconspalace.com/uploads/10997651451607759607.png", # garlic
    "https://aux.iconspalace.com/uploads/10997651451607759607.png", # garlic
    "https://aux.iconspalace.com/uploads/10997651451607759607.png", # garlic
    "https://aux.iconspalace.com/uploads/10997651451607759607.png", # garlic
    "https://aux.iconspalace.com/uploads/10997651451607759607.png", # garlic
    "https://aux.iconspalace.com/uploads/10997651451607759607.png", # garlic
    "https://aux.iconspalace.com/uploads/10997651451607759607.png", # garlic
    "https://aux.iconspalace.com/uploads/10997651451607759607.png", # garlic
    "https://aux.iconspalace.com/uploads/10997651451607759607.png", # garlic
    "https://aux.iconspalace.com/uploads/10997651451607759607.png", # garlic
    "https://aux.iconspalace.com/uploads/10997651451607759607.png", # garlic
    "https://aux.iconspalace.com/uploads/10997651451607759607.png", # Day 24
]


'''
Define a few command handlers. These usually take the two arguments update and context. 
Error handlers also receive the raised TelegramError object in error.
'''
def start(update, context):
    # Send a message when the command /start is issued
    update.message.reply_text('Hallo! ich habe einen einzigartigen Adventskalender für dich gebastelt')

'''
Open todays door and reveal corresponding item along with a text flair and photo
'''
def tuer(update, context):
    
    day = datetime.datetime.today().day
    if day > len(responses):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Glückwunsch, du hast das Ende erreicht! Heute kein Knoblauch für dich. Aber dafür frohe Weihnachten!!")
   
    '''
    Craft the response message text by getting text flair and item based on day
    And get image to attach to message
    '''
    response = responses[day] + "..." + items[day] 
    logger.info("current day: " + str(day) + " " + "response text: " + response)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=item_url[day], caption=response)

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