print('-----------Calculadora Python-----------')

def funcSoma(numPrim, numSeg):
    total = numPrim + numSeg
    print(str(numPrim)+' + '+str(numSeg)+' = '+str(total))

def funcSub(numPrim, numSeg):
    total = numPrim - numSeg
    print(str(numPrim)+' - '+str(numSeg)+' = '+str(total))

def funcDiv(numPrim, numSeg):
    total = numPrim / numSeg
    print(str(numPrim)+' / '+str(numSeg)+' = '+str(total))

def funcMult(numPrim, numSeg):
    total = numPrim * numSeg
    print(str(numPrim)+' * '+str(numSeg)+' = '+str(total))

print()
print('Qual o peração você gostaria de realizar?')
print()
print('1 - soma')
print('2 - subtração')
print('3 - divisão')
print('4 - multiplicação')
print()
 
saida = 'S'

while saida == 'S':

    operacao = input('Digite o número da operação: ')
    numPrim = int(input('Digite o primeiro número: '))
    numSeg = int(input('Digite o segundo número: '))

    if operacao == '1':

        funcSoma(numPrim,numSeg)

    elif operacao == '2':

        funcSub(numPrim,numSeg)

    elif operacao == '3':

        funcDiv(numPrim,numSeg)

    elif operacao == '4':

        funcMult(numPrim,numSeg)

    else:

        print('Digite uma operação valida!')

    saida = input('Deseja realizar outra operação? ( S / N )')
    


