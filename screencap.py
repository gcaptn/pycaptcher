import PIL
import pyautogui
import cv2
import numpy
import threading
import time
from math import floor


def get_formatted_time():
	# Format a timestamp for saving files
	localtime = time.localtime()
	return "{0}{1}{2}_{3}".format(
		localtime.tm_year, localtime.tm_mon, localtime.tm_mday, floor(time.time()*100))


class Recording:
	def __init__(self, interface, path = "."):
		timestamp = get_formatted_time()
		self.interface = interface
		self.name = path+"/" + "pycaptcher"+str(timestamp) + ".avi"
		self.writer = None
		self.recording = False

	def update_region(self):
		if self.interface:
			self.region = self.interface.get_bounding_rect()
	
	def take(self, x, y, width, height):
		# blatant copy paste
		def _take_video():
			self.region = (x, y, width, height)
			self.resolution = (width, height)
			self.codec = cv2.VideoWriter_fourcc(*"XVID")
			self.FPS = 30.0
			self.writer = cv2.VideoWriter(self.name, self.codec, self.FPS, self.resolution)
			self.recording = True

			while self.recording:
				self.update_region()
				image = pyautogui.screenshot(region = self.region)
				frame = numpy.array(image)
				frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
				self.writer.write(frame)

		threading._start_new_thread(_take_video)

	def stop(self):
		self.writer.release()
		self.recording = False

	def save(self):
		del self


class Screenshot():
	def take(self, x, y, width, height):
		image = pyautogui.screenshot(region=(x, y, width, height))
		self.image = image

	def save(self, path = "."):
		timestamp = get_formatted_time()
		self.name = path+"/" + "pycaptcher"+str(timestamp) + ".png"
		self.image.save(self.name)
		del self


if __name__ == "__main__":
	# x, y, width, height = 250, 300, 600, 400

	"""class fake_interface():
		def get_bounding_rect(self):
			return x, y, width, height"""

	"""shot = Screenshot()
	shot.take(x, y, width, height)
	shot.save(".")"""

	"""video = Recording()
	video.take(x, y, width, height)
	time.sleep(5)
	video.stop()
	video.save()"""