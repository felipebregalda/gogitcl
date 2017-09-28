#-*- coding utf-8 -*-
from funcoes import notaFinal

print 'Calculo de notas do Aluno\n'

nome = raw_input ('Nome: ')
nota1 = float( raw_input('Nota 1: '))
nota2 = float( raw_input('Nota 2: '))

notaFinal = notaFinal(nota1, nota2)
print 'Nota final do aluno',nome,'eh',notaFinal