# Добавить добавление экземпляра героя


class Shop:
    def __init__(self):

        self.inventory_shop = {
            "slot_1": {},
            "slot_2": {},
            "slot_3": {},
            "slot_4": {},
            "slot_5": {},
            "slot_6": {},
            "slot_7": {},
            "slot_8": {},
            "slot_9": {},
            "slot_10": {},
            "slot_11": {},
            "slot_12": {},
            "slot_13": {},
            "slot_14": {},
            "slot_15": {},
            "slot_16": {},
            "slot_17": {},
            "slot_18": {},
            "slot_19": {},
            "slot_20": {},
            "slot_21": {},
            "slot_22": {},
            "slot_23": {},
            "slot_24": {},
            "slot_25": {},
            "slot_26": {},
            "slot_27": {},
            "slot_28": {},
            "slot_29": {},
            "slot_30": {},
            "slot_31": {},
            "slot_32": {},
            "slot_33": {},
            "slot_34": {},
            "slot_35": {},
            "slot_36": {},
        }

    # Добавление слотов

    def add_item(self, slot, item_name, item_price):
        if slot in self.inventory_shop:
            self.inventory_shop[slot] = {
                "name": item_name,
                "price": item_price,
            }
            print(f"Добавлен {item_name} в {slot} за {item_price} монет.")
        else:
            print("Указан неверный слот.")

    # Удаление слотов

    def delete_item(self, slot):
        if slot in self.inventory_shop:
            removed_item = self.inventory_shop[slot]
            if removed_item:
                self.inventory_shop[slot] = {}
                print(f"{removed_item['name']} был удален из {slot}.")
            else:
                print(f"{slot} пуст.")
        else:
            print("Указан неверный слот.")

    # Показывает слоты

    def show_items(self):
        print("Инвентарь магазина:")
        for slot, item in self.inventory_shop.items():
            if item:
                print(f"{slot}: {item['name']} - {item['price']} монет.")
            else:
                print(f"{slot}: пусто.")


# shop = Shop()
# shop.add_item("slot_1", "Зелье здоровья", 50)
# # shop.add_item("slot_2", "Меч", 150)
# shop.display_inventory()
# # shop.remove_item("slot_1")
# shop.display_inventory()
