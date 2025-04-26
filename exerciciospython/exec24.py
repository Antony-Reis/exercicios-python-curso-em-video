city = input('O nome da sua cidade: ')
cityup = city.strip().upper()
citylist = cityup.split()

if 'SANTO' in citylist[0] or 'SANTOS' in citylist[0]:
    print(f'{"".join(city)} começa sim')
else:
    print('nahh')