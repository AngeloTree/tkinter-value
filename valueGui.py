from cgitb import text
from pyparsing import col
import tkinter as tk
import valueDb

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Value Entry")
    
        # Event Functions
    def decrease():
        print("Decrease button pressed.")
        text = lbl_value["text"]
        text_value = int(text) - 1
        lbl_value["text"] = str(text_value)
        valueDb.update_number(text_value)

    def increase():
        print("Increase button pressed.")
        text = lbl_value["text"]
        text_value = int(text) + 1
        lbl_value["text"] = str(text_value)
        valueDb.update_number(text_value)


    window.rowconfigure(0, minsize=50, weight=1)
    window.columnconfigure([0, 1, 2], minsize=50, weight=1)

    btn_decrease = tk.Button(master=window, text="-", command=decrease)
    btn_decrease.grid(row=0, column=0, sticky="nsew")

    lbl_value = tk.Label(master=window, text="0")
    lbl_value.grid(row=0, column=1)

    btn_increase = tk.Button(master=window, text="+", command=increase)
    btn_increase.grid(row=0, column=2, sticky="nsew")
    
    btn_clear = tk.Button(master=window, text="Clear")
    btn_clear.grid(row=1, column=1, sticky="new")


    current_number = valueDb.get_number()
    lbl_value["text"] = str(current_number)

    window.mainloop()
