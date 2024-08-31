inicio

    leer alt_inici  //variable entera
    leer coef_ar    //variable de punto flotante
    alt_min         //variable de punto flotante
    definir contador orbita=0
    mientras alt_inici>alt_min       //inicio del bucle
        calcular alt_des= alt_inici*coef_ar
        calcular alt_postorbit=alt_inici-alt_des
        coerf_ar=coef_ar+1e-5
        orbitas=orbitas+1
        imprimir ' para la orbita {orbita} se descendieron {alt_des}km, su alt final es {alt_posorbit} y su nuevo coef de arraste es{coef_ar}' //impresion de datos
        si alt_min>=alt_posorbit:       //condicional para poder finalizar el bucle y decir que se el satelite traspaso el lim de seguridad
            romper //finalizacion
    imprimir 'simulacion finalizada
