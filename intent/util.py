import json

sentenceJSON = '{"id": "","data": [{"text": ""}],"isTemplate": false,"count": 0,"isAuto": false}'

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

def parseJSON():
    fileJSON = open('template.json','r')
    stringJSON = ""
    for line in fileJSON:
        stringJSON += line
    return json.loads(stringJSON)
    #print(type(dictJSON['userSays'][0]))
    # 'userSays': [{'id': '', 'data': [{'text': ''}], 'isTemplate': False, 'count': 0, 'isAuto': False}]

def initializeJSON(dictJSON,intentGUID, questionName):
    dictJSON["id"] = intentGUID
    dictJSON["name"] = questionName

def generateGUID(userSaysGUID, n):
    t = userSaysGUID + str(n)
    while(len(t) < 36):
        t += '0'
    return t
def addSentenceToJson(dictJSON, Sentence, userSaysGUID,id):
    y = json.loads(sentenceJSON)
    y["id"] = generateGUID(userSaysGUID, id)
    id+=1
    y["data"]=[{"text" : Sentence}]
    dictJSON["userSays"].append(y)