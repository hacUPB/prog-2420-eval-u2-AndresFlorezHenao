
def main():
    import random
    from os import system
    import calendar
    from datetime import datetime
    x=['bogota','cartagena','medellin']
    ñ=['a','b','c']
    n=['señor','señora']
    control=True
    while control==True:
        print(" 1. reservar un vuelo\n 2. salir")
        opcion=int(input("ingrese su opcion "))
        system("cls")
        if opcion==1:
            cont=5
            while cont>4:
                    y=input('escriba su genero(señor o señora): ')
                    y=y.lower()
                    if y in n:
                        cont=cont-1
                    if y not in n:
                        print('aunque hallan mas de dos generos por simplicidad escoja si es señor o señora')
                        cont=cont
            y=y.capitalize()
            system("cls")
            z=input('escriba su nombre: ')
            z=z.capitalize()
            system("cls")
            a=input('escriba su apellido: ')
            a=a.capitalize()
            system("cls")
            print(f'Bienvenido a Aviancol {y} {z} {a} ')
            while cont>3:
                    b=input(f'ingrese su ciudad de origen entre {x} ')
                    b=b.lower()
                    if b in x:
                        cont=cont-1
                    if b not in x:  
                        print('ciudad de origen no disponible, llegara proximamente!')
                        cont=cont
            system("cls")
            while cont>2:
                    c=input(f'ingrese su ciudad de destino entre {x} ')
                    c=c.lower()
                    if c in x:
                        cont=cont-1   
                    if c not in x:
                        print('ciudad de destino no disponible, llegara proximamente!')
                        cont=cont
            system("cls")
            if b==c:
                    print('no necesitas viajar :)')
            else:
                    if b=='bogota' and c=='medellin' or b=='medellin' and c=='bogota':
                        f=240
                    if b=='medellin' and c=='cartagena' or b=='cartagena' and c=='medellin':
                        f=461
                    if b=='bogota' and c=='cartagena' or b=='cartagena' and c=='bogota':
                        f=657
                    while cont>1:
                        year=int(input("ingrese su año de viaje: "))
                        if year>2023:
                            cont=cont-1
                        else:
                            print("año del pasado")
                            cont=cont
                    # Generar calendario del año
                    print(calendar.calendar(year))
                    fecha_entrada = input("Introduce una fecha en formato DD/MM/AAAA: ")
        
                    # Convertir la entrada en un objeto de fecha
                    fecha_seleccionada = datetime.strptime(fecha_entrada, "%d/%m/%Y")
                
                    # Comprobar si el día es lunes (0), martes (1), miércoles (2) o jueves (3)
                    if fecha_seleccionada.weekday() in [0, 1, 2, 3] and f<400: 
                        i=79900
                    if fecha_seleccionada.weekday() in [0, 1, 2, 3] and f>400:
                        i=119000
                    if fecha_seleccionada.weekday() in [4, 5, 6] and f<400:
                        i=156900
                    if fecha_seleccionada.weekday() in [4, 5, 6] and f>400:
                        i=213000
                    while cont>0:
                        j=input('ingrese su asiento de preferencia ente (A,B,C), recuerde que A es ventana, C es pasillo y B es silla del centro: ')
                        j=j.lower()
                        if j in ñ:
                            cont=cont-1
                        if j not in ñ:
                            print('silla no valida')
                        cont=cont
                    system("cls")
                    v=random.randint(1,30)
                    b=b.capitalize()
                    c=c.capitalize()
                    print(f'Tu vuelo de {b} a {c} el {fecha_entrada} está reservado.')
                    print(f'Precio del tiquete: {i}cop')
                    j=j.upper()
                    print(f'Tu asiento es: {v}{j}')
        if opcion==2:
                control=False
                print("¡GRACIAS POR VOLAR CON AVIANCOL!")
    

if __name__ == "__main__":
    main()
