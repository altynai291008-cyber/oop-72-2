data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
designations=[]
codes=[]
for element in data:
    if element.isdigit():
        codes.append(element)
    else:
        designations.append(element)
print(codes)
print(designations)

новый_список = [ {code} for code in codes ]
print(новый_список)
ответ=dict(zip(designations, новый_список))
print(ответ)
del ответ['Katel' ]
del ответ['Fonex' ]
print(ответ)
ответ["Beeline"].add('665')
ответ["Beeline"].add('667')
print(ответ)
ответ["O!"].add('888')
ответ["O!"].add('777')
ответ["Megacom"].add('543')
ответ["Megacom"].add('222')
print(ответ)
for operator, code in ответ.items():
    print(f"{operator} - {code}")