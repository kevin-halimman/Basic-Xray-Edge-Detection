import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import cv2

root = tk.Tk()
root.title("Medical Imaging Edge Detection")
root.geometry("800x600")

imageframe = ttk.Frame(root)
imageframe.pack(expand=True, fill='both')

imageframe.columnconfigure(0, weight=1)
imageframe.columnconfigure(1, weight=1)

label_original = ttk.Label(imageframe, text="Original Image")
label_processed = ttk.Label(imageframe, text="Processed Image")
label_original.grid(row=0, column=0, padx=10, pady=10)
label_processed.grid(row=0, column=1, padx=10, pady=10)

def scale_to_fit(image, max_size):
    if image.width > max_size[0] or image.height > max_size[1]:
        ratio = min((max_size[0] - 30) / image.width, (max_size[1] - 30) / image.height)
        new_size = (int(image.width * ratio), int(image.height * ratio))
    else:
        new_size = (image.width, image.height)
    return image.resize(new_size, Image.LANCZOS)
    
def upload_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        image = scale_to_fit(image, (imageframe.winfo_width()//2, imageframe.winfo_height()))
        photo = ImageTk.PhotoImage(image)
        label_original.configure(image=photo, text = "Original Image", compound = 'bottom')
        label_original.image = photo

        image_cv = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        blur = cv2.GaussianBlur(image_cv, (5, 5), 0)
        edges = cv2.Canny(blur, 30, 150)
        image2 = Image.fromarray(edges)
        image2 = scale_to_fit(image2, (imageframe.winfo_width()//2, imageframe.winfo_height()))
        photo2 = ImageTk.PhotoImage(image2)
        label_processed.configure(image=photo2, text = "Processed Image", compound = 'bottom')
        label_processed.image = photo2

ttk.Button(root, text = "Upload Image", command = upload_image).pack()
root.mainloop()