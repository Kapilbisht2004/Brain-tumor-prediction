import pickle
import cv2
import tkinter as tk
from tkinter import filedialog, messagebox, Label, Frame
from PIL import Image, ImageTk

# Load the saved model
model_path = "D:\\tumor_detect\\tumor_detect\\tumor_classification_model.pkl"
with open(model_path, 'rb') as f:
    loaded_model = pickle.load(f)

# Prediction function
def predict_tumor(image_path, model):
    dec = {0: 'No Tumor', 1: 'Tumor'}
    try:
        # Load and preprocess the imageZCX
        img = cv2.imread(image_path, 0)  # Load in grayscale
        if img is None:
            raise FileNotFoundError(f"Image not found at {image_path}")
        img = cv2.resize(img, (200, 200))  # Resize to match model input size
        img = img.reshape(1, -1) / 255.0  # Flatten and normalize

        # Predict using the loaded model
        pred = model.predict(img)[0]  # Get the prediction
        return dec[pred]
    except Exception as e:
        return f"Error: {str(e)}"

# Function to open file dialog and predict tumor
def browse_and_predict():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
    if not file_path:
        return

    try:
        # Display the selected image
        img = Image.open(file_path)
        img.thumbnail((300, 300))
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)
        image_label.image = img_tk

        # Predict tumor
        result = predict_tumor(file_path, loaded_model)
        result_label.config(text=f"Prediction: {result}")
        result_label.config(fg="green" if result == "No Tumor" else "red")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to predict: {str(e)}")

# Create the GUI
root = tk.Tk()
root.title("Tumor Detection System")
root.geometry("600x600")
root.configure(bg="#f0f0f5")

# Title Frame
title_frame = Frame(root, bg="#283593", height=80)
title_frame.pack(fill="x")
title_label = Label(
    title_frame, 
    text="Tumor Detection System", 
    font=("Helvetica", 20, "bold"), 
    bg="#283593", 
    fg="white"
)
title_label.pack(pady=20)

# Image Display
image_frame = Frame(root, bg="#e8eaf6", width=400, height=320)
image_frame.pack(pady=20)
image_label = Label(image_frame, bg="#e8eaf6")
image_label.pack(padx=10, pady=10)

# Result Label
result_label = Label(root, text="Prediction: ", font=("Helvetica", 16, "bold"), bg="#f0f0f5", fg="#333")
result_label.pack(pady=10)

# Browse Button
browse_button = tk.Button(
    root, 
    text="Select Image", 
    command=browse_and_predict, 
    font=("Helvetica", 14), 
    bg="#4caf50", 
    fg="white", 
    activebackground="#388e3c", 
    activeforeground="white", 
    relief="raised", 
    bd=2
)
browse_button.pack(pady=20)

# Footer
footer_label = Label(
    root, 
    text="Developed by Kapil Bisht", 
    font=("Helvetica", 10, "italic"), 
    bg="#f0f0f5", 
    fg="#555"
)
footer_label.pack(side="bottom", pady=10)

# Run the application
root.mainloop()
