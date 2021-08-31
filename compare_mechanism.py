
import cantera as ct
from logging import error


class Mechanism():
    def __init__(self, cti_file):
        # TODO check if cti file exists
        sol = ct.Solution(cti_file)
        for species in sol.species():
            print(species)
        print(f'{len(sol.species())} species imported')
        surf = ct.Interface(cti_file, 'surface1', [gas])
        #for rxn in sol.reactions():
        #     print(rxn)


def import_model(cti):
    Mechanism(cti)
    #print(cti)
    #sol1 = ct.Solution(cti)
    #return sol1


def main():
    import sys
    if len(sys.argv) < 3:
        error("Must provide two input cti's")

    cti1 = sys.argv[1]
    cti2 = sys.argv[2]

    import_model(cti1)
    import_model(cti2)


if __name__ == "__main__":
    main()
