import collections
import autocorrect
import nltk.corpus
nltk.download('words')


def freqAnalysis():
  standardFreq = [("E", 12.702),("T", 9.056),("A", 8.167),("O", 7.507),("I", 6.966),("N", 6.749),("S", 6.327),
                  ("H", 6.094),("R", 5.987),("D", 4.253),("L", 4.025),("C", 2.782),("U", 2.758),("M", 2.406),
                  ("W",2.360),("F", 2.228),("G", 2.015),("Y", 1.974),("P", 1.929),("B", 1.492),("V", 0.978),
                  ("K", 0.772),("J", 0.153),("X", 0.150),("Q", 0.095),("Z", 0.074)] # letter, percentage
  standardFirstLetterFreq = "taoiswcbphfmdrelnguvyjkqxz"
  text = input("Paste the text to analyse below:\n").upper()
  textFreq = collections.Counter(text)
  textFreqPercent = [(i, textFreq[i] / len(text) * 100.0) for i, count in textFreq.most_common()] #sorts and changes freqs to percents
  textFreqPercentAlpha = []
  for t in textFreqPercent:
      if str.isalpha(t[0]) == True:
          textFreqPercentAlpha.append(t)

  estimatedEncoding = []
  for t in range(len(textFreqPercentAlpha)):
      estimatedEncoding.append((textFreqPercentAlpha[t][0], standardFreq[t][0])) #set the esimated to the equivalent in list as a start
  print(estimatedEncoding)
  estimatedText = ""
  for x in range(len(text)): #for every letter of text
    if str.isalpha(text[x]): #if alpha
      for l in estimatedEncoding:#for every estimat
        if text[x] == l[0]:
          estimatedText+=l[1]
    else:
      estimatedText+=text[x]
  
  print(estimatedText)
      
    
    
    

            
          
              
              
freqAnalysis()
