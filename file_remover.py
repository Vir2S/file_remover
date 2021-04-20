from config import *
from watchdog.observers import Observer
import os
import time
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
	folder = FOLDER
	folder_track = FOLDER["tracking"]
	folder["destination"] = FOLDER["destination"]
	extension_track = EXTENSION

	# If modified then moving files inside folder
	def on_modified(self, event):
		# Moving all files inside tracking folder
		for filename in os.listdir(self.folder["tracking"]):
			# Check file extension
			try:
				extension = filename.split(".")[-1]
			except IndexError:
				extension = ""

			self.moving_files(filename, extension)

	def moving_files(self, filename, extension):
		# Check files in extension_track dict
		for key, value in self.extension_track.items():
			if len(extension) > 1 and extension.lower() in value:
				# move file into images folder
				file = self.folder["tracking"] + "/" + filename
				try:
					new_path = self.folder["destination"] + "/" + key + "/" + filename
					os.rename(file, new_path)
				except IOError:
					path = self.folder["destination"] + "/" + key
					os.mkdir(path)
					new_path = path + "/" + filename
					os.rename(file, new_path)


# Start the program
handle = Handler()
observer = Observer()
observer.schedule(handle, FOLDER["tracking"], recursive=True)
observer.start()

# The code will checking every 10 milliseconds
try:
	while True:
		time.sleep(10)
except KeyboardInterrupt:
	observer.stop()

observer.stop()
