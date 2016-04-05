def gc(sequence):
    gc_count = 0
    valid_nucleotides = ['A','C','T','U','G','N']
    for nuc in sequence:
        nuc = nuc.upper()
        if nuc not in valid_nucleotides:
            raise Exception(nuc + ' is not a valid nucleotide.')
        if nuc == 'G':
            gc_count += 1
        if nuc == 'C':
            gc_count += 1
    if len(sequence)==0:
        return 0 
    return (float(gc_count) / len(sequence))
