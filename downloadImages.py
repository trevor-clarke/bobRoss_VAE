# This script will work if the images are named sequentially in a specific folder on a website ie:
# image1.png, image2.png, etc

# Settings 
start_number    = 1  
end_number      = 100
time_delay      = 3  #time in seconds between request
url_to_folder   = "https://example.com/images/"
image_base_name =  "image" #in the example above, this would be image
file_extention  = ".png"
save_folder     = "downloaded_images/"

for x in range(startNumber,endNumber):
  time.sleep(time_delay)
  img_data = requests.get(url_to_folder + image_base_name + str(x) + file_extention).content
  with open(save_folder + image_base_name + str(x)+file_extention, 'wb') as file:
      file.write(img_data)
