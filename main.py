import customtkinter as ctk
import sys
import PIL
import os

scripts = os.path.abspath(os.path.join(os.path.dirname(__file__), "scripts"))
sys.path.append(scripts)

from frames import viewer

ctk.set_default_color_theme("color-theme.json")

class PycturePerfect(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.config(padx=10, pady=10)

        WIN_MIN_WIDTH, WIN_MIN_HEIGHT = 640, 480
        SCREEN_WIDTH, SCREEN_HEIGHT = self.winfo_screenwidth(), self.winfo_screenheight()
        WIN_XCOORD, WIN_YCOORD = (SCREEN_WIDTH // 2) - (WIN_MIN_WIDTH // 2), (SCREEN_HEIGHT // 2) - (WIN_MIN_HEIGHT // 2)

        self.title("PycturePerfect")
        self.after(201, lambda: self.iconbitmap("images/icon.ico"))
        self.geometry(f"{WIN_MIN_WIDTH}x{WIN_MIN_HEIGHT}+{WIN_XCOORD}+{WIN_YCOORD}")
        self.minsize(WIN_MIN_WIDTH, WIN_MIN_HEIGHT)

        viewer.Frame(self).pack(side=ctk.LEFT, fill=ctk.X, expand=True)

        self.mainloop()

if __name__ == "__main__":
    PycturePerfect()