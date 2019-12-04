# In the name of God
from telegram.ext import Dispatcher, ConversationHandler, CommandHandler, RegexHandler

from controller.sci_hub_controller import SciHubController


class StateMachine:
    def __init__(self, dispatcher: Dispatcher):
        self.dispatcher = dispatcher
        self.sci_hub_controller = SciHubController(dispatcher)

    def start(self):
        for member in dir(StateMachine):
            if member.startswith("_set") and callable(getattr(StateMachine, member)):
                states = getattr(StateMachine, member)(self)
                self.dispatcher.add_handler(states)

    def _set_sci_hub_states(self):
        conversation_handler = ConversationHandler(entry_points=[
            CommandHandler("start", self.sci_hub_controller.start),
            RegexHandler(pattern="https://www.sciencedirect.com/science/article/*",
                         callback=self.sci_hub_controller.fetch_paper)],
            states={},
            fallbacks=[],
            allow_reentry=True)
        return conversation_handler

