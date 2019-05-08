def validatePoliteness(sentenceList):
  veryPolite = False
  veryImpolite = False
  for e in sentenceList:
    if e[1] == 2:
      veryPolite = True
      break
  for e in sentenceList:
    if e[1] == 0:
      veryImpolite = True
      break
  return not (veryPolite and veryImpolite)

def list2Sentence(sentenceList):
  return ''.join([e[0] for e in sentenceList])