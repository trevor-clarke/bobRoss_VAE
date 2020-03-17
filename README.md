# bobRoss_VAE
First attempt at machine learning. Aiming to train a model to generate Bob Ross Styled images. 
As this was my first attemt at machine learning, most of what was accomplished, used other people's code. 
What I got to work used a Keras network and was trained on approx. 400 images total. 

### Note 1. Getting the images. 
Bob Ross his name, trademark and copyright are all still enforced. This means that I will be unable to supply you with, well, a copy of his images. However, the output while may appear similar will in no way be a copy of his work. Similar to how those who decided to learn how to paint like him are not breaking copyright by painting in his style. 

I have found a website to download the images from. Again, due to the reasons mentioned above, I will not explain how to do this. However, I will mention this completely unrelated python script (found in downloadImages.py) that you may find useful, should you ever need to download images of which you have the rights to. 

### Note 2. Yikes. 
I started this with a very specific goal to train a the model using my own data. I am finding it very difficult to find examples explaining how to import and transform my own data into something that Keras can understand.

### Note 3. Found something
I stubled upon a video that explained how to import data to Keras. The webpage associated with the video can be found here:
https://pythonprogramming.net/loading-custom-data-deep-learning-python-tensorflow-keras/

### Note 4.
Now that I have the images imported, I am faced with a block of code, that is, the definition of the network and its helper funcitons. I am trying to find some example code that a) supports coloured images as input b) support images larger than the 28x28 defined in the majority of the examples I am finding.

### Note 5. 
After a ton of time, I found this blog with example code that has been written well enough to support coloured images of different sizes (even though it was not intended to work)! YES! Thank you.
https://www.machinecurve.com/index.php/2019/12/30/how-to-create-a-variational-autoencoder-with-keras/

### Note 6.

![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)
