from imports import *


class Table(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief="groove")
        self.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)
        self.create_table_widgets()

        self.editing_entry = None  # Для хранения виджета Entry

    def create_table_widgets(self):
        columns = ("Лексема", "Морфологическая информация", "Частота появления")
        self.table = ttk.Treeview(master=self, columns=columns, show="headings")
        self.table.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.table.heading("Лексема", text="Лексема")
        self.table.heading("Морфологическая информация", text="Морфологическая информация")
        self.table.heading("Частота появления", text="Частота появления")

        self.table.column("Лексема", stretch=False, width=200)
        self.table.column("Морфологическая информация", stretch=False, width=200)
        self.table.column("Частота появления", stretch=False, width=200)

        # Добавляем начальные записи
        self.table.insert("", "end", values=("Example", "Noun", "5"))
        self.table.insert("", "end", values=("Test", "Verb", "3"))
        self.table.insert("", "end", values=("Sample", "Adjective", "4"))

        # Привязываем событие двойного щелчка
        self.table.bind("<Double-1>", self.on_double_click)

    def on_double_click(self, event):
        # Получаем выбранный элемент
        selected_item = self.table.selection()
        if selected_item:
            item = self.table.item(selected_item)
            column = self.table.identify_column(event.x)
            col_index = int(column.replace('#', '')) - 1  # Индекс колонки

            # Получаем координаты ячейки
            x, y, width, height = self.table.bbox(selected_item, column)

            # Создаем Entry для редактирования
            self.editing_entry = tk.Entry(self)
            self.editing_entry.insert(0, item['values'][col_index])
            self.editing_entry.place(x=x, y=y, width=width, height=height)
            self.editing_entry.focus()

            # Устанавливаем обработчик для сохранения изменений
            self.editing_entry.bind("<Return>", lambda e: self.save_changes(selected_item, col_index))
            self.editing_entry.bind("<FocusOut>", lambda e: self.cancel_edit(selected_item))

    def save_changes(self, selected_item, col_index):
        new_value = self.editing_entry.get()
        current_values = list(self.table.item(selected_item)['values'])
        current_values[col_index] = new_value
        self.table.item(selected_item, values=current_values)
        self.editing_entry.destroy()

    def cancel_edit(self, selected_item):
        if self.editing_entry:
            self.editing_entry.destroy()