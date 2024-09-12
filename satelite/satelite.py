
def main():
    x=int(input('ingrese altitud inicial en km '))
    y=float(input('coeficiente de arrastre '))
    z=float(input('altitud minima de seguridad '))
    orbitas=0
    while x>z:
        a=x*y
        b=x-a
        y=y+1e-5
        orbitas=orbitas+1
        print(f'para la orbita {orbitas} se descencieron {a} km, su altitud final es {b} km y su nuevo coeficiente de arrastre es {y}')
        if z>=b:
            break
    print('simulacion finalizada, el satelite se desintegró')


if __name__ == "__main__":
    main()
