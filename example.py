# import Libraries
import addsah as ads
import PIL

# make Image item from PIL.Image class
img2 = PIL.Image.open('خطين.png')

# perpraring an image to comparison - with it self -
ads.perp_img(img2)

# print the similraty percentage
print(ads.compa_imgs('خطين.png', 'خطين.png'))
