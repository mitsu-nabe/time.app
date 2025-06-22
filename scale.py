<<<<<<< HEAD
import tkinter as tk

root = tk.Tk()
root.title('Scale Test')
root.geometry('250x100')

# ウィジェットの生成
var_1 = tk.IntVar()

# Labelウィジェットの生成
label_1 = tk.Label(
    root,
    textvariable=var_1) # ウィジェット変数の設定
label_1.pack(expand=True)

# Scaleウィジェットの生成
scale_1 = tk.Scale(
    root,
    variable=var_1,
    resolution=5,
    orient=tk.HORIZONTAL,
    from_=0,
    to=100)
scale_1.pack(expand=True)

#　初期値を50にする
var_1.set(50)

root.mainloop()
=======
import tkinter as tk

root = tk.Tk()
root.title('Scale Test')
root.geometry('250x100')

# ウィジェットの生成
var_1 = tk.IntVar()

# Labelウィジェットの生成
label_1 = tk.Label(
    root,
    textvariable=var_1) # ウィジェット変数の設定
label_1.pack(expand=True)

# Scaleウィジェットの生成
scale_1 = tk.Scale(
    root,
    variable=var_1,
    resolution=5,
    orient=tk.HORIZONTAL,
    from_=0,
    to=100)
scale_1.pack(expand=True)

#　初期値を50にする
var_1.set(50)

root.mainloop()
>>>>>>> origin/main
