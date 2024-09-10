import tkinter as tk
from tkinter import messagebox, PhotoImage


def exportar_para_pdf():
    pdf_file = "conteúdo_exportado.pdf"

    # Criação de uma figura Matplotlib
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [4, 5, 6])
    ax.set_title('Exemplo de Gráfico')

    # Salvando o gráfico em um arquivo PDF
    with PdfPages(pdf_file) as pdf:
        pdf.savefig(fig)  # Salva a figura no arquivo PDF

    # Mensagem de sucesso
    messagebox.showinfo("Sucesso", f"O gráfico foi exportado para {pdf_file}")


# Configuração da interface gráfica com Tkinter
root = tk.Tk()
root.title("Exportar para PDF")

# Adiciona um botão para exportar o gráfico
btn_exportar = tk.Button(root, text="Exportar Gráfico para PDF", command=exportar_para_pdf)
btn_exportar.pack(pady=20)

# Inicia o loop principal do Tkinter
root.mainloop()