from bustr.core.utils import utils
from os import path, getcwd, makedirs, remove
from subprocess import PIPE, run
from sys import _getframe
import datetime
import logging

logging.basicConfig(level=logging.DEBUG)
debug = logging.getLogger(" export_debugger ")
debug.disabled = True

class registry:
	""" Class to export registry files """
	def __init__(self):
		self.folder = path.join(getcwd(),
								"dumps")

	def debug(self):
		""" Disable stdout to console window """
		debug.disabled = False

	def export(self, hkey, key, name):
		""" Export registry file to disk """
		debug.debug("Checking if path exists")
		if not path.exists(path.join(self.folder, str(datetime.date.today()))):
			debug.debug("Path does not exist, creating directory stucture")
			try:
				makedirs(path.join(self.folder, str(datetime.date.today())),
							mode=0o777,
							exist_ok=False)
			except FileExistsError:
				pass
			else:
				debug.debug("Directory stucture was created successfully")

		debug.debug("Checking if file exists")
		if path.isfile(path.join(path.join(self.folder, str(datetime.date.today())), name)):
			debug.debug("File exists, removing file from disk")
			try:
				remove(path.join(path.join(self.folder, str(datetime.date.today())), name))
			except Exception as error:
				debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
				return False
			else:
				debug.debug("Successfully removed file from disk")

		debug.debug("Attempting to export registry data to directory")
		try:
			result = run("reg export {path} {output}".format(path=path.join(hkey, key),
							output=path.join(path.join(self.folder, str(datetime.date.today())), name)),
							check=True,
							stdout=PIPE)
		except Exception as error:
			debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
			return(False, 0)
		else:
			if result.returncode == 0:
				if path.isfile(path.join(path.join(self.folder, str(datetime.date.today())), name)):
					debug.debug("Successfully exported registry data to directory")
					return(True, result.returncode)
				else:
					debug.debug("Unable to export registry data to directory")
					return(False, result.returncode)
			else:
				debug.debug("Unable to export registry data to directory")
				return(False, result.returncode)