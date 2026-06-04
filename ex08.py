def media_aritmetica (numeros):
    """Função que recebe uma lista de números e retorna a média aritmética."""
    """Args:
        numeros (list): Uma lista de números.
    """
    if len(numeros) == 0:
        return 0
    soma = sum(numeros)
    media = soma / len(numeros)
    return media #saida:20.0
