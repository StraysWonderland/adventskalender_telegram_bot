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
    "Ich weiß dass dir folgendes gefallen wird ", # Day 0 - wont get drafted
    "Dein heutiges Geschenk: ", #1
    "Herzlichen Glückwunsch, du erhälst ", #2
    "Du musst trotzdem jeden Tag dein Tuerchen offenen um das Finale geschenk zu erhalten. Aber heute wird es ", #3
    "Moment...Gibt es etwa jeden Tag das selbe? bestimmt nicht!!! aber heute schon ", #4
    "Zur Feier des heutigen Tages schenke ich dir ", #5
    "Frohlocke! Heute gibts ", #6
    "Hoffe es ist noch nicht genug hiervon im Haus. Denn es gibt mehr ", #7
    "Davon kannst du definitiv nicht genug haben: ", #8
    "Welch herzhafter Tag für ein herzhaftes Stück ", #9
    "Its dangerous to go alone. Take this: ", #10
    "Damit du im nächsten Jahr auch mal ans mittlere Regal kommst: ", #11
    "Gepriesen sei der ", #12
    "Von mir, für dich ", #13
    "Ach wie schön. Es ist ", #14
    "das hast du wohl verpasst -.-", #15
    "Warst du etwa unartig und hast das gestrige Türchen verpasst? denn heute gib es ", #16
    "Ach toll! Heute bekommst du endlich ", #17
    "Wie schön wäre jetzt ", #18
    "Von ganzem Herzem ", #19
    "Heute etwas persönliches ", #20
    "Was du schon immer wolltest ", #21
    "Du warst doch artig dieses Jahr! du erhälst ", #22
    "Wir nähern uns dem Höhepunkt der Weihnachtszeit. Daher gibt es heute ", #23
    "Der Finale Tag!" # Day 24
]

# the items to reveal. send these in progressing order based on current day.
items = [
    "Knoblauch!", #Day 0 - so wont get drafted currently
    "Knoblauch!", # Day 1
    "Knoblauch!", # Day 2
    "Knoblauch!", # Day 3
    "Knoblauch!", # Day 4
    "Ein schönes Glas Senf!", #5
    "Doch wieder Knoblauch!", #6
    "Anti-Aging-Creme!!", #7
    "Butter!", #8
    "Eine saftige Packung Dosenravioli!", #9
    "Knoblauch!", #10
    "Eine ganze Palette Fruchtzwerge!", #11
    "Knoblauch!", #12
    "Knoblauch!", #13
    "Ja nichts halt!", #14
    "Eine ordentliche Tracht Prügel!", #15
    "Zitronen!", #16
    "Eine warme Umarmung von mir (rechts) für dich (links)", #17
    "Knoblauch!", #18
    "Eine ordentliche Tracht Prügel!", #19
    "Ein Pfund Hack!", #20
    "Knoblauch!", #21
    "Knoblauch!", #22
    "Knoblauch!", #23
    "Knoblauch!" # Day 24 - this should be the "best" gift
]

item_url = [
    "https://aux.iconspalace.com/uploads/10997651451607759607.png", # 0 garlic
    "https://aux.iconspalace.com/uploads/10997651451607759607.png", # 1 garlic
    "https://aux.iconspalace.com/uploads/10997651451607759607.png", # 2 garlic
    "https://aux.iconspalace.com/uploads/10997651451607759607.png", # 3 garlic
    "https://aux.iconspalace.com/uploads/10997651451607759607.png", # 4 garlic
    "https://ih1.redbubble.net/image.828904801.5611/st,small,507x507-pad,600x600,f8f8f8.u4.jpg", # 5 mustard
    "https://aux.iconspalace.com/uploads/10997651451607759607.png", # 6 garlic
    "https://emojigraph.org/media/apple/lotion-bottle_1f9f4.png",   # 7 creme emojie
    "https://cdn.mdr.de/nachrichten/welt/osteuropa/land-leute/butter-inflation-preise-102-resimage_v-variantSmall1x1_w-256.jpg?version=115", #butter
    "https://media.istockphoto.com/photos/canned-ravioli-picture-id459388797?k=6&m=459388797&s=170667a&w=0&h=uOIFeqQGyWsaKvCYpQRTO_o9IOsTXi63ofjJf9LyQ1A=", # ravioli
    "https://aux.iconspalace.com/uploads/10997651451607759607.png", # 10 garlic
    "https://www.darello.com/web/image/product.template/9882/image_256", # 11 fruchtzwerge
    "https://aux.iconspalace.com/uploads/10997651451607759607.png", # 12 garlic
    "https://aux.iconspalace.com/uploads/10997651451607759607.png", # 13 garlic
    "https://imgs.search.brave.com/MZBcptfu1Q25GQKqbzRREnm9NH1GApqb9lfgIy1JMbc/rs:fit:256:256:1/g:ce/aHR0cDovL2Rvd25s/b2FkczIuZXNyaS5j/b20vc3VwcG9ydC9U/ZWNoQXJ0aWNsZXMv/YmxhbmsyNTYucG5n",
    "https://t3.ftcdn.net/jpg/02/88/92/54/360_F_288925438_JYRinW7uEvLWameTGgSTfQbuxFVQHTpR.jpg", # 15 schläge
    "https://img-9gag-fun.9cache.com/photo/a7ErEwr_700bwp.webp", # 16 zitronen
    "https://i.redd.it/fdxsmm43jau71.jpg", # 17 hug
    "https://cdn.shopify.com/s/files/1/0801/6115/products/Hackfleisch_gemischt_large_19be004b-d021-4bf6-b90d-49ae49680feb_large.png?v=1432139188", # 18 Pfund Hack
    "https://t3.ftcdn.net/jpg/02/88/92/54/360_F_288925438_JYRinW7uEvLWameTGgSTfQbuxFVQHTpR.jpg", # 19 schläge
    "https://cdn.shopify.com/s/files/1/0801/6115/products/Hackfleisch_gemischt_large_19be004b-d021-4bf6-b90d-49ae49680feb_large.png?v=1432139188", # 20 Pfund Hack
    "https://aux.iconspalace.com/uploads/10997651451607759607.png", # 21 garlic
    "https://aux.iconspalace.com/uploads/10997651451607759607.png", # 22 garlic
    "https://aux.iconspalace.com/uploads/10997651451607759607.png", # 23 garlic
    "https://aux.iconspalace.com/uploads/10997651451607759607.png", # 24 garlic
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

@bot.message_handler(commands=['oeffnen'])
def oeffnen(update, context): 
    text = "Welches Tuerchen willst du oeffnen?."
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, day_handler)

def day_handler(message):
    day = message.text
    if day > len(responses):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Glückwunsch, du hast das Ende erreicht! Heute kein Knoblauch für dich. Aber dafür frohe Weihnachten!!")
   
    '''
    Craft the response message text by getting text flair and item based on day
    And get image to attach to message
    '''
    response = responses[day] + "..." + items[day] 
    logger.info("current day: " + str(day) + " " + "response text: " + response)
    context.bot.send_message(message.chat.id, response, parse_mode="Markdown")
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