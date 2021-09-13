
import string
import cowsay
import random
i = 0
while i <= 1:
    if (i == 0):
        chs = random.choice( [ True,False ] )
        if(chs == True):
            coin = 'Heads'
        else:
            coin = 'Tails'
        cowsay.stimpy("It's " + coin)
        
        cond = str(input('\nDo u want to flip again ?\n Type "y/n"\n->').lower())
        if cond == 'y':
            pass
        else:
            print('Gracias')
            break
