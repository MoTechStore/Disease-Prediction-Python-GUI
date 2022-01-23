import os
Image_path=os.environ['TEMP']+r"\comodo_logo_desktop_wallpaper_by_thanhtai2009-d8h3odf.PGM"  # Enter the path of image file.
###### Image_Path only supports GIF or PGM/PPM images.#####


try:
    # for Python2
    import Tkinter as tk
except ImportError:
    # for Python3
    import tkinter as tk

root = tk.Tk()
root.title('background image')




C = Canvas(top, bg="blue", height=250, width=300)
filename = PhotoImage(file = "m.png")
background_label = Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.mainloop()