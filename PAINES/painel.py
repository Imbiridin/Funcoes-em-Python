import tkinter as tk

def converter():
    try:
        
        c = float(entrada.get())
        f = c * 9 / 5 + 32
        resultado.config(text=f"{c}°C = {f:.1f}°F")
    except ValueError:
        resultado.config(text="Digite um número!")

janela = tk.Tk()
janela.title("Conversor")

tk.Label(janela, text="Celsius:").pack()

entrada = tk.Entry(janela)
entrada.pack()

tk.Button(janela, text="Converter", command=converter).pack()

resultado = tk.Label(janela, text="")
resultado.pack()

janela.mainloop()