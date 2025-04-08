def centralizar_janela(janela, largura, altura):
    lt = janela.winfo_screenwidth()
    at = janela.winfo_screenheight()

    pos_x = (lt - largura) // 2
    pos_y = (at - altura) // 2

    janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")