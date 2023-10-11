import tkinter as tk

# 建立視窗物件
root = tk.Tk()
# 設定視窗標題
root.title("first page")
# 設定icon（格式限定.ico）
#windowDisplay.iconbitmap('database.ico')
# 設定視窗大小
window_width = 800
window_height = 600
# 取得視窗大小
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# 設定視窗起始位置
window_position_x = int((screen_width - window_width)/2)
window_position_y = int((screen_height - window_height)/2)
root.geometry(f"{window_width}x{window_height}+{window_position_x}+{window_position_y}")
# 設定視窗的是否可以縮放
root.resizable(True, True)
# 設定視窗可調整的最小值
root.minsize(700, 500)
# 設定視窗可調整的最大值
root.maxsize(900, 700)
# 設定視窗的顏色
# i6進制
root.configure(background='#F8F8FF')

# 放在主迴圈中
root.mainloop()
