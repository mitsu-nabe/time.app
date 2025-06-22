import tkinter as tk

count = 10

# ハンドラ関数_イベントに対して反応するための関数
def start():
    global count
    count = 10
    button_1['state']=tk.DISABLED
    countdown()

# カウントダウンの関数
def countdown():
    global count
    label_1['text'] = str(count)
    count = count - 1
    if count < 0:
        button_1['state'] = tk.NORMAL
    else:
        root.after(1000, countdown)
    
# トップレベルウインドウの生成
root = tk.Tk()
root.title('after関数')
root.geometry('250x100')

# Labelウィジェットの生成
label_1 = tk.Label(
    root,
    text ='10')
label_1.pack(expand=True)

# Buttonウィジェットの生成
button_1 = tk.Button(
    root,
    text='START',
    command=start)
button_1.pack(expand=True)

root.mainloop()