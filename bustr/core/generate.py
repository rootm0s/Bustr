from bustr.core.parser import parse
from os import path, getcwd, makedirs, walk, remove
from sys import _getframe
import datetime
import logging

logging.basicConfig(level=logging.DEBUG)
debug = logging.getLogger(" generate_debugger ")
debug.disabled = True

class generate:
	""" Class to generate html based reports and log messages """
	def __init__(self):
		self.path_log = path.join(getcwd(), "logs")
		self.path_report = path.join(getcwd(), "reports")
		self.path_dumps = path.join(getcwd(), "dumps")

	def debug(self):
		""" Disable stdout to console window """
		debug.disabled = False

	def log(self, message):
		""" Save message to log file with timestamps 
		generate().log("This is a log message") """
		debug.debug("Checking if path exists")
		if not path.exists(path.join(self.path_log, str(datetime.date.today()))):
			debug.debug("Path does not exist, creating directory structure")
			try:
				makedirs(path.join(self.path_log, str(datetime.date.today())),
							mode=0o777,
							exist_ok=False)
			except FileExistsError:
				pass
			else:
				debug.debug("Directory structure was created successfully")

		debug.debug("Attempting to write to log file")
		with open(path.join(self.path_log, str(datetime.date.today()) + "\\" + str(datetime.date.today()) + ".log"), "a+") as log:
			log.write("{date} - {message}\n".format(date=datetime.datetime.now(), message=str(message)))
			debug.debug("Wrote ({message}) to log file".format(message=str(message)))

	def report(self):
		""" Generate a html based report containing the data we exported
		from parse().regfile("regfile.reg") or/and parse().logfile("logfile.log") """
		debug.debug("Checking if path exists")
		if not path.exists(path.join(self.path_report, str(datetime.date.today()))):
			debug.debug("Path does not exist, creating directory structure")
			try:
				makedirs(path.join(self.path_report, str(datetime.date.today())),
							mode=0o777,
							exist_ok=False)
			except FileExistsError:
				pass
			else:
				debug.debug("Directory structure was created successfully")
		
		debug.debug("Checking if file exists")
		if path.isfile(path.join(path.join(self.path_report, str(datetime.date.today())), "report.html")):
			debug.debug("File exists, removing file from disk")
			try:
				remove(path.join(path.join(self.path_report, str(datetime.date.today())), "report.html"))
			except Exception as error:
				debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
				return False
			else:
				debug.debug("Successfully removed file from disk")
		
		debug.debug("Attempting to write HTML report to disk")
		with open(path.join(path.join(self.path_report, str(datetime.date.today())), "report.html"), "a+") as report:
			report.write("<html>\n")
			report.write("<head>\n")
			report.write("<style>\n")
			report.write("h2 {\n")
			report.write("	font-family: 'Trebuchet MS', Arial, Helvetica, sans-serif;\n")
			report.write("	font-size: 16px;\n")
			report.write("}\n")
			report.write("table, th, td {\n")
			report.write("	font-family: 'Trebuchet MS', Arial, Helvetica, sans-serif;\n")
			report.write("	font-size: 12px;\n")
			report.write("	border: 1px solid black;\n")
			report.write("	border-collapse: collapse;\n")
			report.write("}\n")
			report.write("th, td {\n")
			report.write("	padding: 5px;\n")
			report.write("	text-align: left;\n")
			report.write("}\n")
			report.write("tr:hover {background-color: #ddd;}\n")
			report.write("</style>\n")
			report.write("</head>\n")

			report.write("\n<h2>Monitoring log results:</h2>\n")
			if path.isdir(self.path_log):
				report.write("<table style='width:100%'>\n")
				report.write("<tr>\n")
				for p, s, f in walk(self.path_log):
					for n in f:
						if path.isfile(path.join(p, n)):
							data = parse().logfile(path.join(p, n))
							if data:
								for d in (data[0]):
									report.write("<tr><th>" + d.strip("\n") + "</th></tr>\n")
							else:
								report.write("<td>No available data</td>\n")
						else:
							report.write("<td>No available data</td>\n")
				report.write("</tr>\n")
				report.write("</table>\n")
			else:
				report.write("<table style='width:100%'>\n")
				report.write("<tr>\n")
				report.write("<td>No available data</td>\n")
				report.write("</tr>\n")
				report.write("</table>\n")

			report.write("\n<h2>Exported data log results:</h2>\n")
			if path.isdir(self.path_dumps):
				report.write("<table style='width:100%'>\n")
				for p, s, f in walk(self.path_dumps):
					for n in f:
						if path.isfile(path.join(p, n)):
							data = parse().regfile(path.join(p, n))
							if data:
								for l in range(len(data)):
									if len(data[l]) == 1:
										if "HKEY_" in data[l][0]:
											report.write("<tr><th>" + data[l][0] + "</th></tr>\n")
									if len(data[l]) == 2:
										report.write("<tr><td>" + data[l][0] + " : " + data[l][1] + "</td></tr>\n")
							else:
								report.write("<td>No available data</td>\n")	
						else:
							report.write("<td>No available data</td>\n")				
			else:
				report.write("<table style='width:100%'>\n")
				report.write("<tr>\n")
				report.write("<td>No available data</td>\n")
				report.write("</tr>\n")
				report.write("</table>\n")

			report.write("</table>\n")
			report.write("</html>\n")

		if path.isfile(path.join(path.join(self.path_report, str(datetime.date.today())), "report.html")):
			debug.debug("Successfully created HTML report")
			return True
		else:
			debug.debug("Unable to create HTML report")
			return False