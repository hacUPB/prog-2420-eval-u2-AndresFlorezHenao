Inicio

    importar modulo random
    definir lista_1= [cartagena, Bogota, Medellin]
    definir lista_2= [lunes, martes, miercoles, jueves]
    definir lista_3= [viernes, sabado, domingo]
    escribir genero "señor o señora" 
    leer genero   //cadea
    leer nombre
    leer apellido
    print Bienvenido a Aviancol genero nombre y apellido
    leer ciudad_de_origen
    leer ciudad_de_destimo
    leer dia_semana
    leer dia_mes
    si ciudad_de_origen=ciudad_de_destimo:
        imprimir 'no necesitas viajar'
    si no:
        si ciudad_de_origen=='bogota' and ciudad_de_destimo=='medellin' or ciudad_de_origen=='medellin' and ciudad_de_destimo=='bogota':
            distancia=240
        si ciudad_de_origen=='medellin' and ciudad_de_destimo=='cartagena' or ciudad_de_origen=='cartagena' and ciudad_de_destimo=='medellin':
            distancia=461
        si ciudad_de_origen=='bogota' and ciudad_de_destimo=='cartagena' or ciudad_de_origen=='cartagena' and ciudad_de_destimo=='bogota':
            distancia=657
        si dia_semana está en lista_2 y la distancia<400:
            precio=79900
        si dia_semana está en lista_2 y la distancia>400:
            precio=119000
        si dia_semana está en lista_3 y la distancia<400:
            precio=156900
        si dia_semana está en lista_3 y la distancia>400:
            precio=213000
    asiento= 'ingrese su asiento de preferencia ente (A,B,C), recuerde que A es ventana, C es pasillo y B es silla del centro: '
    fila=random.randint(1,30)
    imprimir 'Tu vuelo de {ciudad_de_origen} a {ciudad_de_destimo} el {dia_semana} {dia_mes} de abril está reservado.'
    imprimir 'Precio del tiquete: {precio}cop'
    imprimir 'Tu asiento es: {fila}{asiento}'
fin

