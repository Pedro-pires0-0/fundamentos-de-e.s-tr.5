print('ola gostaria de saber qual sua media de notas ')
num_de_notas = int(input('quantas notas vc tem? '))
nota = 0
for i in range (num_de_notas):
    nota = float(input('qual a sua nota ? '))
    media = (nota + nota) / num_de_notas

print(f'sua média de notas é {media}')
