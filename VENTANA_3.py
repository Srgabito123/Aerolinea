import customtkinter as ctk


#SE CREA LA VENTANA 1 Y SE BLOQUEA SU TAMAÑO
ventana3 = ctk.CTk()
ventana3.resizable(0, 0)

#SE CONSIGUE EL TAMAÑO DE LA PANTALLA Y SE GUARDA EN UNA VARIABLE LAS MEDIDAS DE VENTANA
screen_width = ventana3.winfo_screenwidth()
screen_height = ventana3.winfo_screenheight()
window_width = 1000
window_height = 600

#SE CALCULA EL CENTRO
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

#SE DA ATRIBUTOS A LA VENTANA
ventana3.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
ventana3.config(background="#d7bb9f")
ventana3.title("Mapaula airline")

#frame
frame_externo = ctk.CTkFrame(ventana3, 
                              width=860, 
                              height=515,
                              bg_color="#d7bb9f",
                              fg_color="#d7bb9f",
                              corner_radius=20,
                              border_color="beige",
                              border_width=4)
frame_externo.place(x=70, y = 25)

frame_texto = ctk.CTkFrame(ventana3, 
                           width=230, 
                           height=40,
                           bg_color="#d7bb9f",
                           fg_color="beige",
                           corner_radius=25)
frame_texto.place(x=-20, y = 15)

#Texto dentro del frame
texto_asientos = ctk.CTkLabel(frame_texto, 
                              text="SELECCIÓN DE ASIENTOS", 
                              font=("Poppins", 18),
                              text_color="brown",
                              bg_color="beige",
                              fg_color="beige",
                              corner_radius=15)
texto_asientos.pack(fill="both", expand=True, pady = 10, padx = 10)

#Texto letras de asientos
texto_letras = ctk.CTkLabel(ventana3, 
                            text=" A         B          C          D          E          F  ", 
                            font=("Poppins", 16),
                            text_color="brown",
                            bg_color="#d7bb9f",
                            fg_color="beige",
                            width = 260,
                            corner_radius=5)
texto_letras.place(x=308, y = 60)

#seleccion de asientos fondos

fondo_padre = ctk.CTkFrame(ventana3,
                            width=320, 
                            height=420,
                            bg_color="#d7bb9f",
                            fg_color="beige",
                            corner_radius=20)
fondo_padre.place(x=290, y = 80)



fondo_asientos1 = ctk.CTkFrame(fondo_padre, 
                              width=300, 
                              height=133,
                              bg_color="beige",
                              fg_color="#ddbdb2",
                              corner_radius=4)
fondo_asientos1.grid(row= 0, column = 0, padx = 10, pady = 10)

fondo_asientos2 = ctk.CTkFrame(fondo_padre, 
                              width=300, 
                              height=133,
                              bg_color="beige",
                              fg_color="#d2a798",
                              corner_radius=4)
fondo_asientos2.grid(row = 1, column = 0)

fondo_asientos3 = ctk.CTkFrame(fondo_padre, 
                              width=300, 
                              height=133,
                              bg_color="beige",
                              fg_color="#c7917e",
                              corner_radius=4)
fondo_asientos3.grid(row = 2, column = 0, padx = 10, pady = 10)


#botones tipo de plan

boton_premium = ctk.CTkButton(ventana3, 
                                 text="Premium",
                                 text_color="white", 
                                 width=150, 
                                 height=40,
                                 font=("Poppins", 16, "bold"),
                                 bg_color="#d7bb9f",
                                 fg_color="#ddbdb2",
                                 cursor="hand2",
                                 hover_color="beige",
                                 border_color="#b38371",
                                 border_width=3)
boton_premium.place(x=635, y=122)

boton_diamante = ctk.CTkButton(ventana3, 
                                 text="Diamante",
                                 text_color="white", 
                                 width=150, 
                                 height=40,
                                 font=("Poppins", 16, "bold"),
                                 bg_color="#d7bb9f",
                                 fg_color="#d2a798",
                                 cursor="hand2",
                                 hover_color="beige",
                                 border_color="#b38371",
                                 border_width=3)
boton_diamante.place(x=635, y=260)

boton_aluminio = ctk.CTkButton(ventana3, 
                                 text="Aluminio",
                                 text_color="white", 
                                 width=150, 
                                 height=40,
                                 font=("Poppins", 16, "bold"),
                                 bg_color="#d7bb9f",
                                 fg_color="#c7917e",
                                 cursor="hand2",
                                 hover_color="beige",
                                 border_color="#b38371",
                                 border_width=3)
boton_aluminio.place(x=635, y=408)

#bototn seleccionar

seleccion_final = ctk.CTkButton(ventana3, 
                                 text="Seleccionar",
                                 text_color="white", 
                                 width=150, 
                                 height=40,
                                 font=("Poppins", 16, "bold"),
                                 bg_color="#d7bb9f",
                                 fg_color="#a06553",
                                 cursor="hand2",
                                 hover_color="beige")
seleccion_final.place(x=790, y=515)

#Creacion seleccionador de asientos

seat_buttons = []
selected_seats = set()
rows = 12
columns = 6

#funcion que indica si un asiento ya está seleccionado
def is_seat_selected(row, col):
    seat = (row, col)
    button = seat_buttons[row][col]
    if seat in selected_seats:
        selected_seats.remove(seat)
        button.configure(fg_color="beige")
    else:
        selected_seats.add(seat)
        button.configure(fg_color="#a06553")

for row in range(rows):
    row_buttons = []
    for col in range(columns):
        if row < 4:
            button = ctk.CTkButton(fondo_asientos1,
                                   width=22,
                                   height=22,
                                   text="",
                                   command=lambda row=row, col=col: is_seat_selected(row, col),
                                   fg_color="beige",
                                   hover_color="gray",
                                   border_color="#a06553",
                                   border_width=2)
            button.grid(row=row, column=col, padx=14, pady=8, sticky="nsew")
        elif row < 8:
            button = ctk.CTkButton(fondo_asientos2,
                                   width=22,
                                   height=22,
                                   text="",
                                   command=lambda row=row, col=col: is_seat_selected(row, col),
                                   fg_color="beige",
                                   hover_color="gray",
                                   border_color="#a06553",
                                   border_width=2)
            button.grid(row=row-4, column=col, padx=14, pady=8, sticky="nsew")
        else:
            button = ctk.CTkButton(fondo_asientos3,
                                   width=22,
                                   height=22,
                                   text="",
                                   command=lambda row=row, col=col: is_seat_selected(row, col),
                                   fg_color="beige",
                                   hover_color="gray",
                                   border_color="#a06553",
                                   border_width=2)
            button.grid(row=row-8, column=col, padx=14, pady=8, sticky="nsew")
        row_buttons.append(button)
    seat_buttons.append(row_buttons)

ventana3.mainloop()

