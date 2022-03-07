def cleanWord(dirtyWord):
    clean = ""
    for c in dirtyWord:
        if c.isalpha():
            clean = clean + c.lower()
    return clean #returns the result to clean = cleanWord(word)





words = {}
sentence = input("input a sentence to count: ")
sentence = "the quick-brown fox jumped over the lazy fox!"
wordlist = sentence.split()

for word in words:
    #word = word.lower()
    clean = cleanWord(word)
    if len(word) > 0:
        if word in wordlist:
            wordlist[word] += 1
        else:
            wordlist[word] = 1
#print(len(wordlist))





 #   if word in words:
       # words[word] += 1
  #  else:
   #     words[word] = 1
for k, v in wordlist.items():
    print(k, ":", v)