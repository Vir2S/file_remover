import os
import time
from random import randint
from config import *


class Handler:
	folder = FOLDER
	extension_track = EXTENSION

	# If modified then moving files inside folder
	def get_files(self):
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

					if os.path.isfile(new_path):
						new_filename = new_path.rstrip("." + extension)
						new_path = new_filename + "_" + str(randint(1, 1000)) + "." + extension

					os.rename(file, new_path)
				except IOError:
					path = self.folder["destination"] + "/" + key
					os.mkdir(path)
					new_path = path + "/" + filename

					if os.path.isfile(new_path):
						new_filename = new_path.rstrip("." + extension)
						new_path = new_filename + "_" + str(randint(1, 1000)) + "." + extension

					os.rename(file, new_path)


# Start the program
handle = Handler()
handle.get_files()
