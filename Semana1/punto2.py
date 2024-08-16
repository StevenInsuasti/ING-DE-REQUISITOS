print ("leche producida en el dia")
leche_dia= input("ingresar cantidad de leche al dia: ")
print ("leche en galones")
leche_galones= int (leche_dia)* float (3.785)

pago_galones= input("Valor del galon: ")

pago=round(int(pago_galones)*leche_galones)
print (f"el pago es de {pago}")
