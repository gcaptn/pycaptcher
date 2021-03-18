import PIL
import pyautogui
import time
import cv2
import numpy
import threading


class Recording:
	def __init__(self, path = "."):
		timestamp = time.time()
		self.name = path+"/" + "pycaptcher"+str(timestamp) + ".avi"
		self.writer = None
		self.recording = False
	
	def take(self, x, y, width, height):
		# This will not follow the window. Originally meant to pass the interface
		# so I could call get_bounding_rect(), but it feels like code smell

		def _take_video():
			# blatant copy paste from a blog
			self.region = (x, y, width, height)
			self.resolution = (width, height)
			self.codec = cv2.VideoWriter_fourcc(*"XVID")
			self.FPS = 30.0
			self.writer = cv2.VideoWriter(self.name, self.codec, self.FPS, self.resolution)
			self.recording = True

			while self.recording:
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
		timestamp = time.time()
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