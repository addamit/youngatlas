"""
IPYthon Magics Extension to play audio without displaying the audio widget.  
"""
import os
import random 
import pathlib
import inspect

from typing import Optional
from IPython import get_ipython
from IPython.display import Audio, display
from IPython.core.magic import line_cell_magic, Magics, magics_class
from IPython.core.magic_arguments import argument, magic_arguments, parse_argstring



# https://stackoverflow.com/questions/61176900/jupyter-colab-play-sound-with-any-error-in-any-cell-play-sound-after-compl/61176901
from IPython.core.ultratb import AutoFormattedTB
# Catch any Exception, play error sound and re-raise the Exception
#-------------------------------------------------
# initialize the formatter for making the tracebacks into strings
itb = AutoFormattedTB(mode = 'Plain', tb_offset = 1)


from yaserver import QUOTES_LOCATION, YASERVER_URI
all_choices = []
included_extensions = ['mp3']


class _InvisibleAudio(Audio):
    """
    An invisible (`display: none`) `Audio` element which removes itself when finished playing.
    Original sample based on https://stackoverflow.com/a/50648266.
    """

    def _repr_html_(self) -> str:
        audio = super()._repr_html_()
        audio = audio.replace(
            "<audio", '<audio onended="this.parentNode.removeChild(this)"'
        )        
        return f'<div style="display:none">{audio}</div>'
        # return f'<div">{audio}</div>'


@magics_class
class NotificationMagics(Magics):
    """
    IPython extension implementing the magic.
    """

    @magic_arguments()
    @argument(
        "-u",
        "--url",
        default="quote1.mp3",
        help="URL of audio file to play.",
    )
    @argument(
        "line_code",
        nargs="*",
        help="Other code on the line will be executed, unless this is called as a cell magic.",
    )
    @line_cell_magic
    def yamoment(self, line: str, cell: Optional[str] = None):
        args = parse_argstring(self.yamoment, line)        
        MOMENTDEBUG = False
        if line and line == '#MOMENTDEBUG':
            MOMENTDEBUG = True

        code = cell if cell else " ".join(args.line_code)
        try:
            ret = self.shell.ex(code)
        finally:
            
            quote_url = random.choice(all_choices)
            audio = _InvisibleAudio(url='{}/{}'.format(YASERVER_URI, quote_url), autoplay=True)
            if MOMENTDEBUG:
                    print ("[MomentAudio]:{}".format(quote_url))
            display(audio)

        return ret

def load_ipython_extension(ipython):
    ipython.register_magics(NotificationMagics)    
    file_names = [fn for fn in os.listdir(QUOTES_LOCATION) if any(fn.endswith(ext) for ext in included_extensions)]
    all_choices.extend(file_names)
    # ipython.shell.set_custom_exc((Exception,), custom_exc)

#get_ipython().register_magics(NotificationMagics)