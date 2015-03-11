#! /usr/bin/env python
#picture_hide.py
#Hidding a message in an image
from PIL import Image
def encode_image (img,msg):
#hiding msg string as characters in ASII values 
	length = len (msg)
	#limit the length of msg to 255
	if length > 255:
	
		print ("text too long; dont exceed 255 characters")
		return False
	if img.mode != 'RGB':
		print ("image needs to be RGB")
		return False
	#use copy of Image to hide text
	encoded = img.copy() 
	width,height = img.size
	index = 0
	for row in range (height):
		for col in range (width):
			r,g,b = img.getpixel((col,row))
		#first Value Is length of Msg
		if row == 0 and col == 0 and index < length:
			asc = length
		elif index<= length:
			c=msg[index -1]
			asc=ord(c)
		else:
			asc = r
		encoded.putpixel((col,row),(asc,g,b))
		index = +1
	return encoded
def decode_image(img):
#check for the red portion of an image (r,g,b) tupule for hidden message characters
	width, height = img.size
	msg = ""
	index = 0
	for row in range (height):
		for col in range (width):
			try:
				r,g,b = img.getpixel((col,row))
			except ValueError:
			#Need to add transparency for some.png files
				r,g,b,a = img.getpixel((col,row))
			if row == 0 and col == 0:
				length = r
			elif index <=lenth:
				msg += chr(r)
			index += 1
	return msg
#Pick .png of bmp file you have in the working directory or give full path
original_image_file = ".png"
img = Image.open(original_image_file)
#image need to be 'RGB'
print (img,img.mode) #test
#create new filename for the encoded image
encoded_image_file = "enc_" + original_image_file
#dont exceed 255 characters in the message
secret_msg = raw_input("enter your message here") #test
img_encoded = encode_image(img,secret_msg)
if img_encoded:
	#save the the image with the hidden text
	img_encoded.save(encoded_image_file)
	print ("{}saved!".format(encoded_image_file))
#view the saved file
	import webbrowser
	webbrowser.open(encoded_image_file)
	#Get Hidden text back
	img2 = Image.open(encoded_image_file)
	hidden_text = decode_image(img2)
	print ("Hidden text :\n{}".format(hidden_text))

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
