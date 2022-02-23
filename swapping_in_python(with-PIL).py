#importing time
import time
#importing Image class from PIL package
from PIL import Image

#creating a object
akshaySwap = Image.open("C:\\Users\\91808\\Pictures\\Saved Pictures\\akshaySwap.jpg")


a = 10
b = 20
print('(', a, ',', b, ')')

akshaySwap.show();
time.sleep(2)

a, b = b, a
print('(', a, ',', b, ')')
