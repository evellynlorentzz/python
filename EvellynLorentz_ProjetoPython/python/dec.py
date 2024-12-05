texto = "oi"
texto2 = str("oi")
numero = 3
numero2 = int(3)
numero3 = 3.0
numero4 = float(3)
print(texto)
print(texto2)
print(numero)
print(numero2)
print(numero3)
print(numero4)
"\n"
val_Feijão = float(input("Qual é o valor do kilo de feijão?"))
qtd_Feijao = int(input("Quantos pacotes de feijão?"))
tot_Feijao = val_Feijão * qtd_Feijao 
print("O valor total dos feijões: ", tot_Feijao)
"\n"
#programa 1)
numero = int(input("Digite um número inteiro: "))
quadrado = numero ** 2
print(f"O quadrado de {numero} é {quadrado}.")
"\n"
#programa 2)
numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite um numero: "))
print(f"Os numeros foram '{numero1}' e '{numero2}'!")
"\n"
#programa 3)
numero = int(input("Digite um número inteiro: "))

antecessor = numero - 1
sucessor = numero + 1

print("O antecessor de", numero, "é", antecessor)
print("O sucessor de", numero, "é", sucessor)
"\n"
#programa 4)
base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

perimetro = 2 * (base + altura)
area = base * altura

print("O perímetro do retângulo é:", perimetro)
print("A área do retângulo é:", area)
