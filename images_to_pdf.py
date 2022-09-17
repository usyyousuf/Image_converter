from PIL import Image

single_image = Image.open(r'C:\Users\USER\Desktop\vlcsnap.png')
one_image = single_image.convert('RGB')
one_image.save(r'C:\Users\USER\Desktop\vlcsnap.pdf')