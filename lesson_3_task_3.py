from address import Address
from mailing import Mailing

to_address = Address("299054", "Симферополь", "Воровского", "кв.24", "кв.1")
from_address = Address("255461", "Краснодар", "Центральная", "д.12", "кв.25")
mailing = Mailing(from_address, to_address, "20000", "5250")

print(mailing)
