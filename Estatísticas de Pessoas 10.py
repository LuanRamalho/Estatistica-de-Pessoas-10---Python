import tkinter as tk
from tkinter import messagebox

# Função para calcular as estatísticas
def calcular_estatisticas():
    try:
        # Obter os valores dos campos de entrada
        computador = int(computador_entry.get() or 0)
        notebook = int(notebook_entry.get() or 0)
        smartphone = int(smartphone_entry.get() or 0)
        tablet = int(tablet_entry.get() or 0)
        console = int(console_entry.get() or 0)

        # Calcular o total de pessoas
        total_pessoas = computador + notebook + smartphone + tablet + console
        total_label.config(text=f"Total de pessoas pesquisadas: {total_pessoas}")

        # Limpar barras anteriores
        for barra in barras:
            barra.destroy()
        barras.clear()

        # Dados dos itens
        itens = [
            {"nome": "Computador", "valor": computador, "cor": "#ff6666"},
            {"nome": "Notebook", "valor": notebook, "cor": "#66b3ff"},
            {"nome": "Smartphone", "valor": smartphone, "cor": "#99ff99"},
            {"nome": "Tablet", "valor": tablet, "cor": "#ffcc99"},
            {"nome": "Console", "valor": console, "cor": "#c266ff"}
        ]

        # Gerar as barras de progresso
        for item in itens:
            porcentagem = (item["valor"] / total_pessoas) * 100 if total_pessoas > 0 else 0

            barra_frame = tk.Frame(barras_frame)
            barra_frame.pack(fill=tk.X, pady=5)

            label = tk.Label(barra_frame, text=f"{item['nome']}:", width=15, anchor="w", font=("Arial", 12, "bold"))
            label.pack(side=tk.LEFT)

            barra = tk.Canvas(barra_frame, height=20, bg="#B0C4DE", relief="solid")
            barra.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
            barra.create_rectangle(0, 0, porcentagem * 2, 20, fill=item['cor'], outline="")

            porcentagem_label = tk.Label(barra_frame, text=f"{porcentagem:.2f}%", font=("Arial", 12, "bold"))
            porcentagem_label.pack(side=tk.RIGHT)

            barras.append(barra_frame)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos nos campos!")

# Criar a janela principal
root = tk.Tk()
root.title("Estatísticas de Preferência de Jogo")
root.geometry("750x700")
root.resizable(False, False)
root.config(bg="#E0FFFF")

# Título
titulo = tk.Label(root, text="Estatísticas de Preferência de Jogo", font=("Arial", 20, "bold"), bg="#B22222", fg="white", pady=10)
titulo.pack(fill=tk.X)

# Frame para os inputs
input_frame = tk.Frame(root, bg="#ffcc99", padx=20, pady=20)
input_frame.pack(fill=tk.X, padx=10, pady=20)

# Labels e campos de entrada
computador_label = tk.Label(input_frame, text="Computador:", font=("Arial", 12, "bold"), bg="#ffcc99")
computador_label.grid(row=0, column=0, sticky="w", pady=5)
computador_entry = tk.Entry(input_frame, font=("Arial", 12))
computador_entry.grid(row=0, column=1, pady=5)

notebook_label = tk.Label(input_frame, text="Notebook:", font=("Arial", 12, "bold"), bg="#ffcc99")
notebook_label.grid(row=1, column=0, sticky="w", pady=5)
notebook_entry = tk.Entry(input_frame, font=("Arial", 12))
notebook_entry.grid(row=1, column=1, pady=5)

smartphone_label = tk.Label(input_frame, text="Smartphone:", font=("Arial", 12, "bold"), bg="#ffcc99")
smartphone_label.grid(row=2, column=0, sticky="w", pady=5)
smartphone_entry = tk.Entry(input_frame, font=("Arial", 12))
smartphone_entry.grid(row=2, column=1, pady=5)

tablet_label = tk.Label(input_frame, text="Tablet:", font=("Arial", 12, "bold"), bg="#ffcc99")
tablet_label.grid(row=3, column=0, sticky="w", pady=5)
tablet_entry = tk.Entry(input_frame, font=("Arial", 12))
tablet_entry.grid(row=3, column=1, pady=5)

console_label = tk.Label(input_frame, text="Console:", font=("Arial", 12, "bold"), bg="#ffcc99")
console_label.grid(row=4, column=0, sticky="w", pady=5)
console_entry = tk.Entry(input_frame, font=("Arial", 12))
console_entry.grid(row=4, column=1, pady=5)

# Botão para calcular
calcular_button = tk.Button(input_frame, text="Calcular", font=("Arial", 12), bg="#66ff66", fg="black", command=calcular_estatisticas)
calcular_button.grid(row=5, columnspan=2, pady=15)

# Label do total de pessoas
total_label = tk.Label(root, text="Total de pessoas pesquisadas: 0", font=("Arial", 15, "bold"), bg="#9400D3", fg="#ADFF2F", pady=10)
total_label.pack(fill=tk.X, padx=10)

# Frame para as barras de progresso
barras_frame = tk.Frame(root)
barras_frame.pack(fill=tk.BOTH, padx=20, pady=10, expand=True)

# Lista para armazenar as barras de progresso
barras = []

# Rodar o aplicativo
root.mainloop()
