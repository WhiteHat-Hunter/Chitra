import os
import cv2
import pyfiglet
from colorama import init
from termcolor import colored 

init()

os.system("cls || clear")

figlet1 = pyfiglet.figlet_format("CHITRA -", width=200)
figlet2 = pyfiglet.figlet_format("PHOTO TO SKETCH CONVERTER", font="bubble", width=100)
print(colored(figlet1,'red'))
print(colored(figlet2,'red'))

print(colored(" ---------------------------------- Creator: SIDDHESH SURVE ---------------------------------- \n", 'blue'))


choice = input("Enter Image Path with Image Name & Extension: ")
image = cv2.imread(choice)

gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

invert = cv2.bitwise_not(gray_img)
blur = cv2.GaussianBlur(invert,(21,21),0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(gray_img, invertedblur, scale=256.0)

output = input("Enter Image Path with Name & Extension to Save: ")
cv2.imwrite(output, sketch)
cv2.imshow(output, sketch)
cv2.waitKey(10000)
