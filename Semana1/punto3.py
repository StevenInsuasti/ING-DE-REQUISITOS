print ("horas_trabajadas")
horas_trabajadas= input("ingrese las horas trabajadas: ")
print ("pago_hora")
pago_hora= input("ingrese el pago por las horas trabajadas al dia:")

pago_semanal= input ("valor pago semanal: ")

pago= round(int(horas_trabajadas)*pago_hora)
print (f"el pago es de {pago}")
