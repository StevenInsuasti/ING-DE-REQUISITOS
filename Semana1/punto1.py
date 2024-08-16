print ("base_triangulo")
base_triangulo= input ("ingrese base del triangulo: ")
print ("altura_triangulo")
altura_triangulo= input ("ingrese altura del triangulo: ")
"-------------------------------------------------------------------"
print ("base_rectangulo")
base_rectangulo= input ("ingrese la base del rectangulo: ")
print ("altura_rectangulo")
altura_rectangulo= input ("ingrese la altura del rectangulo: ")

print ("area_triangulo")
area_triangulo= int (base_triangulo)* int (altura_triangulo)/2

print ("area_rectangulo")
area_rectangulo= int (base_rectangulo)* int (altura_rectangulo)

print ("area_terreno")
area_terreno= area_triangulo+area_rectangulo

print(area_terreno)
