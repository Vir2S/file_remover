from config import *
from watchdog.observers import Observer
import os
import time
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
	folder = FOLDER
	folder_track = FOLDER["tracking"]
	folder_dest = FOLDER["destination"]
	extension_track = EXTENSION

	# If modified then moving files inside folder
	def on_modified(self, event):
		# Moving all files inside tracking folder
		for filename in os.listdir(self.folder_track):
			# Check file extension
			try:
				extension = filename.split(".")[-1]
			except IndexError:
				extension = ""
			# If photo
			if len(extension) > 1 and extension.lower() in self.extension_track["photo"]:
				# move file into photos folder
				file = self.folder_track + "/" + filename
				new_path = self.folder_dest + "/Photos/" + filename
				os.rename(file, new_path)
			# If video then move into videos folder
			elif len(extension) > 1 and extension.lower() in self.extension_track["video"]:
				file = self.folder_track + "/" + filename
				new_path = self.folder_dest + "/Videos/" + filename
				os.rename(file, new_path)
			# If pdf then move into pdfs folder
			elif len(extension) > 1 and extension.lower() in self.extension_track["pdf"]:
				file = self.folder_track + "/" + filename
				new_path = self.folder_dest + "/Pdfs/" + filename
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
