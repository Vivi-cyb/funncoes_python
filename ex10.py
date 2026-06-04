def login (usuario, senha):
    """Função que recebe um nome de usuário e uma senha e verifica se as credenciais são válidas."""
    """Args:
        usuario (str): O nome de usuário a ser verificado.
        senha (str): A senha a ser verificada.
    """
    if usuario == "admin" and senha == "1234":
        return "Login bem-sucedido!"
    else:
        return "Credenciais inválidas. Tente novamente."