#remove espaço e convertendo em maiúscula
Texto_limpo=replace(" ", "").Lowe()
#verificar se o texto é  igual ao seu inverso
if texto_limpo == texto_limpo[::-1]:
    print("O texto é um palíndromo.")
else:

    if __name__ == "__main__":
        print("O texto não é um palíndromo.")
        #saida:true
        