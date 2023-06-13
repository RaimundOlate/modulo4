# Primera parte
class Vehiculo:
    def __init__(self, marca, modelo, nro_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, nro_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


class DatosAutomovil:
    def __init__(self, datosauto):
        self.datosauto = datosauto


n = int(input('¿Cuántos automóviles quiere ingresar? '))
autos_ingresados = []

for i in range(n):
    print(f'\nIngrese los detalles del automóvil {i+1}:')
    marca = input('Marca: ')
    modelo = input('Modelo: ')
    nro_ruedas = int(input('Numero de ruedas: '))
    velocidad = int(input('Velocidad: '))
    cilindrada = int(input('Cilindrada: '))

    auto = Automovil(marca, modelo, nro_ruedas, velocidad, cilindrada)
    datos_auto = DatosAutomovil(auto)
    autos_ingresados.append(datos_auto)

print('\nAutomóviles ingresados:')
for i, datos_auto in enumerate(autos_ingresados):
    print(f'\nDetalles del automóvil {i+1}:')
    print('Marca:', datos_auto.datosauto.marca)
    print('Modelo:', datos_auto.datosauto.modelo)
    print(datos_auto.datosauto.nro_ruedas, 'ruedas')
    print(datos_auto.datosauto.velocidad, 'Km/h')
    print(datos_auto.datosauto.cilindrada, 'cc')


class Automovil_Particular(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, nro_puesto):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.nro_puesto = nro_puesto


class DatosAutomovil_P:
    def __init__(self, datosauto_p):
        self.datosauto_p = datosauto_p


class Automovil_Carga(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, peso_carga):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.peso_carga = peso_carga


class DatosAutomovil_C:
    def __init__(self, datosauto_c):
        self.datosauto_c = datosauto_c


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, tipo):
        super().__init__(marca, modelo, nro_ruedas)
        self.tipo = tipo


class DatosBicicleta:
    def __init__(self, datosbicicleta):
        self.datosbicicleta = datosbicicleta


class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, nro_ruedas, tipo, nro_radios, cuadro, motor):
        super().__init__(marca, modelo, nro_ruedas, tipo)
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor


automovil_particular = Automovil_Particular('Ford', 'Fiesta', 4, 180, 500, 5)
automovil_carga = Automovil_Carga('Daft Trucks', 'G 38', 10, 120, 1000, 20000)
bicicleta = Bicicleta('Shimano', 'MT Ranger', 2, 'Carrera')
motocicleta = Motocicleta('BMW', 'F800s', 2, 'Deportiva', 2, 'Doble viga', 21)

# Mostrar detalles de los vehículos
vehiculos = [automovil_particular, automovil_carga, bicicleta, motocicleta]


def Imprimir_vehiculos_dados():
    print(f'\nAutomovil particular:\nMarca: {automovil_particular.marca}, '
          f'Modelo: {automovil_particular.modelo}, '
          f'Ruedas: {automovil_particular.nro_ruedas}, '
          f'Km/h: {automovil_particular.velocidad}, '
          f'cc: {automovil_particular.cilindrada}, '
          f'Puestos: {automovil_particular.nro_puesto}')
    print(f'\nAutomovil de carga:\nMarca: {automovil_carga.marca}',
          f'Modelo: {automovil_carga.modelo}',
          f'Ruedas: {automovil_carga.nro_ruedas}',
          f'Km/h: {automovil_carga.velocidad}',
          f'cc: {automovil_carga.cilindrada}',
          f'Capacidad de carga: {automovil_carga.peso_carga}')
    print(f'\nBicicleta:\nMarca: {bicicleta.marca}',
          f'Modelo: {bicicleta.modelo}',
          f'Ruedas: {bicicleta.nro_ruedas}',
          f'Tipo: {bicicleta.tipo}')
    print(f'\nMotocicleta:\nMarca: {motocicleta.marca}',
          f'Modelo: {motocicleta.modelo}',
          f'Ruedas: {motocicleta.nro_ruedas}',
          f'Tipo: {motocicleta.tipo}',
          f'Número radios: {motocicleta.nro_radios}',
          f'Cuadro: {motocicleta.cuadro}',
          f'Motor: {motocicleta.motor}')


Imprimir_vehiculos_dados()


instancia_vehiculo = isinstance(motocicleta, Vehiculo)
print(
    f"\nMotocicleta es instancia con relación a Vehiculo: {instancia_vehiculo}")


instancia_automovil = isinstance(motocicleta, Automovil)
print(
    f"Motocicleta es instancia con relación a Automovil: {instancia_automovil}")


instancia_particular = isinstance(motocicleta, Automovil_Particular)
print(
    f"Motocicleta es instancia con relación a Automovil_Particular: {instancia_particular}")


instancia_carga = isinstance(motocicleta, Automovil_Carga)
print(
    f"Motocicleta es instancia con relación a Automovil_Carga: {instancia_carga}")


instancia_bicicleta = isinstance(motocicleta, Bicicleta)
print(
    f"Motocicleta es instancia con relación a Bicicleta: {instancia_bicicleta}")


instancia_motocicleta = isinstance(motocicleta, Motocicleta)
print(
    f"Motocicleta es instancia con relación a Motocicleta: {instancia_motocicleta}")
