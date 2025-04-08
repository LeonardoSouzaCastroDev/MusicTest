import customtkinter
from pygame import mixer
from CentralizarJanela import centralizar_janela
from Finalizar import finalizar

def tocar_musica(rsp):
    janela_ms = customtkinter.CTk()
    janela_ms.geometry("300x200")
    janela_ms.title('Musicas')

    lg_janela3 = 425
    al_janela3 = 250

    centralizar_janela(janela_ms, lg_janela3, al_janela3)

    mixer.init()

    def voltar():
        from EscolherMusica import escolher_musica
        janela_ms.withdraw()
        escolher_musica()

    musicas = {
        '17/05': ("Tim Bernades, BB", "0712.mp3"),
        '25/08': ("Tribalistas, Aliança", "1312.mp3"),
        '14/12': ("Roberto Carlos, Eu te darei o céu", "1412.mp3"),
        '07/12': ("Natiruts, Mergulhei nos seus olhos", "2012.mp3"),
        '30/11': ("Marcelo Jeneci, Pra sonhar", "2512.mp3"),
        '12/08': ("Anavitória, No escuro", "0101.mp3"),
        '01/10': ("Toquinho, Carolina, Carol bela", "0901.mp3")
    }

    if rsp in musicas:
        nome, arquivo = musicas[rsp]

        label = customtkinter.CTkLabel(janela_ms,
                                       text_color='White',
                                       text=f'\n\n{nome}',
                                       font=('Arial', 14))
        label.pack(pady=30)

        mixer.music.stop()
        mixer.music.load(f'C:/Users/leona/OneDrive/Documentos/Programação/PycharmProjects/AppMusic/Music/{arquivo}')
        mixer.music.play()

    else:
        erro = customtkinter.CTkLabel(janela_ms,
                                      text_color='White',
                                      text='Data inválida!',
                                      font=('Arial', 20))
        erro.pack(pady=50)

    bt_v = customtkinter.CTkButton(janela_ms,
                                   text="Voltar",
                                   width=100, height=30,
                                   fg_color="#1f6aa5",
                                   hover_color="#144e75",
                                   font=("Arial", 18),
                                   corner_radius=17,
                                   command=voltar)
    bt_v.place(x=90, y=150)

    bt_p = customtkinter.CTkButton(janela_ms,
                                   text="Finalizar",
                                   width=100, height=30,
                                   fg_color="#1f6aa5",
                                   hover_color="#144e75",
                                   font=("Arial", 18),
                                   corner_radius=17,
                                   command=finalizar)
    bt_p.place(x=230, y=150)

    janela_ms.mainloop()