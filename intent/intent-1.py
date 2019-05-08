"Q1: How to input scores?"

import numpy as np
import os
import json
import util

#0 = bad-mannered, 1 = generic ,2 = well-mannered
D = dict() #check for double occurances
dictJSON = dict()
intentGUID = "a3cb797f-1833-1111-adf3-7d704fa7b000"
userSaysGUID = "a3cb797f-1833-0000-adf3-"
start_phrase = [("จะ",1), ("ต้อง",1) , ("อยากทราบว่า",2) , ("อยากรู้ว่า",1), ("ทำ",1)]
verb = [("เพิ่ม",1), ("กรอก",1), ("ใส่",1), ("เติม",1)]
obj1 = [("คะแนน",1),("แต้ม",1),("point",1),]
#####optional
verb2 = [("ให้",1), ("ให้แก่",2),("ให้กับ",1), ("สำหรับ",2)]
obj2 = [("เด็ก",1),("นักเรียน",2),("เด็กๆ",1), ("นิสิต",2), ("นักศึกษา",2), ("ลูกศิษย์",2)]
#####
question_phrase = [("ยังไง",1),("อย่างไร",2),("ไง",1),("วิธีอะไร",2),("วิธีไหน",1)]
end_phrase = [("ดี",1),("",1)]
manner_phrase = [("ค่ะ",2), ("ครับ",2),("ค่า",1),("คับ",1),("หรอ",1),("วะ",0),("อ่ะ",1),("อ่า",1),("",1)]
question_mark = [("?",1), ("",1)]


def generateSentence(n):
    file = open("intent-1-out.txt","w")
    a = []
    i = 0
    while i < n:
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
    jsonFile = open('intent-1.json','w')
    jsonFile.writelines(json.dumps(dictJSON))
    print(json.dumps(dictJSON))


if __name__ == "__main__":
    dictJSON = util.parseJSON()
    util.initializeJSON(dictJSON, intentGUID, "Q1: How to input scores?")
    generateSentence(2000)