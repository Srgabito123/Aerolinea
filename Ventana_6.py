from customtkinter import *
#ventana 6
root = CTk()
root.title("CONDOR")
root._set_appearance_mode("light")
root.geometry("1000x600")
root.resizable(0,0)
root.config(bg = "light pink")
root.iconbitmap("logo.ico")
#---------------------------VARIABLES---------------------------
hora_llegada = "13:00"
hora_salida = "10:00"
lugar_salida = "Bogotá"
lugar_llegada = "Cartagena"
ida = f"Ida: {lugar_salida} - {lugar_llegada}"
precio = "2.000.000"
fecha = "2024-06-13"
flechita = "-------------------------------------->"
#---------------------------FRAMES---------------------------
frame_viaje = CTkFrame(master = root, 
                       fg_color="white", 
                       bg_color = "light pink",  
                       corner_radius = 10, 
                       width = 0.11, 
                       height = 0.065, 
                       )
frame_opciones = CTkFrame(master = root, 
                       fg_color="transparent",
                       bg_color = "light pink",  
                       width = 0.7, 
                       height = 0.2
                       )
opcion1 = CTkFrame(master = frame_opciones, 
                   bg_color = "light pink", 
                   width = 0.9, 
                   height = 0.2, 
                   corner_radius = 30,
                   fg_color = "beige"
                          )
#---------------------------TEXTOS---------------------------
text_viaje = CTkLabel(master= root, 
                      text = ida, 
                      fg_color = "beige", 
                      width = 0.9, 
                      height = 0.7, 
                      text_color = "black", 
                      font = ("roboto", 12),  
                      bg_color = "light pink",
                      corner_radius = 10
                      )
text_hora_salida = CTkLabel(master = frame_opciones, 
                            text = hora_salida,
                            fg_color = "beige",
                            text_color = "black",
                            font = ("roboto", 18),
                            width = 0.1,
                            height = 0.3,
                            corner_radius = 10,
                            bg_color = "beige"
                            )
text_hora_llegada = CTkLabel(master = frame_opciones, 
                            text = hora_llegada,
                            fg_color = "beige",
                            text_color = "black",
                            font = ("roboto", 18),
                            width = 0.1,
                            height = 0.3,
                            corner_radius = 10,
                            bg_color = "beige"
                            )
text_lugar_salida = CTkLabel(master = frame_opciones, 
                            text = lugar_salida,
                            fg_color = "Beige",
                            text_color = "black",
                            font = ("roboto", 13),
                            width = 0.1,
                            height = 0.3,
                            corner_radius = 10,
                            bg_color = "beige"
                            )
text_lugar_llegada = CTkLabel(master = frame_opciones, 
                            text = lugar_llegada,
                            fg_color = "Beige",
                            text_color = "black",
                            font = ("roboto", 13),
                            width = 0.1,
                            height = 0.3,
                            corner_radius = 10,
                            bg_color = "beige"
                            )
text_desde = CTkLabel(master = frame_opciones,
                      text = """DESDE:

                         COP $""",
                      fg_color = "beige",
                      text_color = "black",
                      font = ("roboto", 11),
                      width = 0.1,
                      height = 0.3,
                      corner_radius = 10,
                      bg_color = "beige"
                      )
text_precio = CTkLabel(master = frame_opciones, 
                       text = precio, 
                       fg_color = "beige", 
                       text_color = "black", 
                       font = ("roboto", 11), 
                       width = 0.1, 
                       height = 0.3, 
                       corner_radius = 10, 
                       bg_color = "beige"
                       )
text_flechita = CTkLabel(master = frame_opciones,
                        text = flechita,
                        fg_color = "beige",
                        text_color = "black",
                        font = ("roboto", 20),
                        width = 0.3,
                        height = 0.3,
                        bg_color = "beige"
                        )
text_reserva = CTkLabel(master = root,
                        text = f"Total de la reserva: COP ${precio}",
                        fg_color = "light pink",
                        text_color = "black",
                        font = ("roboto", 20),
                        width = 0.3,
                        height = 0.3,
                        bg_color = "light pink",
                        corner_radius = 10
                        )
#---------------------------BOTONES---------------------------
boton_seleccionar = CTkButton(master = root,
                               text = "SELECCIONAR",
                               fg_color = "beige",
                               text_color = "black",
                               font = ("roboto", 12),
                               width = 0.3,
                               height = 0.3,
                               corner_radius = 10,
                               bg_color = "beige"
                               )
#---------------------------POSICIONAMIENTO-----------------------
frame_viaje.place(x = 6, y = 5, relwidth = 0.3, relheight = 0.065)
text_viaje.place(x = 6, y = 5, relwidth = 0.3, relheight = 0.065)
frame_opciones.place(x = 50, y = 110, relwidth = 0.9, relheight = 0.3)
opcion1.place(x = 90, y = 22.4, relwidth = 0.8, relheight = 0.66)
text_hora_salida.place(x = 110, y = 60, relwidth = 0.08, relheight = 0.07)
text_lugar_salida.place(x = 110, y = 85, relwidth = 0.08, relheight = 0.085)
text_hora_llegada.place(x = 440, y = 60, relwidth = 0.08, relheight = 0.07)
text_lugar_llegada.place(x = 440, y = 85, relwidth = 0.08, relheight = 0.085)
text_desde.place(x = 525, y = 50, relwidth = 0.19, relheight = 0.2)
text_precio.place(x = 665, y = 76, relwidth = 0.08, relheight = 0.057)
text_flechita.place(x = 196, y = 60, relwidth = 0.265, relheight = 0.1)
boton_seleccionar.place(x = 830, y = 480, relwidth = 0.1, relheight = 0.06)
text_reserva.place(x = 50, y = 480, relwidth = 0.35, relheight = 0.07)
root.mainloop()