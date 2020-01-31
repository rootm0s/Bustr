from bustr.core.enums import enum
from bustr.core.generate import generate
from bustr.core.export import registry
from time import sleep
from os import path
from sys import _getframe
import logging

logging.basicConfig(level=logging.DEBUG)
debug = logging.getLogger(" monitor_debugger ")
debug.disabled = True

class monitor:
	""" Class to monitor registry artifacts in real-time """
	def __init__(self):
		self.results = []
		self.fcheck = []
		self.scheck = []

	def debug(self):
		""" Disable stdout to console window """
		debug.disabled = False

	def scsi(self):
		"""
		This registry artifact is persistent so if the device is unplugged
		we cannot detect it with registry changes

		Path and variable associated with this function:
			> enum().path_scsi -- Registry path as string
			> enum().dump_scsi -- Name of export output
		"""
		if enum().EnumSCSI():
			debug.debug("Monitoring function ({fname}) is running".format(fname=_getframe().f_code.co_name))
			generate().log("Monitoring function ({fname}) is running".format(fname=_getframe().f_code.co_name))
			for data in enum().EnumSCSI():
				self.fcheck.append(data)

			while True:
				for data in enum().EnumSCSI():
					self.scheck.append(data)

				for change in set(self.fcheck).symmetric_difference(self.scheck):
					if len(self.fcheck) < len(self.scheck):
						if not change in self.results:
							debug.debug("Function ({fname}) detected a change ({change})".format(fname=_getframe().f_code.co_name, change=change))
							generate().log("Function ({fname}) detected a change ({change})".format(fname=_getframe().f_code.co_name, change=change))
							self.results.append(change)
							if registry().export("HKLM", enum().path_scsi, enum().dump_scsi)[0]:
								debug.debug("Exported {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_scsi)))
								generate().log("Exported {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_scsi)))
								if generate().report():
									debug.debug("Generated HTML report containing log messages and exported data")
									generate().log("Generated HTML report containing log messages and exported data")
								else:
									debug.debug("Unable to generate HTML report containing log messages and exported data")
									generate().log("Unable to generate HTML report containing log messages and exported data")
							else:
								debug.debug("Unable to export {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_scsi)))
								generate().log("Unable to export {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_scsi)))												
				self.scheck = []
				sleep(1)
		else:
			debug.debug("Monitoring function ({fname}) stopped, returned False".format(fname=_getframe().f_code.co_name))			
			generate().log("Monitoring function ({fname}) stopped, returned False".format(fname=_getframe().f_code.co_name))			
			return False

	def bthenum(self):
		"""
		This registry artifact is persistent so if the device is unplugged
		we cannot detect it with registry changes

		Path and variable associated with this function:
			> enum().path_bthenum -- Registry path as string
			> enum().dump_bthenum -- Name of export output
		"""
		if enum().EnumBTHENUM():
			debug.debug("Monitoring function ({fname}) is running".format(fname=_getframe().f_code.co_name))			
			generate().log("Monitoring function ({fname}) is running".format(fname=_getframe().f_code.co_name))			
			for data in enum().EnumBTHENUM():
				self.fcheck.append(data)

			while True:
				for data in enum().EnumBTHENUM():
					self.scheck.append(data)

				for change in set(self.fcheck).symmetric_difference(self.scheck):
					if len(self.fcheck) < len(self.scheck):
						if not change in self.results:
							debug.debug("Function ({fname}) detected a change ({change})".format(fname=_getframe().f_code.co_name, change=change))
							generate().log("Function ({fname}) detected a change ({change})".format(fname=_getframe().f_code.co_name, change=change))
							self.results.append(change)
							if registry().export("HKLM", enum().path_bthenum, enum().dump_bthenum)[0]:
								debug.debug("Exported {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_bthenum)))
								generate().log("Exported {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_bthenum)))												
								if generate().report():
									debug.debug("Generated HTML report containing log messages and exported data")
									generate().log("Generated HTML report containing log messages and exported data")
								else:
									debug.debug("Unable to generate HTML report containing log messages and exported data")												
									generate().log("Unable to generate HTML report containing log messages and exported data")												
							else:
								debug.debug("Unable to export {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_bthenum)))
								generate().log("Unable to export {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_bthenum)))												
				self.scheck = []
				sleep(1)
		else:
			debug.debug("Monitoring function ({fname}) stopped, returned False".format(fname=_getframe().f_code.co_name))
			generate().log("Monitoring function ({fname}) stopped, returned False".format(fname=_getframe().f_code.co_name))
			return False

	def bthport(self):
		"""
		This registry artifact is persistent so if the device is unplugged
		we cannot detect it with registry changes

		Path and variable associated with this function:
			> enum().path_bthport -- Registry path as string
			> enum().dump_bthport -- Name of export output		
		"""
		if enum().EnumBTHPORT():
			debug.debug("Monitoring function ({fname}) is running".format(fname=_getframe().f_code.co_name))	
			generate().log("Monitoring function ({fname}) is running".format(fname=_getframe().f_code.co_name))	
			for data in enum().EnumBTHPORT():
				self.fcheck.append(data)

			while True:
				for data in enum().EnumBTHPORT():
					self.scheck.append(data)

				for change in set(self.fcheck).symmetric_difference(self.scheck):
					if len(self.fcheck) < len(self.scheck):
						if not change in self.results:
							debug.debug("Function ({fname}) detected a change ({change})".format(fname=_getframe().f_code.co_name, change=change))
							generate().log("Function ({fname}) detected a change ({change})".format(fname=_getframe().f_code.co_name, change=change))
							self.results.append(change)
							if registry().export("HKLM", enum().path_bthport, enum().dump_bthport)[0]:
								debug.debug("Exported {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_bthport)))
								generate().log("Exported {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_bthport)))
								if generate().report():
									debug.debug("Generated HTML report containing log messages and exported data")
									generate().log("Generated HTML report containing log messages and exported data")
								else:
									debug.debug("Unable to generate HTML report containing log messages and exported data")												
									generate().log("Unable to generate HTML report containing log messages and exported data")												
							else:
								debug.debug("Unable to export {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_bthport)))
								generate().log("Unable to export {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_bthport)))
				self.scheck = []
				sleep(1)
		else:
			debug.debug("Monitoring function ({fname}) stopped, returned False".format(fname=_getframe().f_code.co_name))
			generate().log("Monitoring function ({fname}) stopped, returned False".format(fname=_getframe().f_code.co_name))
			return False

	def mountpoints(self):
		"""
		This registry artifact is dynamic, when a USB for an example
		gets inserted a mountpoint GUID will be created in the registry and
		removed when the USB is unplugged

		Path and variable associated with this function:
			> enum().path_mountpoints -- Registry path as string
			> enum().dump_mountpoints -- Name of export output
		"""
		if enum().EnumMountPoints2():
			debug.debug("Monitoring function ({fname}) is running".format(fname=_getframe().f_code.co_name))	
			generate().log("Monitoring function ({fname}) is running".format(fname=_getframe().f_code.co_name))	
			for data in enum().EnumMountPoints2():
				self.fcheck.append(data)

			while True:
				for data in enum().EnumMountPoints2():
					self.scheck.append(data)

				for change in set(self.fcheck).symmetric_difference(self.scheck):
					if len(self.fcheck) < len(self.scheck):
						if not change in self.results:
							debug.debug("Function ({fname}) detected a change ({change})".format(fname=_getframe().f_code.co_name, change=change))
							generate().log("Function ({fname}) detected a change ({change})".format(fname=_getframe().f_code.co_name, change=change))
							self.results.append(change)
							if registry().export("HKCU", enum().path_mountpoints, enum().dump_mountpoints)[0]:
								debug.debug("Exported {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_mountpoints)))
								generate().log("Exported {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_mountpoints)))
								if generate().report():
									debug.debug("Generated HTML report containing log messages and exported data")
									generate().log("Generated HTML report containing log messages and exported data")
								else:
									debug.debug("Unable to generate HTML report containing log messages and exported data")												
									generate().log("Unable to generate HTML report containing log messages and exported data")												
							else:
								debug.debug("Unable to export {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_mountpoints)))
								generate().log("Unable to export {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_mountpoints)))

				for device in self.results:
					if device in self.scheck:
						pass
					else:
						debug.debug("Function ({fname}) detected ({device}) was unplugged or removed from registry".format(fname=_getframe().f_code.co_name, device=device))						
						generate().log("Function ({fname}) detected ({device}) was unplugged or removed from registry".format(fname=_getframe().f_code.co_name, device=device))						
						self.results.remove(device)

				self.scheck = []
				sleep(1)
		else:
			debug.debug("Monitoring function ({fname}) stopped, returned False".format(fname=_getframe().f_code.co_name))
			generate().log("Monitoring function ({fname}) stopped, returned False".format(fname=_getframe().f_code.co_name))
			return False

	def mounteddevices(self):
		"""
		This registry artifact is persistent so if the device is unplugged
		we cannot detect it with registry changes.

		Improvements:
			* Add ability to check if drive letter or volume is present

		Path and variable associated with this function:
			> enum().path_mounteddevices -- Registry path as string
			> enum().dump_mounteddevices -- Name of export output			
		"""
		if enum().EnumMountedDevices():
			debug.debug("Monitoring function ({fname}) is running".format(fname=_getframe().f_code.co_name))
			generate().log("Monitoring function ({fname}) is running".format(fname=_getframe().f_code.co_name))
			for data in enum().EnumMountedDevices():
				self.fcheck.append(data)

			while True:
				for data in enum().EnumMountedDevices():
					self.scheck.append(data)

				for change in set(self.fcheck).symmetric_difference(self.scheck):
					if len(self.fcheck) < len(self.scheck):
						if not change in self.results:
							debug.debug("Function ({fname}) detected a change ({change})".format(fname=_getframe().f_code.co_name, change=change))
							generate().log("Function ({fname}) detected a change ({change})".format(fname=_getframe().f_code.co_name, change=change))
							self.results.append(change)
							if registry().export("HKLM", enum().path_mounteddevices, enum().dump_mounteddevices)[0]:
								debug.debug("Exported {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_mounteddevices)))
								generate().log("Exported {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_mounteddevices)))
								if generate().report():
									debug.debug("Generated HTML report containing log messages and exported data")
									generate().log("Generated HTML report containing log messages and exported data")
								else:
									debug.debug("Unable to generate HTML report containing log messages and exported data")												
									generate().log("Unable to generate HTML report containing log messages and exported data")												
							else:
								debug.debug("Unable to export {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_mounteddevices)))
								generate().log("Unable to export {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_mounteddevices)))
				self.scheck = []
				sleep(1)
		else:
			debug.debug("Monitoring function ({fname}) stopped, returned False".format(fname=_getframe().f_code.co_name))
			generate().log("Monitoring function ({fname}) stopped, returned False".format(fname=_getframe().f_code.co_name))
			return False

	def storage(self):
		"""
		This registry artifact is persistent so if the device is unplugged
		we cannot detect it with registry changes
		
		Path and variable associated with this function:
			> enum().path_storage -- Registry path as string
			> enum().dump_storage -- Name of export output				
		"""
		if enum().EnumSTORAGE():
			debug.debug("Monitoring function ({fname}) is running".format(fname=_getframe().f_code.co_name))
			generate().log("Monitoring function ({fname}) is running".format(fname=_getframe().f_code.co_name))
			for data in enum().EnumSTORAGE():
				self.fcheck.append(data)

			while True:
				for data in enum().EnumSTORAGE():
					self.scheck.append(data)

				for change in set(self.fcheck).symmetric_difference(self.scheck):
					if len(self.fcheck) < len(self.scheck):
						if not change in self.results:
							debug.debug("Function ({fname}) detected a change ({change})".format(fname=_getframe().f_code.co_name, change=change))
							generate().log("Function ({fname}) detected a change ({change})".format(fname=_getframe().f_code.co_name, change=change))
							self.results.append(change)
							if registry().export("HKLM", enum().path_storage, enum().dump_storage)[0]:
								debug.debug("Exported {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_storage)))
								generate().log("Exported {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_storage)))
								if generate().report():
									debug.debug("Generated HTML report containing log messages and exported data")
									generate().log("Generated HTML report containing log messages and exported data")
								else:
									debug.debug("Unable to generate HTML report containing log messages and exported data")												
									generate().log("Unable to generate HTML report containing log messages and exported data")												
							else:
								debug.debug("Unable to export {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_storage)))
								generate().log("Unable to export {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_storage)))
				self.scheck = []
				sleep(1)
		else:
			debug.debug("Monitoring function ({fname}) stopped, returned False".format(fname=_getframe().f_code.co_name))
			generate().log("Monitoring function ({fname}) stopped, returned False".format(fname=_getframe().f_code.co_name))
			return False

	def wpdbusenum(self):
		"""
		This registry artifact is persistent so if the device is unplugged
		we cannot detect it with registry changes

		Path and variable associated with this function:
			> enum().path_wpdbusenum -- Registry path as string
			> enum().dump_wpdbusenum -- Name of export output			
		"""
		if enum().EnumWPDBUSENUM():
			debug.debug("Monitoring function ({fname}) is running".format(fname=_getframe().f_code.co_name))
			generate().log("Monitoring function ({fname}) is running".format(fname=_getframe().f_code.co_name))
			for data in enum().EnumWPDBUSENUM():
				self.fcheck.append(data)

			while True:
				for data in enum().EnumWPDBUSENUM():
					self.scheck.append(data)

				for change in set(self.fcheck).symmetric_difference(self.scheck):
					if len(self.fcheck) < len(self.scheck):
						if not change in self.results:
							debug.debug("Function ({fname}) detected a change ({change})".format(fname=_getframe().f_code.co_name, change=change))
							generate().log("Function ({fname}) detected a change ({change})".format(fname=_getframe().f_code.co_name, change=change))
							self.results.append(change)
							if registry().export("HKLM", enum().path_wpdbusenum, enum().dump_wpdbusenum)[0]:
								debug.debug("Exported {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_wpdbusenum)))
								generate().log("Exported {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_wpdbusenum)))
								if generate().report():
									debug.debug("Generated HTML report containing log messages and exported data")
									generate().log("Generated HTML report containing log messages and exported data")
								else:
									debug.debug("Unable to generate HTML report containing log messages and exported data")												
									generate().log("Unable to generate HTML report containing log messages and exported data")												
							else:
								debug.debug("Unable to export {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_wpdbusenum)))
								generate().log("Unable to export {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_wpdbusenum)))												
				self.scheck = []
				sleep(1)
		else:
			debug.debug("Monitoring function ({fname}) stopped, returned False".format(fname=_getframe().f_code.co_name))
			generate().log("Monitoring function ({fname}) stopped, returned False".format(fname=_getframe().f_code.co_name))
			return False

	def usbstor(self):
		"""
		This registry artifact is persistent so if the device is unplugged
		we cannot detect it with registry changes
	
		Path and variable associated with this function:
			> enum().path_usbstor -- Registry path as string
			> enum().dump_usbstor -- Name of export output
		"""
		if enum().EnumUSBSTOR():
			debug.debug("Monitoring function ({fname}) is running".format(fname=_getframe().f_code.co_name))
			generate().log("Monitoring function ({fname}) is running".format(fname=_getframe().f_code.co_name))
			for data in enum().EnumUSBSTOR():
				self.fcheck.append(data)

			while True:
				for data in enum().EnumUSBSTOR():
					self.scheck.append(data)

				for change in set(self.fcheck).symmetric_difference(self.scheck):
					if len(self.fcheck) < len(self.scheck):
						if not change in self.results:
							debug.debug("Function ({fname}) detected a change ({change})".format(fname=_getframe().f_code.co_name, change=change))
							generate().log("Function ({fname}) detected a change ({change})".format(fname=_getframe().f_code.co_name, change=change))
							self.results.append(change)
							if registry().export("HKLM", enum().path_usbstor, enum().dump_usbstor)[0]:
								debug.debug("Exported {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_usbstor)))
								generate().log("Exported {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_usbstor)))
								if generate().report():
									debug.debug("Generated HTML report containing log messages and exported data")
									generate().log("Generated HTML report containing log messages and exported data")
								else:
									debug.debug("Unable to generate HTML report containing log messages and exported data")												
									generate().log("Unable to generate HTML report containing log messages and exported data")												
							else:
								debug.debug("Unable to export {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_usbstor)))
								generate().log("Unable to export {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_usbstor)))
				self.scheck = []
				sleep(1)
		else:
			debug.debug("Monitoring function ({fname}) stopped, returned False".format(fname=_getframe().f_code.co_name))
			generate().log("Monitoring function ({fname}) stopped, returned False".format(fname=_getframe().f_code.co_name))
			return False

	def usb(self):
		"""
		This registry artifact is persistent so if the device is unplugged
		we cannot detect it with registry changes
		
		Path and variable associated with this function:
			> enum().path_usb -- Registry path as string
			> enum().dump_usb -- Name of export output
		"""
		if enum().EnumUSB():
			debug.debug("Monitoring function ({fname}) is running".format(fname=_getframe().f_code.co_name))
			generate().log("Monitoring function ({fname}) is running".format(fname=_getframe().f_code.co_name))
			for data in enum().EnumUSB():
				self.fcheck.append(data)

			while True:
				for data in enum().EnumUSB():
					self.scheck.append(data)

				for change in set(self.fcheck).symmetric_difference(self.scheck):
					if len(self.fcheck) < len(self.scheck):
						if not change in self.results:
							debug.debug("Function ({fname}) detected a change ({change})".format(fname=_getframe().f_code.co_name, change=change))
							generate().log("Function ({fname}) detected a change ({change})".format(fname=_getframe().f_code.co_name, change=change))
							self.results.append(change)
							if registry().export("HKLM", enum().path_usb, enum().dump_usb)[0]:
								debug.debug("Exported {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_usb)))
								generate().log("Exported {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_usb)))
								if generate().report():
									debug.debug("Generated HTML report containing log messages and exported data")
									generate().log("Generated HTML report containing log messages and exported data")
								else:
									debug.debug("Unable to generate HTML report containing log messages and exported data")												
									generate().log("Unable to generate HTML report containing log messages and exported data")												
							else:
								debug.debug("Unable to export {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_usb)))
								generate().log("Unable to export {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_usb)))
				self.scheck = []
				sleep(1)
		else:
			debug.debug("Monitoring function ({fname}) stopped, returned False".format(fname=_getframe().f_code.co_name))
			generate().log("Monitoring function ({fname}) stopped, returned False".format(fname=_getframe().f_code.co_name))
			return False

	def wpd(self):
		"""
		This registry artifact is persistent so if the device is unplugged
		we cannot detect it with registry changes

		Path and variable associated with this function:
			> enum().path_wpd -- Registry path as string
			> enum().dump_wpd -- Name of export output
		"""
		if enum().EnumWPD():
			debug.debug("Monitoring function ({fname}) is running".format(fname=_getframe().f_code.co_name))
			generate().log("Monitoring function ({fname}) is running".format(fname=_getframe().f_code.co_name))
			for data in enum().EnumWPD():
				self.fcheck.append(data)

			while True:
				for data in enum().EnumWPD():
					self.scheck.append(data)

				for change in set(self.fcheck).symmetric_difference(self.scheck):
					if len(self.fcheck) < len(self.scheck):
						if not change in self.results:
							debug.debug("Function ({fname}) detected a change ({change})".format(fname=_getframe().f_code.co_name, change=change))
							generate().log("Function ({fname}) detected a change ({change})".format(fname=_getframe().f_code.co_name, change=change))
							self.results.append(change)
							if registry().export("HKLM", enum().path_wpd, enum().dump_wpd)[0]:
								debug.debug("Exported {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_wpd)))
								generate().log("Exported {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_wpd)))
								if generate().report():
									debug.debug("Generated HTML report containing log messages and exported data")
									generate().log("Generated HTML report containing log messages and exported data")
								else:
									debug.debug("Unable to generate HTML report containing log messages and exported data")												
									generate().log("Unable to generate HTML report containing log messages and exported data")												
							else:
								debug.debug("Unable to export {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_wpd)))
								generate().log("Unable to export {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_wpd)))
				self.scheck = []
				sleep(1)
		else:
			debug.debug("Monitoring function ({fname}) stopped, returned False".format(fname=_getframe().f_code.co_name))
			generate().log("Monitoring function ({fname}) stopped, returned False".format(fname=_getframe().f_code.co_name))
			return False

	def knowndevices(self):
		"""
		This registry artifact is persistent so if the device is unplugged
		we cannot detect it with registry changes

		Path and variable associated with this function:
			> enum().path_knowndevices -- Registry path as string
			> enum().dump_knowndevices -- Name of export output		
		"""
		if enum().EnumKnownDevices():
			debug.debug("Monitoring function ({fname}) is running".format(fname=_getframe().f_code.co_name))
			generate().log("Monitoring function ({fname}) is running".format(fname=_getframe().f_code.co_name))
			for data in enum().EnumKnownDevices():
				self.fcheck.append(data)

			while True:
				for data in enum().EnumKnownDevices():
					self.scheck.append(data)

				for change in set(self.fcheck).symmetric_difference(self.scheck):
					if len(self.fcheck) < len(self.scheck):
						if not change in self.results:
							debug.debug("Function ({fname}) detected a change ({change})".format(fname=_getframe().f_code.co_name, change=change))
							generate().log("Function ({fname}) detected a change ({change})".format(fname=_getframe().f_code.co_name, change=change))
							self.results.append(change)
							if registry().export("HKLM", enum().path_knowndevices, enum().dump_knowndevices)[0]:
								debug.debug("Exported {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_knowndevices)))
								generate().log("Exported {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_knowndevices)))
								if generate().report():
									debug.debug("Generated HTML report containing log messages and exported data")
									generate().log("Generated HTML report containing log messages and exported data")
								else:
									debug.debug("Unable to generate HTML report containing log messages and exported data")												
									generate().log("Unable to generate HTML report containing log messages and exported data")												
							else:
								debug.debug("Unable to export {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_knowndevices)))
								generate().log("Unable to export {fname} data to ({dpath}) directory".format(fname=_getframe().f_code.co_name,
												dpath=path.join(registry().folder, enum().dump_knowndevices)))
				self.scheck = []
				sleep(1)
		else:
			debug.debug("Monitoring function ({fname}) stopped, returned False".format(fname=_getframe().f_code.co_name))
			generate().log("Monitoring function ({fname}) stopped, returned False".format(fname=_getframe().f_code.co_name))
			return False