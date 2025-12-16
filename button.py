from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

def delete_msg():
    markup = InlineKeyboardMarkup()
    delete_btn = InlineKeyboardButton(' ❌ ' , callback_data='delete_message')
    markup.add(delete_btn)
    return markup

def set_lang():
    markup = InlineKeyboardMarkup()
    en_lang = InlineKeyboardButton('🇬🇧 English', callback_data='set_english_lang')
    fa_lang = InlineKeyboardButton('🇮🇷 Persian', callback_data='set_farsi_lang')
    markup.add(en_lang,fa_lang)
    return markup
    