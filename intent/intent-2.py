"Q2: How to check for assignment?"

import numpy as np 
import os
import json

D = dict() #check for double occurances

start_phrase = ["จะ", "ต้อง" , "อยากทราบว่า" , "อยากรู้ว่า"]
verb = ["ดู", "มี", "ทำ"]
obj1 = ["hw","homework","การบ้าน","งานค้าง","งานที่ต้องส่ง","assignment"]
question_phrase = ["ยังไง","อย่างไร","ไง","ที่ไหน"]
manner_phrase = ["ค่ะ", "ครับ","ค่า","คับ","หรอ","วะ","อ่ะ","อ่า",""]
question_mark = ["?", ""]

def generateSentence(n):
    file = open("intent-2-out.txt","w")
    a = []
    for i in range(n):
        s = ""
        s += start_phrase[np.random.randint(0,len(start_phrase))]
        s += verb[np.random.randint(0,len(verb))]
        s += obj1[np.random.randint(0,len(obj1))]

        s += question_phrase[np.random.randint(0,len(question_phrase))]
        s += manner_phrase[np.random.randint(0,len(manner_phrase))]
        s += question_mark[np.random.randint(0,2)]       
        if(s in D):
            i -= 1
            continue
        D[s] = True
        a.append(s)
    for line in a:
        file.writelines(line + "\n")

if __name__ == "__main__":
    generateSentence(1000)