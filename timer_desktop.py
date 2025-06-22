import tkinter as tk
import time

# ハンドラ関数
def start():
    countdown()

# カウントダウンの関数
def countdown():
    count = 10

    while True:
        label_1['text']=str(count)
        print(count)
        count = count -1
        label_1.update()
        time.sleep(1)
        if count < 0: break

# トップレベルウィンドウの生成
root = tk.Tk()
root.title('GUIが固まるアプリ')
root.geometry('300x100')

# Labelウィジェットの生成
label_1 = tk.Label(
    root,
    text = '10')
label_1.pack(expand=True)

# Buttonウィジェットの生成
button_1 = tk.Button(
    root,
    text='START',
    command=start)
button_1.pack(expand=True)

root.mainloop()