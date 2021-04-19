from config import *
from watchdog.observers import Observer
import os
import time
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
	# If modified then moving files inside folder
	def on_modified(self, event):
		# Moving all files inside folder folder_track
		for filename in os.listdir(folder_track):
			# Check file extension
			extension = filename.split(".")
			# If photo
			if len(extension) > 1 and (extension[1].lower() == "jpg" or extension[1].lower() == "png" or extension[1].lower() == "svg"):
				# move file into photos folder
				file = folder_track + "/" + filename
				new_path = folder_dest + "/Photos/" + filename
				os.rename(file, new_path)
			# If video then move into videos folder
			elif len(extension) > 1 and extension[1].lower() == "mp4":
				file = folder_track + "/" + filename
				new_path = folder_dest + "/Videos/" + filename
				os.rename(file, new_path)


# Start the program
handle = Handler()
observer = Observer()
observer.schedule(handle, folder_track, recursive=True)
observer.start()

# The code will checking every 10 milliseconds
try:
	while True:
		time.sleep(10)
except KeyboardInterrupt:
	observer.stop()

observer.join()
