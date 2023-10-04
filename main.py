import sys
from bjorklund import bjorklund
from patterns import generate_necklace, invert_necklace, generate_anacrusis_necklace, format_pattern

try:
    pulses = int(sys.argv[1])
    onsets = int(sys.argv[2])
except Exception:
    print("usage: python bjorklund.py <STEPS> <PULSES>")
else:
    original_pattern = bjorklund(pulses, onsets)
    necklace = generate_necklace(original_pattern)
    inverted_necklace = invert_necklace(necklace)
    anacrusis_necklace = generate_anacrusis_necklace(original_pattern)
       
    print("1st Onset:", format_pattern(original_pattern))
    print("Necklace:")
    for pattern in necklace:
      print(format_pattern(pattern))
    print("Inverted Necklace:")
    for pattern in inverted_necklace:
      print(format_pattern(pattern))
    print("Anacrusis Necklace:")
    for pattern in anacrusis_necklace:
      print(format_pattern(pattern))
