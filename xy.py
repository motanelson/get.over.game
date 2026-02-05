
import tkinter as tk
from PIL import Image, ImageTk
import random
STEP=10
root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=400, bg="black")
canvas.pack()

img = Image.open("bit.png").convert("RGBA")
img2 = Image.open("pin.png").convert("RGBA")
data = img.getdata()
new_data = []

for pixel in data:
    # se for preto puro, fica transparente
    if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
        new_data.append((0, 0, 0, 0))
    else:
        new_data.append(pixel)

img.putdata(new_data)

data = img2.getdata()
new_data = []

for pixel in data:
    # se for preto puro, fica transparente
    if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
        new_data.append((0, 0, 0, 0))
    else:
        new_data.append(pixel)

img2.putdata(new_data)


pic = ImageTk.PhotoImage(img)
pic2 = ImageTk.PhotoImage(img2)
xy=[]
for n in range(20):
    xx=int(int(random.random()*60)*10)
    yy=int(int(random.random()*40)*10)
    xy=xy+[xx]+[yy]
xxx=50
yyy=50
xxxx=0
yyyy=0
h=[]
score=0
rect = canvas.create_image(xxx, yyy, image=pic)
lens=int(len(xy)//2)
for n in range(0,lens):
    h=h+[canvas.create_image(xy[n*2], xy[n*2+1], image=pic2)]
def move(event):
    global xxx,yyy,xxxx,yyyy,xy,lens,h,score
    if event.keysym == "Up":
        canvas.move(rect, 0, -STEP)
        yyy=yyy-STEP
    elif event.keysym == "Down":
        canvas.move(rect, 0, STEP)
        yyy=yyy+STEP
    elif event.keysym == "Left":
        canvas.move(rect, -STEP, 0)
        xxx=xxx-STEP
    elif event.keysym == "Right":
        canvas.move(rect, STEP, 0)
        xxx=xxx+STEP
    for n in range(lens):
        xxxx=xy[n*2]
        yyyy=xy[n*2+1]
        if xxxx==xxx and yyyy==yyy:
            canvas.move(h[n], 0-xxxx-50,0)
            score=score+10
            print("score : "+str(score))
# Capturar teclas
root.bind("<Up>", move)
root.bind("<Down>", move)
root.bind("<Left>", move)
root.bind("<Right>", move)

root.mainloop()
