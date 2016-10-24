import tkinter as tk

def Call():
        lab= tk.Label(root, text = 'You pressed\nthe button')
        lab.pack()
        button['bg'] = 'blue'
        button['fg'] = 'white'

root = tk.Tk()

root.geometry('100x110+350+70')
button = tk.Button(root, text = 'Press me', command = Call)
button.pack()

root.mainloop()


root.mainloop()