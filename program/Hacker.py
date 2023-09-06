import phonenumbers
from phonenumbers import geocoder
phone_number1=phonenumbers.track("+918618325621")
phone_number2=phonenumbers.track("+916303482074")

print("\n phone Numbers location\n")
print(geocoder.description_for_number(phone_number1,"en"))
print(geocoder.description_for_number(phone_number2,"en"))
print(phonenumbers)