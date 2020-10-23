print ('                   **************************')
print ('                   * Welcome to Frozen land *')
print ('                   **************************')

name = input('What is your name? ')
print ('Hello', name)
print ('')
are_you_ready = input('Are you ready to play? ').lower()
print ('')

ans_elsa = [] #Arendelle, olaf, carrot, summer, Marshmallow
ans_jasmine = [] #abu, agrabah, middle east, monkey, raja

################# Functions --> Start <--- ########################
def play_func():
    gametype = input('What you would like to play (Trivia or Mystery)? ').lower()
    print ('')

    if gametype == 'trivia':
        trivia_func()
    #elif re.findall("character",gametype) == 'character':
    elif gametype == 'mystery':
        mystery_func()
    else:
        print('Sorry cant play now')

def ans_chk_elsa():
    cnt = 0
    if ans_elsa[0] == 'arendelle':
        cnt +=1
    if ans_elsa[1] == 'olaf':
        cnt +=1
    if ans_elsa[2] == 'carrot':
        cnt +=1
    if ans_elsa[3] == 'summer':
        cnt +=1
    if ans_elsa[4] == 'marshmallow':
        cnt +=1 
    
    if cnt>3:
        print ('You got',cnt, 'points. Awesome!!!!')
        print('')
    elif cnt>1 and cnt<3:
        print ('You got',cnt, 'points. Not bad.')
        print('')
    else:
        print ('You got',cnt, 'points. You can do better than this.')
        print('')

def ans_chk_jasmine():
    cnt = 0
    if ans_jasmine[0] == 'abu':
        cnt +=1
    if ans_jasmine[1] == 'agrabah':
        cnt +=1
    if ans_jasmine[2] == 'middle east':
        cnt +=1
    if ans_jasmine[3] == 'monkey':
        cnt +=1
    if ans_jasmine[4] == 'raja':
        cnt +=1 
    
    if cnt>3:
        print ('You got',cnt, 'points. Awesome!!!!')
        print('')
    elif cnt>1 and cnt<3:
        print ('You got',cnt, 'points. Not bad.')
        print('')
    else:
        print ('You got',cnt, 'points. You can do better than this.')
        print('')

def mystery_func():
    print('I am under construction...')
    print('')
    continu = input('Would like to play Trivia for now (Yes/No)? ').lower()
    print('')
    if continu == 'yes':
        trivia_func()
    else:
        print('No problem. See you later. Take care')
    exit()

def trivia_func():

    #char_points = 0

    char = input('What is your fav character? ').lower()
    print ('')

    if char == 'elsa' or char == 'anna':
        print('Thats interesting. My fav character is also', char)
        print ('in elsa section')
        anna_elsa_func()
    elif char == 'jasmine':
        print('Thats interesting. My fav character is also', char)
        print ('in jasmine section')
        jasmine_func()
        #print('I am under construction too....')
        #exit()
    elif char == 'quit':
        exit()
    else:
        print ('')
        print ('----------------------------------------------------------------------------')
        print ('I am sorry. I can help only with Elsa/Anna or Jasmine. Have a wonderful day!')
        print ('----------------------------------------------------------------------------')
        print ('')
        exit()    

def anna_elsa_func():
    quest_elsa1 = input('In which kingdom do Anna and Elsa live? ').lower()
    print ('')
    ans_elsa.append(quest_elsa1)
    quest_elsa2 = input('Who likes “warm hugs”? ').lower()
    print ('')
    ans_elsa.append(quest_elsa2)
    quest_elsa3 = input('What is Sven’s favorite snack? ').lower()
    print ('')
    ans_elsa.append(quest_elsa3)
    quest_elsa4 = input('What is Olaf’s favorite season? ').lower()
    print ('')
    ans_elsa.append(quest_elsa4)
    quest_elsa5 = input('What is the name of the snow monster that Elsa creates in "Frozen"? ').lower()
    print ('')
    ans_elsa.append(quest_elsa5)
    #print (ans)
    ans_chk_elsa()

def jasmine_func(): 
    quest_jasmine1 = input('Who is Aladdins best friend and partner in crime? ').lower()
    print ('')
    ans_jasmine.append(quest_jasmine1)
    quest_jasmine2 = input('What is the town that Aladdin lives in called”? ').lower()
    print ('')
    ans_jasmine.append(quest_jasmine2)
    quest_jasmine3 = input('In what part of the world is the setting for the movie, Aladdin? ').lower()
    print ('')
    ans_jasmine.append(quest_jasmine3)
    quest_jasmine4 = input('What type of pet did Aladdin have? ').lower()
    print ('')
    ans_jasmine.append(quest_jasmine4)
    quest_jasmine5 = input('What is the name of Princess Jasmines tiger? ').lower()
    print ('')
    ans_jasmine.append(quest_jasmine5)
    #print (ans)
    ans_chk_jasmine()
################# Functions --> End <--- ########################

if are_you_ready == 'yes':
    print('Lets get started')
    print ('')
    play_func()
else:
    print ('')
    print ('---------------------------------')
    print ('No worries. Have a wonderful day!')
    print ('---------------------------------')
    print ('')