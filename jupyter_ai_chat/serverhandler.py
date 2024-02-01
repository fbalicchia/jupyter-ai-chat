from jupyter_server.extension.application import ExtensionApp


def load_jupyter_server_extension(nb_app):
    nb_app.log.info("jupyter-ai-chat extension enabled!")
    


class AiExtensionChat(ExtensionApp):
    name = "jupyter_ai_chat"
