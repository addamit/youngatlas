from IPython.utils.io import capture_output
from pytest import raises
#import yamagics 


# https://github.com/davidesarra/jupyter_spaces/blob/master/tests/test_magics.py

def test_magics_code_execution_simple(session_ip):
	"""Given code in a cell, the magics will always the code."""

	with capture_output() as captured:
			session_ip.run_cell(raw_cell=" x = 2+2; assert x == 4")
	print ("{}".format(captured.stdout))
	assert session_ip.user_global_ns["x"] == 4
	

def test_magics_code_execution_complex(session_ip):
	"""Given code cell with definitions, are run as well without issues."""
	
	with capture_output() as captured:
			session_ip.run_cell_magic("moment", "", "f = lambda x: x + 1; y = f(x=2); assert y == 3")
	print ("{}".format(captured.stdout))
	assert session_ip.user_global_ns["y"] == 3
	assert callable(session_ip.user_global_ns["f"])


def test_magics_code_execution_returns_random_clip(session_ip):
	"""Given multiple code cells, each run will randomly run a new quote."""

	clips = []
	with capture_output() as captured:
			session_ip.run_cell_magic("moment", "#MOMENTDEBUG", "2+2")
			session_ip.run_cell_magic("moment", "#MOMENTDEBUG", "2+2")
			session_ip.run_cell_magic("moment", "#MOMENTDEBUG", "2+2")
	print ("cell execution result :{}".format(captured.stdout))
	msg = captured.stdout
	msg = msg.replace("\n", "") # remove new line 
	#print (msg)
	clips_names = msg.replace("[MomentAudio]:",",") # remove the tag
	clips_names = clips_names[1:] # remove the front comma
	clips_list = clips_names.split(",") # split all quotes
	print (clips_list)
	# assert atleast there are two different quotes from a list of 3
	assert len(set(clips_list)) >= 2
		

def test_magics_code_execution_raises_exception(session_ip):
	"""Given code cell with syntax errors will also result in execution.
	Errors will be reported by the kernel and displayed appropriately."""

	with capture_output() as captured:
			with raises(SyntaxError):
					session_ip.run_cell_magic("moment", "", "2+%3")
	print ("cell execution result :{}".format(captured.stdout))


