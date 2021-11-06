import tkinter as tk
from tkinter import ttk

try:
    with open('settings.txt', "r") as f:
        vals = f.readlines()
        balance_value = int(vals[0])
        risk_per_value = int(vals[1])
except:
    pass
FONT = ('Helvetica', 16)

root = tk.Tk()
root.title("Lot Size Calculator")
root.config(bg="orange")

main_frame = tk.Frame(root)
main_frame.pack(padx=5, pady=5)

balance_lab = tk.Label(main_frame, text="Balance", font=FONT).grid(row=0, column=0, padx=40, pady=5)
risk_per_lab = tk.Label(main_frame, text="Risk %", font=FONT).grid(row=0, column=1, padx=40, pady=5)

def find_lotsize(name, index, mode):
    global lotsize
    try:
        balance = float(balance_var.get())
        risk = float(risk_per_var.get())
        sl = float(sl_price_var.get())
        ATR = float(ATR_val_var.get())
        lotsize = (balance * (risk / 100)) / (sl * ATR)
        lot_size_var.set(f"Lot Size: {lotsize:.2f}")
        try:
            margin()
        except ValueError:
            pass

    except ValueError:
        lotsize = None
        lot_size_var.set(f"Lot Size:")

balance_var = tk.StringVar(value=balance_value)
balance_var.trace_add("write", find_lotsize)
balance_entry = ttk.Entry(main_frame, textvariable=balance_var)
balance_entry.grid(row=1, column=0, padx=20, pady=5)


risk_per_var = tk.StringVar(value=risk_per_value)
risk_per_var.trace_add("write", find_lotsize)
risk_per_entry = ttk.Entry(main_frame, textvariable=risk_per_var)
risk_per_entry.grid(row=1, column=1, padx=20, pady=5)

Sl_price_lab = tk.Label(main_frame, text="SL Price", font=FONT).grid(row=2, column=0, padx=40, pady=5)

sl_price_var = tk.StringVar()
sl_price_var.trace_add("write", find_lotsize)
sl_price_entry = ttk.Entry(main_frame, textvariable=sl_price_var)
sl_price_entry.grid(row=3, column=0, padx=20, pady=5)

ATR_val_lab = tk.Label(main_frame, text="ATR", font=FONT).grid(row=2, column=1, padx=40, pady=5)

ATR_val_var = tk.StringVar(value=1)
ATR_val_var.trace_add("write", find_lotsize)
ATR_val_entry = ttk.Entry(main_frame, textvariable=ATR_val_var)
ATR_val_entry.grid(row=3, column=1, padx=20, pady=5)

lot_size_var = tk.StringVar(value="Lot Size:")
lot_size_lab = tk.Label(main_frame, textvariable=lot_size_var, font=('Helvetica', 25)).grid(row=4, column=0, columnspan=2, padx=40, pady=5)

sub_frame = tk.Frame(root)
sub_frame.pack(padx=5, pady=5)

def margin():
    exposure = float(exposure_var.get())
    price = float(price_var.get())
    margin = (price * lotsize) / exposure
    margin_var.set(f"Margin: {margin:.2f}")

def find_margin(name, index, mode) :
    try:
       margin() 
    except ValueError:
        margin_var.set(f"Margin: ")


exposure_lab = tk.Label(sub_frame, text="Exposure", font=FONT).grid(row=0, column=0, padx=40, pady=5)
exposure_var = tk.StringVar()
exposure_var.trace_add("write", find_margin)
exposure_entry = ttk.Entry(sub_frame, textvariable=exposure_var)
exposure_entry.grid(row=1, column=0, padx=20, pady=5)

price_lab = tk.Label(sub_frame, text="Price", font=FONT).grid(row=0, column=1, padx=40, pady=5)
price_var = tk.StringVar()
price_var.trace_add("write", find_margin)
price_entry = ttk.Entry(sub_frame, textvariable=price_var)
price_entry.grid(row=1, column=1, padx=20, pady=5)

margin_var = tk.StringVar(value="Margin:")
margin_lab = tk.Label(sub_frame, textvariable=margin_var, font=('Helvetica', 25)).grid(row=4, column=0, columnspan=2, padx=40, pady=5)

root.mainloop()


with open('settings.txt', 'w') as f:
    f.write(f"{balance_var.get()}\n")
    f.write(risk_per_var.get())
