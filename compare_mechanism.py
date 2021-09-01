
from rmgpy.molecule import adjlist
import cantera as ct
from logging import error
from rmgpy.chemkin import load_species_dictionary
from rmgpy.species import Species


def ct2rmg_species(ct_spec, species_dictionary):
    rmg_spec = species_dictionary[ct_spec.name]
    # don't worry about thermo yet
    
     def __init__(self, coeffs=None, Tmin=None, Tmax=None, E0=None, label='', comment=''):
        HeatCapacityModel.__init__(self, Tmin=Tmin, Tmax=Tmax, E0=E0, label=label, comment=comment)
        self.coeffs = coeffs


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

    model1 = import_model(cti1, dict1)
    model2 = import_model(cti2, dict2)

    common_sp, unique_sp1, unique_sp2 = compare_species(model1, model2)


if __name__ == "__main__":
    main()
