# Move files from one folder to another

# import the necessary libraries
import os
import shutil
from datetime import datetime

# Set directories
from_wd = "" # Specify the folder where you intend to move your files from such as ~/Desktop/Temp
trash = os.path.expanduser("~/.Trash") # Change the file path to where your trash is located
current_time = datetime.now().strftime("%Y%m%dT%H%M%S") # Use timestamp to ensure that the new file name is always unique
number_of_files = 0

# Loop through the number of files in the specified directory
for file in os.listdir(from_wd):
	if file != ".DS_Store":
		try:
			shutil.move(from_wd + "/" + file, trash)
			number_of_files += 1
		except Exception as e:
			# Trash bin has a file that shares the same name as the one we are trying to move there
			if "already exists" in str(e): 
				file_name_array = file.split(".") # Split the file so we can append the time before the file extension
				new_file_name = file_name_array[0] + "_" + current_time + "." + file_name_array[-1] # Create new file name
				os.rename(from_wd + "/" + file, new_file_name)
				shutil.move(new_file_name, trash) # Move files to trash
				number_of_files += 1
			else:
				pass
	else:
		pass

print(str(number_of_files) + " " + "files have been moved to the trash bin")