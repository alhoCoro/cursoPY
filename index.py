
nome = str(input("Digite o nome do aluno: "))
b1 = float(input("Nota da primeira prova: "))
b2 = float(input("Nota da segunda prova: "))
b3 = float(input("nota da terceira prova: "))
b4 = float(input("nota da quarta prova: "))
media = (b1+b2+b3+b4)/4
print(f"sua média foi de: {media}")
if media < 20:
    {
        print("Reprovado! Se esforce mais!")
    }
if media >= 20:
    {
        print("Parabéns, você passou!")
    }
