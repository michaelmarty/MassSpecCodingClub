from glypy.io import glycoct
from molmass import Formula
from rdkit.Chem.Descriptors import *

glycan = """
RES
1b:a-dman-HEX-1:5
2b:b-dglc-HEX-1:5
3s:n-acetyl
4b:b-dgal-HEX-1:5
5b:a-dgro-dgal-NON-2:6|1:a|2:keto|3:d
6s:n-acetyl
7b:b-dglc-HEX-1:5
8s:n-acetyl
9b:b-dgal-HEX-1:5
10b:a-dgro-dgal-NON-2:6|1:a|2:keto|3:d
11s:n-acetyl
LIN
1:1o(2+1)2d
2:2d(2+1)3n
3:2o(4+1)4d
4:4o(6+2)5d
5:5d(5+1)6n
6:1o(6+1)7d
7:7d(2+1)8n
8:7o(4+1)9d
9:9o(3+2)10d
10:10d(5+1)11n"""


def calc_glycan_mass(glycan_string, monoisotopic=False):
    gc = glycoct.loads(glycan_string)
    return gc.mass(average=(not monoisotopic))


glycan_mass = calc_glycan_mass(glycan, monoisotopic=False)
# print(glycan_mass)

formula = 'C8H10N4O2'


# exit()


def calc_formula_mass(formula, monoisotopic=False):
    f = Formula(formula)
    if monoisotopic:
        return f.monoisotopic_mass
    else:
        return f.mass


# print(calc_formula_mass(formula, monoisotopic=False))



smiles = "[C@](COP(=O)([O-])OCC[N+](C)(C)C)([H])(OC(CCCCCCC/C=C\CCCCCCCC)=O)COC(CCCCCCCCCCCCCCC)=O"


def calc_smiles_mass(smiles, monoisotopic=False):
    mol = Chem.MolFromSmiles(smiles)
    if monoisotopic:
        mass = ExactMolWt(mol)
    else:
        mass = MolWt(mol)
    return mass


# print(calc_smiles_mass(smiles, monoisotopic=False))
