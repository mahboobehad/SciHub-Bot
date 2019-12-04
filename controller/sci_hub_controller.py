# In the name of God
from scihub import SciHub
from telegram import Update
from telegram.ext import Dispatcher

from view.sci_hub_view import SciHubView


class SciHubController:
    def __init__(self, dispatcher: Dispatcher):
        self.dispatcher = dispatcher
        self.view = SciHubView(dispatcher.bot)

    def start(self, bot, update: Update):
        chat_id = update.effective_chat.id
        self.view.send_start(chat_id)

    def fetch_paper(self, bot,  update: Update):
        chat_id = update.effective_chat.id
        url = update.edited_message.text
        self._save_paper(url)
        self.view.send_paper(chat_id, "output.pdf")

    @staticmethod
    def _save_paper(url):
        hub = SciHub()
        result = hub.fetch(url)
        with open('output.pdf', 'wb+') as fd:
            fd.write(result['pdf'])

