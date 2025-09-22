# import Libraries
import addsah as ads
import PIL

# make Image item from PIL.Image class
img1 = PIL.Image.open('Addsah_test_imgs/مخطط3.png')
img2 = PIL.Image.open('Addsah_test_imgs/خطين.png')

# perpraring an images to comparison
ads.perp_img(img1)
ads.perp_img(img2)

# print the similraty percentage
print(ads.compa_imgs('Addsah_test_imgs/خطين.png', 'Addsah_test_imgs/خطين.png'))
