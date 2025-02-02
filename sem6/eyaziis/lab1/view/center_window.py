def center_window(window, w, h):
    ws, hs = window.winfo_screenwidth(), window.winfo_screenheight()
    x, y = (ws / 2) - (w / 2), (hs / 2) - (h / 2)

    window.geometry('%dx%d+%d+%d' % (w, h, x, y))