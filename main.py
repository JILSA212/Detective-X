from formalLang import formal
from RuleOfInfer import infer
from Conclude import write

import nltk
nltk.download("punkt", quiet=True)
nltk.download("averaged_perceptron_tagger", quiet=True)

if(__name__ == "__main__"):
    # input_sentenses = ["Den is a man.", "All man are mortal."]
    input_sentenses = ["Some cars are red.", "Maruti is a car."]
   
    var = "a"
    pos_tagged_list = []

    for line in input_sentenses:
        pos_tagged_list.append(nltk.pos_tag(nltk.word_tokenize(line)))

    formal_lang = []

    for line in pos_tagged_list:
        formal_lang.append(formal(line, var))

    final_ans = []

    final_ans.append(infer(formal_lang, var))
    # print(final_ans)

    for lines in final_ans[0]:
        print(write(lines))