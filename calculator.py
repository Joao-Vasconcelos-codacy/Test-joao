import tkinter as tk
from tkinter import messagebox

# Função para processar a entrada do usuário
def press(button_text):
    if button_text == "=":
        try:
            # Avaliar a expressão na entrada
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Erro", "Entrada inválida!")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)
"Implementa melhorias na calculadora"
# Criar a janela principal
root = tk.Tk()
root.title("Calculadora")

# Caixa de entrada para os números e operações
entry = tk.Entry(root, width=20, font=("Arial", 18), bd=5, insertwidth=4, justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Botões da calculadora
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Adicionar botões à interface
row_val = 1
col_val = 0
for button_text in buttons:
    button = tk.Button(root, text=button_text, padx=20, pady=20, font=("Arial", 14),
                       command=lambda b=button_text: press(b))
    button.grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 
