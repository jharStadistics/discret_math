# this program calculates a sequence of numbers
#if the first contestant ate one hotdog, the second 3 three hotdogs. a contenstant ate two more 
# than the previous one
def hotdogsNumber(num):
    return 1+(num-1)*2

def howManyHotdogs(n):
    num =0
    for i in range(1,n+1):
        num += 1+(i-1)*2
    return num    

hotdogs =int(input('enter the hotdog eater: '))
print(f'the contenstant number {hotdogs} ate {hotdogsNumber(hotdogs)} hotdogs')
print(f'the hotdogs sum {howManyHotdogs(hotdogs)}')
