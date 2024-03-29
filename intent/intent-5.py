"Q5: How to access portfolio"

import numpy as np 
import os
import json
import util

D = dict() #check for double occurances
dictJSON = dict()
intentGUID = "a3cb797f-1833-1111-adf3-7d704fa7b400"
userSaysGUID = "a3cb797f-1833-0000-adf6-"

start_phrase = [("จะ",1), ("ต้อง",1) , ("อยากทราบว่า",2) , ("อยากรู้ว่า",1) , ("มัน",0)]
verb = [("ดู",1)]
obj1 = [("portfolio",1),("คะแนน",1),("คะแนนเก็บ",1),("คะแนนสอบ",1),("",1)]
question_phrase = [("ยังไง",1),("อย่างไร",2),("ไง",1),("ที่ไหน",1),("ได้ที่ไหน",1)]
manner_phrase = [("ค่ะ",2), ("ครับ",2),("ค่า",1),("คับ",1),("หรอ",1),("วะ",0),("อ่ะ",1),("อ่า",1),("",1),("วะสาส",0)]
question_mark = [("?",1), ("",1)]


def generateSentence(n):
    file = open("intent-5-out.txt","w")
    a = []
    i = 0
    while i < n:
        s = []
        s.append(start_phrase[np.random.randint(0,len(start_phrase))])
        s.append(verb[np.random.randint(0,len(verb))])
        s.append(obj1[np.random.randint(0,len(obj1))])

        s.append(question_phrase[np.random.randint(0,len(question_phrase))])
        s.append(manner_phrase[np.random.randint(0,len(manner_phrase))])
        s.append(question_mark[np.random.randint(0,2)])

        if not util.validatePoliteness(s):
            continue
        s = ''.join([e[0] for e in s])
        if(s in D):
            continue
        D[s] = True
        a.append(s)
        util.addSentenceToJson(dictJSON,s,userSaysGUID,i)
        i += 1
    for line in a:
        file.writelines(line + "\n")
    jsonFile = open('intent-5.json','w')
    jsonFile.writelines(json.dumps(dictJSON))
    print(json.dumps(dictJSON))

if __name__ == "__main__":
    dictJSON = util.parseJSON()
    util.initializeJSON(dictJSON, intentGUID, "Q5: How to access portfolio")
    generateSentence(2000)