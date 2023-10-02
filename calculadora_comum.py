
operacao = input("Digite a operacao desejada (Soma, Sub, Mult, Div): ")
numero1 = float( input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if operacao == "Soma":
	resultado = int(numero1) + int(numero2)
	print("O resultado da operação é: ", resultado)
if operacao == "Sub":
	resultado = int(numero1) - int(numero2)
	print("O resultado da operação é: ", resultado)
if operacao == "Mult":
	resultado = int(numero1) * int(numero2)
	print("O resultado da operação é: ",resultado)
if operacao == "Div":
	resultado = int(numero1) / int(numero2)
	print("O resultado da operação é: ", resultado)
else:
	resultado = "Operação não suportada"
    
print("O resultado da operação é: " + str(resultado))