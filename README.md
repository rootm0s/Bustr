# Bustr

```
     ____             __
    / __ )__  _______/ /______
   / /_/ / / / / ___/ __/ ___/
  / /_/ / /_/ (__  ) /_/ /    
 /_____/\__,_/____/\__/_/     Version 1.0.0
 ```

Bustr is a utility built to discover if any new USB, Storage, Phone or Bluetooth device has been attached/paired with the operating system, by monitoring registry artifacts.

#### Usecase:
The idea is to run Bustr on a fresh installed computer. If it discover a new usb, storage, phone or bluetooth device has been attached/paired with system, log the results and generate a HTML report with the registry data and log results. Tested this with 4 different USB manufacturers and Android and iPhone.

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
