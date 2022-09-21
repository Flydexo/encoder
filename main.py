import sys

MAX_LENGTH=8
BIT_SPLIT=4

def base_to_decimal(value, base):
    value_list = list(value)
    value_list.reverse()
    dec_value=0
    for i in range(len(value_list)):
        try:
            v=IBASES.index(value_list[i])
            if v >= base:
                print('Wrong character in string for base')
                exit()
                return 0
            dec_value+=v*base**i 
        except:
            print('Wrong character in string for base')
            exit()
    return dec_value

def decimal_to_base(value, base):
    remainder=0
    multiplier=value
    remainders=[];

    while(multiplier > 0):
        remainder=multiplier % base # remainder obtained with the modulo operator
        multiplier=( multiplier - remainder ) / base # multiplier obtained because p = q * m + so m = (p - r) / q
        remainders.append(GBASES[int(remainder)]) # add remainder to list
    
    zeros_to_add=((len(remainders) - (len(remainders) % BIT_SPLIT)) - len(remainders)) % BIT_SPLIT
    if zeros_to_add != 0:
        remainders = remainders + [GBASES[0]] * zeros_to_add

    ordered_remainders=[]

    # REVERSE THE ARRAY
    for i in range(len(remainders)):
        index=len(remainders)-1-i # get index starting from the end
        ordered_remainders.append(remainders[index])

    bits=[]

    for i in range(int(len(ordered_remainders) / BIT_SPLIT)):
        start_index_to_slice=i*BIT_SPLIT
        end_index_to_slice=i*BIT_SPLIT+BIT_SPLIT
        bits.append(''.join(ordered_remainders[start_index_to_slice:end_index_to_slice])) # add to bits a string of a slice of 4 bits

    bits_string = ' '.join(bits)

    return bits_string

def convert_base_to_base(value, i_base, g_base):
    dec_value=base_to_decimal(value, i_base)
    final_value=decimal_to_base(dec_value, g_base)
    if len(final_value.replace(' ', '')) > MAX_LENGTH:
        return print('Value too high (max 8 symbols)')
    if(g_base == 10):
        final_value = str(int(final_value))
    print('Result: '+final_value)

def check_int(i): 
    try:
        return int(i)
    except:
        return -1

def main():
    print('Type --help for help')

    arguments = {}

    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            try:
                decomposed_arg=sys.argv[i].split('=')
                index=decomposed_arg[0]
                value=decomposed_arg[1]
                arguments[index] = value
            except:
                print('Could not read argument', sys.argv[i])
                            
    global IBASES
    global GBASES
    global MAX_IBASE
    global MAX_GBASE
    IBASES=open('bases/16', 'r').read()
    if arguments.get('--initial_base_file') != None:
        try:
            IBASES=open(arguments['--initial_base_file'], 'r').read()
        except:
            print('Could not get your custom initial base')
            exit()
    GBASES=open('bases/16', 'r').read()
    if arguments.get('--goal_base_file') != None:
        try:
            GBASES=open(arguments['--goal_base_file'], 'r').read()
        except:
            print('Could not get your custom goal base')
            exit()
    MAX_IBASE=len(IBASES)-1
    MAX_GBASE=len(GBASES)-1

    initial_base=0
    if None == arguments.get('--initial_base'):
        initial_base=check_int(input('What is your initial base ? '))
    else:
        initial_base=check_int(arguments['--initial_base'])
    if initial_base < 2:
        return print('Incorrect base')
    if initial_base > MAX_IBASE:
        try:
            IBASES=open('bases/'+str(initial_base), 'r').read()
            MAX_IBASE=len(IBASES)-1
        except:
            return print('Initial base is too high or not found')
    goal_base=0
    if None == arguments.get('--goal_base'):
        goal_base=check_int(input('What is your goal base ? '))
    else:
        goal_base=check_int(arguments['--goal_base'])
    if goal_base < 2:
        return print('Incorrect base')
    if goal_base > MAX_GBASE:
        try:
            GBASES=open('bases/'+str(goal_base), 'r').read()
            MAX_GBASE=len(GBASES)-1
        except:
            return print('Goal base is too high or not found')
    if goal_base == initial_base:
        return print('Useless operation (same base)')
    value='0'
    if arguments.get('--value') != None:
        value=arguments['--value']
    else:
        value=input('What is your value ? ').replace(' ', '')
    convert_base_to_base(value, initial_base, goal_base)

def help():
    print('\nTo automate the program you can provide parameters via console arguments')
    print('\nArguments:')
    print('--initial_base      | The base of your value')
    print('--goal_base         | The base you want to encode to')
    print('--value             | Your value')
    print('--initial_base_file | The path to the base of your value if not between 2 and 16 or 32, 58, 64')
    print('--goal_base_file    | The path to the base you want to encode to if not between 2 and 16 or 32, 58, 64')
    print('\n')

if len(sys.argv) > 1 and sys.argv[1] == '--help':
    help()
else:
    main()