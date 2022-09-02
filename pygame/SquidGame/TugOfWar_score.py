# Calculate Score of Tug of War

## Needs Object
## 1. Number of people
## 2. People's strength
## 3. Strategy
## 4. People's willpower

import random


def tw(num, str, sgy, pwp) : 
    result = 0
    # The luck is other ect element
    luk = random.uniform(0,1)
    # The parameter need individual influence
    num_i = 1
    str_i = 1
    sgy_i = 1
    pwp_i = 1
    result = (num*num_i) + (str*str_i) + (sgy*sgy_i) + (pwp*pwp_i)
    return result * luk
