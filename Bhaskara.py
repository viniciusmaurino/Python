Exercício Equação Segundo Grau
#usuário informando os dados
coef_a = int(input("Digite o valor do coeficiente A da equação: "))

#não prosseguir enquanto usuário não digitar valor diferente de zero
while (a = 0):
	coef_a = int(input("Digite um número inteiro diferente de zero! "))

coef_b = int(input("Digite o valor do coeficiente B da equação: "))
coef_c = int(input("Digite o valor do coeficiente C da equação: "))

#cálculo do delta
delta = b**2 – 4*a*c
raiz_delta = delta ** 0,5

#cálculo das raízes
x1 = (-b + raiz_delta) / 2*a
x2 = (-b - raiz_delta) / 2*a

#exibição do resultado
print("As raízes da equação são: ", x1, " e ", x2)
