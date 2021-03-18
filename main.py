import ui
import screencap

import os
import re
import keyboard


def clean_path(path):
	path = path.replace("\\", "/")
	path = re.sub("/$", "", path)
	return path


def find_or_create_dir(path):
	path = clean_path(path)
	if not os.path.isdir(path):
		os.mkdir(path)

def main():
	# User state
	state = {
		"current_recording": None
	}

	interface = ui.UI()
	interface.set_filesave(os.path.expanduser("~\\Desktop") + "\\pycaptcher")

	def take_screenshot():
		shot = screencap.Screenshot()
		x, y, width, height = interface.get_bounding_rect()
		shot.take(x, y, width, height)

		save_dir = interface.get_filesave()
		find_or_create_dir(save_dir)
		shot.save(save_dir)

	def start_recording():
		save_dir = interface.get_filesave()
		find_or_create_dir(save_dir)

		state["current_recording"] = screencap.Recording(interface, save_dir)
		recording = state["current_recording"]
		interface.set_statustext("Recording")
		interface.set_lock()

		x, y, width, height = interface.get_bounding_rect()
		recording.take(x, y, width, height)

	def stop_recording():
		recording = state["current_recording"]
		recording.stop() # stop writing
		recording.save() # trash the recording object

		state["current_recording"] = None
		interface.set_statustext("pycaptcher")
		interface.set_lock(False)

	def take_recording():
		if state["current_recording"]:
			stop_recording()
		else:
			start_recording()

	interface.set_capture_callback(take_screenshot)
	interface.set_record_callback(take_recording)
	keyboard.add_hotkey("ctrl+f12", take_screenshot)
	keyboard.add_hotkey("ctrl+f11", take_recording)
	interface.run()


if __name__ == "__main__":
	main()