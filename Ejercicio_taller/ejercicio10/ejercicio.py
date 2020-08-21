
suspendidos = 0
aprobados = 0
alumnos = int(input("Alumnos  "))
cont = 1

while cont <= alumnos:
    notas = int(input(f"nota del \"alumno{cont}\"?: "))
    if (notas >= 5):
        aprobados += 1
    else:
        suspendidos += 1
    cont += 1

print(f"\nAlumnos aprobados: {aprobados} =)")
print(f"Alumnos suspensos: {suspendidos} sigue intentando")