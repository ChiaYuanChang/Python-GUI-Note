import tkinter as tk

root = tk.Tk()
root.title("first page")
window_width = 800
window_height = 600
root.geometry(f"{window_width}x{window_height}")
# label 設定
## tkinter.Label([視窗物件], text=[label上的文字: str], font=([字型: str], [字型大小: int]))
label1 = tk.Label(root,
                  text="A Label",
                  font=("System", 24))
# 不宣告變數直接使用也行
# 在pack裡面也可以設定變數
tk.Label(root, text="Second Label").pack(side="right",
                                         padx=50,
                                         pady=50,
                                         anchor="nw")
# 設定label在視窗上的位置
label1.place(x=0, y=0)
# 顯示視窗
root.mainloop()