import tkinter

def window():
    win = tkinter.Tk()
    win.title('Dowloader image')
    win.geometry('400x200')
    tkinter.Label(win,text="Podaj adres URL:",).grid(row = 0)
    #tkinter.Label(win,text="Test pliku1").grid(row = 1)
    e1 = tkinter.Entry(win)
    e1.grid(row = 0,column = 2,sticky=W+E+N+S)

    win.mainloop()
