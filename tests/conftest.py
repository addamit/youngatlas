"""
tests
"""

from IPython.testing.globalipapp import start_ipython
import pytest

@pytest.fixture(scope="session")
def session_ip():
	print ("session IPython")
	session_ip = start_ipython()
	session_ip.run_line_magic(magic_name="load_ext", line="yamagics")
	return session_ip


@pytest.fixture(scope="function")
def ip(session_ip):
	"""Verify the extension is automatically loaded."""
	status = session_ip.find_cell_magic("yamagics")
	print ("magics status: {}".format(status))
	session_ip.run_line_magic(magic_name="load_ext", line="yamagics")
	print ("Yielding IPython")
	yield session_ip

	# session_ip.run_line_magic(magic_name="unload_ext", line="yamagics")
	#session_ip.run_line_magic(magic_name="reset", line="-f")
	#ip.extension_manager.reload_extension('storemagic')

	