import argparse
from typing import List


# alphabet used for the caesar cipher
__ALPHABETH__ = 'abcdefghijklmnopqrstuvwxyz'

# common word frequency in english plaintext
__ENGLISH_FREQUENCY_TABLE__ = [
    8.17,
    1.49,
    2.78,
    4.25,
    12.7,
    2.23,
    2.02,
    6.09,
    6.97,
    0.15,
    0.77,
    4.03,
    2.41,
    6.75,
    7.51,
    1.93,
    0.1,
    5.99,
    6.33,
    9.06,
    2.76,
    0.98,
    2.36,
    0.15,
    1.97,
    0.07
]


def shift(character: str, shiftment: int) -> str:
    """
    Shift the given character of the shiftment factor specified.
    """
    if not character.isalpha(): return character
    return chr(ord('a') + ((ord(character.lower())-ord('a')+shiftment) % 26))

def encode(text: str, shiftment: int) -> str:
    """
    Apply the shift function on all the text with the same shifment factor.
    """
    return ''.join([shift(character=c, shiftment=shiftment) for c in text])

def theoric_frequencies() -> List[float]:
    """
    Get an ordered list of word frequencies.
    """
    return __ENGLISH_FREQUENCY_TABLE__

def calculate_frequencies(text: str) -> List[float]:
    """
    Calculate the ordered list of words frequencies in the text.
    """
    frequencies = {}

    for character in text.lower():
        if character.isalpha():  
            if character in frequencies:
                frequencies[character] += 1
            else:
                frequencies[character] = 1

    total_frequency = sum(frequencies.values())
    normalized_frequencies = {character: float(freq) / float(total_frequency) * 100 for character, freq in frequencies.items()}
    return [round(normalized_frequencies.get(c, 0),2) for c in __ALPHABETH__]

def calculate_distribution(calc_freq: List[float], theo_freq: List[float] = theoric_frequencies()):
    """
    Frequency distribution
    """
    return round(sum([((int(calc_freq-theo_freq)^2)/theo_freq) for calc_freq, theo_freq in zip(calc_freq, theo_freq)]),2)

def main():
    parser = argparse.ArgumentParser(
        prog='Caesar Chiper',
        description='Simple Encryption, Decription, Bruteforce and Frequency Attacks using the Caesar cipher.',
        epilog='Simple Encryption, Decription, Bruteforce and Frequency Attacks using the Caesar cipher.'
    )
    
    parser.add_argument('-e', '--encrypt', action='store_true')
    parser.add_argument('-d', '--decrypt', action='store_true')
    parser.add_argument('-b', '--bruteforce', action='store_true')
    parser.add_argument('-f', '--frequency', action='store_true')

    parser.add_argument('-t', '--text', type=str, default=None)
    parser.add_argument('-s', '--shiftment', type=int, default=0)
    
    args = parser.parse_args()

    if args.text is None:
        raise ValueError('--text args must be setted')
    
    if (args.encrypt or args.decrypt) and args.shiftment == 0:
        raise ValueError('--shiftment args must be setted')

    if args.encrypt:
        encrypted: str = encode(text=args.text, shiftment=args.shiftment)
        print(f'Encrypted: {encrypted}')

    if args.decrypt:
        decrypted: str = encode(text=args.text, shiftment=-args.shiftment)
        print(f'Decrypted: {decrypted}')

    if args.bruteforce:
        for shiftment in range(1, 26):
            decrypted: str = encode(text=args.text, shiftment=-shiftment)
            print(f'Shiftment {shiftment}; Decrypted: {decrypted}')

    if args.frequency:
        calculated_frequencies = calculate_frequencies(text=args.text)
        calculated_distributions = [calculate_distribution(calc_freq=calculated_frequencies[n:]+calculated_frequencies[:n]) for n in range(0,25)]
        calculated_shiftment = calculated_distributions.index(min(calculated_distributions))
        decrypted: str = encode(text=args.text, shiftment=-calculated_shiftment)
        print(f'Shiftment {calculated_shiftment}; Decrypted: {decrypted}')

if __name__ == '__main__':
    main()