from tkinter import *                       #tinker = untuk gui (graphical user interface)

root=Tk()
root.title("Calculator")
root.geometry("570x600+100+200")
root.resizable(False,False)                 # membuat layar tidak bisa di ubah ukurannya
root.configure(bg="#878787")              # mengatur warna belakang jendela utama

DEFAULT_FONT = ("arial",30,"bold")
LIGHT_BLUE = "#CCEDFF"
WHITE = "#FAFAFA"
DEEP_BLUE = "#25265E"

equation = ""                               # membuat variabel untuk menyimpan persamaan aritmatika

def show(value):                            # function/fungsi untuk menampilkan nilai atau value pada label
    global equation
    equation+=value
    label_result.config(text=equation)
    
def delete_one():
    global equation
    equation = equation[:-1]
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    result =""
    if equation !="":
        try:
            result=eval(equation)
        except:
                result ="error"
                equation = ""
    label_result.config(text=result)

label_result= Label(root,width=25, height=2, text="",font=("arial",30)) # layar kalkulator
label_result.pack()                                                     # menampilkan widget label/angka dalam jendela aplikasi

Button(root,text="C", width=5, height=1, font=DEFAULT_FONT, bd=1, fg=DEEP_BLUE, bg=LIGHT_BLUE,command=lambda: clear()).place(x=10,y=100)
Button(root,text="/", width=5, height=1, font=DEFAULT_FONT, bd=1, fg=DEEP_BLUE, bg=LIGHT_BLUE,command=lambda: show("/")).place(x=290,y=100)
Button(root,text="x", width=5, height=1, font=DEFAULT_FONT, bd=1, fg=DEEP_BLUE, bg=LIGHT_BLUE,command=lambda: show("*")).place(x=430,y=100)
Button(root,text="\u232b", width=5, height=1, font=DEFAULT_FONT, bd=1, fg=DEEP_BLUE, bg=LIGHT_BLUE,command=lambda: delete_one()).place(x=150,y=100)

Button(root,text="7", width=5, height=1, font=DEFAULT_FONT, bd=1, fg=DEEP_BLUE, bg=WHITE,command=lambda: show("7")).place(x=10,y=200)
Button(root,text="8", width=5, height=1, font=DEFAULT_FONT, bd=1, fg=DEEP_BLUE, bg=WHITE,command=lambda: show("8")).place(x=150,y=200)
Button(root,text="9", width=5, height=1, font=DEFAULT_FONT, bd=1, fg=DEEP_BLUE, bg=WHITE,command=lambda: show("9")).place(x=290,y=200)
Button(root,text="-", width=5, height=1, font=DEFAULT_FONT, bd=1, fg=DEEP_BLUE, bg=LIGHT_BLUE,command=lambda: show("-")).place(x=430,y=200)

Button(root,text="4", width=5, height=1, font=DEFAULT_FONT, bd=1, fg=DEEP_BLUE, bg=WHITE,command=lambda: show("4")).place(x=10,y=300)
Button(root,text="5", width=5, height=1, font=DEFAULT_FONT, bd=1, fg=DEEP_BLUE, bg=WHITE,command=lambda: show("5")).place(x=150,y=300)
Button(root,text="6", width=5, height=1, font=DEFAULT_FONT, bd=1, fg=DEEP_BLUE, bg=WHITE,command=lambda: show("6")).place(x=290,y=300)
Button(root,text="+", width=5, height=1, font=DEFAULT_FONT, bd=1, fg=DEEP_BLUE, bg=LIGHT_BLUE,command=lambda: show("+")).place(x=430,y=300)

Button(root,text="1", width=5, height=1, font=DEFAULT_FONT, bd=1, fg=DEEP_BLUE, bg=WHITE,command=lambda: show("1")).place(x=10,y=400)
Button(root,text="2", width=5, height=1, font=DEFAULT_FONT, bd=1, fg=DEEP_BLUE, bg=WHITE,command=lambda: show("2")).place(x=150,y=400)
Button(root,text="3", width=5, height=1, font=DEFAULT_FONT, bd=1, fg=DEEP_BLUE, bg=WHITE,command=lambda: show("3")).place(x=290,y=400)
Button(root,text="0", width=11, height=1, font=DEFAULT_FONT, bd=1, fg=DEEP_BLUE, bg=WHITE,command=lambda: show("0")).place(x=10,y=500)

Button(root,text=".", width=5, height=1, font=DEFAULT_FONT, bd=1, fg=DEEP_BLUE, bg=WHITE,command=lambda: show(".")).place(x=290,y=500)
Button(root,text="=", width=5, height=3, font=DEFAULT_FONT, bd=1, fg=DEEP_BLUE, bg=LIGHT_BLUE,command=lambda: calculate()).place(x=430,y=400)
# comand=lamda : digunakan untuk menentukan aksi yang akan di jalankan ketika tombol di tekan. 

root.mainloop() # perulangan dan fungsi menjalankan aplikasi hingga apk tersebut di tutup