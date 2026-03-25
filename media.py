print('Olá! Gostaria de saber qual a sua média de notas?')
num_de_notas = int(input('quantas notas vc tem? '))
total = 0.0
nota = 0.0
for i in range(num_de_notas):
    nota = float(input('qual a sua nota? '))
    total += nota
media = total / num_de_notas

print(f'sua média de notas é {media}')
