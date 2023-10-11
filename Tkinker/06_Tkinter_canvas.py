import tkinter as tk

window_width = 800
window_height = 600
root = tk.Tk()
root.geometry(f"{window_width}x{window_height}")
root.title("first canvas")
# 宣吿canvas物件
## tkinter.Canvas([視窗元件], width=[寬度: int], height=[高度: int])
canvas1 = tk.Canvas(root,
                    width=800,
                    height=600,
                    bg="green")
# pack() 和 place()都可以
canvas1.pack()
root.mainloop()
