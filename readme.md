# Base encoder

## Commands

Type --help for the list of available arguments

## Custom base file

A custom base file is a file with all your encoded values in order

So in the case of base32:

| Value | Symbol |
|-------|--------|
|0|A|
|1|B|
|2|C|
|3|D|
|4|E|
|5|F|
|6|G|
|7|H|
|8|I|
|9|J|
|10|K|
|11|L|
|12|M|
|13|N|
|14|O|
|15|P|
|16|Q|
|17|R|
|18|S|
|19|T|
|20|U|
|21|V|
|22|W|
|23|X|
|24|Y|
|25|Z|
|26|1|
|27|2|
|28|3|
|29|4|
|30|5|
|31|6|
|32|7|
|Padding|=|

The base file will look like:

> ABCDEFGHIJKLMNOPQRSTUVWXYZ234567=

**Note**: The last character represents the padding so in most cases 0 unless for 32, 58 and 64