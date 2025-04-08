import customtkinter
from CentralizarJanela import centralizar_janela
from EscolherMusica import escolher_musica

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

def fechar_Escolher():
    janela_p.withdraw()
    escolher_musica()

botao = customtkinter.CTkButton(janela_p,
                                text="Clique Aqui!",
                                width=100, height=50,
                                fg_color="#1f6aa5",
                                hover_color="#144e75",
                                font=("Arial", 18),
                                corner_radius= 17,
                                command= fechar_Escolher)
botao.pack(fill="x",padx=20,pady=20)

janela_p.mainloop()