''' الإصدارُ 0.01
 أهدافُ المكتبةِ :
 	-[إيجاد نسبة التشابه بينَ الصورِ ]
 	-[العمل على الأجهزة متوسطة الأداء ]
 	-[السرعة والكفاءة ]

'''

# إستدعاءُ مكتبةِ التعامُلِ مَعَ الصورِ
from PIL import Image


def perp_img(img):
	pxl = img.load()
	x, y = img.size
	img_colors = ''
	
	with open(f'{img.filename}.txt', 'w') as text_img:
		for i in range(y):
			img_colors = ''
			for j in range(x):
				if pxl[j, i][0] >= 127.5 or pxl[j, i][1] >= 127.5:
					img_colors += '1'
				else:
					img_colors += '0'
			
			img_colors += '\n'
			text_img.write(img_colors)

def _compa_lins(bits1, bits2):
	matches = []
	for i in range(len(bits1)) :
		if bits1[i] == bits2[i]:
			matches.append(1)
	
	return matches

def _add_array(array):
	count = 0
	for i in array:
		count += i
	print(count)
	return count


def compa_imgs(img1, img2):
	with open(img1+'.txt', 'r') as file:
		img1_lines = file.readlines()
	with open(img2+'.txt', 'r') as file:
		img2_lines = file.readlines()
	
	img1 = Image.open(img1)
	img2 = Image.open(img2)
	
	if img1.size == img2.size:
		
		matching_pxl_nums = list(map(_compa_lins, img1_lines, img2_lines))
		
		for i in matching_pxl_nums:
			matching_pxl_nums[matching_pxl_nums.index(i)] = len(i)
		
		return (len(matching_pxl_nums) / list(img1.size)[0]) * 100
	else : 
		return None


