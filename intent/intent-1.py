"Q1: How to input scores?"

import numpy as np
import os
import json
#0 = bad-mannered, 1 = generic ,2 = well-mannered
D = dict() #check for double occurances
dictJSON = dict()
intent_GUID = "a3cb797f-1833-1111-adf3-7d704fa7b000"
user_says_GUID = "a3cb797f-1833-0000-adf3-"
sentenceJSON = '{"id": "","data": [{"text": ""}],"isTemplate": false,"count": 0,"isAuto": false}'
start_phrase = [("จะ",1), ("ต้อง",1) , ("อยากทราบว่า",2) , ("อยากรู้ว่า",1), ("ทำ",1)]
verb = [("เพิ่ม",1), ("กรอก",1), ("ใส่",1), ("เติม",1)]
obj1 = [("คะแนน",1),("แต้ม",1),("point",1),]
#####optional
<<<<<<< HEAD
verb2 = [("ให้",1), ("ให้แก่",2),("ให้กับ",1), ("สำหรับ",2)]
obj2 = [("เด็ก",1),("นักเรียน",2),("เด็กๆ",1), ("นิสิต",2), ("นักศึกษา",2), ("ลูกศิษย์",2)]
=======
verb2 = ["ให้", "ให้แก่","ให้กับ", "สำหรับ"]
obj2 = ["เด็ก","นักเรียน","เด็กๆ", "นิสิต", "นักศึกษา", "ลูกศิษย์"]
>>>>>>> refs/remotes/origin/master
#####
question_phrase = [("ยังไง",1),("อย่างไร",2),("ไง",1),("วิธีอะไร",2),("วิธีไหน",1)]
end_phrase = [("ดี",1),("",1)]
manner_phrase = [("ค่ะ",2), ("ครับ",2),("ค่า",1),("คับ",1),("หรอ",1),("วะ",0),("อ่ะ",1),("อ่า",1),("",1)]
question_mark = [("?",1), ("",1)]
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
        s = []
        s.append(start_phrase[np.random.randint(0,len(start_phrase))])
        s.append(verb[np.random.randint(0,len(verb))])
        s.append(obj1[np.random.randint(0,len(obj1))])
        if(np.random.randint(0,2) != 0):
            s.append(verb2[np.random.randint(0,len(verb2))])
            s.append(obj2[np.random.randint(0,len(obj2))])
        s.append(question_phrase[np.random.randint(0,len(question_phrase))])
        s.append(end_phrase[np.random.randint(0,len(end_phrase))])
        s.append(manner_phrase[np.random.randint(0,len(manner_phrase))])
        s.append(question_mark[np.random.randint(0,1)])
        check0 = False
        check2 = False
        for item in s:
            if(item[1] == 0): check0 = True
            elif(item[1] == 2): check2 = True
        
        
        if(s in D):
            i -= 1
            continue
        D[s] = True
        a.append(s)
        addSentenceToJson(s,i)
    for line in a:
        file.writelines(line + "\n")
    jsonFile = open('intent-1.json','w')
    jsonFile.writelines(json.dumps(dictJSON))
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
    generateSentence(2000)