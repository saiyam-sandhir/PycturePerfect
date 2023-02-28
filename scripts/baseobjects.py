import customtkinter as ctk
import tkinter as tk
import tktooltip
import PIL

class Frame(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk):
        super().__init__(
            master,
            fg_color="gray14",
            corner_radius=0
            )

class ToolTip(tktooltip.ToolTip):
    def __init__(self, master: tk.Widget, msg: str):
        super().__init__(
            master,
            msg=msg,
            delay=0.75,
            bg="gray45",
            fg="white"
        )

class Button(ctk.CTkButton):
    def __init__(self, master: ctk.CTkFrame, image_path: str, msg: str, command=lambda: []):
        button_img = ctk.CTkImage(
            light_image=PIL.Image.open(image_path),
            dark_image=PIL.Image.open(image_path),
            size=(20, 20)
        )

        super().__init__(
            master,
            text="",
            image=button_img,
            width=35,
            height=35,
            command=command
        )

        ToolTip(
            self,
            msg=msg,
        )

class Label(ctk.CTkLabel):
    def __init__(self, master: ctk.CTkFrame, text: str):
        super().__init__(
            master,
            text=text,
            width=35,
            height=35,
        )