import json
from difflib import get_close_matches


data = json.load(open('document/data.json'))


def dictionary(args):
    args = args.title()
    if args in data:
        return data[args]
    elif len(get_close_matches(args, data.keys())) > 0:
        yesOrno = input('Did you mean {} instead, Enter Y for Yes or N for No:- '.format(
            get_close_matches(args, data.keys())[0]))
        if yesOrno == 'y' or yesOrno == 'Y':
            return data[get_close_matches(args, data.keys())[0]]
        elif yesOrno == 'n':
            return 'The word you searching not exists in our storage'
        else:
            return "We don't understand your entry"
    else:
        return "The word does't exit, We are really sorry!!!"


word = input('Enter Word: ')
print(dictionary(word))
