# Addsah: images comparison library &#124; العدسة: مكتبة مقارنة الصور
Addsah, is a Python Library that compapre between Images.  
العدسة، هيَ مكتبةٌ للغةِ Python تهتمُّ بمقارنةِ الصورِ.  

written by | كُتِبَت بيدِ:
- Sari Muhammad Alzahrani | ساري محمد الزهراني
- Qutbi | قُطبيّ

## introduction | المقدمة
**بسمِ اللهِ الرحمانِ الرحيمِ**

### Goals | الأهداف

أهم ما نركزُ عليهِ في تطويرِ المكتبةِ :  
- السرعة
- الكفاء
- سهولة الاستخدام

The most important things that we focus in Library development :  
- speed
- efficiency
- user-frindliness

### what can this version do | ما يمكن لذا الإصدارِ فعلُه

يمكنُكَ أن تقارنَ بينَ الصور بنظامِ ألوانِ الأبيضِ والأسودِ ( فقط )  
You can ( just ) compare btween images with black and white color system  

> Note | ملاحفظة :
> 
>&nbsp;&nbsp;&nbsp;&nbsp;إن وُجِدَت مربعاتٌ مُلَوّنةٌ؛ فلن تُقاَنَ؛ فقد تحصلُ على IndexError.  
>&nbsp;&nbsp;&nbsp;&nbsp;if there is a colored pixel; it will not comparing; so, maybe you will get IndexError.  

## using way | طريقة الاستخدام

أولُ ما تحتاجُ فعلَهُ هوَ إعدادُ الصورِ، أنظر للمثال الأول.  
First thing that you need is to perpare the images, see the first example.

> First example | المثال الأول
> ``` python
> # import Libraries
> import addsah as ads
> import PIL
>
> # make Image item from PIL.Image class
> img = PIL.Image.open('خطين.png')
> 
> # perpraring an image to comparison - with it self -
> ads.perp_img(img)
> ```

بعدَ إعدادِ الصورةِ، يمكنكَ استخدامُها بالمقارنةِ - سنُقارِنُها بنفسِها للاختصارِ - ، أنظر للمثالِ الثاني.  
Afrer perpartio the image, you can use it in comparison - we will co,parat it with it self for the sake of brevity - , see second example.  

> Second example | المثال الثاني
> ``` python
> # print the similraty percentage
> print(ads.compa_imgs('خطين.png', 'خطين.png'))
>```
** output | المُخرَج **
> ``` output
> 100.00
> ```
