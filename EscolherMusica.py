import customtkinter
from CentralizarJanela import centralizar_janela
from Finalizar import finalizar

def escolher_musica():
    janela_tocar = customtkinter.CTk()
    janela_tocar.geometry("300x200")
    janela_tocar.title('Músicas')

    lg_janela2 = 425
    al_janela2 = 250

    centralizar_janela(janela_tocar, lg_janela2, al_janela2)

    text2 = customtkinter.CTkLabel(janela_tocar,
                                   text_color='White',
                                   text='Escolha:\n\n17/05  25/08  14/12  07/12  25/12  30/11  01/10',
                                   font=('Arial', 14))
    text2.pack(pady=20)

    pergunta1 = customtkinter.CTkEntry(janela_tocar)
    pergunta1.pack(pady=15)

    def fechar_confirmar():
        from TocarMusica import tocar_musica
        rsp = pergunta1.get()
        janela_tocar.withdraw()
        tocar_musica(rsp)

    bt_2 = customtkinter.CTkButton(janela_tocar,
                                   text="Confirmar",
                                   width=50, height=30,
                                   fg_color="#1f6aa5",
                                   hover_color="#144e75",
                                   font=("Arial", 18),
                                   corner_radius=17,
                                   command= fechar_confirmar)
    bt_2.place(x=90, y=170)

    bt_3 = customtkinter.CTkButton(janela_tocar,
                                   text="Finalizar",
                                   width=100, height=30,
                                   fg_color="#1f6aa5",
                                   hover_color="#144e75",
                                   font=("Arial", 18),
                                   corner_radius=17,
                                   command= finalizar)
    bt_3.place(x=230, y=170)

    janela_tocar.mainloop()
