def restou():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, raiting=0):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = raiting

        def describe_restaurant(self):
            print(f"Ресторан {self.restaurant_name} специализируется на {self.cuisine_type} кухне Рейтинг: {self.raiting} ")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт!")

        def up_raiting(self, new_raiting):
            if 0 <= new_raiting <= 5:
                self.raiting = new_raiting
                print(f"Рейтинг ресторана {self.restaurant_name} успешно обновлен! Новый рейтинг: {self.raiting}")
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


restou()
