def conta_vogais(frase):
    vogais = 'aeiouAEIOU'
    contador = 0
    for char in frase:
        if char in vogais:
            contador += 1
    return contador
print(conta_vogais("Viviane"))