from smartphone import Smartphone

catalog = [
    Smartphone("Nokia", "3310", "+79785553535"),
    Smartphone("Samsung", "Galaxy S50", "+79165478521"),
    Smartphone("Apple", "iPhone 14", "+79562157889"),
    Smartphone("Xiaomi", "Redmi Note 5", "+79562157889"),
    Smartphone("Tecno", "Spark S10", "+79562157889")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
