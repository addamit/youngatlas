import os
import sys
import shutil
import fileinput
from os import remove
from shutil import move


from setuptools import setup, find_packages
from setuptools.command.install import install


from jupyter_core.paths import jupyter_config_dir
from notebook.services.config import ConfigManager
from notebook.nbextensions import install_nbextension


import IPython
from IPython.paths import get_ipython_dir
from traitlets.config import Configurable
from traitlets.config.loader import JSONFileConfigLoader, PyFileConfigLoader
from notebook.serverextensions import ToggleServerExtensionApp, toggle_serverextension_python

# Original idea from here
# https://github.com/davidesarra/jupyter_spaces/blob/master/setup.py


ya_server_extension = 'yaserver'
ya_magics_extension = 'yamagics'

def replace(source_file_path, pattern, new_pattern):

	for line in fileinput.input([source_file_path], inplace=True):
		if line.strip().startswith('c.InteractiveShellApp.extensions'):
			line = '{}\n'.format(new_pattern)
		sys.stdout.write(line)


def enable_ipython_extension():

	c = PyFileConfigLoader(IPython.paths.locate_profile()+"\\ipython_config.py")
	cfg = c.load_config()
	extns = cfg['InteractiveShellApp']['extensions']
	if ya_magics_extension not in extns:
		cfg['InteractiveShellApp']['extensions'] += [ya_magics_extension]
		exts = cfg['InteractiveShellApp']['extensions']
		exts_list_str = "c.InteractiveShellApp.extensions = {}".format(exts)

		# update config file with new extn added to list for c.InteractiveShellApp.extensions 
		ipy_config_file = os.path.join(IPython.paths.locate_profile(), "ipython_config.py")
		replace(ipy_config_file, "c.InteractiveShellApp.extensions", exts_list_str)


class InstallCommand(install):

	def __init__(self, *args, **kwargs):
		super(InstallCommand, self).__init__(*args, **kwargs)

	def run(self):
		
		# Install Python package itself. 
		install.run(self)

		# Enable the server extension			
		# Below API should enable.
		# For a fresh install this will enable the extension
		toggle_serverextension_python(ya_server_extension)

		# now enable the extension 
		enable_ipython_extension()

setup(
    name='youngatlas',
    version='0.1',
    packages=['yaserver', 'yamagics'], ##find_packages(where = 'src_new'),
    package_dir = {'': 'src'},
    include_package_data=True,    
    cmdclass={
        'install': InstallCommand
    }
)	