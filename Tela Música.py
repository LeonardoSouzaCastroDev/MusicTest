from pygame import mixer
import customtkinter

def centralizar_janela(janela, largura, altura):
    lt = janela.winfo_screenwidth()
    at = janela.winfo_screenheight()

    pos_x = (lt - largura) // 2
    pos_y = (at - altura) // 2

    janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

def finalizar():
    exit()

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

janela_p = customtkinter.CTk()
janela_p.geometry("300x200")
janela_p.title('MP3')

lg_janela = 425
al_janela = 250

centralizar_janela(janela_p, lg_janela, al_janela)

text1 = customtkinter.CTkLabel(janela_p,
                               text_color='White',
                               text='Vamos começar?',
                               font=('Arial', 20))
text1.pack(pady=40)

def tocar():
    janela_p.withdraw()

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

    def confirmar():
        janela_tocar.withdraw()

        janela_ms = customtkinter.CTk()
        janela_ms.geometry("300x200")
        janela_ms.title('Musicas')

        lg_janela3 = 425
        al_janela3 = 250

        centralizar_janela(janela_ms, lg_janela3, al_janela3)

        rsp = str(pergunta1.get())

        mixer.init()

        def voltar():
            janela_ms.withdraw()

            tocar()

        if rsp == '17/05':
            text3 = customtkinter.CTkLabel(janela_ms,
                                           text_color='White',
                                           text='\n\nTim Bernades, BB',
                                           font=('Arial', 14))
            text3.pack(pady=30)

            mixer.music.stop()
            mixer.music.load('0712.mp3')
            mixer.music.play()

            janela_ms.configure(bg_color='green')

        elif rsp == '25/08':
            text4 = customtkinter.CTkLabel(janela_ms,
                                           text_color='White',
                                           text='\n\nTribalistas, Aliança',
                                           font=('Arial', 14))
            text4.pack(pady=20)

            mixer.music.stop()
            mixer.music.load('1312.mp3')
            mixer.music.play()

        elif rsp == '14/12':
            text5 = customtkinter.CTkLabel(janela_ms,
                                           text_color='White',
                                           text='\n\nRoberto Carlos, Eu te darei o céu',
                                           font=('Arial', 14))
            text5.pack(pady=20)

            mixer.music.stop()
            mixer.music.load('1412.mp3')
            mixer.music.play()

        elif rsp == '07/12':
            text6 = customtkinter.CTkLabel(janela_ms,
                                           text_color='White',
                                           text='\n\nNatiruts, Mergulhei nos seus olhos',
                                           font=('Arial', 14))
            text6.pack(pady=20)

            mixer.music.stop()
            mixer.music.load('2012.mp3')
            mixer.music.play()

        elif rsp == '30/11':
            text7 = customtkinter.CTkLabel(janela_ms,
                                           text_color='White',
                                           text='\n\nMarcelo Jeneci, Pra sonhar',
                                           font=('Arial', 14))
            text7.pack(pady=20)

            mixer.music.stop()
            mixer.music.load('2512.mp3')
            mixer.music.play()

        elif rsp == '12/08':
            text8 = customtkinter.CTkLabel(janela_ms,
                                           text_color='White',
                                           text='\n\nAnavitória, No escuro',
                                           font=('Arial', 14))
            text8.pack(pady=20)

            mixer.music.stop()
            mixer.music.load('0101.mp3')
            mixer.music.play()

        elif rsp == '01/10':
            text9 = customtkinter.CTkLabel(janela_ms,
                                           text_color='White',
                                           text='\n\nToquinho, Carolina, Carol bela',
                                           font=('Arial', 14))
            text9.pack(pady=20)
            janela_ms.configure(bg='#6b5d38')

            mixer.music.stop()
            mixer.music.load('0901.mp3')
            mixer.music.play()

        else:
            text0 = customtkinter.CTkLabel(janela_ms,
                                           text_color='White',
                                           text='Data inválida!',
                                           font=('Arial', 20))

            text0.pack(pady=50)

        bt_v = customtkinter.CTkButton(janela_ms,
                                       text="Voltar",
                                       width=100, height=30,
                                       fg_color="#1f6aa5",
                                       hover_color="#144e75",
                                       font=("Arial", 18),
                                       corner_radius=17,
                                       command= voltar)
        bt_v.place(x=90, y=150)

        bt_p = customtkinter.CTkButton(janela_ms,
                                       text="Finalizar",
                                       width=100, height=30,
                                       fg_color="#1f6aa5",
                                       hover_color="#144e75",
                                       font=("Arial", 18),
                                       corner_radius=17,
                                       command= finalizar)
        bt_p.place(x=230, y=150)

        janela_ms.mainloop()

    bt_2 = customtkinter.CTkButton(janela_tocar,
                                   text="Confirmar",
                                   width=50, height=30,
                                   fg_color="#1f6aa5",
                                   hover_color="#144e75",
                                   font=("Arial", 18),
                                   corner_radius=17,
                                   command= confirmar)
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

botao = customtkinter.CTkButton(janela_p,
                                text="Clique Aqui!",
                                width=100, height=50,
                                fg_color="#1f6aa5",
                                hover_color="#144e75",
                                font=("Arial", 18),
                                corner_radius= 17,
                                command= tocar)
botao.pack(fill="x",padx=20,pady=20)

janela_p.mainloop()
