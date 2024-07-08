VLANNum = int(input("Cual es el número de VLAN? "))
if VLANNum >= 1 and VLANNum <= 1005:
    print("Esta VLAN se trata de una VLAN de rango estandar.")
elif VLANNum >=1006 and VLANNum <= 4094:
    print("Esta VLAN se trata de una VLAN de rango extendido")
else:
    print("Esta VLAN no pertenece a ningun grupo.")