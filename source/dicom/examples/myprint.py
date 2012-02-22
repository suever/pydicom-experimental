# myprint.py
"""Example of printing a dataset in your own format"""
# Copyright (c) 2008 Darcy Mason
# This file is part of pydicom, relased under an MIT license.
#    See the file license.txt included with this distribution, also
#    available at http://pydicom.googlecode.com

def myprint(dataset, indent=0):
    """Go through all item in the dataset and print.
    Modelled after Dataset._PrettyStr()
    """
    dont_print = ['Pixel Data', 'File Meta Information Version']

    indent_string = "   " * indent
    next_indent_string = "   " *(indent+1)

    for data_element in dataset:
        if data_element.VR == "SQ":   # a sequence
            print indent_string, data_element.name
            for sequence_item in data_element.value:
                myprint(sequence_item, indent+1)
                print next_indent_string + "---------"
        else:
            if data_element.name in dont_print:
                print """<item not printed -- in the "don't print" list>"""
            else:
                repr_value = repr(data_element.value)
                if len(repr_value) > 50:
                    repr_value = repr_value[:50] + "..."
                print indent_string, data_element.name, "=", repr_value

if __name__ == "__main__":
    import dicom
    import sys
    usage = """Usage: myprint filename"""
    if len(sys.argv) != 2:
        print usage
        sys.exit()
        
    ds = dicom.read_file(sys.argv[1])
    myprint(ds)