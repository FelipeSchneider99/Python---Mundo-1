var = input("Digite algo: ")
print("O tipo primitivo desse valor é {}".format(type(var)),
    "\nSó tem espaços? {}".format(var.isspace()),
    "\nÉ um numero? {}".format(var.isnumeric()),
    "\nÉ alfabetico? {}".format(var.isalpha()),
    "\nÉ alfanumerico: {}".format(var.isalnum()),
    "\nEstá em maiusculas? {}".format(var.isupper()),
    "\nEstá em minusculas? {}".format(var.islower()),
    "\nEsta capitalizada? {}".format(var.istitle()))