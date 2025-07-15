import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Carga variables de entorno
load_dotenv()
TOKEN = os.getenv("TELEGRAM_SHOP_TOKEN")

PRODUCTOS = {
    "es": [
        ("Llaveros Pasha Collection", "Llaveros coloridos, cute y divertidos, para que lleves tu estilo a todas partes.", "https://pashalove.com/producto/pasha-collection-keychains/"),
        ("Llaveros Sweet Collection", "Llaveros inspirados en macarons, colores vivos y diseño adorable.", "https://pashalove.com/producto/sweet-macaron-keychains/"),
        ("Llaveros Happy Collection", "Llaveros con forma de perrito globo, súper vibrantes y llenos de felicidad.", "https://pashalove.com/producto/cute-balloon-dog-keychain/"),
        ("Llaveros Puffy Collection", "Llaveros estilo puffy, colores brillantes, textura divertida.", "https://pashalove.com/producto/puffy-collection/"),
        ("Llaveros Bubble Collection", "Llaveros con bolitas coloridas, para un toque chic y bold.", "https://pashalove.com/producto/bubble-collection/"),
        ("Llaveros Teachy Collection", "Llaveros didácticos, con frases y colores llamativos.", "https://pashalove.com/producto/teachy-collection/"),
        ("Llaveros Glam Collection", "Llaveros con mucho brillo y glam, para destacar a donde vayas.", "https://pashalove.com/producto/glam-collection/"),
        ("Hearts & Kisses Water Bottle", "Botella en forma de corazón, rosa, girly y aesthetic.", "https://pashalove.com/producto/hearts-and-kisses/"),
        ("Love Candy Steel Tumbler", "Tumbler de acero, diseño candy colorido, pastel y llamativo.", "https://pashalove.com/producto/love-candy-steel-tumbler/"),
        ("Love & Sip Tumbler", "Tumbler elegante, ideal para regalar.", "https://pashalove.com/producto/love-sip-tumbler/"),
        ("Gradient Glow Tumbler", "Tumbler estilo ombré con colores vibrantes.", "https://pashalove.com/producto/https-pashalove-com-producto-gradient-glow-tumbler/"),
        ("Love Heart Sports Bottle", "Botella con corazón, vibes cute para gym o escuela.", "https://pashalove.com/producto/love-heart-sports-bottle/"),
        ("Cozy Pup Blanket", "Manta vibrante con estampado de perrito globo.", "https://pashalove.com/producto/cozy-pup-blanket/"),
        ("Plush Heart Pillow – Let Me Sleep", "Almohada en forma de corazón, rosa, extra suave.", "https://pashalove.com/producto/plush-heart-pillow/"),
        ("XO Plush Pillow", "Cojín XO rosa y blanco, aesthetic y cute.", "https://pashalove.com/producto/xo-plush-pillow/"),
        ("Velvet Heart Pillow", "Almohada de terciopelo en forma de corazón, elegante y suave.", "https://pashalove.com/producto/velvet-heart-pillow/"),
        ("Cute & Cozy Kitchen Towel Set", "Set de toallas (3 variaciones: cat, hearts, lips), cada set incluye 3 toallas. Colores y estampados vibrantes.", "https://pashalove.com/producto/cute-cozy-kitchen-towels/"),
        ("Happy Vibes Collection – Coasters", "Colección de portavasos con 3 estilos: checkered, optical illusion y smiley face. Juego de 6, colores alegres.", "https://pashalove.com/producto/happy-vibes/"),
        ("Vibrant Smiley Cosmetic Bag", "Cosmetic bag con smileys coloridos, práctica y divertida.", "https://pashalove.com/producto/vibrant-smiley-bag/"),
        ("Smiley Rope Handle Tote Bag", "Bolsa tote con asas de cuerda y smileys, casual y divertida.", "https://pashalove.com/producto/smiley-rope-tote-bag/"),
        ("Hello Kitty Dinner Set", "Set de cena Hello Kitty, cute y colorido.", "https://pashalove.com/producto/hello-kitty-dinner-set/"),
        ("Ver todo el catálogo", "Descubre todos los productos vibrantes y cute aquí:", "https://pashalove.com/")
    ],
    "en": [
        ("Pasha Collection Keychains", "Colorful, cute and fun keychains to brighten your day, wherever you go!", "https://pashalove.com/producto/pasha-collection-keychains/"),
        ("Sweet Collection Keychains", "Macaron-inspired keychains, vibrant colors and adorable design.", "https://pashalove.com/producto/sweet-macaron-keychains/"),
        ("Happy Collection Keychains", "Balloon dog-shaped keychains, super vibrant and full of happiness.", "https://pashalove.com/producto/cute-balloon-dog-keychain/"),
        ("Puffy Collection Keychains", "Puffy style keychains, bright colors, fun texture.", "https://pashalove.com/producto/puffy-collection/"),
        ("Bubble Collection Keychains", "Keychains with colorful beads, for a chic and bold touch.", "https://pashalove.com/producto/bubble-collection/"),
        ("Teachy Collection Keychains", "Didactic keychains, with phrases and bold colors.", "https://pashalove.com/producto/teachy-collection/"),
        ("Glam Collection Keychains", "Super shiny and glam keychains, perfect to stand out.", "https://pashalove.com/producto/glam-collection/"),
        ("Hearts & Kisses Water Bottle", "Heart-shaped bottle, pink, girly and aesthetic.", "https://pashalove.com/producto/hearts-and-kisses/"),
        ("Love Candy Steel Tumbler", "Steel tumbler, colorful candy design, pastel and bold.", "https://pashalove.com/producto/love-candy-steel-tumbler/"),
        ("Love & Sip Tumbler", "Elegant tumbler, ideal as a gift.", "https://pashalove.com/producto/love-sip-tumbler/"),
        ("Gradient Glow Tumbler", "Ombre tumbler with vibrant colors.", "https://pashalove.com/producto/https-pashalove-com-producto-gradient-glow-tumbler/"),
        ("Love Heart Sports Bottle", "Bottle with heart, cute vibes for gym or school.", "https://pashalove.com/producto/love-heart-sports-bottle/"),
        ("Cozy Pup Blanket", "Vibrant blanket with balloon dog print.", "https://pashalove.com/producto/cozy-pup-blanket/"),
        ("Plush Heart Pillow – Let Me Sleep", "Heart-shaped pillow, pink, extra soft.", "https://pashalove.com/producto/plush-heart-pillow/"),
        ("XO Plush Pillow", "XO pillow in pink and white, aesthetic and cute.", "https://pashalove.com/producto/xo-plush-pillow/"),
        ("Velvet Heart Pillow", "Velvet pillow in heart shape, elegant and soft.", "https://pashalove.com/producto/velvet-heart-pillow/"),
        ("Cute & Cozy Kitchen Towel Set", "Set of towels (3 styles: cat, hearts, lips), each set includes 3 towels. Vibrant colors and prints.", "https://pashalove.com/producto/cute-cozy-kitchen-towels/"),
        ("Happy Vibes Collection – Coasters", "Set of coasters in 3 styles: checkered, optical illusion, smiley face. Set of 6, cheerful colors.", "https://pashalove.com/producto/happy-vibes/"),
        ("Vibrant Smiley Cosmetic Bag", "Cosmetic bag with colorful smileys, practical and fun.", "https://pashalove.com/producto/vibrant-smiley-bag/"),
        ("Smiley Rope Handle Tote Bag", "Tote bag with rope handles and smileys, casual and fun.", "https://pashalove.com/producto/smiley-rope-tote-bag/"),
        ("Hello Kitty Dinner Set", "Hello Kitty dinner set, cute and colorful.", "https://pashalove.com/producto/hello-kitty-dinner-set/"),
        ("See full catalog", "Discover all our vibrant, cute products here:", "https://pashalove.com/")
    ]
}

# Guardamos idioma del usuario en memoria temporal
user_lang = {}

def start(update, context):
    msg = (
        "¡Hola! / Hi!\n"
        "¿En qué idioma quieres chatear?\n"
        "What language do you prefer?\n\n"
        "1️⃣ Español\n"
        "2️⃣ English"
    )
    update.message.reply_text(msg)

def handle_message(update, context):
    user_id = update.message.from_user.id
    text = update.message.text.strip().lower()

    # Si el usuario no ha elegido idioma
    if user_id not in user_lang:
        if text in ["1", "español", "es"]:
            user_lang[user_id] = "es"
            return show_menu(update, "es")
        elif text in ["2", "english", "en"]:
            user_lang[user_id] = "en"
            return show_menu(update, "en")
        else:
            update.message.reply_text("Elige 1️⃣ para Español o 2️⃣ for English.\nChoose 1️⃣ for Spanish or 2️⃣ for English.")
            return

    lang = user_lang[user_id]
    productos = PRODUCTOS[lang]

    # Mostrar menú si el usuario escribe "menú" o "menu"
    if text in ["menu", "menú"]:
        return show_menu(update, lang)

    # Si escoge una opción de producto
    try:
        idx = int(text) - 1
        if 0 <= idx < len(productos):
            nombre, desc, link = productos[idx]
            update.message.reply_text(f"{nombre}:\n{desc}\n{link}")
            update.message.reply_text("¿Quieres ver otro producto? Escribe el número o 'menú' para volver.\nWant to see another product? Type the number or 'menu' to go back.")
        else:
            raise Exception()
    except:
        update.message.reply_text(
            "No entendí tu mensaje. Por favor escribe el número del producto o 'menú' para volver.\n"
            "I didn't understand. Please type the product number or 'menu' to go back."
        )

def show_menu(update, lang):
    productos = PRODUCTOS[lang]
    # Números normales en vez de emojis
    menu = "\n".join([f"{i+1}. {nombre}" for i, (nombre, _, _) in enumerate(productos)])
    if lang == "es":
        update.message.reply_text("¿Qué te gustaría ver? Elige una colección o producto vibrante:\n" + menu)
    else:
        update.message.reply_text("What would you like to see? Choose a vibrant collection or product:\n" + menu)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
