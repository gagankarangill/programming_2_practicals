COLOUR_CODES = { "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb", "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378", "aquamarine2": "#76eec6", "aquamarine4": "#458b74", "azure1": "#f0ffff","azure2": "#e0eeee", "azure3": "#c1cdcd", "azure4": "#838b8b"}

colour_name = input("Enter  name of your color please: ")
while colour_name != "":
    print("The code for \"{}\" is {}".format(colour_name,
                                             COLOUR_CODES.get(colour_name)))
    colour_name = input(Enter name of your color please: ")