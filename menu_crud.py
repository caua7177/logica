import sqlite3

conn = sqlite3.connect("bd_senai")
cursor = conn.cursor()
cursor.execute("""
               
               CREATE TABLE IF NOT EXIST alunos (
               id INTEGRER PRYMARY KEY AUTOINCRIMENT,
               nome TEXT NOT NULL,
               nota INTEGRER
               )      
        """)
    
print("\n--- Adicionar novo aluno---")
nome_novo_aluno = input("Digite o nome do novo aluno ")
while True:
   try:
        nota_novo_aluno = int(input("digite do novo aluno:"))
        break
   except ValueError:
        print("Entrada invalida. Por favor digite um numero inteiro!")

cursor.execute("INSERT INTO alunos (nome,nota)VALUES(?,?)",
(nome_novo_aluno, nota_novo_aluno))

conn.commit()

print(f"aluno{nome_novo_aluno} com a nota {nota_novo_aluno} adicionado com sucesso ao banco de dados\n ")

print("===dados da tabela (sem ordenação)===\n")
cursor.execute("SELECT*FROM alunos")
alunos = cursor.fetchall()

for aluno in alunos:
    print(aluno)
    print("\n"+"="*20)
