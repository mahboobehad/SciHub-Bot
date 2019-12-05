from telegram import Bot, ReplyKeyboardMarkup

from view.button import Button


class SciHubView:
    start_text = ("Send me a *science direct* url, "
                  "I will fetch the paper and upload it for you here, otherwise I won't response :D")
    add_cat = "Do you want to add category for downloaded paper?"

    enter_cat = "Enter category:"

    cat_added = "#{category} added to {title}"

    def __init__(self, bot: Bot):
        self.bot = bot

    def send_start(self, chat_id):
        text = self.start_text
        self.bot.send_message(chat_id, text)

    def send_paper(self, chat_id, file, title):
        keyboard = [[Button.add_category]]
        markup_keyboard = ReplyKeyboardMarkup(keyboard)
        text = self.add_cat
        self.bot.send_document(chat_id, document=file, caption=title)
        self.bot.send_message(chat_id, text, markup_keyboard=markup_keyboard)

    def send_add_category(self, chat_id):
        text = self.enter_cat
        self.bot.send_message(chat_id, text)

    def send_cat_added(self, chat_id, category, title):
        text = self.cat_added.format(category="_".join(x for x in category.strip().split(" ")), title=title)
        self.bot.send_message(chat_id, text)
