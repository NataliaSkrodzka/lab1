liczba1 = input('Wpisz liczbe: ')
liczba1 = int(liczba1)
dzialanie = input("""Wpisz znak +, -, * (mnozenie), / (dzielenie), // (dzielenie calkowite), 
% (reszta z dzielenia), ** (potega): """)
liczba2 = input('Wpisz liczbe: ')
liczba2 = int(liczba2)
if dzialanie == '+':
    print(liczba1 + liczba2)
elif dzialanie == '-':
    print(liczba1 - liczba2)
elif dzialanie == '*':
    print(liczba1 * liczba2)
elif dzialanie == '/':
    print(liczba1 / liczba2)
elif dzialanie == '//':
    print(liczba1 // liczba2)
elif dzialanie == '%':
    print(liczba1 % liczba2)
elif dzialanie == '**':
    print(liczba1 ** liczba2)
else:
    print("""Niepoprawny znak, wybierz sposrod podanych +, -, * (mnozenie), / (dzielenie), 
    // (dzielenie calkowite), % (reszta z dzielenia), ** (potega)""")


