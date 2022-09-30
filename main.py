from ast import arg
import hashlib
import sys
import os
import importlib

MAX_LENGTH=8
BIT_SPLIT=4

# getting all available implementations
def load_implementations():
    implementations_files = [f for f in os.listdir('implementations') if os.path.isfile('./implementations/'+f) and f.endswith('.py')]
    implementations={}
    
    for f in implementations_files:
        implementations[f[0:-3]]='./implementations/'+f

    return implementations

def base_to_decimal(value, base):
    value_list = list(value)
    value_list.reverse()
    dec_value=0
    for i in range(len(value_list)):
        try:
            v=IBASES.index(value_list[i]) # gets the index of the character
            if v >= base:
                print('Wrong character in string for base')
                exit()
            dec_value+=v*base**i # to decimal with the base, index and power
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

def convert_base_to_base(value, i_base, g_base, initial_base_module, goal_base_module):
    dec_value=0
    if initial_base_module: # check if implementation for initial base, and if so execute its function if not default function
        dec_value=initial_base_module.from_base(value)
    else:
        dec_value=base_to_decimal(value, i_base)
    final_value=0
    if goal_base_module: # check if implementation for goal base, and if so execute its function if not default function
        final_value=goal_base_module.to_base(value)
    else:
        final_value=decimal_to_base(dec_value, g_base)

    if len(final_value.replace(' ', '')) > MAX_LENGTH: # check if final length is more than MAX_LENGTH
        return print('Value too high (max 8 symbols)')
    if(g_base == 10): # if base is ten remove all spaces
        final_value = str(int(final_value.replace(' ', '')))
    print('Result: '+final_value)

# check if i is an int
def check_int(i): 
    try:
        return int(i)
    except:
        return -1

# check if an implementation is valid
def check_implementations(implementations, initial_base, goal_base, IBASES, GBASES):
    if implementations.get(str(goal_base)) != None:
        goal_base_module=importlib.import_module('implementations.'+str(goal_base), '.')
        if goal_base_module.implementation() != hashlib.sha256((str(goal_base)+'BASE'+'implementation'+'from_base'+'to_base').encode()).hexdigest():
            print('Invalid implementation')
            exit()
        GBASES=goal_base_module.BASE

    if implementations.get(str(initial_base)) != None:
        initial_base_module=importlib.import_module('implementations.'+str(initial_base), '.')
        if initial_base_module.implementation() != hashlib.sha256((str(initial_base)+'BASE'+'implementation'+'from_base'+'to_base').encode()).hexdigest():
            print('Invalid implementation')
            exit()
        IBASES=initial_base_module.BASE
    
    return [IBASES, GBASES]

# transforms string args to an object
def parse_arguments():
    arguments = {}
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            try:
                decomposed_arg=sys.argv[i].split('=')
                index=decomposed_arg[0]
                value=sys.argv[i][len(index)+1:len(sys.argv[i])] # get first part before equal sign and after
                arguments[index] = value
            except:
                print('Could not read argument', sys.argv[i])

    return arguments

# check if provided bases files
def check_bases(arguments):
    IBASES=open('bases/16', 'r').read()
    GBASES=open('bases/16', 'r').read()
    if arguments.get('--initial_base_file') != None:
        try:
            IBASES=open(arguments['--initial_base_file'], 'r').read()
        except:
            print('Could not get your custom initial base')
            exit()
    if arguments.get('--goal_base_file') != None:
        try:
            GBASES=open(arguments['--goal_base_file'], 'r').read()
        except:
            print('Could not get your custom goal base')
            exit()

    return [IBASES, GBASES]

# get base from argument of input
def get_base(arguments, implementations, key, MAX_BASE, BASES):
    base=0
    
    if None == arguments.get('--'+key+'_base'):
        base=check_int(input('What is your '+key+' base ? '))
    else:
        base=check_int(arguments['--'+key+'_base'])
    if base < 2:
        return print('Incorrect base')
    if base > MAX_BASE and implementations.get(str(base)) == None:
        try:
            BASES=open('bases/'+str(base), 'r').read()
            MAX_BASE=len(BASES)-1
        except:
            return print(key+' base is too high or not found')
    
    return [base, MAX_BASE, BASES]

# get value from argument or input
def get_value(arguments):
    value='0'
    if arguments.get('--value') != None:
        value=arguments['--value']
    else:
        value=input('What is your value ? ').replace(' ', '')

    return value

def main():
    print('Type --help for help')

    arguments = parse_arguments()
    implementations = load_implementations()

    global IBASES
    global GBASES
    global MAX_IBASE
    global MAX_GBASE

    [IBASES, GBASES] = check_bases(arguments)

    MAX_IBASE=len(IBASES)-1
    MAX_GBASE=len(GBASES)-1

    [initial_base, MAX_GBASE, GBASES]=get_base(arguments, implementations, "initial", MAX_IBASE, IBASES)
    [goal_base, MAX_IBASE, IBASES]=get_base(arguments, implementations, "goal", MAX_GBASE, GBASES)

    if goal_base == initial_base:
        return print('Useless operation (same base)')

    value=get_value(arguments)

    initial_base_module=None
    goal_base_module=None

    [IBASES, GBASES] = check_implementations(implementations, initial_base, goal_base, IBASES, GBASES)

    convert_base_to_base(value, initial_base, goal_base, initial_base_module, goal_base_module)

# help function executed when --help is typed
def help():
    print('\nTo automate the program you can provide parameters via console arguments')
    print('\nArguments:')
    print('--initial_base      | The base of your value')
    print('--goal_base         | The base you want to encode to')
    print('--value             | Your value')
    print('--initial_base_file | The path to the base of your value if not between 2 and 16 or 32, 58, 64')
    print('--goal_base_file    | The path to the base you want to encode to if not between 2 and 16 or 32, 58, 64')
    print('\n')

# check if help, is so execute help if not main
if len(sys.argv) > 1 and sys.argv[1] == '--help':
    help()
else:
    main()