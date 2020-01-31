from os import path
from sys import _getframe
import logging

logging.basicConfig(level=logging.DEBUG)
debug = logging.getLogger(" parse_debugger ")
debug.disabled = True

class parse:
	""" Class to parse exported registry files """
	def __init__(self):
		self.logdata = []
		self.regdata = []

	def debug(self):
		""" Disable stdout to console window """
		debug.disabled = False

	def logfile(self, file):
		""" Return received file data to function """
		debug.debug("Checking if file exists")
		if path.isfile(path.join(file)):
			debug.debug("File detected, attempting to read file data")
			try:
				with open(path.join(file), "r") as f:
					data = f.readlines()
			except Exception as error:
				debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
				return False
			else:
				debug.debug("Appended ({data}) to logdata list".format(data=data))
				self.logdata.append(data)
				return self.logdata
		else:
			debug.debug("Log file does not exist")		
			return False

	def regfile(self, file):
		""" Return received file data to function """
		debug.debug("Checking if file exists")
		if path.isfile(path.join(file)):
			debug.debug("Registry file detected, attempting to read file data")
			try:
				with open(path.join(file), "r", encoding="utf-8") as f:
					data = str(f.read())
			except UnicodeDecodeError:
				with open(path.join(file), "r", encoding="utf-16") as f:
					data = str(f.read())
			
			debug.debug("Attempting to split and sanitize the registry data")
			for d in data.split():
				self.regdata.append(d.replace('"="', " ").replace('"=', " ").strip('"').split())
			
			debug.debug("Appended ({data}) to regdata list".format(data=self.regdata))
			return self.regdata
		else:
			debug.debug("Registry file does not exist")
			return False