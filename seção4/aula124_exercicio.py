questions = [
    {
        'Question': 'How much is 3 + 2 ?',
        'Options' : ['1','4','5','7'],
        'Answer' : '5'
    },

    {
        'Question': 'How much is 3 * 2 ?',
        'Options' : ['6','4','5','7'],
        'Answer' : '6'  
    }, 

    {
        'Question': 'How much is 10/2 ?',
        'Options' : ['1','4','5','7'],
        'Answer' : '5'
    },
]

hits = 0
errors = 0

for question in questions:
    print('Question:', question['Question'])

    options = question['Options']

    for i,j in enumerate(options):
        print(f'{i}) {j}')

    while True:
        try:
            option = input('What is the answer?:')
            
            if len(option) != 1:
                print('Invalid')
                continue
            answer = options[int(option)]
            if answer == question['Answer']:
                print('You got it')
                hits+=1
            else:
                print('You missed')
                errors+=1
            break
        except:
            print('Its just a number')

print(f'Você acertou {hits} vezes e errou {errors} vezes.')