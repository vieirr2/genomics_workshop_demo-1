complimentary_nucleotides = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}


class RNA:
    def __init__(self, sequence: str):
        self.sequence = sequence
        if not self._check_validity():
            raise ValueError("Bad sequence. Sequences must only contain G, C, A, and U")

    def __eq__(self, other):
        return True if str(self) == str(other) else False

    def __str__(self):
        return self.sequence

    def __repr__(self):
        return "RNA(sequence='{}')".format(self.sequence)

    def _check_validity(self):
        return all(nucleotide.upper() in 'GCAU' for nucleotide in self.sequence)

    @property
    def complimentary_sequence(self):
        return RNA(''.join(complimentary_nucleotides[nt.upper()] for nt in self.sequence))

    @property
    def rna_start_codon(self):
        if 'AUG' in self.sequence:
            return('coding RNA')
        else:
            return('non coding RNA')







