''' 
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 
'''
n = int(input())

while(n > 0):
    a = int(input())
    b = int(input())

    length_a = len(str(a))
    length_b = len(str(b))

    if b > a:
        print("nao encaixa")
    else:
        difference = length_a - length_b
        a = str(a)
        b = str(b)

        if(a[difference:] == b[:]):
            print("encaixa")
        else:
            print("não encaixa")
    n -= 1