# In the name of God
from telegram import Bot


class SciHubView:
    start_text = ("Send me a *science direct* url, "
                  "I will fetch the paper and upload it for you here, otherwise I won't response :D")

    def __init__(self, bot: Bot):
        self.bot = bot

    def send_start(self, chat_id):
        text = self.start_text
        self.bot.send_message(chat_id, text)

    def send_paper(self, chat_id, file):
        self.bot.send_document(chat_id, document=open(file, "rb"))