import customtkinter as ctk
from PIL import Image
import tkinter as tk
import time

import baseobjects

class ImageLoader(ctk.CTkFrame):
    def __init__(self, master: baseobjects.Frame):
        super().__init__(master)

        # File Button to import image from the system
        file_button = baseobjects.Button(
            self, 
            image_path="images/viewer-frame/open-file.png"
        )
        file_button.pack(
            side=ctk.LEFT,
            padx=(5, 0),
            pady=5
        )

        # Link Button to import image from web
        link_button = baseobjects.Button(
            self, 
            image_path="images/viewer-frame/link.png"
        )
        link_button.pack(
            side=ctk.LEFT,
            padx=(0, 5),
            pady=5
        )

class Toolbar(ctk.CTkFrame):
    def __init__(self, master: baseobjects.Frame):
        super().__init__(master)

        # Edit button that leads to image editor frame
        edit_button = baseobjects.Button(
            self, 
            image_path="images/viewer-frame/edit.png"
        )
        edit_button.pack(
            side=ctk.LEFT,
            padx=(5, 0),
            pady=5
        )

        # Rotate button to rotate the image clock-wise
        rotate_button = baseobjects.Button(
            self, 
            image_path="images/viewer-frame/rotate.png"
        )
        rotate_button.pack(
            side=ctk.LEFT,
            pady=5
        )

        # Delete button to delete the image if in the system
        delete_button = baseobjects.Button(
            self, 
            image_path="images/viewer-frame/delete.png"
        )
        delete_button.pack(
            side=ctk.LEFT,
            pady=5
        )

        # Info button to get information about the image
        info_button = baseobjects.Button(
            self, 
            image_path="images/viewer-frame/info.png"
        )
        info_button.pack(
            side=ctk.LEFT,
            pady=5
        )

        # Share button for user to share image
        share_button = baseobjects.Button(
            self, 
            image_path="images/viewer-frame/share.png"
        )
        share_button.pack(
            side=ctk.LEFT,
            padx=(0, 5),
            pady=5
        )

class MoreButton(baseobjects.Button):
    def __init__(self, master: baseobjects.Frame):
        super().__init__(
            master,
            image_path="images/viewer-frame/more.png"
        )

class ZoomControler(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        ZOOM_MAGNITUDE = 0.5

        self.clicked_once = False
        self.zoom_value = 100

        # Zoom value label
        self.zoom_label = baseobjects.Label(
            self,
            text=f"{int(self.zoom_value)}%",
        )
        self.zoom_label.pack(
            side=ctk.RIGHT,
            padx=(5, 10),
            pady=5
        )

        # Zoom out button
        zoomout_button = baseobjects.Button(
            self, 
            image_path="images/viewer-frame/zoom-out.png",
            command=lambda: self.zoom_on_click(-ZOOM_MAGNITUDE)
        )
        zoomout_button.bind("<ButtonPress-1>", lambda event: self.start_zoom_on_hold(-ZOOM_MAGNITUDE * 1.5))
        zoomout_button.bind("<ButtonRelease-1>", lambda event: self.stop_zoom_on_hold())
        zoomout_button.pack(
            side=ctk.RIGHT,
            pady=5
        )

        # Zoom in button
        zoomin_button = baseobjects.Button(
            self, 
            image_path="images/viewer-frame/zoom-in.png",
            command=lambda: self.zoom_on_click(ZOOM_MAGNITUDE)
        )
        zoomin_button.bind("<ButtonPress-1>", lambda event: self.start_zoom_on_hold(ZOOM_MAGNITUDE * 1.5))
        zoomin_button.bind("<ButtonRelease-1>", lambda event: self.stop_zoom_on_hold())
        zoomin_button.pack(
            side=ctk.RIGHT,
            padx=(5, 0),
            pady=5
        )

    def zoom_on_click(self, value):
        if (value < 0 and self.zoom_value > 100) or (value > 0 and self.zoom_value < 200):
            self.zoom_value += value
        
        self.zoom_label.configure(text=f"{int(self.zoom_value)}%")

        if not self.clicked_once:
            time.sleep(0.08)
            self.clicked_once = True

    def start_zoom_on_hold(self, value):
        if self.clicked_once:
            self.zoom_on_click(value)
            self.hold_id = self.after(50, lambda: self.start_zoom_on_hold(value))

    def stop_zoom_on_hold(self):
        self.after_cancel(self.hold_id)
        self.clicked_once = False

class ViewController(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Fullscreen button
        fullscreen_button = baseobjects.Button(
            self, 
            image_path="images/viewer-frame/fullscreen.png"
        )
        fullscreen_button.pack(
            side=ctk.LEFT,
            padx=(5, 0),
            pady=5
        )

        # Fitscreen button
        fitscreen_button = baseobjects.Button(
            self,
            image_path="images/viewer-frame/fitscreen.png"
        )
        fitscreen_button.pack(
            side=ctk.LEFT,
            padx=(0, 5),
            pady=5
        )

class Frame(baseobjects.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Placing the above created widgets in the image viewer frame
        ImageLoader(master).place(relx=0.0, rely=0.0, anchor=ctk.NW)
        Toolbar(master).pack(side=ctk.TOP)
        MoreButton(master).place(relx=1.0, rely=0.0, anchor=ctk.NE)
        ctk.CTkCanvas(master, bg="gray14", highlightthickness=False).place(relx=0.5, rely=0.5, relwidth=1.0, relheight=0.76, anchor=ctk.CENTER)
        ZoomControler(master).place(relx=1.0, rely=1.0, anchor=ctk.SE)
        ViewController(master).place(relx=0.0, rely=1.0, anchor=ctk.SW)