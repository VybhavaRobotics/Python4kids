import tkinter
tk = tkinter.Tk()

canvas = tkinter.Canvas(tk, width=500, height=500)
canvas.create_line(0, 0, 500, 500)
canvas.pack()
print('hello')
