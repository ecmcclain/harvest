############
# Part 1   #
############
#okay justreviewingnotes / yeah im reading through the lab now

class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""
        #filling in the initialization temporarily
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller # okay, saw the updated commenti think since they dont all have this attribute, it should be a list? / NEVERMIND! looks like it should be a boolean
        self.name = name

        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []
    
    muskmelon = MelonType(
        "musk", 
        1998,   
        "green", 
        True,   
        True,
        "Muskmelon"
    )
    muskmelon.add_pairing("mint")

    casaba = MelonType(
        "cas",
        2003,
        "orange",
        True,
        False,
        "Casaba"
    )
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")


    crenshaw = MelonType(
        "cren",
        1996,
        "green",
        False,
        False,
        "Crenshaw"
    )
    crenshaw.add_pairing("prosciutto")

    yellow_watermelon = MelonType(
        "yw",
        2013,
        "yellow",
        True,
        True,
        "Yellow Watermelon"
    )
    yellow_watermelon.add_pairing("ice cream")

    # Fill in the rest

    #add all these melons we just initialized to the all_melon_types_list
    all_melon_types.extend([muskmelon, casaba, crenshaw, yellow_watermelon])

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon in melon_types:
        print(f"\n{melon.name} pairs well with")
        for item in melon.pairings: 
            print(f"- {item}")


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    reporting_codes = {}

    for melon in melon_types:
        reporting_codes[melon.code] = melon

    
    return reporting_codes



############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(
        self, melon_type, shape, color, field, harvester
    ):
        self.melon_type = melon_type # instance of class MelonType
        self.shape = shape
        self.color = color
        self.field = field
        self.harvester = harvester

    def is_sellable(self):
        if self.shape > 5 and self.color > 5 and self.field != 3:
            return True
        return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest
    melons = []
    melons_by_id = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')

    melons.extend([melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7, melon_8, melon_9])

    return melons

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    for melon in melons:
        if melon.is_sellable():
            sellable = "(CAN BE SOLD)" 
        else:
            sellable = "(NOT SELLABLE)"
        print(f"Harvested by {melon.harvester} from field {melon.field} {sellable}")

    # Fill in the rest


## FOR TESTING ## 
melon_kinds = make_melon_types()
codes = make_melon_type_lookup(melon_kinds)
print(codes.items())
print_pairing_info(melon_kinds)

melons = make_melons(melon_kinds)
print(melons[0].melon_type.name)

get_sellability_report(melons)
