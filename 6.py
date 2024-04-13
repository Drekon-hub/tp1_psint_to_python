    # Un profesor desea saber qué porcentaje de hombres y qué porcentaje de mujeres hay en un grupo de estudiantes.

def porcentaje():
    h = int(input('Ingrese la cantidad de hombres: '))
    m = int(input('Ingrese la cantidad de mujeres: '))
    porcentaje_h = (h / (h + m)) * 100
    porcentaje_m = (m / (h + m)) * 100
    print(f'El porcentaje de hombres es de {porcentaje_h:.2f}% y el porcentaje de mujeres es {porcentaje_m:.2f}%') #eso que pongo despues del procentaje_m '.2f' es para que los decimales no pasen las dos cifras 

porcentaje()