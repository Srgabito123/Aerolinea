from tkinter import *
import customtkinter as ctk
#ventana 4
root = ctk.CTk()
root.title("CONDOR")
root._set_appearance_mode("light")
root.geometry("1000x600")
root.resizable(0, 0)
root.config(bg = "light pink")
root.iconbitmap("logo.ico")

#---------------------------funciones---------------------------
def eleccion_vuelo():
    if frame_eleccion_vuelo.winfo_viewable():
        frame_eleccion_vuelo.place_forget()
    else:
        frame_eleccion_vuelo.place(relx=0.42, rely=0.2, anchor="n")
#---------------------------VARIABLES---------------------------
hora_llegada = "13:00"
hora_salida = "10:00"
lugar_salida = "Bogotá"
lugar_llegada = "Cartagena"
ida = f"Ida: {lugar_salida} - {lugar_llegada}"
precio = "2.000.000"
fecha = "2024-06-13"
flechita = "-------------------------------------->"

#---------------------------FONTS---------------------------
font_1 = ctk.CTkFont(family="Inherit", size=18, weight="bold")
#---------------------------FRAMES---------------------------
frame_principal = ctk.CTkFrame(master = root,
                           width = 1000,
                           height = 600,
                           corner_radius = 10,
                           fg_color = "light pink",
                           border_color = "white",
                           border_width = 2
                           )

opcion1 = ctk.CTkFrame(master = frame_principal, 
                          bg_color = "light pink",    
                          width = 0.9, 
                          height = 0.2, 
                          corner_radius = 30,
                          fg_color = "beige"
                          )

opcion2 = ctk.CTkFrame(master = frame_principal, 
                          fg_color = "beige",  
                          width = 0.9, 
                          height = 0.2, 
                          corner_radius = 30,
                          bg_color = "light pink"
                          )

opcion3 = ctk.CTkFrame(master = frame_principal,
                          fg_color = "beige",  
                          width = 0.9, 
                          height = 0.2, 
                          corner_radius = 30,
                          bg_color = "light pink"
                          )

opcion4 = ctk.CTkFrame(master = frame_principal,
                          fg_color = "beige",
                          bg_color = "light pink",
                          width = 0.9, 
                          height = 0.2, 
                          corner_radius = 30
                          )

frame_eleccion_vuelo = ctk.CTkFrame(master = frame_principal,
                          width=825,
                          height=462, 
                          fg_color="white",
                          border_width=2,
                          corner_radius=32)
frame_eleccion_vuelo.place_forget()

frame_aluminio = ctk.CTkFrame(master = frame_eleccion_vuelo,
                          width=250,
                          height=430, 
                          fg_color="white",
                          border_width=2,
                          corner_radius=32)
frame_aluminio.place(relx=0.17, rely=0.03, anchor="n")

frame_diamante = ctk.CTkFrame(master = frame_eleccion_vuelo,
                          width=250,
                          height=430, 
                          fg_color="white",
                          border_width=2,
                          corner_radius=32)
frame_diamante.place(relx=0.50, rely=0.03, anchor="n")

frame_esmeralda = ctk.CTkFrame(master = frame_eleccion_vuelo,
                          width=250,
                          height=430, 
                          fg_color="white",
                          border_width=2,
                          corner_radius=32)
frame_esmeralda.place(relx=0.83, rely=0.03, anchor="n")

#---------------------------TEXTOS---------------------------
text_viaje = ctk.CTkLabel(master = frame_principal, 
                      text = ida, 
                      fg_color = "beige", 
                      width = 0.2, 
                      height = 0.065, 
                      text_color = "black", 
                      font = ("roboto", 12), 
                      corner_radius = 10, 
                      bg_color = "light pink",
                      )
text_hora_salida = ctk.CTkLabel(master = opcion1, 
                            text = hora_salida,
                            fg_color = "beige",
                            text_color = "black",
                            font = ("roboto", 18),
                            width = 0.1,
                            height = 0.3,
                            corner_radius = 10,
                            bg_color = "beige"
                            )
text_hora_llegada = ctk.CTkLabel(master = opcion1, 
                            text = hora_llegada,
                            fg_color = "beige",
                            text_color = "black",
                            font = ("roboto", 18),
                            width = 0.1,
                            height = 0.3,
                            corner_radius = 10,
                            bg_color = "beige"
                            )
text_lugar_salida = ctk.CTkLabel(master = opcion1, 
                            text = lugar_salida,
                            fg_color = "Beige",
                            text_color = "black",
                            font = ("roboto", 13),
                            width = 0.1,
                            height = 0.3,
                            corner_radius = 10,
                            bg_color = "beige"
                            )
text_lugar_llegada = ctk.CTkLabel(master = opcion1, 
                            text = lugar_llegada,
                            fg_color = "Beige",
                            text_color = "black",
                            font = ("roboto", 13),
                            width = 0.1,
                            height = 0.3,
                            corner_radius = 10,
                            bg_color = "beige"
                            )
text_desde = ctk.CTkLabel(master = opcion1,
                      text = """DESDE:

                         COP $""",
                      fg_color = "beige",
                      text_color = "black",
                      font = (font_1, 11),
                      width = 0.1,
                      height = 0.3,
                      corner_radius = 10,
                      bg_color = "beige"
                      )
text_precio = ctk.CTkLabel(master = opcion1,
                        text = precio,
                        fg_color = "beige",
                        text_color = "black",
                        font = ("roboto", 11),
                        width = 0.1,
                        height = 0.3,
                        corner_radius = 10,
                        bg_color = "beige"
                        )
text_flechita = ctk.CTkLabel(master = opcion1,
                        text = flechita,
                        fg_color = "beige",
                        text_color = "black",
                        font = ("roboto", 20),
                        width = 0.3,
                        height = 0.3,
                        bg_color = "beige"
                        )
#---------------------------BOTONES---------------------------
boton_eleccion1 = ctk.CTkButton(master = frame_principal,
                        text="Elegir",
                        font=font_1, 
                        text_color="black",
                        width=100, 
                        height=50, 
                        corner_radius=32, 
                        fg_color="white", 
                        command=eleccion_vuelo, 
                        hover_color="#DBB2FF")

boton_eleccion2 = ctk.CTkButton(master = frame_principal,
                        text="Elegir",
                        font=font_1, 
                        text_color="black",
                        width=100, 
                        height=50, 
                        corner_radius=32, 
                        fg_color="white", 
                        command=eleccion_vuelo, 
                        hover_color="#DBB2FF")

boton_eleccion3 = ctk.CTkButton(master = frame_principal,
                        text="Elegir",
                        font=font_1, 
                        text_color="black",
                        width=100, 
                        height=50, 
                        corner_radius=32, 
                        fg_color="white", 
                        command=eleccion_vuelo, 
                        hover_color="#DBB2FF")

boton_eleccion4 = ctk.CTkButton(master = frame_principal,
                        text="Elegir",
                        font=font_1, 
                        text_color="black",
                        width=100, 
                        height=50, 
                        corner_radius=32, 
                        fg_color="white", 
                        command=eleccion_vuelo, 
                        hover_color="#DBB2FF")

boton_dias1 = ctk.CTkButton(master = frame_principal,
                        text = f"Fecha: {fecha}",
                        font=(font_1, 13), 
                        text_color="black",
                        width=100, 
                        height=50, 
                        corner_radius=32, 
                        fg_color="beige",  
                        hover_color="light blue")

boton_dias2 = ctk.CTkButton(master = frame_principal,
                        text = f"Fecha: {fecha}",
                        font=(font_1, 13), 
                        text_color="black",
                        width=100, 
                        height=50, 
                        corner_radius=32, 
                        fg_color="beige",  
                        hover_color="light blue")

boton_dias3 = ctk.CTkButton(master = frame_principal,
                        text = f"Fecha: {fecha}",
                        font=(font_1, 13), 
                        text_color="black",
                        width=100, 
                        height=50, 
                        corner_radius=32, 
                        fg_color="beige",  
                        hover_color="light blue")

boton_dias4 = ctk.CTkButton(master = frame_principal,
                        text = f"Fecha: {fecha}",
                        font=(font_1, 13), 
                        text_color="black",
                        width=100, 
                        height=50, 
                        corner_radius=32, 
                        fg_color="beige",  
                        hover_color="light blue")

boton_dias5 = ctk.CTkButton(master = frame_principal,
                        text = f"Fecha: {fecha}",
                        font=(font_1, 13), 
                        text_color="black",
                        width=100, 
                        height=50, 
                        corner_radius=32, 
                        fg_color="beige",  
                        hover_color="light blue")

#---------------------------POSICIONAMIENTO-----------------------
frame_principal.place(relx = 0.5, rely = 0.5, anchor = "center")

text_viaje.place(x = 6, y = 5, relwidth = 0.3, relheight = 0.065)
boton_dias1.place(x = 20, y = 66, relwidth = 0.16, relheight = 0.057)
boton_dias2.place(x = 220, y = 66, relwidth = 0.16, relheight = 0.057)
boton_dias3.place(x = 420, y = 66, relwidth = 0.16, relheight = 0.057)
boton_dias4.place(x = 620, y = 66, relwidth = 0.16, relheight = 0.057)
boton_dias5.place(x = 820, y = 66, relwidth = 0.16, relheight = 0.057)
#frame_opciones.place(x = 48.35, y = 135, relwidth = 0.9, relheight = 0.7)
opcion1.place(x = 60, y = 120, relwidth = 0.75, relheight = 0.17)
opcion2.place(x = 60, y = 240, relwidth = 0.75, relheight = 0.17)
opcion3.place(x = 60, y = 360, relwidth = 0.75, relheight = 0.17)
opcion4.place(x = 60, y = 480, relwidth = 0.75, relheight = 0.17)
text_hora_salida.place(x = 60, y = 35, relwidth = 0.08, relheight = 0.13)
text_lugar_salida.place(x = 60, y = 60, relwidth = 0.08, relheight = 0.15)
text_hora_llegada.place(x = 400, y = 35, relwidth = 0.08, relheight = 0.13)
text_lugar_llegada.place(x = 400, y = 60, relwidth = 0.08, relheight = 0.15)
text_desde.place(x = 500, y = 33, relwidth = 0.19, relheight = 0.33)
text_precio.place(x = 640, y = 65, relwidth = 0.08, relheight = 0.076)
text_flechita.place(x = 140, y = 42, relwidth = 0.35, relheight = 0.1)
boton_eleccion1.place(relx = 0.9, rely = 0.28, anchor = "center")
boton_eleccion2.place(relx = 0.9, rely = 0.48, anchor = "center")
boton_eleccion3.place(relx = 0.9, rely = 0.68, anchor = "center")
boton_eleccion4.place(relx = 0.9, rely = 0.88, anchor = "center")

root.mainloop()