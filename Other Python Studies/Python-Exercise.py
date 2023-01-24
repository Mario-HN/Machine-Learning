
#MARIO HADDAD NETO
#1)
# -Na programação, a recursividade é uma utilidade que permite a uma função 
# chamar a si mesma direta ou indiretamente, sendo assim, a função é dita 
# recursiva se ela contém, no mínimo, uma chamada explícita ou implícita a 
# si própria. 

# -Computação Lazy é um padrão de projeto de software, normalmente usado em linguagens, 
# para adiar a inicialização de um objeto até o ponto em que ele é necessário.
# Isso pode ajudar a melhorar o funcionamento do programa, se utilizado da forma correta.

# -Os Monads são uma especificação ─ um conjunto de normas ─ que permite controlarmos a ordem e a 
# dependência de computações em linguagens funcionais e possuirmos algo relativamente próximo aos 
# statements ou afirmações das linguagens imperativas.

# -Um efeito colateral pode referir-se à modificação de algum estado - por exemplo: alterando
# o valor de uma variável, gravando dados em disco, ativando ou desativando o botão na interface 
# do usuário. Ou seja, quando há uma ação planejada ou não que foi ocasionada por algo dentro do código.

#2)
# List Comprehension é uma forma eficiente e rápida de criar
# uma lista a partir de outra lista. Sendo da sua implementação 
# simplificada em apenas uma linha, este método torna-se uma 
# forma bem interessante de ser utilizada, também é um método de
# fácil interpretação além se dar pela forma que é
# construída, por exemplo: 
# [expressão for cada elemento in lista de valores if condição].

#3)
#a)
def nresto(x, l):
    if(l[0]==x):
        return l[1:]
    else:
        return nresto(x,l[1:])

#b)
def subseq(l,x,y):
    if(l[0]==x):
        k = [i for i in l if i<=y]
        return k
    else:
        return subseq(l[1:],x,y)

#c)
import numpy as np
def mult_todos_pares(l):
    l = [j for sublista in l for j in sublista]
    k = [i for i in l if i%2==0]
    if k==[]:
        return 1
    else:
        return np.prod(k)
