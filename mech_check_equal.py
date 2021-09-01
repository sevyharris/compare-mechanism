# Script to check whether two surface mechanisms are equal
# Sevy Harris
# 8/31/2021

from rmgpy.tools import diffmodels

from rmgpy.chemkin import load_species_dictionary

chemkin1_gas = "/home/moon/methanol/meOH-synthesis/base/chemkin/chem_annotated-gas.inp"
chemkin1_surf = "/home/moon/methanol/meOH-synthesis/base/chemkin/chem_annotated-surface.inp"
species_dict1 = "/home/moon/methanol/meOH-synthesis/base/chemkin/species_dictionary.txt"
tran1 = "/home/moon/methanol/meOH-synthesis/base/chemkin/tran.dat"

chemkin2_gas = "/home/moon/methanol/meOH-synthesis/perturbed_runs/chemkin/chem_annotated-gas.inp"
chemkin2_surf = "/home/moon/methanol/meOH-synthesis/perturbed_runs/chemkin/chem_annotated-surface.inp"
species_dict2 = "/home/moon/methanol/meOH-synthesis/perturbed_runs/chemkin/species_dictionary.txt"
tran2 = "/home/moon/methanol/meOH-synthesis/perturbed_runs/chemkin/tran.dat"


# sd = load_species_dictionary(species_dict1)


#exit(0)



# gas_results = diffmodels.execute(chemkin1=chemkin1_gas,
#                                  species_dict1=species_dict1,
#                                  thermo1=None,
#                                  species_dict2=species_dict2,
#                                  chemkin2=chemkin2_gas,
#                                  thermo2=None)

# common_gas_species = gas_results[0]
# unique_gas_species1 = gas_results[1]
# unique_gas_species2 = gas_results[2]
# common_gas_reactions = gas_results[3]
# unique_gas_reactions1 = gas_results[4]
# unique_gas_reactions2 = gas_results[5]

# same_gas_species = True
# same_gas_reactions = True
# if len(unique_gas_species1) + len(unique_gas_species2) > 0:
#     print("Models have different gas species")
#     same_gas_species = False
# if len(unique_gas_reactions1) + len(unique_gas_reactions2) > 0:
#     print("Models have different gas reactions")
#     same_gas_reactions = False

# if same_gas_species and same_gas_reactions:
#     print("Mechanisms are equal in the gas phase")


surf_results = diffmodels.execute(chemkin1=chemkin1_surf,
                                  species_dict1=species_dict1,
                                  thermo1=None,
                                  species_dict2=species_dict2,
                                  chemkin2=chemkin2_surf,
                                  thermo2=None)
