# import yaserver
import pytest
import requests

from notebook.serverextensions import toggle_serverextension_python
from notebook import nbextensions, serverextensions, extensions
from notebook.notebookapp import NotebookApp



# #TODO: fixture
# url = 'https://localhost:tree/{}'.format(yaserver.YASERVER_URI)

@pytest.fixture(scope="module")
def notebook():
	app = NotebookApp(nbserver_extensions={'yaserver': True})
	app.init_server_extensions()

def test_valid_endpoint_returns_audio_clip(notebook):
	"""Given a valid clip request, the server returns a valid audio clip."""
	assert False

def test_invalid_request(notebook):
	"""Requesting an invalid clip returns an empty response. """
	assert False


# def test_get_method_support():
# 	"""Server currently only supports GET."""
# 	assert False


# def test_audio_play_time():
# 	"""Given a valid GET request, server returns a valid clip less than 20 seconds play time."""
# 	assert False