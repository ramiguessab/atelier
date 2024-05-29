import customtkinter


class CTkTable(customtkinter.CTkFrame):
    def __init__(self, master, columns: list[str], rows: list[dict]):
        super().__init__(master=master)
        self.columns = columns

        self.selected_value = customtkinter.StringVar()

        for index, column in enumerate(columns):
            customtkinter.CTkLabel(master=self, text=column).grid(
                row=0, column=index + 1, padx=8, pady=8
            )

        for row_index, row in enumerate(rows):
            customtkinter.CTkRadioButton(
                master=self,
                text="",
                variable=self.selected_value,
                width=16,
                value=row["id"],
            ).grid(row=row_index + 1, column=0, padx=8, pady=8)
            for column_index, column in enumerate(row.values()):
                customtkinter.CTkLabel(master=self, text=column).grid(
                    row=row_index + 1, column=column_index + 1, padx=8, pady=8
                )
