# In the name of God
from io import BytesIO

from scihub import SciHub
from telegram import Update
from telegram.ext import Dispatcher, ConversationHandler

from state.state import State
from view.sci_hub_view import SciHubView


class SciHubController:
    def __init__(self, dispatcher: Dispatcher):
        self.dispatcher = dispatcher
        self.view = SciHubView(dispatcher.bot)

    def start(self, bot, update: Update):
        chat_id = update.effective_chat.id
        self.view.send_start(chat_id)
        return ConversationHandler.END

    def fetch_paper(self, bot, update: Update):
        chat_id = update.effective_chat.id
        url = update.effective_message.text
        pdf, title = self._fetch_pdf(url)
        self.dispatcher.user_data["title"] = title
        self.dispatcher.user_data["pdf"] = pdf
        self.view.send_paper(chat_id, pdf, title)
        return ConversationHandler.END

    def ask_category(self, bot, update: Update):
        chat_id = update.effective_chat.id
        self.view.send_add_category(chat_id)
        return State.set_category

    def set_category(self, bot, update: Update):
        chat_id = update.effective_chat.id
        category = update.effective_message.text
        title = self.dispatcher.user_data["title"]
        self.view.send_cat_added(chat_id, category, title)
        return ConversationHandler.END

    @staticmethod
    def _fetch_pdf(url):
        hub = SciHub()
        result = hub.fetch(url)
        pdf_bytes = result['pdf']
        file = BytesIO(pdf_bytes)
        title = result['title'].split("|")[1]
        file.name = result["url"].split("/")[~0].split(".pdf")[0] + ".pdf"
        return file, title
