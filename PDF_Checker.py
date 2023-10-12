import tkinter as tk
from tkinter import filedialog
import fitz  # PyMuPDF for PDF 
from PIL import Image, ImageTk  # Import Pillow for image handling

def check_pdf():
    file_path = file_entry.get()
    try:
        doc = fitz.open(file_path)
        is_scanned = True

        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text = page.get_text()
            # print(text.strip())
            if text.strip():
                is_scanned = False
                break

        doc.close()

        if is_scanned:
            result_label.config(text="The PDF is a scanned image.", foreground="red", font=("Helvetica", 20, "bold"))
        else:
            result_label.config(text="The PDF contains text.", foreground="red", font=("Helvetica", 20, "bold"))
        
    except Exception as e:
        result_label.config(text="An error occurred. Please check the file or try again.")

def clear_result():
    result_label.config(text="")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)
    clear_result()

def retry():
    file_entry.delete(0, tk.END)
    result_label.config(text="")

    

# Create the main application window
app = tk.Tk()
app.title("PDF Checker")

# Create and configure widgets
file_label = tk.Label(app, text="PDF File:")
file_entry = tk.Entry(app, width=50)
browse_button = tk.Button(app, text="Browse", command=browse_file)
check_button = tk.Button(app, text="Check PDF", command=check_pdf)
clear_button = tk.Button(app, text="Clear Result", command=clear_result)
retry_button = tk.Button(app, text="Retry", command=retry)
result_label = tk.Label(app, text="", wraplength=300)
image_path = './PDF_LOGO_1.png'  # Replace with your image path
img = Image.open(image_path)
img = img.resize((250, 250),Image.LANCZOS)  # Resize the image to 100x100 pixels
img = ImageTk.PhotoImage(img)
image_label = tk.Label(app)  # Create a label for the image
image_label.config(image=img)
image_label.image = img

# Place widgets in the window
file_label.pack()
file_entry.pack()
browse_button.pack()
check_button.pack()
retry_button.pack()
image_label.pack()

# check_button.pack(side=tk.LEFT, padx=50)
# retry_button.pack(side=tk.LEFT, padx=2)
# clear_button.pack()

result_label.pack()

# Start the GUI application
app.mainloop()
