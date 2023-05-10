# JPG/JPEG EXIF Data Scrubber

A Python script that allows you to scrub EXIF (Exchangeable Image File Format) data from JPG/JPEG images.

## Overview

The **JPG/JPEG EXIF Data Scrubber** is a script that removes EXIF metadata from JPG/JPEG image files. EXIF data often contains information such as camera settings, location, and timestamps, which some users may prefer to remove for privacy or security reasons.

This script utilizes the `exif` library to read and modify the EXIF data in the provided image file. It deletes all available tags and saves the modified image as a new file.

## Features

- Removes all EXIF metadata from a JPG/JPEG image.
- Preserves the image content while removing EXIF data.
- Simple and easy-to-understand Python script.

## Dependencies

To run the script, you need to have the following dependency installed:

- `exif` library: You can install it using `pip` by running the following command:
  ```
  pip install exif
  ```

## Usage

1. Place the `source.jpg` file in the same directory as the script.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the script using the following command:
   ```
   python exif_scrubber.py
   ```
4. The script will read the EXIF data from `source.jpg`, delete all available tags, and save the modified image as `result.jpg` in the same directory.
5. The script will display the list of available tags before and after the deletion process.
6. Check the output to verify if the EXIF data has been successfully removed. If the second list is empty, it confirms that all tags have been deleted.
7. You can now use the `result.jpg` file, which is free of EXIF metadata.
