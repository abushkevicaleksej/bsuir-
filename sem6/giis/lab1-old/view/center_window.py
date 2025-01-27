def center_window(window, w, h):
    ws, hs = window.winfo_screenwidth(), window.winfo_screenheight()  # dimensions of screen
    x, y = (ws / 2) - (w / 2), (hs / 2) - (h / 2)  # calculate center

    window.geometry('%dx%d+%d+%d' % (w, h, x, y))