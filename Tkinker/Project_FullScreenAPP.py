import tkinter as tk


class FullScreenApp:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-fullscreen', True)
        self.root.bind('<Escape>', self.quit)
        self.root.overrideredirect(True)  # 隐藏窗口管理按钮
        self.close_button = tk.Button(self.root, text="关闭", command=self.quit)
        self.close_button.pack(expand=True, fill=tk.BOTH)

    def quit(self, event=None):
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = FullScreenApp(root)
    root.mainloop()