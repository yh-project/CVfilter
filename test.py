from tkinter import *
import PIL
from PIL import ImageTk, Image

root = Tk()
image = Image.open("testImage.jpg")
height = 500
width = 500

canvas = Canvas(root, height=500, width=500)
image = image.resize((height,width),PIL.Image.Resampling.LANCZOS)

photo = ImageTk.PhotoImage(image)
item4 = canvas.create_image(height/2, width/2, image=photo)

canvas.pack()
root.mainloop()