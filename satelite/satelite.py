
def main():
    control=True
    while control==True:
        print("1. Hacer Simulacion\n2. Salir")
        opcion=int(input("ingrese la opcion que desea ejecutar "))
        if opcion==1:
            conta=1
            x=int(input('ingrese altitud inicial en km '))
            while conta>0:
                y=float(input('coeficiente de arrastre debe (estar entre 0 y 1) '))
                if 0<y<1:
                    conta=conta-1 
                elif y>1:
                    print("coeficiente no valido")
                    conta=conta
            z=float(input('altitud minima de seguridad '))
            orbitas=0
            while x>z:
                        a=x*y
                        b=x-a
                        y=y+1e-5
                        orbitas=orbitas+1
                        print(f'para la orbita {orbitas} se descencieron {a} km, su altitud final es {b} km y su nuevo coeficiente de arrastre es {y}')
                        if 0<a<0.0001:
                            print(f'simulacion finalizada, el satelite se estabilizo')
                            break
                        elif z>=b:
                            print(f'simulacion finalizada, el satelite se desintegró')
                            break
        if opcion==2:
            control=False
                


if __name__ == "__main__":
    main()
