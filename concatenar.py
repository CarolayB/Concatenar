# Defino una variable de cada tipo de primitivo
string = "Hola, soy una cadena"
entero = 10
flotante = 15.5
booleano = True #False

# Concateno a la cadena las otras variables aplicando la conversión correcta para funcionar
resultado_string = string + " " + str(entero) + " " + str(flotante) + " " + str(booleano)

# Investigo sobre el límite de los enteros y los flotantes en python
# El límite de los enteros en Python es -9223372036854775808 a 9223372036854775807
# El límite de los flotantes en Python es aproximadamente 1.8e308

# Aplico la fórmula de la suma de los primeros n números pares
# La fórmula es: n*(n+1)
# Tomo como n la variable de tipo entero
resultado_suma = entero * (entero + 1)

# Imprimo los resultados de las tareas anteriores
print(resultado_string)
print(resultado_suma)