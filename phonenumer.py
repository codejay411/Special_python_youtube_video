import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder

phone = phonenumbers.parse("+917510094565")

print(geocoder.description_for_number(phone, 'en'))
print(carrier.name_for_number(phone, 'en'))