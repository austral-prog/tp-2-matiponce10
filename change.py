def change():
    expense = 23.75
    money = 100
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print("")
    print("Vuelto")
    print("")
    diferencia = money - expense
    diferencia_entero = int(diferencia)
    print("Pesos:")
    print(diferencia_entero)
    print("Centavos:")
    print(int((diferencia % 1) * 100)) # 25
