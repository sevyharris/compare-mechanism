
from rmgpy.molecule.element import P
from rmgpy.molecule import adjlist
import cantera as ct
from logging import error
from rmgpy.chemkin import load_species_dictionary
from rmgpy.species import Species
from rmgpy.reaction import Reaction


def ct2rmg_reaction(ct_reaction, species_dictionary):

    reactants = [species_dictionary[reaction] for reaction in ct_reaction.reactants.keys()]
    products = [species_dictionary[product] for product in ct_reaction.products.keys()]
    rxn = Reaction(reactants=reactants, products=products)
    # __init__(
    #              label='',
    #              reactants=None,
    #              products=None,
    return rxn


def ct2rmg_species(ct_spec, species_dictionary):
    rmg_spec = species_dictionary[ct_spec.name]
    # don't worry about thermo yet
    
    #  def __init__(self, coeffs=None, Tmin=None, Tmax=None, E0=None, label='', comment=''):
    #     HeatCapacityModel.__init__(self, Tmin=Tmin, Tmax=Tmax, E0=E0, label=label, comment=comment)
    #     self.coeffs = coeffs
    rmg_spec = Species().from_adjacency_list(adjlist)


class Mechanism():
    species = []
    reactions = []

    def __init__(self, cti_file, dict_file):
        # TODO check if cti file exists
        # TODO make this work for gases and or surfaces

        gas = ct.Solution(cti_file)
        surf = ct.Interface(cti_file, 'surface1', [gas])
        species_dictionary = load_species_dictionary(dict_file)

        spec1 = ct2rmg_species(gas.species()[0], species_dictionary)
        print(spec1)
        self.species = gas.species() + surf.species()
        self.reactions = gas.reactions() + surf.reactions()


def import_model(cti, spec_dict):
    model = Mechanism(cti, spec_dict)
    return model


def compare_species(model1, model2):

    unique1 = []
    # unique1 = spec1 for spec1 in model1.species()
    # for spec1 in model1.species():


def main():
    import sys
    if len(sys.argv) < 5:
        error("Must provide two input cti's and two input species dictionaries")

    cti1 = sys.argv[1]
    dict1 = sys.argv[2]
    cti2 = sys.argv[3]
    dict2 = sys.argv[4]

    gas1 = ct.Solution(cti1)
    surf1 = ct.Interface(cti1, 'surface1', [gas1])
    species_dictionary1 = load_species_dictionary(dict1)
    gas2 = ct.Solution(cti2)
    surf2 = ct.Interface(cti2, 'surface1', [gas2])
    species_dictionary2 = load_species_dictionary(dict2)

    unique_sp1 = gas1.species() + surf1.species()
    unique_sp2 = []
    common_spec = []

    for spec2 in gas2.species() + surf2.species():
        for spec1 in unique_sp1[:]:  # make a copy so you don't remove from the list you are iterating over
            sp1 = species_dictionary1[spec1.name]
            sp2 = species_dictionary2[spec2.name]
            if sp1.is_isomorphic(sp2):
                common_spec.append([spec1, spec2])
                unique_sp1.remove(spec1)
                break
        else:
            unique_sp2.append(spec2)

    if len(unique_sp1) == 0 and len(unique_sp2) == 0:
        print("mechanisms have the same species")
    else:
        print(f'\n\n1:\t{unique_sp1}')
        print(f'\n\n2:\t{unique_sp2}')

    reaction_list1 = gas1.reactions()[:] + surf1.reactions()[:]
    reaction_list2 = gas2.reactions()[:] + surf2.reactions()[:]

    common_reactions = []
    unique_reactions1 = []
    unique_reactions2 = []
    for rxn1 in reaction_list1:
        for rxn2 in reaction_list2[:]:  # make a copy so you don't remove from the list you are iterating over
            # reaction1 = rxn1
            reaction2 = ct2rmg_reaction(rxn2, species_dictionary2)
            reaction1 = ct2rmg_reaction(rxn1, species_dictionary1)

            if reaction1.is_isomorphic(reaction2):
                common_reactions.append([rxn1, rxn2])
                # Remove reaction 2 from being chosen a second time.
                # Let each reaction only appear only once in the diff comparison.
                # Otherwise this miscounts number of reactions in model 2.
                reaction_list2.remove(rxn2)
                break
    for rxn1 in reaction_list1:
        for r1, r2 in common_reactions:
            if rxn1 is r1:
                break
        else:
            unique_reactions1.append(rxn1)
    for rxn2 in reaction_list2:
        for r1, r2 in common_reactions:
            if rxn2 is r2:
                break
        else:
            unique_reactions2.append(rxn2)

    print(unique_reactions1)
    print(unique_reactions2)



if __name__ == "__main__":
    main()
