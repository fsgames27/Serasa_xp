programa {
   cadeia resposta
  funcao inicio() {
    acesso() //Iniciar� apenas a primeira fun��o aos outras iram se integrar sozinhas 
  }
  funcao acesso(){
   inteiro tabela
    escreva(" BEM VINDO A CL�NICA Pet-Repet \n 1- Cadastro \n 2-Convers�o de anos caninos em Humanos \n 3-Finalizar Progama \n (Digite um numero pra ter acesso ao que deseja) \n\n ")
    leia(tabela)

    enquanto( tabela >= 4){ // Caso o usuario decida escolher outro numero al�m de 1 e 2
    // Loop
      escreva(" Escolha um desses numeros ( 1-2)")
      leia(tabela)
      pare
    }

    escolha(tabela){ // Ap�s selecionar um dos numeros ele ser� levado pra outra fun��o 
    //Condicional
      caso 1 :
      cadastro()
      pare

      caso 2:
      agendamento()
      pare
      
      caso 3 :
      escreva("Progama Finalizado")
    }
  }

  funcao cadastro(){
     cadeia vetor[] = { "Animal:" , "Nome do animal: ", "Voc� possui carteira de vacina��o?: ", "Ra�a: ", "idade: "}
     //vetor
   
   escreva( "Preencha apartir da ordem do cadastro \n" , vetor[0], "\n", vetor[1], "\n", vetor[2], "\n", vetor[3], "\n",  vetor[4], "\n")
   escreva("Agora escreva na mesma ordem \n \n")

   para (inteiro posicao = 0; posicao < 5; posicao++)// Loop para que seja feitos todas as perguntas e salvas em "Respostas"
		{
      
			escreva(vetor[posicao])
      leia(resposta)
		}

    escreva(" Seu cadastro foi salvo com sucesso \n Voltando ao in�cio")


    acesso()// Novamente voltando pro In�cio pra caso ele decida fazer outra fun��o
  }
  funcao agendamento(){
     real idade_H , idade_P

     escreva("Digite a idade do animal em anos: ")
     leia(idade_P)

     se(idade_P <= 2 ){
      idade_H = idade_P * 12
     }
     senao{
      idade_H = 24 + (idade_P - 2) * 4
     }

     escreva("A idade equivalente em anos humanos �: ", idade_H)
     escreva("\t \n Voltando para o menu principal \n \n")

     acesso()
  }

}
