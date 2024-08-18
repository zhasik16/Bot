import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Initialize the bot with your token
bot = telebot.TeleBot("YOUR TOKEN HERE")

# Handler for any text message
@bot.message_handler(func=lambda message: True)
def send_message_with_inline_keyboard(message):
    # Create an inline keyboard markup
    markup = InlineKeyboardMarkup()
    
    # Add buttons to the markup
    button1 = InlineKeyboardButton("Button 1", callback_data="button1")
    button2 = InlineKeyboardButton("Button 2", callback_data="button2")
    
    # Add buttons to the keyboard
    markup.add(button1, button2)
    
    # Send a message with the inline keyboard
    bot.send_message(message.chat.id, "Here are some options:", reply_markup=markup)

# Handler for callback queries from the inline buttons
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == "button1":
        bot.answer_callback_query(call.id, "You clicked Button 1!")
    elif call.data == "button2":
        bot.answer_callback_query(call.id, "You clicked Button 2!")

# Polling
bot.polling()
