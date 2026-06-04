def contado_regressivo(n):
    """Função que recebe um número inteiro e exibe um contador regressivo a partir desse número até zero."""
    """Args:
        n (int): O número inteiro a partir do qual o contador regressivo começará.
    """
    for i in range(n, -1, -1):
        print(i)