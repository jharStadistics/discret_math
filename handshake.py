#this program calculates the handshake number among any persons number 
def handshake(persons):
    return int((persons-1)*(persons/2))

persons = int(input('enter the persons number which do handshake: '))
print(f'the handshake number is {handshake(persons)}')