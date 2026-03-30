programa
{
	funcao real prazo3(real entrega){
	real resultado = 25.0 + entrega
	
	retorne resultado
	}
	

	funcao real prazo5(real entrega){
		real resultado = 20.0 + entrega
	
	retorne resultado
	}
	

		funcao real prazo7(real entrega){
		real resultado = 15.0 + entrega
	
	retorne resultado
	}

		funcao real prazo10(real entrega){
		real resultado = 10.0 + entrega
	
	retorne resultado
	}
	


		
	funcao inicio()
	{
		inteiro dias 
		real valor 

		escreva("qual o valor da compra: ")
	leia(valor)

faca{
	escreva("quantos dias uteis vc deseja a entrega? ")
		escreva("3,5,7,10 dias uteis: ")
		leia(dias)

	

	se(dias==3){
		escreva(prazo3(valor))
	}

	se(dias==5){
		escreva(prazo5(valor))
	}

	se(dias==7){
		escreva(prazo7(valor))
	}

	se(dias==10){
		escreva(prazo10(valor))
	}
}
enquanto(dias !=3 e dias !=5 e dias != 7 e dias!=10)


}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 238; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */