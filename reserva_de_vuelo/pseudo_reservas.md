Inicio

    definir lista= [cartagena, Bogota, Medellin]
    definir lista= [lunes, martes, miercoles, jueves]
    definir lista= [viernes, sabado, domingo]
    escribir genero "señor o señora" 
    leer genero
    leer nombre
    leer apellido
    print Bienvenido a Aviancol genero nombre y apellido
    leer ciudad_de_origen
    leer ciudad_de_destimo
    leer dia_semana
    leer dia_mes
    



b=input(f'ingrese su ciudad de origen entre {x}')
b=b.lower()
c=input(f'ingrese su ciudad de destino entre {x}')
c=c.lower()
d=input('ingrese el dia de su viaje (por ejemplo: lunes)')
d=d.lower()
e=int(input('ingresese su dia del mes (1-30)'))
if b==c:
    print('no necesitas viajar :)')
else:
    if b=='bogota' and c=='medellin' or b=='medellin' and c=='bogota':
        f=240
    if b=='medellin' and c=='cartagena' or b=='cartagena' and c=='medellin':
        f=461
    if b=='bogota' and c=='cartagena' or b=='cartagena' and c=='bogota':
        f=657
    if d in g and f<400:
        i=79900
    if d in g and f>400:
        i=119000
    if d in h and f<400:
        i=156900
    if d in h and f>400:
        i=213000
    j=input('ingrese su asiento de preferencia ente (A,B,C), recuerde que A es ventana, C es pasillo y B es silla del centro: ')
    j=j.upper()
    v=random.randint(1,30)
    print(f'Tu vuelo de {b} a {c} el {d} {e} de abril está reservado.')
    print(f'Precio del tiquete: ${i}')
    print(f'Tu asiento es: {v}{j}')
