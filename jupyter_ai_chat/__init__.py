from ._version import __version__

# expose engines and tasks on the module root so that they may be declared as
# entrypoints in `pyproject.toml`
from .engine import TestModelEngine
from .tasks import tasks


def ():
    return [{"src": "labextension", "dest": "jupyter-ai-chat"}]
