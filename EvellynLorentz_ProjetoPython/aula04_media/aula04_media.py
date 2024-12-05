valorUM = float(input("Insira um valor: "))
valorDois = float(input("Insira outro valor: "))
valorTres = float(input("Insira um valor: "))
valorQuatro = float(input("Insira outro valor: "))
media = float(valorUM + valorDois + valorTres + valorQuatro) / 4
print('Sua média é: ', media)
class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

if media <= 4:
    print(bcolors.RED + 'você foi reprovado, talvez na proxima' + bcolors.ENDC)

elif media <= 6:
    print(bcolors.YELLOW +'Você foi aprovado, regular' + bcolors.ENDC)


elif media <=8 :
    print(bcolors.GREEN + 'Você foi aprovado, bom!' + bcolors.ENDC)    

elif media <=10 :
    print(bcolors.BLUE + 'Você foi aprovado, execelente!' + bcolors.ENDC)
