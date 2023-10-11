import tkinter

window_width = 800
window_height = 600
root = tkinter.Tk()
root.title("button click")
root.geometry(f"{window_width}x{window_height}")


# 設定button1動作
def click_btn1():
    button1["text"] = "clicked"


button1 = tkinter.Button(root,
                         text="click it",
                         font=("System", 24),
                         command=click_btn1)
button1.place(x=400, y=300)
root.mainloop()