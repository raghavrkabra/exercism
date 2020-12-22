codons = {
        **dict.fromkeys(["UUU", "UUC"],"Phenylalanine"),
        **dict.fromkeys(["UUA", "UUG"], "Leucine"),
        **dict.fromkeys(["UCU", "UCC", "UCA", "UCG"], "Serine"),
        **dict.fromkeys(["UAU", "UAC"], "Tyrosine"),
        **dict.fromkeys(["UGU", "UGC"], "Cysteine"),
        **dict.fromkeys(["UGG"], "Tryptophan"),
        **dict.fromkeys(["CUU","CUC","CUA","CUG"], "Leucine"),
        **dict.fromkeys(["CCU", "CCC", "CCA", "CCG"], "Proline"),
        **dict.fromkeys(["CAU", "CAC"], "Histidine"),
        **dict.fromkeys(["CAA", "CAG"], "Glutamine"),
        **dict.fromkeys(["CGU", "CGC", "CGA", "CGG"], "Arginine"),
        **dict.fromkeys(["AUU", "AUC", "AUA"], "Isoleucine"),
        **dict.fromkeys(["AUG"], "Methionine"),
        **dict.fromkeys(["ACU", "ACC", "ACA", "ACG"], "Threonine"),
        **dict.fromkeys(["AAU", "AAC"], "Asparagine"),
        **dict.fromkeys(["AAA", "AAG"], "Lysine"),
        **dict.fromkeys(["AGU", "AGC"], "Serine"),
        **dict.fromkeys(["AGA", "AGG"], "Arginine"),
        **dict.fromkeys(["GUU", "GUC", "GUA", "GUG"], "Valine"),
        **dict.fromkeys(["GCU", "GCC", "GCA", "GCG"], "Alanine"),
        **dict.fromkeys(["GAU", "GAC"], "Aspartic acid"),
        **dict.fromkeys(["GAA", "GAG"], "Glutamic acid"),
        **dict.fromkeys(["GGU", "GGC", "GGA", "GGG"], "Glycine"),
        **dict.fromkeys(["UAA", "UAG", "UGA"], "STOP")
        }

def proteins(strand):
    protein_list = []
    for i in range(0, len(strand), 3):
        chunk = strand[i:i+3]
        if codons[chunk] == "STOP":
            break
        protein_list.append(codons[chunk])
    return protein_list
