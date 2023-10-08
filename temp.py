import tkinter as tk
from tkinter import ttk
import csv

def submit_form():
    # Retrieve data from the form fields
    name = name_entry.get()
    email = email_entry.get()
    feedback = feedback_entry.get("1.0", "end")

    # Open the CSV file in append mode (create it if it doesn't exist)
    with open("feedback.csv", mode="a", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write the form data to the CSV file
        csv_writer.writerow([name, email, feedback])

    # Clear the form fields
    name_entry.delete(0, "end")
    email_entry.delete(0, "end")
    feedback_entry.delete("1.0", "end")

# Create a Tkinter window
window = tk.Tk()
window.title("Feedback Form")

# Change the background color to a mix of light blue and blue
window.configure(bg='#66a3ff')

# Create a frame for better organization
frame = ttk.Frame(window, padding=10)
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create a LabelFrame to group the input fields and change the title color to blue
input_frame = ttk.LabelFrame(frame, text="User Information", padding=(10, 5))
input_frame.grid(column=0, row=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)

# Set the style for the LabelFrame title (change title color to blue)
style = ttk.Style()
style.configure("TLabel", foreground="blue")  # Change title color to blue

# Create form fields and labels
label_font = ('Young Serif', 12)
entry_font = ('Young Serif', 11)

name_label = ttk.Label(input_frame, text="Name:", font=label_font)
name_label.grid(column=0, row=0, sticky=tk.W)
name_entry = ttk.Entry(input_frame, font=entry_font)
name_entry.grid(column=1, row=0, padx=5, ipady=5, sticky=tk.W)

email_label = ttk.Label(input_frame, text="Email:", font=label_font)
email_label.grid(column=0, row=1, sticky=tk.W)
email_entry = ttk.Entry(input_frame, font=entry_font)
email_entry.grid(column=1, row=1, padx=5, pady=5, sticky=tk.W)

feedback_label = ttk.Label(input_frame, text="Your Idea:", font=label_font)
feedback_label.grid(column=0, row=2, sticky=tk.W)
feedback_entry = tk.Text(input_frame, height=5, width=30, font=entry_font)
feedback_entry.grid(column=1, row=2, padx=5, pady=5, sticky=tk.W)

# Submit button
submit_button = ttk.Button(frame, text="Submit", command=submit_form)
submit_button.grid(column=1, row=1, sticky=tk.E)

# Add some padding for a cleaner look
for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Start the Tkinter main loop
window.mainloop()
