import tkinter as tk
from tkinter import messagebox
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression

# Load dataset and train model
housing = fetch_california_housing()
X = housing.data
y = housing.target
features = housing.feature_names

model = LinearRegression()
model.fit(X, y)

# Predict function
def predict_price():
    try:
        input_data = [float(entry.get()) for entry in entries]
        input_array = np.array(input_data).reshape(1, -1)
        predicted = model.predict(input_array)[0]
        messagebox.showinfo("Prediction", f"Predicted House Price: ${round(predicted * 100000, 2)}")
    except:
        messagebox.showerror("Error", "Please fill all fields with valid numbers.")

# Autofill sample data
def autofill_sample():
    sample_values = [8.3252, 41.0, 6.9841, 1.0238, 322.0, 2.5556, 37.88, -122.23]
    for i in range(len(entries)):
        entries[i].delete(0, tk.END)
        entries[i].insert(0, str(sample_values[i]))

# Main window
root = tk.Tk()
root.title("🏡 California House Price Predictor")
root.geometry("500x720")
root.configure(bg="#f4f4f4")

tk.Label(root, text="🏠 California House Price Predictor", font=("Helvetica", 18, "bold"), fg="#333", bg="#f4f4f4").pack(pady=20)
tk.Label(root, text="Enter House Details Below", font=("Helvetica", 12), bg="#f4f4f4").pack(pady=5)

entries = []
for feature in features:
    frame = tk.Frame(root, bg="#f4f4f4")
    frame.pack(pady=5)
    label = tk.Label(frame, text=feature, font=("Helvetica", 10), width=20, anchor='w', bg="#f4f4f4")
    label.pack(side=tk.LEFT, padx=10)
    entry = tk.Entry(frame, width=30, font=("Helvetica", 10))
    entry.pack(side=tk.RIGHT, padx=10)
    entries.append(entry)

# Buttons
btn_frame = tk.Frame(root, bg="#f4f4f4")
btn_frame.pack(pady=30)

predict_btn = tk.Button(btn_frame, text="Predict Price", command=predict_price, bg="#007acc", fg="white",
                        font=("Helvetica", 12), padx=15, pady=5)
predict_btn.grid(row=0, column=0, padx=10)

sample_btn = tk.Button(btn_frame, text="Autofill Sample", command=autofill_sample, bg="#4CAF50", fg="white",
                       font=("Helvetica", 12), padx=15, pady=5)
sample_btn.grid(row=0, column=1, padx=10)

root.mainloop()