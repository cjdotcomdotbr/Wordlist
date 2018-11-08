from itertools import product
from time import asctime, time
import sys
from os import path

print('''
################ EXEMPLOS DE USO #########################
#                                                        #
#>> Entre com os caracteres para combinação: ABCabc123@;.#
#>> Entre com a quantidade de caracteres: 8              #
#>> Entre com o nome do arquivo: wordlist.txt            #
#                                                        #        
##########################################################
''')
input('Pressione enter...')

#Aqui começa a solicitação de requisitos
print('')
chrs = input('[*] Entre com os caracteres para combinação >> ')
print('')
try:
    l = int(input('[*] Entre com a quantidade minima de caracteres >> '))
    k = l
except:
    print('\033[1;31mQUANTIDADE MINIMA INVALIDA')
    exit()
print('')
try:
    j = int(input('[*] Entre coma a quantidade maxima de caracteres >> '))
except:
    print('\033[1;31mQUANTIDADE MAXIMA INVALIDA')
    exit()
print('')
qtchrs = len(chrs)
p = []
#Nome do arquivo
zt = input('[*] Entre com o nome do arquivo >> ')
#Fim

#Calculando o numero de combinações(linhas)
for y in range(k, j+1):
    ans = qtchrs**y
    p.append(ans)
tline=sum(p)

print(f'[*] Numero de linhas: {tline}')

go = input("\n[*] Começar?(Enter/N) >> ").upper()

#Inicio do programa
while True:
    if go == 'N':
        break
    time1 = asctime()
    start = time()

    #Criando o arquivo
    wlist = open(zt, 'a')

    #Percentual do processo e definindo combinações
    for i in range(k, j+1):
        r = (i*100)/j+1
        l = r
        sys.stdout.write(f'\nProgresso: {l:.2f}%')
        sys.stdout.flush()
        wlist.flush()
        for x in product(chrs, repeat=i):
            wlist.write(''.join(x)+'\n')
    wlist.flush()
    wlist.close()

    print('''\n\n
*************************************************
*              CRIADO COM SUCESSO               *
*************************************************
''')

    print(f"\n{'*'*20}RELATÓRIO{'*'*21}")
    print(f'\t [*] Inicio: {time1}')
    end=time()
    print(f'\t [*] Conclusão: {asctime()}')
    totaltime = end-start
    print(f'\t [*] Tempo total: {totaltime:.2f} segundos')
    rate = totaltime/tline
    print(f'\t [*] Taxa de combinações por segundo: {rate:.2f}')
    print(f'\t [*] Tamanho: {path.getsize(zt)} Bytes')
    print(f"{'*'*50}")
    break
