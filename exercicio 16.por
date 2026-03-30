programa
{
	funcao inteiro somar(inteiro v1,inteiro v2){ 
		inteiro resultado= v1+v2


	retorne resultado

	}
	
funcao inteiro subtrair(inteiro v1,inteiro v2){ 
		inteiro resultado= v1-v2


	retorne resultado}
	funcao inteiro multiplicar(inteiro v1,inteiro v2){ 
		inteiro resultado= v1*v2


	retorne resultado}
	
	funcao inteiro dividir(inteiro v1,inteiro v2){ 
		inteiro resultado= v1/v2


	retorne resultado}

	
	funcao inicio()
	{inteiro num1, num2
	caracter operacao
	  escreva("Escreva qual operação matematica vc qr?\n")
	  escreva("+ para soma , - para subtrair , x para multiplicar , / para dividir:  ")
	  leia (operacao)

	  escreva("Numero:")
	  leia(num1)

	  escreva("Numero:")
	  leia(num2)

	  

	  se(operacao=='+'){
	  	escreva(somar(num1,num2))
	  }
	  senao se(operacao=='-'){
	  	escreva(subtrair(num1,num2))
	  }
	  senao se(operacao=='x'){
	  	escreva(multiplicar(num1,num2))
	  }
	   senao se(operacao=='/'){
	  	escreva(dividir(num1,num2))
	  }
	  
	  
	

	
	
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 751; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */