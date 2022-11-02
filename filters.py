from tkinter import *
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog

"""
tk = Tk()
tk.title('Spatial Filtering')
 
def image_open():
    global image_path 
    tk.filename = filedialog.askopenfilename(initialdir='', title='파일선택', filetypes=(('png files', '*.png'), ('jpg files', '*.jpg'), ('all files', '*.*')))
 
    image_path = ImageTk.PhotoImage(Image.open(tk.filename))
    print(tk.filename)
    Label(image=image_path, width=400, height=400).pack()
 
my_btn = Button(tk, text='파일열기', command=image_open).pack()
 
tk.mainloop()
"""

def median_filter(img, filter_size=(3,3), stride=1):
    img_shape = np.shape(img)

    result_shape = tuple(np.int64((np.array(img_shape)-np.array(filter_size))/stride+1))
    result = np.zeros(result_shape)

    for h in range(0, result_shape[0], stride):
        for w in range(0, result_shape[1], stride):
            tmp = img[h:h+filter_size[0], w:w+filter_size[1]]
            tmp = np.sort(tmp.ravel())
            result[h,w] = tmp[int(filter_size[0]*filter_size[1]/2)]

    return result

def show(img, max_ylim=12500):
    
    plt.imshow(img, cmap='gray')
    plt.show()
    
    if max_ylim != 'none':
        axes = plt.axes()
        axes.set_ylim([0, max_ylim])
    plt.hist(img.ravel(), bins=256, range=[0,256])
    plt.show()

#hello
