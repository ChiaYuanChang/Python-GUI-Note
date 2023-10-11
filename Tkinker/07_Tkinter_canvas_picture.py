import tkinter as tk

window_width = 910
window_height = 910
root = tk.Tk()
root.geometry(f"{window_width}x{window_height}")
canvas1_width = 910
canvas1_height = 910
canvas1 = tk.Canvas(root,
                    width=canvas1_height,
                    height=canvas1_height)
canvas1.pack()
# 將圖檔宣告成物件（first_image）
# tkinter只支援GIF
first_image = tk.PhotoImage(file="1.png")
# 在canvas裡繪製圖片物件（first_image）
canvas1.create_image(453.5, 453.5,
                     image=first_image)
## canvas1.create_image([圖像在Canvas的X座標位置: num], [圖像在Canvas的Y座標位置: num],image=[物件名稱])
### (如果沒有設定anchor則是中心點座標，如果有設定anchor則是設置的端點座標 )
root.mainloop()
