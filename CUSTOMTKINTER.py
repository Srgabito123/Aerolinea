from tkinter import *
import customtkinter

root = customtkinter.CTk()
root.geometry("1000x600")
root.resizable(0,0)
root.title("Condor")
#--------------------------------------------funciones------------------------------------------
def eleccion_vuelo():
    if frame_eleccion_vuelo.winfo_viewable():
        frame_eleccion_vuelo.place_forget()
    else:
        frame_eleccion_vuelo.place(relx=0.5, rely=0.45, anchor="n")

#----------------------------------------------letra--------------------------------------------

font_1 = customtkinter.CTkFont(family="Inherit", size=18, weight="bold")

#----------------------------------------------frames-------------------------------------------

frame_principal = customtkinter.CTkFrame(master = root, width=750, height=600,corner_radius=10, 
                fg_color="light pink", border_color="white", border_width=2)
frame_principal.place(relx = 0.25, rely = 0.5, anchor="w")

frame_menu = customtkinter.CTkFrame(master = root,width=250, height=600,corner_radius=10, 
                fg_color="beige", border_color="white", border_width=2)
frame_menu.place(relx = 0, rely = 0.5, anchor="w")

frame_eleccion_vuelo = customtkinter.CTkFrame(master = frame_principal, width=700, height=300, corner_radius=32, 
                fg_color="white")
frame_eleccion_vuelo.place_forget()

frame_aluminio = customtkinter.CTkFrame(master = frame_eleccion_vuelo, width=200, height=250, corner_radius=32, 
                fg_color="light green", border_color="white", border_width=2)
frame_aluminio.place(relx = 0.3, rely = 0.5, anchor = "e")

#----------------------------------------------botones------------------------------------------

# bnt = customtkinter.CTkButton(master = frame_principal, text="Realizar Check-In", corner_radius=32, fg_color="transparent",
#                 hover_color="light blue", border_color="white", border_width=2, text_color="black",
#                 font= font_1)
# bnt.place(relx = 0.5, rely = 0.8, anchor = "s")

boton_avion1 = customtkinter.CTkButton(master = frame_principal,text="Avion 1", font=font_1, text_color="black",
                width=700, height=120, corner_radius=32, fg_color="white", command=eleccion_vuelo, cursor="hand2",
                hover_color="light blue")
boton_avion1.place(relx = 0.5, rely = 0.33, anchor = "center")

#----------------------------------------------labels--------------------------------------------
aluminio = customtkinter.CTkLabel(master = frame_aluminio, text="Aluminio", font=font_1, text_color="black")
aluminio.place(relx = 0.5, rely = 0.1, anchor = "n")


root.mainloop()