import os
from notebook.utils import url_path_join
from notebook.base.handlers import IPythonHandler

YASERVER_URI = '/yamoment'
QUOTES_FOLDER = 'quotes'
QUOTES_LOCATION = os.path.join(os.path.dirname(__file__), QUOTES_FOLDER)
YASERVER_ENDPOINT_URI_PATH = "{}/.*".format(YASERVER_URI) 

class HelloWorldHandler(IPythonHandler):

    def get(self):

        self.log.info("uri path: {}".format(self.request.uri))
        uri_file_name = self.request.uri.split('/')[-1]
        quote_file_name = uri_file_name.lower()
        

        if quote_file_name.endswith('mp3'):
            quote_file_path = "{}/{}".format('quotes', quote_file_name)
            # file_name = os.path.join(os.path.dirname(__file__), quote_file_path)
            file_name = os.path.join(QUOTES_LOCATION, quote_file_name)
            self.log.info("Returning content: {}".format(file_name))
            self.log.info("=======================")        

            # TODO: check if file present. Also assuming no more than 1MB file for now.
            with open(file_name, "rb") as f:
                data = f.read(1024 * 1024)
                self.write(data)

            self.finish()
        else:            
            self.finish()
        



def load_jupyter_server_extension(nb_app):
    '''
    Register a hello world handler.

    Based on https://github.com/Carreau/jupyter-book/blob/master/extensions/server_ext.py
    '''
    web_app = nb_app.web_app
    host_pattern = '.*$'    
    route_pattern = url_path_join(web_app.settings['base_url'], YASERVER_ENDPOINT_URI_PATH)
    print ("route_pattern  :{}".format(route_pattern))
    nb_app.log.info("yaserver core enabled!. Route pattern: {}".format(route_pattern))
    web_app.add_handlers(host_pattern, [(route_pattern, HelloWorldHandler)])
