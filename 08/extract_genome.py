

def extract_genes(input_path, output_path):
    genes = []
    with open(input_path, "r") as infile:
        for line in infile:
            if line.startswith("gene:"):
                gene_name = line.split("gene:")[1].split()[0]
                genes.append(gene_name)

    with open(output_path, "w") as outfile:
        outfile.write(",".join(genes))

    print(f"Extracted {len(genes)} gene names → saved to {output_path}")

def main():
    input_path = input("Enter input file path: ")
    output_path = input("Enter output CSV path: ")
    extract_genes(input_path, output_path)

if __name__ == "__main__":
    main()
