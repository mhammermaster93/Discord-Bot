import random


quotes = [
    #potentially learn JSON and write a JSON file for this.
    'test1',
    'test2',
    'test3'
]


def get_quote():
    return random.choice(quotes)


#read into help.txt


#open the file.
#(path to file, mode)
def write_help():
  with open('help.txt', 'r') as f:
    contents = f.read()
    return (contents)


#code for updating help
#will read and write to help file and update based on the
#commands given
