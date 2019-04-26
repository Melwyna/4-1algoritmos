from funciones11 import functions111
nl=[]
print("Cuando quiera terminar de ingresar valores a la lista digite 0")
while True:
 nn=int(input("ingrese los numero que quiere ingresar a la lista, los valores deben ser positivos:"))
 if nn!=0 and nn>0:
  nl.append(nn)
 else:
  print("la lista contiene:", nl)
  break
x=functions111.mayor(nl)
x2=functions111.menor(nl)
print("\n", "el valor mayor de la lista es:", x, "\n", "el valor menor de la lista es:", x2)