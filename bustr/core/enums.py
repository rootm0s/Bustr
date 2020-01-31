from bustr.core.utils import utils
from sys import _getframe
from os import path
import logging

try:
	import _winreg	
except ImportError:
	import winreg as _winreg

logging.basicConfig(level=logging.DEBUG)
debug = logging.getLogger(" enum_debugger ")
debug.disabled = True

class enum:
	""" Class to handle enumeration """
	def __init__(self):
		self.results = []
		self.devices = []
		self.path_mounteddevices = r"SYSTEM\MountedDevices"
		self.path_usb = r"SYSTEM\CurrentControlSet\Enum\USB"
		self.path_scsi = r"SYSTEM\CurrentControlSet\Enum\SCSI"
		self.path_bthenum = r"SYSTEM\CurrentControlSet\Enum\BTHENUM"
		self.path_usbstor = r"SYSTEM\CurrentControlSet\Enum\USBSTOR"
		self.path_storage = r"SYSTEM\CurrentControlSet\Enum\STORAGE\Volume"
		self.path_wpd = r"SOFTWARE\Microsoft\Windows Portable Devices\Devices"
		self.path_wpdbusenum = r"SYSTEM\CurrentControlSet\Enum\SWD\WPDBUSENUM"
		self.path_bthport = r"SYSTEM\CurrentControlSet\Services\BTHPORT\Parameters\Devices"
		self.path_mountpoints = r"Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2\CPC\Volume"
		self.path_knowndevices = r"Software\Microsoft\Windows\CurrentVersion\Explorer\AutoplayHandlers\KnownDevices"
		self.dump_mounteddevices = "dump_mounteddevices.reg"
		self.dump_knowndevices = "dump_knowndevices.reg"
		self.dump_mountpoints = "dump_mountpoints.reg"
		self.dump_wpdbusenum = "dump_wpdbusenum.reg"
		self.dump_bthport = "dump_bthport.reg"
		self.dump_storage = "dump_storage.reg"
		self.dump_usbstor = "dump_usbstor.reg"
		self.dump_bthenum = "dump_bthenum.reg"
		self.dump_scsi = "dump_scsi.reg"
		self.dump_usb = "dump_usb.reg"
		self.dump_wpd = "dump_wpd.reg"

	def debug(self):
		""" Disable stdout to console window """
		debug.disabled = False

	def EnumSCSI(self):
		""" Enumerate SCSI registry artifacts and return results.
		If registry key does not exist it returns False """
		try:
			key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,
									path.join(self.path_scsi),
									0,
									_winreg.KEY_READ)
		except WindowsError as error:
			debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
			return False
		else:
			for index in range(0, _winreg.QueryInfoKey(key)[0]):
				try:
					self.devices.append(_winreg.EnumKey(key, index))
				except WindowsError as error:
					debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
					pass
				else:
					debug.debug("Appended ({data}) to devices list".format(data=_winreg.EnumKey(key, index)))

			for device in self.devices:
				try:
					key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,
											path.join(self.path_scsi, device),
											0,
											_winreg.KEY_READ)
				except WindowsError as error:
					debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
					pass
				else:
					self.results.append(path.join(self.path_scsi, device))
					debug.debug("Appended ({data}) to results list".format(data=path.join(self.path_scsi, device)))

			_winreg.CloseKey(key)
		finally:
			return self.results

	def EnumBTHENUM(self):
		""" Enumerate BTHENUM registry artifacts and return results.
		If registry key does not exist it returns False """	
		try:
			key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,
									path.join(self.path_bthenum),
									0,
									_winreg.KEY_READ)
		except WindowsError as error:
			debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
			return False
		else:
			for index in range(0, _winreg.QueryInfoKey(key)[0]):
				try:
					self.devices.append(_winreg.EnumKey(key, index))
				except WindowsError as error:
					debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
					pass
				else:
					debug.debug("Appended ({data}) to devices list".format(data=_winreg.EnumKey(key, index)))

			for device in self.devices:
				try:
					key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,
											path.join(self.path_bthenum, device),
											0,
											_winreg.KEY_READ)
				except WindowsError as error:
					debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
					pass
				else:
					self.results.append(path.join(self.path_bthenum, device))
					debug.debug("Appended ({data}) to results list".format(data=path.join(self.path_bthenum, device)))

			_winreg.CloseKey(key)
		finally:
			return self.results

	def EnumBTHPORT(self):
		""" Enumerate BTHPORT registry artifacts and return results.
		If registry key does not exist it returns False """		
		try:
			key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,
									path.join(self.path_bthport),
									0,
									_winreg.KEY_READ)
		except WindowsError as error:
			debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
			return False
		else:
			for index in range(0, _winreg.QueryInfoKey(key)[0]):
				try:
					self.results.append(_winreg.EnumKey(key, index))
				except WindowsError as error:
					debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
					pass
				else:
					debug.debug("Appended ({data}) to results list".format(data=_winreg.EnumKey(key, index)))

			_winreg.CloseKey(key)		
		finally:
			return self.results

	def EnumKnownDevices(self):
		""" Enumerate KnownDevices registry artifacts and return results.
		If registry key does not exist it returns False """		
		try:
			key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,
									path.join(self.path_knowndevices),
									0,
									_winreg.KEY_READ)
		except WindowsError as error:
			debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
			return False
		else:
			for index in range(0, _winreg.QueryInfoKey(key)[0]):
				try:
					self.devices.append(_winreg.EnumKey(key, index))
				except WindowsError as error:
					debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
					pass
				else:
					debug.debug("Appended ({data}) to devices list".format(data=_winreg.EnumKey(key, index)))

			for device in self.devices:
				try:
					key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,
											path.join(self.path_knowndevices, device),
											0,
											_winreg.KEY_READ)
				except WindowsError as error:
					debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
					pass
				else:
					self.results.append(path.join(self.path_knowndevices, device))
					debug.debug("Appended ({data}) to results list".format(data=path.join(self.path_knowndevices, device)))
					
			_winreg.CloseKey(key)
		finally:
			return self.results

	def EnumWPD(self):
		""" Enumerate WPD registry artifacts and return results.
		If registry key does not exist it returns False """
		try:
			key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,
									path.join(self.path_wpd),
									0,
									_winreg.KEY_READ)
		except WindowsError as error:
			debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
			return False
		else:
			for index in range(0, _winreg.QueryInfoKey(key)[0]):
				try:
					self.devices.append(_winreg.EnumKey(key, index))
				except WindowsError as error:
					debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
					pass
				else:
					debug.debug("Appended ({data}) to devices list".format(data=_winreg.EnumKey(key, index)))

			for device in self.devices:
				try:
					key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,
											path.join(self.path_wpd, device),
											0,
											_winreg.KEY_READ)
				except WindowsError as error:
					debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
					pass
				else:
					self.results.append(path.join(self.path_wpd, device))
					debug.debug("Appended ({data}) to results list".format(data=path.join(self.path_wpd, device)))

			_winreg.CloseKey(key)
		finally:
			return self.results

	def EnumSTORAGE(self):
		""" Enumerate STORAGE registry artifacts and return results.
		If registry key does not exist it returns False """
		try:
			key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,
									path.join(self.path_storage),
									0,
									_winreg.KEY_READ)
		except WindowsError as error:
			debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
			return False
		else:
			for index in range(0, _winreg.QueryInfoKey(key)[0]):
				try:
					self.devices.append(_winreg.EnumKey(key, index))
				except WindowsError as error:
					debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
					pass
				else:
					debug.debug("Appended ({data}) to devices list".format(data=_winreg.EnumKey(key, index)))

			for device in self.devices:
				try:
					key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,
											path.join(self.path_storage, device),
											0,
											_winreg.KEY_READ)
				except WindowsError as error:
					debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
					pass
				else:
					self.results.append(path.join(self.path_storage, device))
					debug.debug("Appended ({data}) to results list".format(data=path.join(self.path_storage, device)))

			_winreg.CloseKey(key)		
		finally:
			return self.results

	def EnumWPDBUSENUM(self):
		""" Enumerate WPDBUSENUM registry artifacts and return results.
		If registry key does not exist it returns False """	
		try:
			key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,
									path.join(self.path_wpdbusenum),
									0,
									_winreg.KEY_READ)
		except WindowsError as error:
			debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
			return False
		else:
			for index in range(0, _winreg.QueryInfoKey(key)[0]):
				try:
					self.devices.append(_winreg.EnumKey(key, index))
				except WindowsError as error:
					debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
					pass
				else:
					debug.debug("Appended ({data}) to devices list".format(data=_winreg.EnumKey(key, index)))

			for device in self.devices:
				try:
					key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,
											path.join(self.path_wpdbusenum, device),
											0,
											_winreg.KEY_READ)
				except WindowsError as error:
					debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
					pass
				else:
					self.results.append(path.join(self.path_wpdbusenum, device))
					debug.debug("Appended ({data}) to results list".format(data=path.join(self.path_wpdbusenum, device)))
					
			_winreg.CloseKey(key)
		finally:
			return self.results

	def EnumUSB(self):
		""" Enumerate USB registry artifacts and return results.
		If registry key does not exist it returns False """	
		try:
			key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,
									path.join(self.path_usb),
									0,
									_winreg.KEY_READ)
		except WindowsError as error:
			debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
			return False
		else:
			for index in range(0, _winreg.QueryInfoKey(key)[0]):
				try:
					self.devices.append(_winreg.EnumKey(key, index))
				except WindowsError as error:
					debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
					pass
				else:
					debug.debug("Appended ({data}) to devices list".format(data=_winreg.EnumKey(key, index)))

			for device in self.devices:
				try:
					key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,
											path.join(self.path_usb, device),
											0,
											_winreg.KEY_READ)
				except WindowsError as error:
					debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
					pass
				else:
					self.results.append(path.join(self.path_usb, device))
					debug.debug("Appended ({data}) to results list".format(data=path.join(self.path_usb, device)))

			_winreg.CloseKey(key)
		finally:
			return self.results

	def EnumUSBSTOR(self):
		""" Enumerate USBSTOR registry artifacts and return results.
		If registry key does not exist it returns False """	
		try:
			key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,
									path.join(self.path_usbstor),
									0,
									_winreg.KEY_READ)
		except WindowsError as error:
			debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
			return False
		else:
			for index in range(0, _winreg.QueryInfoKey(key)[0]):
				try:
					self.devices.append(_winreg.EnumKey(key, index))
				except WindowsError as error:
					debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
					pass
				else:
					debug.debug("Appended ({data}) to devices list".format(data=_winreg.EnumKey(key, index)))

			for device in self.devices:
				try:
					key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,
											path.join(self.path_usbstor, device),
											0,
											_winreg.KEY_READ)
				except WindowsError as error:
					debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
					pass
				else:
					self.results.append(path.join(self.path_usbstor, device))
					debug.debug("Appended ({data}) to results list".format(data=path.join(self.path_usbstor, device)))

			_winreg.CloseKey(key)
		finally:
			return self.results

	def EnumMountedDevices(self):
		""" Enumerate MountedDevices registry artifacts and return results.
		If registry key does not exist it returns False """	
		try:
			key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,
									path.join(self.path_mounteddevices),
									0,
									_winreg.KEY_READ)
		except WindowsError as error:
			debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
			return False
		else:
			for index in range(0, _winreg.QueryInfoKey(key)[1]):
				try:
					self.results.append(_winreg.EnumValue(key, index))
				except WindowsError as error:
					debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
					pass
				else:
					debug.debug("Appended ({data}) to results list".format(data=_winreg.EnumValue(key, index)))

			_winreg.CloseKey(key)
		finally:			
			return self.results

	def EnumMountPoints2(self):
		""" Enumerate MountPoints2 registry artifacts and return results.
		If registry key does not exist it returns False """	
		try:
			key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,
									path.join(self.path_mountpoints),
									0,
									_winreg.KEY_READ)
		except WindowsError as error:
			debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
			return False
		else:
			for index in range(0, _winreg.QueryInfoKey(key)[0]):
				try:
					self.results.append(_winreg.EnumKey(key, index))
				except WindowsError as error:
					debug.debug("Exception in function ({fname}) error message ({error})".format(fname=_getframe().f_code.co_name, error=error))
					pass
				else:
					debug.debug("Appended ({data}) to results list".format(data=_winreg.EnumKey(key, index)))

			_winreg.CloseKey(key)
		finally:
			return self.results