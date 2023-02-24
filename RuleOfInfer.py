def infer(list_of_logic, var):
  final_ans = []
  remember_term = []

  for i in range(len(list_of_logic)):
    
    # print("I : ", i)
    
    current_logic = list_of_logic[i]
    if("predicate" in current_logic.keys()):
      current_term = current_logic["predicate"]
      
    #   print("Current logic : ", current_logic, "\tCurrent term : ", current_term)

      if(len(current_term)==3):
        if(current_term[2] == var):
          for j in range(len(list_of_logic)):

            # print("J : ", j)

            if(i != j):
              logic2 = list_of_logic[j]
              if("extra" in logic2.keys()):
                term2 = logic2["extra"]

                # print("Logic2 : ", logic2, "\tTerm2 : ", term2)

                if(term2[3].lower() == current_term[1]):
                  # temp_term = term2[2]
                  remember_term.append(term2[1])
                  remember_term.append(term2[2])
                  for k in range(len(list_of_logic)):
                    logic3 = list_of_logic[k]

                    # print("K : ", k)
                    # print("Logic 3 : ",logic3)

                    # if(i != k and j != k):
                    if(True):
                      if("AND" in logic3.keys()):
                        term3 = logic3["AND"]
                      elif("IMPLIES" in logic3.keys()):
                        term3 = logic3["IMPLIES"]
                      else:
                        term3 = []

                    #   print("Term3 : ",term3)

                      if(var in term3):
                        # remember_term.append(term3[1])
                        # remember_term.append(temp_term)
                        remember_term.append(term3[3])

    temp_ans = []
    if(len(remember_term) > 0):
      term_ans_str = str(remember_term[0] + "(" + remember_term[1] + "," + remember_term[2] + ")")
      temp_ans.append(term_ans_str)
      temp_ans += remember_term

    # print("Temp_ans : ", temp_ans)

    if(temp_ans != [] and temp_ans not in final_ans):
      final_ans.append(temp_ans)
    
  return final_ans