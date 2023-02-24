import nltk
from nltk.stem import WordNetLemmatizer 

nltk.download("wordnet", quiet=True)
nltk.download("omw-1.4", quiet=True)

lemmatizer = WordNetLemmatizer()

def formal(pos_tagged, var):
  final_ans = {}
  remember_var = []

  if(len(pos_tagged) > 0):
    if(pos_tagged[0][1].lower() == "dt"):
      if(pos_tagged[0][0].lower() in ["some", "any"]):
        temp_term = "THERE EXISTS(" + var + ")"
        final_ans["proposition"] = [str(temp_term), var]
      elif(pos_tagged[0][0].lower() in ["all"]):
        temp_term = "FOR ALL(" + var + ")"
        final_ans["proposition"] = [str(temp_term), var]
      elif(pos_tagged[0][0].lower() in ["not", "no"]):
        temp_term = "NOT"
        final_ans["proposition"] = [str(temp_term), var]
        if(pos_tagged[1][1].lower() == "dt"):
          if(pos_tagged[1][0].lower() in ["some", "any"]):
            temp_term = "NOT THERE EXISTS(" + var + ")"
            final_ans["proposition"] = [str(temp_term), var]
          elif(pos_tagged[1][0].lower() in ["all"]):
            temp_term = "NOT FOR ALL(" + var + ")"
            final_ans["proposition"] = [str(temp_term), var]
        else:
          temp_term = "THERE EXISTS(" + var + ")"
          final_ans["proposition"] = [str(temp_term), var]
    
    for i in range(len(pos_tagged)):
      if(pos_tagged[i][1].lower() in ["nn", "nns"]):
        if(i > 0 and pos_tagged[i-1][0].lower() == "the"):
          remember_var.append(pos_tagged[i][0])
        else:
          temp_term = str(lemmatizer.lemmatize(pos_tagged[i][0].lower()) + " (" + var + ")")
          final_ans["predicate"] = [str(temp_term), lemmatizer.lemmatize(pos_tagged[i][0].lower()), var]
        break

    for i in range(len(pos_tagged)):
      if(pos_tagged[i][1].lower() in ["nnp", "nnps"]):
        remember_var.append(pos_tagged[i][0])
        break


    for i in range(len(pos_tagged)):
      if(pos_tagged[i][1].lower() in ["vb", "vbd", "vbg", "vbn", "vbz", "vbp"]):
        for j in range(i, len(pos_tagged)):
          if(pos_tagged[j][1].lower() in ["nn", "nns", "jj", "jjr", "jjs"]):
            if(len(remember_var) != 0):
              new_var = remember_var[0]
              remember_var = []
            else:
              new_var = var
            temp_term = str(lemmatizer.lemmatize(pos_tagged[i][0].lower()) + "(" + new_var + ", " + lemmatizer.lemmatize(pos_tagged[j][0].lower()) + ")")
            
            # print("VB temp_term : ", temp_term)
            
            try:
              
              # print("VB try")
              # print("THERE EXISTS" in final_ans["proposition"][0])
              # print("FOR ALL" in final_ans["proposition"][0])
              
              if("THERE EXISTS" in final_ans["proposition"][0]):
                final_ans["AND"] = [str(temp_term), lemmatizer.lemmatize(pos_tagged[i][0].lower()), new_var, lemmatizer.lemmatize(pos_tagged[j][0].lower())]
              elif("FOR ALL" in final_ans["proposition"][0]):
                final_ans["IMPLIES"] = [str(temp_term), lemmatizer.lemmatize(pos_tagged[i][0].lower()), new_var, lemmatizer.lemmatize(pos_tagged[j][0].lower())]
            except:

              # print("VB except")

              if("predicate" in final_ans.keys()):
                final_ans["extra"] = [str(temp_term), lemmatizer.lemmatize(pos_tagged[i][0].lower()), new_var, lemmatizer.lemmatize(pos_tagged[j][0].lower())]
              else:
                final_ans["predicate"] = [str(temp_term), lemmatizer.lemmatize(pos_tagged[i][0].lower()), new_var, lemmatizer.lemmatize(pos_tagged[j][0].lower())]

    for i in range(len(pos_tagged)):
      if(pos_tagged[i][1].lower() in ["md"]):
        for j in range(i, len(pos_tagged)):
          if(pos_tagged[j][1].lower() in ["vb", "vbd", "vbg", "vbn", "vbz", "vbp"]):
            if(len(remember_var) != 0):
              new_var = remember_var[0]
              remember_var = []
            else:
              new_var = var
            temp_term = str(lemmatizer.lemmatize(pos_tagged[i][0].lower()) + "(" + new_var + ", " + lemmatizer.lemmatize(pos_tagged[j][0].lower()) + ")")
            try:
              if("THERE EXISTS" in final_ans["proposition"][0]):
                final_ans["AND"] = [str(temp_term), lemmatizer.lemmatize(pos_tagged[i][0].lower()), new_var, lemmatizer.lemmatize(pos_tagged[j][0].lower())]
              elif("FOR ALL" in final_ans["proposition"][0]):
                final_ans["IMPLIES"] = [str(temp_term), lemmatizer.lemmatize(pos_tagged[i][0].lower()), new_var, lemmatizer.lemmatize(pos_tagged[j][0].lower())]
            except:
              if("predicate" in final_ans.keys()):
                final_ans["extra"] = [str(temp_term), lemmatizer.lemmatize(pos_tagged[i][0].lower()), new_var, lemmatizer.lemmatize(pos_tagged[j][0].lower())]
              else:
                final_ans["predicate"] = [str(temp_term), lemmatizer.lemmatize(pos_tagged[i][0].lower()), new_var, lemmatizer.lemmatize(pos_tagged[j][0].lower())]

    # print("Final ans : ",final_ans)
    return final_ans           