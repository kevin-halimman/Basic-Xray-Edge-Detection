import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import cv2

root = tk.Tk()
root.title("Medical Imaging Edge Detection")
root.geometry("800x600")

def upload_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        image = image.resize((400, 400))
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(root, image=photo)
        label.image = photo

        image_cv = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        blur = cv2.GaussianBlur(image_cv, (5, 5), 0)
        edges = cv2.Canny(blur, 20, 210)
        image2 = Image.fromarray(edges)
        image2 = image2.resize((400, 400))
        photo2 = ImageTk.PhotoImage(image2)
        label2 = ttk.Label(root, image=photo2)
        label2.image = photo2
        label2.pack()
        label.pack()

ttk.Button(root, text = "Upload Image", command = upload_image).pack()
root.mainloop()