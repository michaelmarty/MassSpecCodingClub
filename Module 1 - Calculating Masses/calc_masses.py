import numpy as np

aa_masses = {'A': 71.0788, 'C': 103.1388, 'D': 115.0886, 'E': 129.1155, 'F': 147.1766,
             'G': 57.0519, 'H': 137.1411, 'I': 113.1594, 'K': 128.1741, 'L': 113.1594,
             'M': 131.1926, 'N': 114.1038, 'P': 97.1167, 'Q': 128.1307, 'R': 156.1875,
             'S': 87.0782, 'T': 101.1051, 'V': 99.1326, 'W': 186.2132, 'Y': 163.1760}

aa_masses_monoisotopic = {'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259, 'F': 147.06841,
                          'G': 57.02146, 'H': 137.05891, 'I': 113.08406, 'K': 128.09496, 'L': 113.08406,
                          'M': 131.04049, 'N': 114.04293, 'P': 97.05276, 'Q': 128.05858, 'R': 156.10111,
                          'S': 87.03203, 'T': 101.04768, 'V': 99.06841, 'W': 186.07931, 'Y': 163.06333}

rna_masses = {'A': 329.2, 'U': 306.2, 'C': 305.2, 'G': 345.2, 'T': 306.2}

dna_masses = {'A': 313.2, 'T': 304.2, 'C': 289.2, 'G': 329.2, 'U': 304.2}

mass_water = 18.0153
mass_water_monoisotopic = 18.0105

test_seq = ("GSTFSKLREQLGPVTQEFWDNLEKETEGLRQEMSKDLEEVKAKVQPYLDDFQKKWQEEMELYRQKVEPLRAELQEGARQKLHELQEKLSPLGEEMRD"
            "RARAHVDALRTHLAPYSDELRQRLAARLEALKENGGARLAEYHAKATEHLSTLSEKAKPALEDLRQGLLPVLESFKVSFLSALEEYTKKLNTQ")


def calc_aa_mass(a, monoisotopic=False):
    a = a.upper()

    if a in aa_masses.keys():
        if monoisotopic:
            return aa_masses_monoisotopic[a]
        else:
            return aa_masses[a]
    else:
        print("Unrecognized Character:", a)
        return 0


def calc_prot_mass(seq, monoisotopic=False):
    if monoisotopic:
        water = mass_water_monoisotopic
    else:
        water = mass_water
    return np.sum([calc_aa_mass(s, monoisotopic=monoisotopic) for s in test_seq]) + water


tot_mass = calc_prot_mass(test_seq, monoisotopic=True)

print(tot_mass)
