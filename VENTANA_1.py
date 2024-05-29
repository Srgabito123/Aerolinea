import customtkinter as ctk
from PIL import Image

#FUNCION PARA DESPUES
def check_in():
    caja1.delete(0, ctk.END)
    caja2.delete(0, ctk.END)

#SE CREA LA VENTANA 1 Y SE BLOQUEA SU TAMAÑO
ventana1 = ctk.CTk()
ventana1.resizable(0, 0)

#SE CONSIGUE EL TAMAÑO DE LA PANTALLA Y SE GUARDA EN UNA VARIABLE LAS MEDIDAS DE VENTANA
screen_width = ventana1.winfo_screenwidth()
screen_height = ventana1.winfo_screenheight()
window_width = 1000
window_height = 600

#SE CALCULA EL CENTRO
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

#SE DA ATRIBUTOS A LA VENTANA
ventana1.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
ventana1.config(background="#d7bb9f")
ventana1.title("Mapaula airline")

#SE AGREGAN WIDGETS
#IMPORTANDO Y PONIENDO LA IMÁGEN
imagen1 = ctk.CTkImage(light_image=Image.open("D:/GABO/2024/UNIVERSIDAD/SEMESTRE 1/FUNDAMENTOS DE PROGRAMACIÓN IMPERATIVA/PROYECTO FINAL/Repositorio/LOGO AEROLINEA.png"),
                      dark_image=Image.open("D:/GABO/2024/UNIVERSIDAD/SEMESTRE 1/FUNDAMENTOS DE PROGRAMACIÓN IMPERATIVA/PROYECTO FINAL/Repositorio/LOGO AEROLINEA.png"),
                      size = (340, 340))
imagen1_label = ctk.CTkLabel(ventana1, image=imagen1, text = "", bg_color="#d7bb9f")
imagen1_label.place(x=330, y=1)


#CREACIÓN DE TITULOS Y CAJAS DE TEXTO
texto1 = ctk.CTkLabel(ventana1, 
                      text="Código", 
                      width=150, 
                      height=40, 
                      bg_color="#d7bb9f",
                      font=("Poppins", 18))
texto1.place(x=270, y=300)
caja1 = ctk.CTkEntry(ventana1, 
                     width=190, 
                     height=30, 
                     bg_color="#d7bb9f", 
                     border_width=3,
                     border_color="#a06553")
caja1.place(x=250, y=350)

texto2 = ctk.CTkLabel(ventana1, 
                      text="Apellido", 
                      width=150, 
                      height=40, 
                      bg_color="#d7bb9f",
                      font=("Poppins", 18))
texto2.place(x=580, y=300)
caja2 = ctk.CTkEntry(ventana1, 
                     width=190, 
                     height=30, 
                     bg_color="#d7bb9f",
                     border_width=3,
                     border_color="#a06553")
caja2.place(x=560, y=350)

#CREACION DE BOTON


boton = ctk.CTkButton(ventana1, 
                      text="Realizar Check-In",
                      text_color="white", 
                      width=150, 
                      height=40,
                      font=("Poppins", 16, "bold"),
                      bg_color="#d7bb9f",
                      fg_color="#a06553",
                      cursor="hand2",
                      hover_color="beige",
                      command = check_in)
boton.place(x=425, y=440)

ventana1.mainloop()