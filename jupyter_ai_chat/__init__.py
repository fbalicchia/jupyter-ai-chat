from ._version import __version__

# expose engines and tasks on the module root so that they may be declared as
# entrypoints in `pyproject.toml`
from .myhandler import CustomChatHandler
from .serverhandler import load_jupyter_server_extension
from .serverhandler import AiExtensionChat


def _jupyter_labextension_paths():
    return [{"src": "labextension", "dest": "@jupyter-ai/jupyter-ai-chat"}]


def _jupyter_server_extension_points():
    return [{"module": "jupyter_ai", "app": AiExtensionChat}]