# Adapted from Brian House's bjorklund function:
# https://github.com/brianhouse/bjorklund
# under the MIT License
# https://github.com/brianhouse/bjorklund/blob/master/LICENSE.txt
# Copyright (c) 2011 Brian House


def bjorklund(pulses, onsets):
    pulses = int(pulses)
    onsets = int(onsets)
    if onsets > pulses:
        raise ValueError    
    pattern = []    
    counts = []
    remainders = []
    divisor = pulses - onsets
    remainders.append(onsets)
    level = 0
    while True:
        counts.append(divisor // remainders[level])
        remainders.append(divisor % remainders[level])
        divisor = remainders[level]
        level = level + 1
        if remainders[level] <= 1:
            break
    counts.append(divisor)
    
    def build(level):
        if level == -1:
            pattern.append(0)
        elif level == -2:
            pattern.append(1)         
        else:
            for i in range(0, counts[level]):
                build(level - 1)
            if remainders[level] != 0:
                build(level - 2)
    
    build(level)
    i = pattern.index(1)
    pattern = pattern[i:] + pattern[0:i]
    return pattern
