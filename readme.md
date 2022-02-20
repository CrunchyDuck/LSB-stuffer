# What is this?
A couple scripts for basic LSB steganography. What is that? Basically, hiding some data, like a .txt or .png, inside of an image!
Entirely made for fun.

## Set up 
Install python from [here](https://www.python.org/downloads/) (big yellow download button)
Download the script and place it in a folder
Open your command line in that folder
  - On windows, you can type "cmd" into the search bar of the file browser to open that folder in command line.
Install the requirements by typing in `pip install -r requirements.txt`

## Usage
### Stuffing an image
You can stuff any image with any other file, so long as it can fit inside of the target image. The program will tell you if there is not enough space.
The "stuffing" algorithm uses LSB stuffing - if you're curious how this works, look into "LSB steganography"
Change the variables under `### Input variables ###` to do what you need.
Run the program!
Your resultant image will look identical to a human, but will be quite obviously modified to anyone who is searching.

### Unstuffing an image
You can try to unstuff any image, but most of them will give garbage.
Change the variables under `### Input variables ###` to point to the files.
Run the program!
Unless you know the file type of what was originally stuffed, you may need to try different types to get the correct format. You should try to open it as a .txt file first - if it looks like junk, it's likely a different file format. Try to look for the [file signature](https://en.wikipedia.org/wiki/List_of_file_signatures) or "magic numbers" at the very start of the file and rename it to that file format. For example, a PNG will start with `‰PNG␍␊␚␊`.
