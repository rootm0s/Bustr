from bustr.core.monitor import monitor
from bustr.core.generate import generate
from bustr.core.enums import enum
from bustr.core.utils import utils
from bustr.core.export import registry
from bustr.core.parser import parse
from multiprocessing import Pool, freeze_support
import argparse

#enum().debug()
#generate().debug()
#utils().debug()
#monitor().debug()
#registry().debug()
#parse().debug()

if __name__ == "__main__":
	""" Support if being compiled to executable """
	freeze_support()

	""" Script and executable arguments """
	parser = argparse.ArgumentParser()
	parser.add_argument("-m", "--monitor", action="store_true", help="monitor registry artifacts in real-time and log the results", required=False)
	parser.add_argument("-q", "--quite", action="store_true", help="hides the console window, logging is still active", required=False)
	parser.add_argument("-r", "--report", action="store_true", help="parse logs and exported data and generate HTML report", required=False)
	parser.add_argument("-d", "--debug", action="store_true", help="turn debug on", required=False)
	args = parser.parse_args()

	""" Hide the console window """
	if args.quite:
		utils().hide()

	""" Turn on debugging on all functions """
	if args.debug:
		enum().debug()
		generate().debug()
		utils().debug()
		monitor().debug()
		registry().debug()
		parse().debug()

	""" Parse through logs and exported data and generate a
	HTML file using simple tables """
	if args.report:
		with Pool(processes=1) as pool:
			p = pool.apply_async(generate().report,())
			p.wait()

	""" Multiple watchdogs """
	if args.monitor:
		watchdogs = {"mounteddevices" : monitor().mounteddevices, 
					"knowndevices" : monitor().knowndevices,
					"mountpoints" : monitor().mountpoints,
					"wpdbusenum" : monitor().wpdbusenum,
					"storage" : monitor().storage,
					"usbstor" : monitor().usbstor,
					"bthport" : monitor().bthport,
					"bthenum" : monitor().bthenum,
					"scsi" : monitor().scsi,
					"wpd" : monitor().wpd,
					"usb" : monitor().usb}

		jobs = 0
		with Pool(processes=len(watchdogs)) as pool:
			for function in watchdogs:
				p = pool.apply_async(watchdogs[function],())
				jobs += 1
				if jobs == len(watchdogs):
					p.wait()