#Creada por Pilar Sahonero Diaz
#Calculadora Basica de solo dos datos Intefaz Grafica
#Primero importamos la biblioteca que se utilizara para la interfaz grafica
import tkinter as tk
# Creamos la ventana Definimos como se vera 
root=tk.Tk()
root.title('Calculadora')
root.resizable(False,False)
root.geometry('490x350')
root.configure(bg="#000839")
tk.Label(root, text='Calculadora',bg ='#005082',fg='#F5EAEA', font=('Cantarell Extra Bold',30),width='150',height='2').pack()
# Se define la variable universales que se utizara en el programa 
numero_1 = tk.StringVar()
numero_2 = tk.StringVar()
Resultado = tk.StringVar()
# Se crea las funsiones de suma, resta, multiplicacion, division
def suma():
    a = int(numero_1.get())
    b = int(numero_2.get())
    Resultado.set(str(a+b))
def resta():
    a = int(numero_1.get())
    b = int(numero_2.get())
    Resultado.set(str((a-b)))
def multiplicacion():
    a = int(numero_1.get())
    b = int(numero_2.get())
    Resultado.set(str((a*b)))
def division():
    a = int(numero_1.get())
    b = int(numero_2.get())
    if b == 0:
        Resultado.set('Error')
    Resultado.set(str((a/b)))
#en este punto se crea Los paneles de entrada donde se mostrara el resultado 
tk.Entry(root,width='12',textvariable = numero_1, justify='center').place(x='80',y='110')
tk.Entry(root,width='12',textvariable = numero_2, justify='center').place(x='290',y='110')
tk.Label(root, text=' = ',bg ='#000839',fg='#F5EAEA',justify='center').place(x='225',y='145')
tk.Label(root, textvariable=Resultado, bg="#000839", fg='white', font=('', 24)).place(x='225',y='170')
# Se cra los botones y se conecta con las funciones ya revisadas anteriormente
tk.Button(root, text='SUMA', command=suma , width='8',height='2',bg='#ffa41b',font=('Source Code Pro Semibold',10)).place(x='9',y='230')
tk.Button(root, text='RESTA', command=resta , width='8',height='2',bg='#ffa41b',font=('Source Code Pro Semibold',10)).place(x='130',y='230')
tk.Button(root, text='MULTIPLI', command=multiplicacion , width='8',height='2',bg='#ffa41b',font=('Source Code Pro Semibold',10)).place(x='260',y='230')
tk.Button(root, text='DIVISION', command=division , width='8',height='2',bg='#ffa41b',font=('Source Code Pro Semibold',10)).place(x='390',y='230')
tk.Button(root, text='SALIR',bg='#ffa41b', width='10',height='1', command=root.destroy,font=('Source Code Pro Semibold',9)).place(x='200',y='300')
# con este comando se mostrara la ventana siempre debe estar al fina aqui se demuestra que el orden si importa
root.mainloop()
 