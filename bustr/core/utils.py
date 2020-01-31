from winsound import Beep
from sys import _getframe
import ctypes
import logging

logging.basicConfig(level=logging.DEBUG)
debug = logging.getLogger(" utils_debugger ")
debug.disabled = True

class utils:
	def __init__(self):
		self.frequency = 2500
		self.duration = 1000

	def debug(self):
		""" Disable stdout to console window """
		debug.disabled = False

	def hide(self):
		""" Hide the console window """
		debug.debug("Attempting to hide console window using Windows API ShowWindow")
		try:
			ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(),0)
		except Exception as error:
			debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
			return False
		else:
			debug.debug("Successfully hidden console window using Windows API ShowWindow")
			return True

	def lock(self):
		""" Locks the running system (Mimics CTRL+ALT+DEL > Lock) """
		debug.debug("Attempting to lock running system mimicking CTRL+ALT+DEL > Lock")
		if ctypes.windll.user32.LockWorkStation() == 0:
			debug.debug("Unable to lock system using Windows API LockWorkStation")
			return False
		else:
			debug.debug("Successfully locked system using Windows API LockWorkStation")
			return False

	def beep(self):
		""" Sends a high pitched beep for 1 second """
		debug.debug("Attempting to send a high pitched beep")
		try:
			Beep(self.frequency, self.duration)	
		except RuntimeError as error:
			debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
			return False
		else:
			debug.debug("Successfully sent high pitched beep")
			return True