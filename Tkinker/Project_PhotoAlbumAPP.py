import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class PhotoAlbumAPP:
    def __init__(self, root):
        # Variable
        self.photo_paths = []
        self.current_index = 0
        # window
        self.root = root
        self.root.title("相簿")
        # canvas
        self.canvas = tk.Canvas(root, width=600, height=600)
        self.canvas.pack()
        # button
        self.button_prev = tk.Button(root,
                                     text="上一張",
                                     font="System",
                                     command=self.show_prev_photo)
        self.button_prev.pack(side=tk.LEFT)
        self.button_next = tk.Button(root,
                                     text="下一張",
                                     font="System",
                                     command=self.show_next_photo)
        self.button_next.pack(side=tk.RIGHT)
        self.load_button = tk.Button(root,
                                     text="load_button",
                                     font="System",
                                     anchor="center",
                                     command=self.load_button)
        self.load_button.pack(side=tk.BOTTOM)
        self.load_image_button = tk.Button(root,
                                           text="load_image_button",
                                           font="System",
                                           anchor="center",
                                           command=self.load_image_button)
        # TODO: 讓照片可以新增 / 刪除
        self.load_image_button.pack(side=tk.BOTTOM)
        self.load_fold_button = tk.Button(root,
                                          text="load_fold_button",
                                          font="System",
                                          anchor="center",
                                          command=self.load_fold_button)
        # TODO: 可以選擇資料夾一次新增
        self.load_fold_button.pack(side=tk.BOTTOM)

    def load_button(self):
        self.photo_paths = filedialog.askopenfilenames(title="選擇圖片文件",
                                                       filetypes=[("圖片文件", "*.jpg *.png *.gif *.jpeg")])
        if self.photo_paths:
            self.current_index = 0
            self.show_photo()

    def load_image_button(self):
        for path in filedialog.askopenfilenames(title="選擇圖片文件", filetypes=[("圖片文件", "*.jpg *.png *.gif *.jpeg")]):
            self.photo_paths.append(str(path))
        if self.photo_paths:
            self.current_index = 0
            self.show_photo()

    def load_fold_button(self):
        self.photo_paths = filedialog.askopenfilenames(title="選擇圖片資料夾",
                                                       filetypes=[("圖片文件", "*.jpg *.png *.gif *.jpeg")])
        if self.photo_paths:
            self.current_index = 0
            self.show_photo()

    def show_photo(self):
        if self.photo_paths:
            image_path = self.photo_paths[self.current_index]
            image = Image.open(image_path)
            photo = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            self.canvas.photo = photo

    def show_prev_photo(self):
        if self.photo_paths:
            self.current_index = (self.current_index - 1) % len(self.photo_paths)
            self.show_photo()

    def show_next_photo(self):
        if self.photo_paths:
            self.current_index = (self.current_index + 1) % len(self.photo_paths)
            self.show_photo()


if __name__ == "__main__":
    # 宣告視窗物件
    root = tk.Tk()
    # 宣告視窗物件變數
    ## 視窗大小
    window_width = 600
    window_height = 600
    ## 視窗位置
    window_position_x = int((root.winfo_screenwidth() - window_width) / 2)
    window_position_y = 10
    # 宣告視窗物件參數
    root.geometry(f"+{window_position_x}+{window_position_y}")
    root.resizable(False, False)
    app = PhotoAlbumAPP(root)
    root.mainloop()
    print(app.photo_paths)
