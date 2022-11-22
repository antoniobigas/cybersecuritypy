###################
# pip3 install phonenumbers
###################

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

phone = input('Digite o telefone no formato: (+CountryCode)XXxxxxXXXX: ')
print()
try:
    phone_number = phonenumbers.parse(phone)
    print(phone_number)

    is_Valid = phonenumbers.is_valid_number(phone_number)
    is_Possible = phonenumbers.is_possible_number(phone_number)
    print(f'\n{phone} is_valid_number: {is_Valid}')
    print(f'{phone} is_possible_number: {is_Possible}')

    if is_Valid:
        # Indentificar regiao do numero de telefone:
        Region = geocoder.description_for_number(phone_number, 'pt')
        print(f'\nRegion: {Region}')

        operadora = carrier.name_for_number(phone_number, 'pt')
        if operadora != '':
            print(f'Operadora Original: {operadora}')

except:
    print('\n\tErro...')

print('#' * 60)
###################
# Exemplos de telefones:
# +16502230000	#Google
# +40721234567
# +551140028922
# +551100002222
###################