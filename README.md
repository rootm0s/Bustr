# Bustr

```
     ____             __
    / __ )__  _______/ /______
   / /_/ / / / / ___/ __/ ___/
  / /_/ / /_/ (__  ) /_/ /    
 /_____/\__,_/____/\__/_/     Version 1.0.0
 ```

Bustr is a framework built to discover if any new Usb, Storage, Phone or Bluetooth device has been attached/paired with system. Designed to run with either administrator account or as normal user.

#### Features:
   * Works on all Windows versions
   * Live monitoring of registry artifacts, logging the results to disk
   * Ability to run hidden, the console window hides but the application still running
   * Generate a HTML report using logs and exported registry data
   * Ability to debug all Bustr functions
   * Play system beep sound if a new discovery happened
   * Lock the machine by mimicking "CTRL+ALT+DEL > Lock" if a new discovery happened
   
#### Ability to monitor activity of these registry artifacts simultaneously:
   * SYSTEM\MountedDevices
   * SYSTEM\CurrentControlSet\Enum\USB
   * SYSTEM\CurrentControlSet\Enum\SCSI
   * SYSTEM\CurrentControlSet\Enum\BTHENUM
   * SYSTEM\CurrentControlSet\Enum\USBSTOR
   * SYSTEM\CurrentControlSet\Enum\STORAGE\Volume
   * SOFTWARE\Microsoft\Windows Portable Devices\Device
   * SYSTEM\CurrentControlSet\Enum\SWD\WPDBUSENUM
   * SYSTEM\CurrentControlSet\Services\BTHPORT\Parameters\Devices
   * Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2\CPC\Volume
   * Software\Microsoft\Windows\CurrentVersion\Explorer\AutoplayHandlers\KnownDevices

#### Preview of the utility running with monitoring debugging active
![bustr](https://i.imgur.com/DJUg7Oj.jpg)
