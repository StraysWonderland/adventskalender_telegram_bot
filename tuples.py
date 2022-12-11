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


data = list(zip(responses,items,item_url))
print(data)


calendar = [('Ich weiß dass dir folgendes gefallen wird ', 'Knoblauch!', 'https://aux.iconspalace.com/uploads/10997651451607759607.png'), ('Dein heutiges Geschenk: ', 'Knoblauch!', 'https://aux.iconspalace.com/uploads/10997651451607759607.png'), ('Herzlichen Glückwunsch, du erhälst ', 'Knoblauch!', 'https://aux.iconspalace.com/uploads/10997651451607759607.png'), ('Du musst trotzdem jeden Tag dein Tuerchen offenen um das Finale geschenk zu erhalten. Aber heute wird es ', 'Knoblauch!', 'https://aux.iconspalace.com/uploads/10997651451607759607.png'), ('Moment...Gibt es etwa jeden Tag das selbe? bestimmt nicht!!! aber heute schon ', 'Knoblauch!', 'https://aux.iconspalace.com/uploads/10997651451607759607.png'), ('Zur Feier des heutigen Tages schenke ich dir ', 'Ein schönes Glas Senf!', 'https://ih1.redbubble.net/image.828904801.5611/st,small,507x507-pad,600x600,f8f8f8.u4.jpg'), ('Frohlocke! Heute gibts ', 'Doch wieder Knoblauch!', 'https://aux.iconspalace.com/uploads/10997651451607759607.png'), ('Hoffe es ist noch nicht genug hiervon im Haus. Denn es gibt mehr ', 'Anti-Aging-Creme!!', 'https://emojigraph.org/media/apple/lotion-bottle_1f9f4.png'), ('Davon kannst du definitiv nicht genug haben: ', 'Butter!', 'https://cdn.mdr.de/nachrichten/welt/osteuropa/land-leute/butter-inflation-preise-102-resimage_v-variantSmall1x1_w-256.jpg?version=115'), ('Welch herzhafter Tag für ein herzhaftes Stück ', 'Eine saftige Packung Dosenravioli!', 'https://media.istockphoto.com/photos/canned-ravioli-picture-id459388797?k=6&m=459388797&s=170667a&w=0&h=uOIFeqQGyWsaKvCYpQRTO_o9IOsTXi63ofjJf9LyQ1A='), ('Its dangerous to go alone. Take this: ', 'Knoblauch!', 'https://aux.iconspalace.com/uploads/10997651451607759607.png'), ('Damit du im nächsten Jahr auch mal ans mittlere Regal kommst: ', 'Eine ganze Palette Fruchtzwerge!', 'https://www.darello.com/web/image/product.template/9882/image_256'), ('Gepriesen sei der ', 'Knoblauch!', 'https://aux.iconspalace.com/uploads/10997651451607759607.png'), ('Von mir, für dich ', 'Knoblauch!', 'https://aux.iconspalace.com/uploads/10997651451607759607.png'), ('Ach wie schön. Es ist ', 'Knoblauch!', 'https://aux.iconspalace.com/uploads/10997651451607759607.png'), ('Ach toll! Heute gibt es ', 'Knoblauch!', 'https://aux.iconspalace.com/uploads/10997651451607759607.png'), ('Wie schön wäre jetzt ein Stück ', 'Knoblauch!', 'https://aux.iconspalace.com/uploads/10997651451607759607.png'), ('Von ganzem Herzem ', 'Knoblauch!', 'https://aux.iconspalace.com/uploads/10997651451607759607.png'), ('Was du schon immer wolltest ', 'Knoblauch!', 'https://aux.iconspalace.com/uploads/10997651451607759607.png'), ('Was wäre jetzt besser als ', 'Knoblauch!', 'https://aux.iconspalace.com/uploads/10997651451607759607.png'), ('Du warst artig dieses Jahr! du erhälst ', 'Knoblauch!', 'https://aux.iconspalace.com/uploads/10997651451607759607.png'), ('Warst du etwa doch unartig? denn heute gib es ', 'Knoblauch!', 'https://aux.iconspalace.com/uploads/10997651451607759607.png'), ('Wir nähern uns dem Höhepunkt der Weihnachtszeit. Daher gibt es heute ', 'Knoblauch!', 'https://aux.iconspalace.com/uploads/10997651451607759607.png'), ('', 'Knoblauch!', 'https://aux.iconspalace.com/uploads/10997651451607759607.png'), ('', 'Knoblauch!', 'https://aux.iconspalace.com/uploads/10997651451607759607.png')]