"Q3: How to enroll courses (for students)"
import numpy as np 
import os
import json
import util

D = dict() #check for double occurances
dictJSON = dict()
intentGUID = "a3cb797f-1833-1111-adf3-7d704fa7b300"
userSaysGUID = "a3cb797f-1833-0000-adf5-"

" -- not configured yet -- "
start_phrase = [("จะ",1), ("มันต้อง",1) , ("อยากทราบวิธี",1) , ("แม่ง",0)]
verb = [("สมัคร",1), ("ลงทะเบียน",1), ("ลง",1)]
obj1 = [("รายวิชา",1),("คอร์สเรียน",1),("เรียน",1)]
question_phrase = [("ไหม",1),("อย่างไร",2),("ไง",1)]
manner_phrase = [("ครับ",2),("ค้าบ",0),("หรอ",1),("วะ",0),("",1)]
question_mark = [("?",1), ("",1)]

def generateSentence(n):
    file = open("intent-3-out.txt","w")
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
    jsonFile = open('intent-3.json','w')
    jsonFile.writelines(json.dumps(dictJSON))
    print(json.dumps(dictJSON))

if __name__ == "__main__":
    dictJSON = util.parseJSON()
    util.initializeJSON(dictJSON, intentGUID, "Q3: How to enroll courses (for students)")
    generateSentence(100)