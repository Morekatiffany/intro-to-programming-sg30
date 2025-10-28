

def reverse_complement(seq):
    seq = seq.upper()
    complement = {"A": "T", "T": "A", "G": "C", "C": "G"}
    rev_comp = "".join(complement.get(base, base) for base in reversed(seq))
    return rev_comp

def main():
    dna = input("Enter a DNA sequence: ")
    print(f"Reverse complement: {reverse_complement(dna)}")

if __name__ == "__main__":
    main()
