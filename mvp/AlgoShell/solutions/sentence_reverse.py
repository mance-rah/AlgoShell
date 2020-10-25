def sentence_reverse(arr):
 
  wordList = convertCharListToWordList(arr)
  reversedWordList = list(reversed(wordList))
  return convertWordListToCharList(reversedWordList)

def convertCharListToWordList(arr):
  words = []
  currWord = ''
  for char in arr:
    if char.isalpha():
      currWord += char
    else:
      words.append(currWord)
      currWord = ''
  words.append(currWord)
  return words

def convertWordListToCharList(arr):
  chars = []
  for word in arr:
    splitWord = list(word)
    chars += splitWord
    chars.append(' ')
  return chars[:-1]
      

arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
                'm', 'a', 'k', 'e', 's', '  ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]