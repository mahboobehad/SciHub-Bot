# In the name of God
import datetime
from io import BytesIO

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

    def fetch_paper(self, bot, update: Update):
        chat_id = update.effective_chat.id
        url = update.effective_message.text
        pdf = self._fetch_pdf(url)
        self.view.send_paper(chat_id, pdf)

    @staticmethod
    def _fetch_pdf(url):
        hub = SciHub()
        result = hub.fetch(url)
        pdf_bytes = result['pdf']
        file = BytesIO(pdf_bytes)
        file.name = str(datetime.datetime.now()) + ".pdf"
        return file
