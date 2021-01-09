def listarDespachos(despachos):
    print("\nDespachos: \n")
    for des in despachos:
        datos = "Cliente: {0} - Dirección: {1} - Ciudad: {2} - Telefono: {3} - Unidades: {4} - Observación: {5} - Fecha: {6}"
        print(datos.format(des[1], des[2], des[3], des[4], des[5], des[6], des[7]))
    print("")