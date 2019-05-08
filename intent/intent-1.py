"Q1: How to input scores?"

import numpy as np 
import os
import json

D = dict() #check for double occurances
dictJSON = dict()
intent_GUID = "a3cb797f-1833-1111-adf3-7d704fa7b000"
user_says_GUID = "a3cb797f-1833-0000-adf3-"
sentenceJSON = '{"id": "","data": [{"text": ""}],"isTemplate": false,"count": 0,"isAuto": false}'
start_phrase = ["จะ", "ต้อง" , "อยากทราบว่า" , "อยากรู้ว่า", "ทำ"]
verb = ["เพิ่ม", "กรอก", "ใส่", "เติม"]
obj1 = ["คะแนน","แต้ม","point",]
#####optional
verb2 = ["ให้", "ให้แก่","ให้กับ", "สำหรับ"]
obj2 = ["เด็ก","นักเรียน","เด็กๆ", "นิสิต", "นักศึกษา", "ิลูกศิษย์"]
#####
question_phrase = ["ยังไง","อย่างไร","ไง","วิธีอะไร","วิธีไหน"]
end_phrase = ["ดี",""]
manner_phrase = ["ค่ะ", "ครับ","ค่า","คับ","หรอ","วะ","อ่ะ","อ่า",""]
question_mark = ["?", ""]
def generateGUID(n):
    t = user_says_GUID + str(n)
    while(len(t) < 36):
        t += '0'
    return t
def addSentenceToJson(Sentence,id):
    y = json.loads(sentenceJSON)
    print(y)
    y["id"] = generateGUID(id)
    id+=1
    y["data"]=[{"text" : Sentence}]
    dictJSON["userSays"].append(y)
def generateSentence(n):
    file = open("intent-1-out.txt","w")
    a = []
    for i in range(n):
        s = ""
        s += start_phrase[np.random.randint(0,len(start_phrase))]
        s += verb[np.random.randint(0,len(verb))]
        s += obj1[np.random.randint(0,len(obj1))]

        if(np.random.randint(0,2) != 0):
            s += verb2[np.random.randint(0,len(verb2))] + obj2[np.random.randint(0,len(obj2))]
        s += question_phrase[np.random.randint(0,len(question_phrase))]
        s += end_phrase[np.random.randint(0,len(end_phrase))]
        s += manner_phrase[np.random.randint(0,len(manner_phrase))]
        s += question_mark[np.random.randint(0,1)]
        
        if(s in D):
            i -= 1
            continue
        D[s] = True
        a.append(s)
        addSentenceToJson(s,i)
    for line in a:
        file.writelines(line + "\n")
    jsonFile = open('intent-1.json','w')
    #jsonFile.writelines(json.dumps(dictJSON))
    print(json.dumps(dictJSON))
def parseJSON():
    fileJSON = open('template.json','r')
    stringJSON = ""
    for line in fileJSON:
        stringJSON += line
    return json.loads(stringJSON)
    #print(type(dictJSON['userSays'][0]))
    # 'userSays': [{'id': '', 'data': [{'text': ''}], 'isTemplate': False, 'count': 0, 'isAuto': False}] 
def initializeJSON():
    global dictJSON
    dictJSON["id"] = intent_GUID
    dictJSON["name"] = "Q1: How to input scores?"
if __name__ == "__main__":
    dictJSON = parseJSON()
    initializeJSON()
    generateSentence(5)