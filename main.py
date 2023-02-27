import customtkinter as ctk

class PycturePerfect(ctk.CTk):
    def __init__(self):
        super().__init__()

        WIN_MIN_WIDTH, WIN_MIN_HEIGHT = 640, 480
        SCREEN_WIDTH, SCREEN_HEIGHT = self.winfo_screenwidth(), self.winfo_screenheight()
        WIN_XCOORD, WIN_YCOORD = (SCREEN_WIDTH // 2) - (WIN_MIN_WIDTH // 2), (SCREEN_HEIGHT // 2) - (WIN_MIN_HEIGHT // 2)

        self.title("PycturePerfect")
        self.after(201, lambda: self.iconbitmap("images/icon.ico"))
        self.geometry(f"{WIN_MIN_WIDTH}x{WIN_MIN_HEIGHT}+{WIN_XCOORD}+{WIN_YCOORD}")
        self.minsize(WIN_MIN_WIDTH, WIN_MIN_HEIGHT)

        self.mainloop()

if __name__ == "__main__":
    PycturePerfect()