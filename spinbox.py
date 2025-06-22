import tkinter as tk

# トップレベルウインドウの生成
root = tk.Tk()
root.title('spinbox Test')
root.geometry('250x100')

# ウィジェット変数の生成
var_spin_1 =tk.IntVar(value=0)

# Labelウィジェットの生成
label_1 = tk.Label(
    root,
    # ウィジェット変数を設定
    textvariable=var_spin_1)
label_1.pack(expand=True)

# Spinboxウィジェットの生成
spinbox_1 = tk.Spinbox(
    root,
    width=3,    # 最小値
    from_=0,    # 最大値
    to=100,     # 増減幅
    increment=5,
    # ウィジェット変数を設定
    textvariable=var_spin_1)
spinbox_1.pack(expand=True)

# 初期値を設定
var_spin_1.set(50)

root.mainloop()