def restou():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating=0):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def describe_restaurant(self):
            print(f"Ресторан {self.restaurant_name} специализируется на {self.cuisine_type} кухне Рейтинг: {self.rating} ")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт!")

        def up_rating(self, new_rating):
            if 0 <= new_rating <= 5:
                self.rating = new_rating
                print(f"Рейтинг ресторана {self.restaurant_name} обновлен! Новый рейтинг: {self.rating}")
            else:
                print("Рейтинг только от 0 до 5")
    newRestaurant = Restaurant("Токио-Сити", "универсальной", 5)
    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)
    newRestaurant.up_rating(4)
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

    restaurant1 = Restaurant("Recolte", "европейская", 2)
    restaurant2 = Restaurant("El Celler de Can Roca", "испанская", 5)
    restaurant3 = Restaurant("The Lobby Bar", "русская и европейская", 1)

    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()


    class IceCreamStand:
        def __init__(self, name, cuisine_type, flavors, location, working_hours):
            super().__init__(name, cuisine_type)
            self.location = location
            self.working_hours = working_hours
            self.flavors = flavors

        def add_flavor(self, new_flavor):
            if new_flavor not in self.flavors:
                self.flavors.append(new_flavor)

        def remove_flavor(self, old_flavor):
            if old_flavor in self.flavors:
                self.flavors.remove(old_flavor)

        def has_flavor(self, target_flavor):
            return target_flavor in self.flavors

        # Методы для разных типов мороженого будут реализованы аналогично
        # Например, метод для мороженого на палочке может выглядеть так:
        def stick_ice_cream(self):
            pass

        # Метод для мягкого мороженого:
        def soft_ice_cream(self):
            pass

    # Пример использования класса IceCreamStand
    cafe_location = "ул. Авиаторов Балтики, д. 10"
    working_hours = "Пн-Вс: 10:00 - 22:00"
    ice_creamm = IceCreamStand("Baskin Robbins", "мороженое", ["ванильное", "шоколадное"],
                                    cafe_location, working_hours)

    print("Локация:", ice_creamm.location)
    print("Время работы:", ice_creamm.working_hours)
    print("Сорта мороженого: ", ice_creamm.flavors)

    # Добавление нового сорта мороженого
    ice_creamm.add_flavor("банановое")
    print("Новый сорт мороженого добавлен: ", ice_creamm.flavors)

    # Удаление старого сорта мороженого
    ice_creamm.remove_flavor("ванильное")
    print("Старый сорт мороженого удален: ", ice_creamm.flavors)

    # Проверка наличия сорта мороженого
    if ice_creamm.has_flavor("шоколадное"):
        print("Мороженое 'Шоколадное' присутствует в меню.")
    else:
        print("Мороженое 'Шоколадное' отсутствует в меню.")


    ice_creamm.stick_ice_cream()
    ice_creamm.soft_ice_cream()

restou()



import tkinter as tk
from tkinter import messagebox


'''class IceCreamStand(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Кафе-мороженое')

        self.menu_frame = tk.Frame(self)
        self.menu_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.create_menu()

        self.status_bar = tk.Frame(self)
        self.status_bar.pack(side=tk.RIGHT, fill=tk.Y)

        self.create_status_bar()

    def create_menu(self):
        self.menu_buttons = {}
        for i, flavor in enumerate(['ванильное', 'шоколадное', 'клубничное']):
            button = tk.Button(self.menu_frame, text=flavor, command=lambda f=flavor: self.order_ice_cream(f))
            button.grid(row=i, column=0, sticky=tk.W + tk.E)
            self.menu_buttons[flavor] = button

    def order_ice_cream(self, flavor):
        messagebox.showinfo(title='Ваш заказ', message=f'Вы заказали мороженое "{flavor}"')

    def create_status_bar(self):
        self.status_label = tk.Label(self.status_bar, text="Ваше любимое мороженое?", bd=1, relief=tk.SUNKEN,
                                     anchor=tk.W)
        self.status_label.pack(fill=tk.X)


def main():
    app = IceCreamStand()
    app.mainloop()


if __name__ == '__main__':
    main()'''