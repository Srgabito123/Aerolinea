import customtkinter as ctk
from PIL import Image, ImageTk

#SE CREA LA VENTANA 2 Y SE BLOQUEA SU TAMAÑO
ventana2 = ctk.CTk()
ventana2.resizable(0, 0)

#FRAME PRINCIPAL
frame1 = ctk.CTkFrame(ventana2, 
                      fg_color = "#d7bb9f", 
                      width = 860, 
                      height = 400, 
                      border_color = "beige", 
                      border_width = 4).place(x = 70, y = 70)

borde_desplegable = ctk.CTkFrame(ventana2, 
                      fg_color = "#d7bb9f",
                      bg_color = "#d7bb9f", 
                      width = 147.9, 
                      height = 35, 
                      border_color = "#a06553", 
                      border_width = 3,
                      corner_radius = 3).place(x = 97, y = 115)

borde_personas = ctk.CTkFrame(ventana2, 
                      fg_color = "#d7bb9f",
                      bg_color = "#d7bb9f", 
                      width = 77, 
                      height = 56, 
                      border_color = "#a06553", 
                      border_width = 3,
                      corner_radius = 3).place(x = 797, y = 96.8)

borde_origen = ctk.CTkFrame(ventana2, 
                      fg_color = "#d7bb9f",
                      bg_color = "#d7bb9f", 
                      width = 156, 
                      height = 50, 
                      border_color = "#a06553", 
                      border_width = 3,
                      corner_radius = 3).place(x = 97, y = 241)

borde_destino = ctk.CTkFrame(ventana2, 
                      fg_color = "#d7bb9f",
                      bg_color = "#d7bb9f", 
                      width = 156, 
                      height = 50, 
                      border_color = "#a06553", 
                      border_width = 3,
                      corner_radius = 0).place(x = 250, y = 241)

linea_divisora = ctk.CTkFrame(ventana2, 
                      fg_color = "#d7bb9f", 
                      width = 860, 
                      height = 12,
                      corner_radius = 0,
                      border_color = "beige", 
                      border_width = 4).place(x = 70, y = 190)



#SE CONSIGUE EL TAMAÑO DE LA PANTALLA Y SE GUARDA EN UNA VARIABLE LAS MEDIDAS DE VENTANA
screen_width = ventana2.winfo_screenwidth()
screen_height = ventana2.winfo_screenheight()
window_width = 1000
window_height = 600

#SE CALCULA EL CENTRO
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

#SE DA ATRIBUTOS A LA VENTANA
ventana2.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
ventana2.config(background="#d7bb9f")
ventana2.title("Mapaula airline")

#CREACIÓN DEPLEGABLE OPCIONES IDA O IDA Y VUELTA
opciones_ida_vuelta = ["Solo ida", "Ida y vuelta"] #Valores
valor_idavuelta = ctk.StringVar() #Tipo de variable
valor_idavuelta.set(opciones_ida_vuelta[0]) #Valor por defecto
desplegable_ida_vuelta = ctk.CTkOptionMenu(ventana2, 
                                        variable = valor_idavuelta, 
                                        values = opciones_ida_vuelta,
                                        font=("Poppins", 16),
                                        text_color = "brown",
                                        bg_color = "#a06553",
                                        fg_color = "beige",
                                        cursor = "hand2",
                                        button_color = "beige",
                                        button_hover_color = "#a06553",
                                        dropdown_font = ("Poppins", 16),
                                        dropdown_text_color = "brown",
                                        dropdown_hover_color = "#a06553",
                                        dropdown_fg_color = "beige",
                                        corner_radius = 2)

desplegable_ida_vuelta.place(x = 100, y = 118)

#CREACIÓN CONTENEDOR PARA CAJA DE TEXTO E ICONO
entry_frame = ctk.CTkFrame(ventana2, 
                           fg_color="beige",
                           bg_color="#d7bb9f", 
                           corner_radius = 2,
                           border_width = 3, 
                           border_color = "beige")
entry_frame.place(x = 800, y = 100)

#CREAR CAJA DE TEXTO
entry_personas = ctk.CTkEntry(entry_frame, 
                     width = 40,  
                     height = 50,  
                     fg_color="beige", 
                     border_width=0, 
                     font=("Poppins", 14, "bold"))
entry_personas.grid(row=0, column=1, sticky="nsew", padx=(0, 5))

#IMPORTACIÓN Y POSICIONAMIENTO DE LA IMAGEN
icon_image = Image.open("D:/GABO/2024/UNIVERSIDAD/SEMESTRE 1/FUNDAMENTOS DE PROGRAMACIÓN IMPERATIVA/PROYECTO FINAL/Repositorio/PERSONAS.png")
icon_image = icon_image.resize((20, 20), Image.Resampling.LANCZOS)
icon_photo = ImageTk.PhotoImage(icon_image)

icon_personas_label = ctk.CTkLabel(entry_frame, 
                                   image=icon_photo, 
                                   text="", 
                                   fg_color="beige",
                                   height = 30)
icon_personas_label.grid(row=0, column=0, sticky="nsew", padx=(5, 0))

ciudades_origen = ["Bogotá", "Medellin", "Santa Marta", "Cali", "Cartagena"] 
valor_origen = ctk.StringVar() 
valor_origen.set(ciudades_origen[0]) 
opciones_origen = ctk.CTkOptionMenu(ventana2, 
                                        variable = valor_origen, 
                                        values = ciudades_origen,
                                        width = 150,
                                        font=("Poppins", 16),
                                        text_color = "brown",
                                        bg_color = "beige",
                                        fg_color = "beige",
                                        cursor = "hand2",
                                        button_color = "beige",
                                        button_hover_color = "#a06553",
                                        dropdown_font = ("Poppins", 16),
                                        dropdown_text_color = "brown",
                                        dropdown_hover_color = "#a06553",
                                        dropdown_fg_color = "beige",
                                        corner_radius = 2)
origen_label = ctk.CTkLabel(ventana2, 
                            text = "Origen",
                            width = 150,
                            height = 16,
                            font=("Poppins", 12), 
                            text_color = "brown",
                            fg_color = "beige", 
                            bg_color = "#d7bb9f",
                            anchor = "w").place(x = 100, y = 244)

opciones_origen.place(x = 100, y = 260)


ciudades_destino = ["Bogotá", "Medellin", "Santa Marta", "Cali", "Cartagena"] 
valor_destino = ctk.StringVar() 
opciones_destino = ctk.CTkOptionMenu(ventana2, 
                                        variable = valor_destino, 
                                        values = ciudades_destino,
                                        width = 150,
                                        font=("Poppins", 16),
                                        text_color = "brown",
                                        bg_color = "beige",
                                        fg_color = "beige",
                                        cursor = "hand2",
                                        button_color = "beige",
                                        button_hover_color = "#a06553",
                                        dropdown_font = ("Poppins", 16),
                                        dropdown_text_color = "brown",
                                        dropdown_hover_color = "#a06553",
                                        dropdown_fg_color = "beige",
                                        corner_radius = 2)
destino_label = ctk.CTkLabel(ventana2, 
                            text = "Destino",
                            width = 150,
                            height = 16,
                            font=("Poppins", 12), 
                            text_color = "brown",
                            fg_color = "beige", 
                            bg_color = "#d7bb9f",
                            anchor = "w").place(x = 253, y = 244)

opciones_destino.place(x = 253, y = 260)

ventana2.mainloop()