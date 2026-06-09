def se(condicao, valor_verdadeiro, valor_se_falso):
    return (valor_verdadeiro if condicao else valor_se_falso)

alunos = [
    ("joão", 30),
    ("felipe", 38),
    ("emily", 52),
    ("leo", 67),
    ("carlos", 75),
    ("pedro", 55),
    ("maria", 97),
]

print(f"{'ALUNO':^15} {'NOTA':^6} {'SITUAÇÃO':^12}")
print("-" * 38)

aprovados = []
recuperacao = []
reprovados = []

for nome, nota in alunos:
    situacao = se(nota >= 70, "APROVADO", se(nota >= 50, "RECUPERAÇÃO", "REPROVADO"))

    print(f"{nome:^15} {nota:^6} {situacao:^12}")

    if nota >= 70:
        aprovados.append((nome, nota))
    elif nota >= 50:
        recuperacao.append((nome, nota))
    else:
        reprovados.append((nome, nota))

print("-" * 38)
print("\n----BOLETIM ESCOLAR-----\n")

print("APROVADOS:")
for nome, nota in aprovados:
    print(f"   {nome} - Nota: {nota}")

print("\nRECUPERAÇÃO:")
for nome, nota in recuperacao:
    print(f"   {nome} - Nota: {nota}")

print("\nREPROVADOS:")
for nome, nota in reprovados:
    print(f"   {nome} - Nota: {nota}")

print("-" * 38)