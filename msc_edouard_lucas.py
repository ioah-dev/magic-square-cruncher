# imports
import time
import math

# globals/constants
__debug_mode = False
__version = "0.1"
__min_c_value = 1
__max_c_value = 100 
# Elapsed time (1 - 100): 97.5942s


# misc functions
def print_card(text, width):
    top_row = "╔"+"".ljust(width-2, "═")+"╗"
    print(top_row)
    text_row = text.center(width - 2, " ").center(width, "║")
    print(text_row)
    bottom_row = "╚"+"".ljust(width-2, "═")+"╝"
    print(bottom_row)

# app functions
def combinations_edouard_lucas(c):
    '''
    Function to generate all posible combinations with no repetition where the 
    order of elements doesn't matter, to fulfill the rules: 
        0 < a < b < (c - a)
        b != 2a
    '''
    for a in range(1, c + 1):
        for b in range(a+1, c-a):
            if b != 2 * a:
                yield (a, b, c)

def get_square_from_a_b_c(a, b, c):
    if(math.sqrt(c - b).is_integer() and 
       math.sqrt(c - (a - b)).is_integer() and 
       math.sqrt(c + a).is_integer() and 
       math.sqrt(c + (a + b)).is_integer() and 
       math.sqrt(c - (a + b)).is_integer() and 
       math.sqrt(c - a).is_integer() and 
       math.sqrt(c + (a - b)).is_integer() and 
       math.sqrt(c + b).is_integer()):
        return (
            c - b,          c - (a - b),    c + a, 
            c + (a + b),    c,              c - (a + b), 
            c - a,          c + (a - b),    c + b
            )

# msc app
print_card(f"Magic Square - Cruncher v.{__version}", 80)

bm_start = time.time()

for c in range(__min_c_value, __max_c_value + 1):
    if __debug_mode: print(f"c value of {c**2}:")
    i = 0
    for item in combinations_edouard_lucas(c**2):
        output = get_square_from_a_b_c(*item)
        if __debug_mode: print(output)
        if output != None: 
            i += 1
    print(f"c({c}) has {i} valid magic squares.")

bm_end = time.time(); print(f"\nElapsed time: {bm_end - bm_start}\n")