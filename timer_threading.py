import tkinter as tk
import threading as th

count = 10
timer = None

# ハンドラ関数
def start():
    global count
    count = 10
    button_1['state'] = tk.DISABLED
    countdown()

#　カウントダウンの関数
def countdown():
    global count
    global timer
    label_1['text'] = str(count)
    count = count -1
    timer = th.Timer(1, countdown)
    timer.start()

# アクティブなスレッドのオブジェクトを表示
for thread in th.enumerate():
    print(thread)
print('\n')

if count < 0:
    timer.cancel()
    button_1['start'] = tk.NORMAL

# 以下、おなじみのトップレベルウインドウの生成
root = tk.Tk()
root.title('スレッド')
root.geometry('250x100')

label_1 = tk.Label(
    root,
    text ='10')
label_1.pack(expand=True)

button_1 = tk.Button(
    root,
    text = 'START',
    command=start)
button_1.pack(expand=True)

root.mainloop()

if timer != None : timer.cancel()
 