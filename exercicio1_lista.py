import random

print("\n"+"="*45)
print("EXERCICIO 02 - quem vai ao quadro ?")
print("="*45)

turma =[
    "Eduardo Sambay Cavalari",
    "Emily Pereira Doliveira",
    "Gabriel Santana Nadolny Pec",
    "João Pedro Albino Scotti",
    "Joaquim Bomfim Zacarias",
    "Matheus Alencar Do Nascimento",
    "Vinícius Carneiro Maciel",
    "Vitor Hugo Parnaiba Amorim",
    "Abiner Alves Paz",
    "Afonso Alves Takasugui Filho",
    "Alysson Del Rosal Pawlack",
    "Andrey Gonçalves Carneiro",
    "Antonio Gabriel Santos De Almeida",
    "Anuar Martins De Lima",
    "Carlos Eduardo Cidral De Siqueira",
    "Cauã Amaral Rocha",
    "Cauan Henrique Macedo Santos",
    "Daniel Dalla Rosa Dos Santos",
    "Eduardo Moreti Da Freiria",
    "Fabio Augusto Vaz",
    "Felipe Mello Pereira",
    "Felipe Reiz Navas",
    "Gabriel Junqueira Mamede",
    "Guilherme Mazzo Roberto",
    "Henrique Cochinski",
    "Henrique Portinho Nauiack",
    "Hilan Santos Teixeira De Paula",
    "Izadora Venâncio Prestes",
    "João Marcos Santos Rebá",
    "Leonardo Antonio Cruz",
    "Luis Eduardo De Aquino",
    "Marco Antonio De Souza Vitto",
    "Marcos Antonio Domingos Prina Junior",
    "Maria Clara Faustina Pereira",
    "Mateus André Staut",
    "Mateus Klinczak Belotti",
    "Pedro Henrique Silva Dos Santos",
    "Rodrigo Kamaroski Evangelista",
    "Vandré Luiz Barros Santana",
    "Wederson Ferreira Roberto"
]


random.shuffle(turma)

sorteado1=random.choice(turma)
turma.remove(sorteado1)
sorteado2=random.choice(turma)

print(f"1º sorteado: {sorteado1}")
print(f"2º sorteado:{sorteado2}")