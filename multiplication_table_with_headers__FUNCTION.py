'''Written by:
A Module for printing the multiplication table of any given size

Name:  pupil-Engr. Dabak, Aaron Yildong
Date:  6th January 2020
Phone: +234 9036951421
Email: dabakaaron@gmail.com

'''
    
        
       
        

def header():
    
    global size
    #request table size from the user
    size=int(input('please enter the Table size: '))
    #print head  of all columns
    print('   ',end='')
    for column in range(1,size+1):
        print('{0:5}'.format(column),end='')
    #go to next line..  print dashes

    print() #.......GO_TO_NEXT_LINE
    print('   +',end='')
    for column in range(1, size+1): #........DASHES.......z
        print('-----',end='')

def multiply():
     print()  #....... NEXT_LINE
     for row in range(1,size+1):
        print('{0:2} |'.format(row),end='')
        #print()
        for column in range(1,size+1):
            product=row*column
            print('{0:5}'.format(product),end='')
        print()

print('This is the handwork of bobs')

    
        
        

header()
multiply()

    
        
