import encrypt as cipher
import decrypt as decipher   

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

import gui_support

def vp_start_gui():
    global val, w, root
    root = tk.Tk()
    top = Toplevel1(root)
    gui_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    global w, w_win, rt
    rt = root
    w = tk.Toplevel(root)
    top = Toplevel1(w)
    gui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        _bgcolor = '#1e1e1e'
        _fgcolor = '#ffffff'
        _compcolor = '#333333'
        _buttoncolor = '#007bff'
        _highlightcolor = '#ffcc00'

        top.geometry("902x600+385+154")
        top.minsize(148, 1)
        top.maxsize(1924, 1030)
        top.resizable(1, 1)
        top.title("DotDash")
        top.configure(background="#1e1e1e")

        self.text1 = tk.Entry(top)
        self.text1.place(relx=0.089, rely=0.333, height=174, relwidth=0.304)
        self.text1.configure(background="white", font=("Arial", 12), foreground="#333333", insertbackground="black", bd=0, relief="solid")
        
        self.text1_1 = tk.Message(top)
        self.text1_1.place(relx=0.621, rely=0.333, height=174, relwidth=0.304)
        self.text1_1.configure(background="white", font=("Arial", 12), foreground="#333333", bd=0, relief="solid")
        self.text1_1.configure(width=100)

        def call():
            plain_text = self.text1.get().upper()
            ans = cipher.encryptor(plain_text)
            self.text1_1.configure(text=ans)

        def get():
            encrypted_text = self.text1.get()
            x = decipher.decryptor(encrypted_text)
            self.text1_1.configure(text=x)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.443, rely=0.383, height=40, width=150)
        self.Button1.configure(activebackground="#ececec", activeforeground="#000000", background=_buttoncolor, foreground="#ffffff", font=("Arial", 12, "bold"), relief="solid", bd=0, highlightbackground=_highlightcolor, highlightcolor="#000000", pady=10)
        self.Button1.configure(text='Encrypt', command=call)

        self.Button1_2 = tk.Button(top)
        self.Button1_2.place(relx=0.443, rely=0.5, height=40, width=150)
        self.Button1_2.configure(activebackground="#ececec", activeforeground="#000000", background=_buttoncolor, foreground="#ffffff", font=("Arial", 12, "bold"), relief="solid", bd=0, highlightbackground=_highlightcolor, highlightcolor="#000000", pady=10)
        self.Button1_2.configure(text='Decrypt', command=get)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.356, rely=0.067, height=50, width=242)
        self.Label1.configure(background="#1e1e1e", foreground=_highlightcolor, text='DotDash', font=("Arial", 36, "bold"))

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.1, rely=0.283, height=30, width=252)
        self.Label2.configure(background="#1e1e1e", foreground=_fgcolor, text='USER INPUT', font=("Arial", 16, "bold"))

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.632, rely=0.283, height=30, width=252)
        self.Label3.configure(background="#1e1e1e", foreground=_fgcolor, text='OUTPUT', font=("Arial", 16, "bold"))

        self.menubar = tk.Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)

if __name__ == '__main__':
    vp_start_gui()