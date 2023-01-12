from datetime import date
 


pesels = ['90040735138',
'01291813874',
'77061959752',
'55042939393',
'60041526172',
'70012731322',
'87021178411',
'49082775987',
'99111153859',
'00211100157']

def how_old(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


def pesel_to_age(pesel):

    if int(pesel[2]) > 1:
        year = int('20' + pesel[:2])

        month = int(pesel[2:4])-20
    else:
        year = int('19' + pesel[:2])
        if pesel[2] != '0':
            month = int(pesel[2:4])
        else:
            month = int(pesel[3])
        
    if pesel[4] != '0':
        day = int(pesel[4:6])
    else:
        day = int(pesel[5])
    
    print(str(year) +' '+ str(month) +' '+ str(day))
        
    return how_old(date(year, month, day))

for p in pesels:
    age = pesel_to_age(p)
    print(age)

    