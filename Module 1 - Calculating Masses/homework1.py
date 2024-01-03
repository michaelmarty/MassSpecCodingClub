# Homework 1 for Module 1
#
# Problem 1 of 2: Calculate the neutral monoisotopic mass of this RNA oligonucliotide
#

oligo = "aacauucaACgcugucggugAgu"

#
# I will give you the atomic formulas of the nucleobases
# You will need to add ribose and phosphate to each nucleobase
# and take away 3 waters, one for the nucleobase-ribose bond, one for the phosphate-ribose bond, and
# one for the second phosphate-ribose bond.
#

A = "C5H5N5"
C = "C4H5N3O"
G = "C5H5N5O"
U = "C4H4N2O2"
ribose = "C5H10O5"
phos = "H3PO4"
water = "H2O"

# I will help you out with a hint here

from calc_masses_chem import calc_formula_mass

mono = True
mass_water = calc_formula_mass(water, monoisotopic=mono)

form_a = A + ribose + phos  # This just stacks the strings of formulas back to back
mass_a = calc_formula_mass(form_a, monoisotopic=mono) - 3 * mass_water

# Don't forget, this mass is just for a single unterminated nucleotide fragment.
# You will then need to add back a water for the terminal phosphate.
#

# [ Your code here]



# Print the final answer:

print("The oligo mass is:")

# If you are curious about checking your answer, try: http://mass.rega.kuleuven.be/mass/mongo.htm.
# Select monoisotopic, RNA, -OH terminal on 5', and 3' phosphate terminal

#
#
#  Problem 2 of 2: Calculate the difference between the monoisotopic mass and the average mass for this oligo
#
#


# [Your code here]


# Print the final answer:

print("The difference between average and monoisotopic:")
