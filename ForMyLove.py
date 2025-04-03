from pygame import mixer, image
import tkinter as tk

def centralizar_janela(janela, largura, altura):
    lt = janela.winfo_screenwidth()
    at = janela.winfo_screenheight()

    pos_x = (lt - largura) // 2
    pos_y = (at - altura) // 2

    janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

def finalizar():
    exit()

janela_p = tk.Tk()
janela_p.title('MP3')

lg_janela = 425
al_janela = 250

centralizar_janela(janela_p, lg_janela, al_janela)

text1 = tk.Label(janela_p, fg='White', bg='Black', text='Vamos começar?', font=('Arial', 20))
text1.pack(pady=40)

def tocar():
    janela_p.withdraw()

    janela_tocar = tk.Tk()
    janela_tocar.title('Musicas')
    lg_janela2 = 425
    al_janela2 = 250
    centralizar_janela(janela_tocar, lg_janela2, al_janela2)

    janela_tocar.configure(bg='Black')

    text2 = tk.Label(janela_tocar, fg='White', bg='Black', text='Escolha:\n\n07/12  13/12  14/12  20/12  25/12  01/01  09/01', font=('Arial', 14))
    text2.pack(pady=20)

    pergunta = tk.Entry(janela_tocar, fg='Black', bg='Grey', font=('Arial', 14))
    pergunta.pack(pady=15)

    def confirmar():
        janela_tocar.withdraw()

        janela_ms = tk.Tk()
        janela_ms.title('Musicas')
        lg_janela3 = 425
        al_janela3 = 250
        centralizar_janela(janela_ms, lg_janela3, al_janela3)

        rsp = str(pergunta.get())

        mixer.init()

        def voltar():
            janela_ms.withdraw()

            tocar()

        if rsp == '07/12':
            text3 = tk.Label(janela_ms, fg='black', bg='#117812', text='Nossa primeira música postada:\n\nTim Bernades, BB', font=('Arial', 14))
            text3.pack(pady=30)
            janela_ms.configure(bg='#117812')

            mixer.music.stop()
            mixer.music.load('0712.mp3')
            mixer.music.play()

        elif rsp == '13/12':
            text4 = tk.Label(janela_ms, fg='Black', bg='#b4b5ab', text='Nossa segunda música postada:\n\nTribalistas, Aliança', font=('Arial', 14))
            text4.pack(pady=20)
            janela_ms.configure(bg='#b4b5ab')

            mixer.music.stop()
            mixer.music.load('1312.mp3')
            mixer.music.play()

        elif rsp == '14/12':
            text5 = tk.Label(janela_ms, fg='Black', bg='#7db6ca', text='Nossa terceira música postada:\n\nRoberto Carlos, Eu te darei o céu', font=('Arial', 14))
            text5.pack(pady=20)
            janela_ms.configure(bg='#7db6ca')

            mixer.music.stop()
            mixer.music.load('1412.mp3')
            mixer.music.play()

        elif rsp == '20/12':
            text6 = tk.Label(janela_ms, fg='Black', bg='#973b40', text='Nossa quarta música postada:\n\nNatiruts, Mergulhei nos seus olhos', font=('Arial', 14))
            text6.pack(pady=20)
            janela_ms.configure(bg='#973b40')

            mixer.music.stop()
            mixer.music.load('2012.mp3')
            mixer.music.play()

        elif rsp == '25/12':
            text7 = tk.Label(janela_ms, fg='Black', bg='#d0ccae', text='Nossa quinta música postada:\n\nMarcelo Jeneci, Pra sonhar', font=('Arial', 14))
            text7.pack(pady=20)
            janela_ms.configure(bg='#d0ccae')

            mixer.music.stop()
            mixer.music.load('2512.mp3')
            mixer.music.play()

        elif rsp == '01/01':
            text8 = tk.Label(janela_ms, fg='Black', bg='#c5c1a6', text='Nossa sexta música postada:\n\nAnavitória, No escuro', font=('Arial', 14))
            text8.pack(pady=20)
            janela_ms.configure(bg='#c5c1a6')

            mixer.music.stop()
            mixer.music.load('0101.mp3')
            mixer.music.play()

        elif rsp == '09/01':
            text9 = tk.Label(janela_ms, fg='Black', bg='#6b5d38', text='Nossa setima música postada:\n\nToquinho, Carolina, Carol bela', font=('Arial', 14))
            text9.pack(pady=20)
            janela_ms.configure(bg='#6b5d38')

            mixer.music.stop()
            mixer.music.load('0901.mp3')
            mixer.music.play()

        else:
            text0 = tk.Label(janela_ms, fg='White', bg='Black', text='Data inválida!', font=('Arial', 20))
            text0.pack(pady=50)
            janela_ms.configure(bg="black")

        bt_v = tk.Button(janela_ms, text='Voltar', command=voltar)
        bt_v.place(x=140, y=150)

        bt_p = tk.Button(janela_ms, text='Finalizar', command=finalizar)
        bt_p.place(x=240, y=150)

    bt_2 = tk.Button(janela_tocar, text='Confirmar', command=confirmar)
    bt_2.place(x=135, y=170)

    bt_3 = tk.Button(janela_tocar, text='Finalizar', command=finalizar)
    bt_3.place(x=235, y=170)

bt_1 = tk.Button(janela_p, text='Vamos!', font=('Arial', 12), command=tocar)
bt_1.pack(pady=20)

janela_p.configure(bg='Black')
janela_p.mainloop()
