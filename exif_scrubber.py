# JPG EXIF Data Scrubber
# MIT License
# Copyright (c) 2023 Yetkin Degirmenci

# Importing exif library
from exif import Image

# Define source and target filenames
source="source.jpg"
result="result.jpg"

# Open for reading the exif data
with open(source, 'rb') as img_file:
    img = Image(img_file)

# Print all available tags    
print ("\n ALL THE AVAILABLE TAGS IN THIS IMAGE \n")
print ("\n",sorted(img.list_all()),"\n")

# Delete all available tags
img.delete_all()

# Save as a new file
with open(result, 'wb') as edited_file:
     edited_file.write(img.get_file())

# open for reading the exif data
with open(result, 'rb') as  endresult:
    rimg = Image(endresult)

# Print and see if any available tags    
print ("\n",sorted(rimg.list_all()),"\n")

if rimg!=[]:
    print("CONFIRMED ALL TAGS ARE DELETED \(ˆ˚ˆ)/ ")
else:
    print("SOMETHING WENT WRONG ¯\_(ツ)_/¯")

