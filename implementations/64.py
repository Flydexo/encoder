import hashlib
from operator import index

BASE="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
PADDING="="

def base_to_binary(value):
    binary=''
    for v in range(len(value.replace('=', ''))):
        remainder=0
        multiplier=basestr.index(value[v])
        remainders=[];

        if multiplier == 0:
            remainders = ['0'] * 6

        while(multiplier > 0):
            remainder=multiplier % 2 # remainder obtained with the modulo operator
            multiplier=( multiplier - remainder ) / 2 # multiplier obtained because p = q * m + so m = (p - r) / q
            remainders.append(str(int(remainder))) # add remainder to list
        
        zeros_to_add=((len(remainders) - (len(remainders) % 6)) - len(remainders)) % 6
        if zeros_to_add != 0:
            remainders = remainders + ['0'] * zeros_to_add

        remainders.reverse()

        print(remainders)

        binary+=''.join(remainders)
        
    print(binary, binary[0:-(len(binary)%8)])
    return binary

def decimal_to_binary(value, l=8):
    remainder=0
    multiplier=int(value)
    remainders=[];

    while(multiplier > 0):
        remainder=multiplier % 2 # remainder obtained with the modulo operator
        multiplier=( multiplier - remainder ) / 2 # multiplier obtained because p = q * m + so m = (p - r) / q
        remainders.append(str(int(remainder))) # add remainder to list
    
    zeros_to_add=((len(remainders) - (len(remainders) % l)) - len(remainders)) % l
    if zeros_to_add != 0:
        remainders = remainders + ['0'] * zeros_to_add

    remainders.reverse()

    return ''.join(remainders)

def binary_to_decimal(value):
    value_list = list(value)
    value_list.reverse()
    dec_value=0
    for i in range(len(value_list)):
        try:
            v=int(value_list[i])
            if v >= 2:
                print('Wrong character in string for base')
                exit()
            dec_value+=v*2**i 
        except:
            print('Wrong character in string for base')
            exit()
    return dec_value

def binary_to_index(value):
    zeros_to_add=((len(value) - (len(value) % 6)) - len(value)) % 6
    formatted=value + '0' * zeros_to_add
    binary_indexes=[formatted[i:i+6] for i in range(0, len(formatted), 6)]
    decimal_indexes=[binary_to_decimal(i) for i in binary_indexes]
    return decimal_indexes

def to_base(value):
    indexes=binary_to_index(decimal_to_binary(value))
    encoded=''
    for i in indexes:
        encoded+=BASE[i]
    padding_to_add=((len(encoded) - (len(encoded) % 4)) - len(encoded)) % 4
    encoded+= '='*padding_to_add
    return encoded

def from_base(value):
    formatted=value.replace('=','')
    paddings=len(value)-len(formatted)
    if paddings > 2:
        print("Incorrect base64 input")
        exit()
    indexes=[BASE.index(v) for v in formatted]
    binary_indexes=[decimal_to_binary(i,6) for i in indexes]
    binary=''.join(binary_indexes)
    binary=binary[0:-(paddings*2)]
    return binary_to_decimal(binary)

def implementation():
    return hashlib.sha256(('64'+'BASE'+'implementation'+'from_base'+'to_base').encode()).hexdigest()