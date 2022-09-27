# Base encoder

## Commands

Type --help for the list of available arguments

## Custom display

You can edit this variables:

> MAX_LENGTH
> BIT_SPLIT

**MAX_LENGTH** is the maximum length of the final encoded string (no spaces) and **BIT_SPLIT** is the number of characters between spaces on the final encoded string.

Example with **MAX_LENGTH=8** and **BIT_SPLIT=4**:
> 0110 1011

## Custom base file

A custom base file is a file with all your encoded values in order

So in the case of **hexadecimal**:

| Value | Symbol |
|-------|--------|
|0|0|
|1|1|
|2|2|
|3|3|
|4|4|
|5|5|
|6|6|
|7|7|
|8|8|
|9|9|
|10|A|
|11|B|
|12|C|
|13|D|
|14|E|
|15|F|
|padding|0|

The base file will look like:

> 0123456789ABCDEF0

**Note**: The last character represents the **padding** so in most cases 0 unless for 32, 58 and 64

## Custom implementation

To encode and decode with bases with more complex logic (eg: 64) you can create your own **implementation**. 

### Implementation python file

Create a **python file** the number of your base in the implementations folder.

Example:

> ./implementations/64.py

### Implentation code interface

Your implementation file must respect a specific **interface**. It must contain:

| type | name | input | output |
|------|------|-------|--------|
|root variable|BASE|None|str|
|function|from_base|str|int|
|function|to_base|int|str|
|function|implementation|None|str|

---

- The **BASE** variable is your base string. For example for base 64:

> ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=

- The **from_base** function takes a string encoded in your base and must return the decimal decoded version

- The **to_base** function takes a decimal and must return the string encoded with your base

- The **implementation** function returns a hexadecimal hash of the string encoded interface

Example of base64 implementation
> '64'+'BASE'+'from_base'+'implementation'+'to_base' => 'b69d5d0cc2cff31d0058485cba3368c3a4e016fc1abff85ae489aa70655aeb72'