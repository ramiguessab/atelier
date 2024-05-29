import customtkinter


def edithisto(root):
    root = customtkinter.CTk()

    def exit():
        root.destroy()

    root.title("L'historique des revenus du patient")
    root.geometry("500x600")
    root.resizable(False, False)
    ("icons/edit.ico")
    frame = customtkinter.CTkFrame(root, height=500, width=450)
    mod = customtkinter.CTkButton(
        root,
        text="Modifier",
        font=("Madimi One Regular", 18),
        fg_color="#FFC552",
        hover_color="#A8833A",
        border_width=2,
        border_color="white",
        text_color="black",
    )
    ok = customtkinter.CTkButton(
        root,
        text="Ok",
        font=("Madimi One Regular", 18),
        command=exit,
        fg_color="#FFC552",
        hover_color="#A8833A",
        border_width=2,
        border_color="white",
        text_color="black",
    )
    mod.grid(row=1, column=0, padx=(30, 150), pady=20)
    ok.grid(row=1, column=0, padx=(180, 0), pady=20)
    frame.grid(row=0, column=0, sticky="nsew", padx=(25, 0), pady=(25, 0))
    root.mainloop()
