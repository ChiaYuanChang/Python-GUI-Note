import tkinter as tk

# window設定
window_width = 800
window_height = 600
root = tk.Tk()
root.title("first button")
root.geometry(f"{window_width}x{window_height}")
# 宣告button物件
## tkinter.Button([視窗物件], text=[label上的文字: str], font=([字型: str], [字型大小: int]))
button1 = tk.Button(root,
                    text="A Button",
                    font=("System", 24))
# 設定button在視窗上的位置
button1.place(x=400, y=300)
root.mainloop()
