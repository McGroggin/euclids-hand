def generate_necklace(pattern):
    necklace = []
    onsets = [i for i, bit in enumerate(pattern) if bit == 1]
    
    for onset in onsets:
        rotated_pattern = pattern[onset:] + pattern[:onset]
        necklace.append(rotated_pattern)
    
    return necklace

def invert_necklace(necklace):
    inverted_necklace = []

    for pattern in necklace:
        inverted_pattern = [1 if bit == 0 else 0 for bit in pattern]
        inverted_necklace.append(inverted_pattern)

    return inverted_necklace

def generate_anacrusis_necklace(pattern):
    anacrusis_necklace = []
    rests = [i for i, bit in enumerate(pattern) if bit == 0]

    for rest in rests:
        rotated_pattern = pattern[rest:] + pattern[:rest]
        anacrusis_necklace.append(rotated_pattern)

    return anacrusis_necklace

def format_pattern(pattern):
    formatted_pattern = ""

    for bit in pattern:
        if bit == 1:
            formatted_pattern += "X"  # Use "X" to represent onsets
        else:
            formatted_pattern += "."  # Use "-" to represent rests

    return formatted_pattern
