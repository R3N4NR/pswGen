import tkinter as tk
from tkinter import messagebox
import random

# Função para gerar a senha
def gerar_senha(nome_usuario):
    substituicoes = {
        'a': ['4', 'A', '@'], 'A': ['a','@', 'A'],
        'e': ['3', '&'], 'E': ['3', '&'],
        'i': ['1', '!', 'I'], 'I': ['1', '!', 'i'],
        'o': ['0'], 'O': ['0'],
        'u': ['V'], 'U': ['V']
    }

    senha = ""
    
    for char in nome_usuario:
        if char in substituicoes:
            senha += random.choice(substituicoes[char])
        else:
            senha += char

    opcao_p5 = random.choice(['start', 'end', 'random'])
    
    # Inserir "p5" antes ou depois da senha
    if random.choice([True, False]):
        senha = opcao_p5 + senha
    else:
        senha = senha + opcao_p5

    return senha

# Função para ser chamada ao clicar no botão
def gerar_senha_interface():
    nome_usuario = entry_usuario.get()  # Obtemos o nome de usuário
    if nome_usuario:  # Verifica se o campo não está vazio
        senha = gerar_senha(nome_usuario)
        label_senha.config(text="Senha gerada: " + senha)  # Atualiza o label com a senha
    else:
        messagebox.showerror("Erro", "Por favor, insira um nome de usuário!")  # Mostra erro se o campo estiver vazio

# Configuração da interface gráfica
root = tk.Tk()
root.title("Gerador de Senha")

# Tamanho da janela
root.geometry("400x300")

# Texto explicativo
label_instrucoes = tk.Label(root, text="Digite seu nome de usuário:", font=("Arial", 12))
label_instrucoes.pack(pady=10)

# Campo de entrada para o nome de usuário
entry_usuario = tk.Entry(root, font=("Arial", 12), width=25)
entry_usuario.pack(pady=10)

# Botão para gerar a senha
button_gerar = tk.Button(root, text="Gerar Senha", font=("Arial", 12), command=gerar_senha_interface)
button_gerar.pack(pady=10)

# Label para exibir a senha gerada
label_senha = tk.Label(root, text="Senha gerada: ", font=("Arial", 12))
label_senha.pack(pady=10)

# Iniciar a interface
root.mainloop()
