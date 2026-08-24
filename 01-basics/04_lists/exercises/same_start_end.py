

def match_words(words):

    ctr = 0


    for x in words:
       if len(x) > 1 and  x[0] == x[-1]:
          ctr += 1
    return ctr


print(match_words([ "aanaa", "is"," developer ", "who", "love" , "python"]))
