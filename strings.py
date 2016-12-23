my_string = "Hola Mundo!"
my_string = """este es un string que contiene
            saltos de linea"""

course = "Python 3"
name = "David"

final_message = "Nuevo curso de " + course + " por " + name
final_message = "Nuevo curso de %s por %s" %(course, name)
final_message = "Nuevo curso de {} por {}".format(course, name)

print(my_string)
print(final_message)