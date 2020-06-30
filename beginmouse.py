#!/usr/bin/python
import sys
import usb.core
import usb.util
# decimal vendor and product values
#idVendor               : 0x0c76
#idProduct              : 0x1529

dev = usb.core.find(idVendor=0x0c76, idProduct=0x1529)
print("dev -->",dev)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# or, uncomment the next line to search instead by the hexidecimal equivalent
#dev = usb.core.find(idVendor=0x45e, idProduct=0x77d)
# first endpoint
#endpoint = dev[0].interfaces()[1](1)
#endpoint = dev[0][(2,1)][0]
endpoint = dev[0][(2)][0]
print("endpoint-->", endpoint)
#endpoint = dev[0].interfaces()[1].endpoints()[0]
interface = dev[0][(2)].bInterfaceNumber
#dev.reset()
# if the OS kernel already claimed the device, which is most likely true
# thanks to http://stackoverflow.com/questions/8218683/pyusb-cannot-set-configuration
if dev.is_kernel_driver_active(interface):
  # tell the kernel to detach
  dev.detach_kernel_driver(interface)
  # claim the device
  # usb.util.claim_interface(dev, interface)

#dev.set_configuration()
eaddr = endpoint.bEndpointAddress

r = dev.read(eaddr, 200)
print(len(r))  
#collected = 0
#attempts = 50
#while collected < attempts :
#    try:
#        data = dev.read(endpoint.bEndpointAddress,endpoint.wMaxPacketSize)
#        collected += 1
#        print(data)
#    except usb.core.USBError as e:
#        data = None
#        if e.args == ('Operation timed out',):
#            continue
# release the device
usb.util.release_interface(dev, interface)
# reattach the device to the OS kernel
dev.attach_kernel_driver(interface)
