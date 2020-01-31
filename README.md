# bustr

```
     ____             __
    / __ )__  _______/ /______
   / /_/ / / / / ___/ __/ ___/
  / /_/ / /_/ (__  ) /_/ /    
 /_____/\__,_/____/\__/_/     Version 1.0.0
 ```

Bustr is a framework built to detect if any new Usb, Storage, Phone or Bluetooth device has been attached/paired with system. Designed to run under a non-administrator account but also works while running with higher privileges.

All the activity detected by Bustr is logged.

#### Features:
   * Live monitoring of registry artifacts, logging the results to disk
   * Ability to run hidden, the console window hides but the application still running
   * Generate a HTML report using logs and exported registry data
   * Ability to debug all Bustr functions
   
#### Ability to monitor activity of:
   * USB (USB device stack)
   * Storage (Disks)
   * USBSTOR (Flash drives)
   * BTHPORT (Bluetooth pairing)
   * WPDBUSENUM (USB/Flash drives)
   * Mounted devices (Devices with drive letter or volume)
   * Mountpoints (Anything with a valid mountpoint)  
   * Known devices (Phones, disks etc)
   * Windows Portable devices (Phones, Flash drives, USB drives etc)
