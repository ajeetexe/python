from user_package import AddToSentence


sentence_collect = []
while True:
    msg = input('Add Something')
    if msg != '/end':
        sentence_collect.append(AddToSentence.add_to_sentence(msg))
    else:
        break
print(" ".join(sentence_collect))
