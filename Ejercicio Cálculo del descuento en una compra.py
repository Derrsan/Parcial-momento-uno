monto_compra=int(input("Ingrese el monto de la compra"))
if(monto_compra<50):
    descuento1=monto_compra*0
    print(f"Descuento aplicado:${descuento1}")
    print(f"Total a pagar: ${monto_compra - descuento1}")
    
elif(50<=monto_compra<=100):
    descuento2=monto_compra*0.05
    print(f"Descuento aplicado:${descuento2}")
    print(f"Total a pagar:${monto_compra - descuento2}")    

    
elif(monto_compra>100):
    descuento3=monto_compra*0.1
    print(f"Descuento aplicado:${descuento3}")
    print(f"Total a pagar:${monto_compra - descuento3}")
