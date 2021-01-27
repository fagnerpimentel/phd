#!/usr/bin/env python

import subprocess
import sys
import os

class Path_Finder(object):

	def __init__(self, arg):
		
		if len(arg) < 3:
			print "\n\nERR: takes two arguments the id of the vendor and the id of the model, whitch can be found by using \'lsusb\' on the terminal\n\n"
		else:		
			self.id_vendor = arg[1]
			self.id_model = arg[2]
			self.path_finder()

	def list_creator(self, cmd):
		final_list=[]
		l = subprocess.check_output(cmd).split("\n")
		for i in l:
			if i != '':
				final_list.append(i)
		return final_list

	def yalm_maker(self, dev_path, is_arduino):

		os.chdir(os.path.expanduser("/") + "tmp/") #"/catkin_ws/src/elevator/launch/"
		with open('%s_%s.yalm' %(self.id_vendor, self.id_model), 'w') as file:
			lines = []
			lines.append("port: %s\n" %(dev_path))
			if (is_arduino):
				lines.append("baud: %s\n" %(57600))
			file.seek(0)
			file.truncate()			
			file.writelines(lines)
			file.close()
		

	def path_finder(self):

		for usb_port in range(1,5):
			syspath = self.list_creator(["find","/sys/bus/usb/devices/usb%s/" %(usb_port) ,"-name","dev"])
			for i in syspath:
				i = i[:len(i) - 4]
				properties = self.list_creator(["udevadm","info","-q","property","-p",i])
				devname = subprocess.check_output(["udevadm","info","-q","name","-p",i])
				devname = devname[:len(devname) - 1]
				if (("bus/" != devname[:4]) and ("ID_MODEL_ID=%s" %(self.id_model)) in properties) and (("ID_VENDOR_ID=%s" %(self.id_vendor)) in properties):
					self.yalm_maker("/dev/%s" %devname, "ID_VENDOR_FROM_DATABASE=Arduino SA" in properties)

if __name__ == '__main__':
		try:
			Path_Finder(sys.argv)
		except subprocess.CalledProcessError:
			pass
