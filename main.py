from PIL import Image
import os

directory = os.getcwd() + '\\images\\'
print(directory)

testImg = Image.open(os.path.join(directory, os.listdir(directory)[0]))

num_files = len([f for f in os.listdir(directory)if os.path.isfile(os.path.join(directory, f))])

totalRes = testImg.height * num_files

finalImage = Image.new('RGB', (testImg.width, totalRes))

currentHeight = 0

'''
create an image that stores the final image

'''

for img in os.listdir(directory):

    if img.endswith('.jpg') or img.endswith('.png'):
        img1 = Image.open(os.path.join(directory, img))

        finalImage.paste(img1, (0, currentHeight))

        currentHeight += img1.height

    else:
        continue

finalImage.save(os.getcwd() + '\\final.jpg')
