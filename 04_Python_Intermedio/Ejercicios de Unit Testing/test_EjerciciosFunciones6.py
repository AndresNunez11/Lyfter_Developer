from EjerciciosFunciones6class import alphabetic_order

def test_alphabetic_order_big_strig_return_sort_words():
    #Arrange
    input_string ="zapato-arbol-mesa-computadora-avion-libro-casa-elefante-banana-gato-perro-ventana-escuela-telefono-naranja-bicicleta-sol-luna-mar-montana-camisa-reloj-puerta-flor-jardin-cuchara-tenedor-plato-vaso-cafe-pan-queso-leche-arroz-fruta-rio-playa-arena-piedra-musica-pelicula-juego-pelota-balon-futbol-correr-saltar-nadar-caminar-amigo-familia-escuchar-hablar-escribir-leer-dibujar-pintar-cocinar-viajar-trabajo-oficina-empresa-proyecto-reunion-programa-codigo-python-java-servidor-internet-teclado-pantalla-raton-impresora-carro-autobus-tren-barco-doctor-hospital-salud-cancion-primavera-verano-otono-invierno-lluvia-nube-viento-trueno-estrella-planeta-universo-energia-tiempo-espacio-naturaleza-desierto-volcan-funcion-variable-metodo-clase-objeto"
    sort_string ="amigo-arbol-arena-arroz-autobus-avion-balon-banana-barco-bicicleta-cafe-caminar-camisa-cancion-carro-casa-clase-cocinar-codigo-computadora-correr-cuchara-desierto-dibujar-doctor-elefante-empresa-energia-escribir-escuchar-escuela-espacio-estrella-familia-flor-fruta-funcion-futbol-gato-hablar-hospital-impresora-internet-invierno-jardin-java-juego-leche-leer-libro-lluvia-luna-mar-mesa-metodo-montana-musica-nadar-naranja-naturaleza-nube-objeto-oficina-otono-pan-pantalla-pelicula-pelota-perro-piedra-pintar-planeta-plato-playa-primavera-programa-proyecto-puerta-python-queso-raton-reloj-reunion-rio-saltar-salud-servidor-sol-teclado-telefono-tenedor-tiempo-trabajo-tren-trueno-universo-variable-vaso-ventana-verano-viajar-viento-volcan-zapato"
    #Act
    Result = alphabetic_order(input_string)
    #Assert
    assert Result == sort_string

def test_alphabetic_order_small_strig_return_sort_words():
    #Arrange
    input_string = "zebra-arbol-casa"
    sort_string = "arbol-casa-zebra"
    #Act
    Result = alphabetic_order(input_string)
    #Assert
    assert Result == sort_string

def test_alphabetic_order_sort_strig_return_sort_words():
    #Arrange
    input_string = "banana-manzana-uva"
    sort_string = "banana-manzana-uva"
    #Act
    Result = alphabetic_order(input_string)
    #Assert
    assert Result == sort_string
