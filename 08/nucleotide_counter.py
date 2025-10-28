

def count_nucleotides(seq):
    seq = seq.upper()
    return {
        "A": seq.count("A"),
        "T": seq.count("T"),
        "G": seq.count("G"),
        "C": seq.count("C")
    }

def main():
    seq = input("Enter a DNA sequence: ")
    counts = count_nucleotides(seq)
    print(f"A={counts['A']}, T={counts['T']}, G={counts['G']}, C={counts['C']}")

if __name__ == "__main__":
    main()
