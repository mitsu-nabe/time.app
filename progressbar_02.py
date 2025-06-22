<<<<<<< HEAD
import tkinter as tk
from tkinter import ttk

# トップレベルウィンドウの生成
root = tk.Tk()
root.title('Progressbar Test')
root.geometry('300x300')

# progressbarウィジェットの生成
progressbar_1 = ttk.Progressbar(
    root,
    orient=tk.VERTICAL,
    maximum=10,
    mode='indeterminate')
progressbar_1.pack(expand=True)

progressbar_2 = ttk.Progressbar(
    root,
    orient=tk.HORIZONTAL,
    maximum=10,
    mode='indeterminate')
progressbar_2.pack(expand=True)

# アニメーション開始
progressbar_1.start()
progressbar_2.start()

=======
import tkinter as tk
from tkinter import ttk

# トップレベルウィンドウの生成
root = tk.Tk()
root.title('Progressbar Test')
root.geometry('300x300')

# progressbarウィジェットの生成
progressbar_1 = ttk.Progressbar(
    root,
    orient=tk.VERTICAL,
    maximum=10,
    mode='indeterminate')
progressbar_1.pack(expand=True)

progressbar_2 = ttk.Progressbar(
    root,
    orient=tk.HORIZONTAL,
    maximum=10,
    mode='indeterminate')
progressbar_2.pack(expand=True)

# アニメーション開始
progressbar_1.start()
progressbar_2.start()

>>>>>>> origin/main
root.mainloop()