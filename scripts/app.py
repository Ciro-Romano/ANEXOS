import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("ANEXOS")
        self.geometry("1200x1000")

        # TITULO
        titulo = ctk.CTkLabel(
            self,
            text="Generador de Modulos",
            font=("Arial", 28, "bold"),
        )
        titulo.pack(pady=30)

        # FRAME PRINCIPAL
        frame = ctk.CTkFrame(self)
        frame.pack(padx=30, pady=20, fill="both", expand=True)

        # RAZON SOCIAL
        self.label_empresa = ctk.CTkLabel(
            frame,
            text="Razon Social"
        )
        self.label_empresa.pack(pady=(20, 5))

        self.entry_empresa = ctk.CTkEntry(
            frame,
            width=400
        )
        self.entry_empresa.pack()

        # CUIT
        self.label_cuit = ctk.CTkLabel(
            frame,
            text="C.U.I.T"           
        )
        self.label_cuit.pack(pady=(20, 5))

        self.entry_cuit = ctk.CTkEntry(
            frame,
            width=400
        )
        self.entry_cuit.pack()

        #convenio
        self.label_convenio = ctk.CTkLabel(
            frame,
            text="Convenio"
        )
        self.label_convenio.pack(pady=(20, 5))
        
        self.combo_convenio = ctk.CTkComboBox(
            frame,
            values=[
                "86/89",
                "321/75",
                "402/05",
                "375/04",
            ],
            width=250
        )
        self.combo_convenio.pack()

        # DESDE
        self.label_desde = ctk.CTkLabel(
            frame,
            text="Desde (YYYY-MM)"
        )
        self.label_desde.pack(pady=(20, 5))

        self.entry_desde = ctk.CTkEntry(
            frame,
            placeholder_text="2020-01",
            width=150,
        )
        self.entry_desde.pack()

        # HASTA
        self.label_hasta = ctk.CTkLabel(
            frame,
            text="Hasta (YYYY-MM)"
        )
        self.label_hasta.pack(pady=(20, 5))

        self.entry_hasta = ctk.CTkEntry(
            frame,
            placeholder_text="2020-01",
            width=150,
        )
        self.entry_hasta.pack()

        # BOTON
        self.boton_generar = ctk.CTkButton(
            frame,
            text="Generar",
            command=self.generar_modulo,
            height=40,
            width=200,
        )
        self.boton_generar.pack(pady=30)

    def generar_modulo(self):

        empresa = self.entry_empresa.get()
        cuit = self.entry_cuit.get()
        convenio = self.combo_convenio.get()
        desde = self.entry_desde.get()
        hasta = self.entry_hasta.get()

        info = F"""
            Empresa     :   {empresa}
            CUIT        :   {cuit}  
            Convenio    :   {convenio}
            Desde       :   {desde}
            Hasta       :   {hasta}
            """
        
        messagebox.showinfo(
            "Datos Cargados",
            info
        )

if __name__ == "__main__":
    app = App()
    app.mainloop()