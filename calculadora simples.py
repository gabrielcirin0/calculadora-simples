import tkinter as tk
janela = tk.Tk()
janela.geometry('440x420')
janela.resizable(False, False)
janela.title('CALCULADORA SIMPLES')
def apagar_elemento():
    del(mostrar[-1])
    display.config(text=mostrar)
def number_7():
    mostrar.append(7)
    display.config(text=mostrar)
def number_8():
    mostrar.append(8)
    display.config(text=mostrar)
def number_9():
    mostrar.append(9)
    display.config(text=mostrar)
def number_4():
    mostrar.append(4)
    display.config(text=mostrar)
def number_5():
    mostrar.append(5)
    display.config(text=mostrar)
def number_6():
    mostrar.append(6)
    display.config(text=mostrar)
def number_1():
    mostrar.append(1)
    display.config(text=mostrar)
def number_2():
    mostrar.append(2)
    display.config(text=mostrar)
def number_3():
    mostrar.append(3)
    display.config(text=mostrar)
def number_0():
    mostrar.append(0)
    display.config(text=mostrar)
def ponto():
    mostrar.append('.')
    display.config(text=mostrar)
def operador_divisao():
    mostrar.append('/')
    display.config(text=mostrar)
def operador_soma():
    mostrar.append('+')
    display.config(text=mostrar)
def operador_subtracao():
    mostrar.append('-')
    display.config(text=mostrar)
def operador_multiplicacao():
    mostrar.append('*')
    display.config(text=mostrar)
def igual():
    global mostrar
    if len(mostrar) == 0:
        mostrar.append(0)
    resultado_2 = ''
    display.config(text=mostrar)
    resultado_1 = [str(num) for num in mostrar]
    for letra in resultado_1:
        resultado_2 += letra
    print(eval(resultado_2))
    display.config(text=(eval(resultado_2)))
def limpar():
    global display, mostrar
    display.config(text=0)
    mostrar = []
mostrar = list()
mostrar_display= 0
display_status = list()

display = tk.Label(janela, text=mostrar_display, anchor='e', font=('Times New roman', 35)) 
display.place(x=50, y=20)

botao_7 = tk.Button(janela, text='7', font=('Arial black', 25), fg='white', bg="#6369A5", width=3, command=number_7)
botao_7.place(x=20, y=80)
botao_8 = tk.Button(janela, text='8', font=('Arial black', 25), fg='white', bg='#6369A5', width=3, command=number_8)
botao_8.place(x=100, y=80)
botao_9 = tk.Button(janela, text='9', font=('Arial black', 25), fg='white', bg='#6369A5', width=3, command=number_9)
botao_9.place(x=180, y=80)

botao_div = tk.Button(janela, text='÷', font=('Arial black', 25), fg='white', bg='#414461', width=3, command=operador_divisao)
botao_div.place(x=260, y=80)

botao_apagar = tk.Button(janela, text='←', font=('Arial', 15),anchor='w', fg='white', bg="#26283A", width=6, height=7, command=apagar_elemento)
botao_apagar.place(x=340, y=236)
botao_limpar = tk.Button(janela, text='C', font=('Arial', 15), fg='white', bg='#26283A', width=6, height=6, command=limpar)
botao_limpar.place(x=340, y=80)

botao_4 = tk.Button(janela, text='4', font=('Arial black', 25), fg='white', bg='#6369A5', width=3, command=number_4)
botao_4.place(x=20, y=165)
botao_5 = tk.Button(janela, text='5', font=('Arial black', 25), fg='white', bg='#6369A5', width=3, command=number_5)
botao_5.place(x=100, y=165)
botao_6 = tk.Button(janela, text='6', font=('Arial black', 25), fg='white', bg='#6369A5', width=3, command=number_6)
botao_6.place(x=180, y=165)

botao_soma = tk.Button(janela, text='+', font=('Arial black', 25), fg='white', bg='#414461', width=3, command=operador_soma)
botao_soma.place(x=260, y=165)

botao_1 = tk.Button(janela, text='1', font=('Arial black', 25), fg='white', bg='#6369A5', width=3, command=number_1)
botao_1.place(x=20, y=250)
botao_2 = tk.Button(janela, text='2', font=('Arial black', 25), fg='white', bg='#6369A5', width=3, command=number_2)
botao_2.place(x=100, y=250)
botao_3 = tk.Button(janela, text='3', font=('Arial black', 25), fg='white', bg='#6369A5', width=3, command=number_3)
botao_3.place(x=180, y=250)

botao_sub = tk.Button(janela, text='-', font=('Arial black', 25), fg='white', bg='#414461', width=3, command=operador_subtracao)
botao_sub.place(x=260, y=250)

botao_0 = tk.Button(janela, text='0', font=('Arial black', 25), fg='white', bg='#6369A5', width=3, command=number_0)
botao_0.place(x=20, y=335)
botao_ponto = tk.Button(janela, text='.', font=('Arial black', 25), fg='white', bg="#414461", width=3, command=ponto)
botao_ponto.place(x=100, y=335)
botao_igual = tk.Button(janela, text='=', font=('Arial black', 25), fg='white', bg="#DAA22A", width=3, command=igual)
botao_igual.place(x=180, y=335)

botao_mult = tk.Button(janela, text='*', font=('Arial black', 25), fg='white', bg='#414461', width=3, command=operador_multiplicacao)
botao_mult.place(x=260, y=335)

janela.mainloop()