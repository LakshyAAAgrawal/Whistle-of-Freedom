import pickle
a=[]
def f_save():
    final_list=[]
    for i in a:
        xx=i.get()
        xx=xx.lower()
        """
        if xx.lower()=="enter" or xx.lower=="return":
            xx="Return"
        if xx.l=="win" or xx.lower=="meta":
            xx="Super_L"
        """
        xx = xx.replace("enter", "Return")
        xx = xx.replace("return", "Return")
        xx = xx.replace("tab", "Tab")
        xx = xx.replace("win", "Super_L")
        xx = xx.replace("meta", "Super_L")
        xx = xx.replace("shift", "Shift_L")
        xx = xx.replace("control", "ctrl")
        #xx = xx.replace("return", "Return")
        final_list.append(xx)
    with open('listfile.data', 'wb') as filehandle:
    # store the data as binary data stream
        pickle.dump(final_list, filehandle)


from tkinter import *
window=Tk()
window.title("Whistle of Freedom")
window.configure(background="black")
Label(window, text="Freq 1 :", bg="black", fg="white").grid(row=2,column=0, sticky=N)
Label(window, text="Freq 2 :", bg="black", fg="white").grid(row=3,column=0, sticky=N)
Label(window, text="Freq 3 :", bg="black", fg="white").grid(row=4,column=0, sticky=N)
Label(window, text="Freq 4 :", bg="black", fg="white").grid(row=5,column=0, sticky=N)
Label(window, text="Freq 5 :", bg="black", fg="white").grid(row=6,column=0, sticky=N)
Label(window, text="Freq 6 :", bg="black", fg="white").grid(row=7,column=0, sticky=N)
Label(window, text="Freq 7 :", bg="black", fg="white").grid(row=8,column=0, sticky=N)
Label(window, text="Freq 8 :", bg="black", fg="white").grid(row=9,column=0, sticky=N)
#a=[Entry(window, width=10, bg="white").grid(row=2,column=1, sticky=N), Entry(window, width=10, bg="white").grid(row=3,column=1, sticky=N), Entry(window, width=10, bg="white").grid(row=4,column=1, sticky=N), Entry(window, width=10, bg="white").grid(row=5,column=1, sticky=N), Entry(window, width=10, bg="white").grid(row=6,column=1, sticky=N), Entry(window, width=10, bg="white").grid(row=7,column=1, sticky=N), Entry(window, width=10, bg="white").grid(row=8,column=1, sticky=N), Entry(window,
for i in range(8):
    z=Entry(window, width=10, bg="white")
    z.grid(row=i+2,column=1, sticky=N)
    a.append(z)
#width=10, bg="white").grid(row=9,column=1, sticky=N)]
Button(window, text="Save", width=15, command=f_save).grid(row=10, column=0, sticky=S)
window.mainloop()
