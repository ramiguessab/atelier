import customtkinter


def disco(root):
    app = customtkinter.CTk()
    app.title("Disconnect?")
    app.geometry("550x150")
    app.resizable(False, False)

    def yes():
        app.destroy()
        root.destroy()
    def no():
        app.destroy()

    dis = customtkinter.CTkLabel(app, text="Do you want to disconnect?", font=("Madimi One Regular", 18)).grid(row=0, column=3)
    yes = customtkinter.CTkButton(app, text="YES",
                                       font=("Madimi One Regular", 18),
                                    border_width=1,
                                    border_color="white",
                                  fg_color="#9C5F40",
                                  hover_color="#663D29",
                                       command=yes).grid(row=1, column=2)
    no = customtkinter.CTkButton(app, text="NO",
                                      font=("Madimi One Regular", 18),
                                 border_width=1,
                                 border_color="white",
                                      command=no).grid(row=1, column=4, padx=20)

    app.grid_rowconfigure(1, weight=3)
    app.grid_columnconfigure(1, weight=5)

    app.mainloop()
