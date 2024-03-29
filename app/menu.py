import tkinter as tk
from tables import Application
import splash_screen

def main():
    root = tk.Tk()
    menu_page(root)
    root.mainloop()

def settings():
    # Логика для перехода на страницу settings()
    pass

def about():
    # Логика для перехода на страницу about()
    pass


def open_tables(master):
    # Создание окна таблиц при нажатии кнопки
    root_tables = tk.Toplevel(master)
    root_tables.title("Tables Page")

    # Создание экземпляра класса Application из файла tables.py
    app_tables = Application(master=root_tables)
    app_tables.pack(expand=True, fill='both')  # Подгонка виджета по размерам окна
    app_tables.mainloop()  # Запуск цикла для отображения окна


def menu_page(root):
    menu = root
    menu.title("Main Page")

    width_of_window = 800
    height_of_window = 800
    screen_width = menu.winfo_screenwidth()
    screen_height = menu.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (width_of_window / 2)
    y_coordinate = (screen_height / 2) - (height_of_window / 2)
    menu.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))

    frame = tk.Frame(menu, width=450, height=450, bg='#E7F1FD')
    frame.place(x=0, y=0)

    # Создание кнопок меню
    btn_main = tk.Button(frame, text='Main', command=main)
    btn_main.grid(row=0, column=0, sticky="w")

    btn_settings = tk.Button(frame, text='Settings', command=settings)
    btn_settings.grid(row=1, column=0, sticky="w")

    btn_about = tk.Button(frame, text='About', command=about)
    btn_about.grid(row=2, column=0, sticky="w")

    btn_tables = tk.Button(frame, text='Tables', command=lambda: open_tables(menu))
    btn_tables.grid(row=3, column=0, sticky="w")


# Запуск приложения
if __name__ == "__main__":
    main()
