from jupyter_ai.chat_handlers.base import BaseChatHandler, SlashCommandRoutingType
from jupyter_ai.models import HumanChatMessage

class CustomChatHandler(BaseChatHandler):
    id = "custom"
    name = "Custom"
    help = "A chat handler that does something custom"
    routing_type = SlashCommandRoutingType(slash_id="custom")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def process_message(self, message: HumanChatMessage):
        # Put your custom logic here
        self.reply("Hello I'm an extension", message)