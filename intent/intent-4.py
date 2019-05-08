"Q4: How to view announcement?"

import numpy as np
import os
import json
import util

D = dict()  # check for double occurances

start_phrase = [("จะ", 1), ("อยากทราบว่า", 2),
                ("อยากรู้ว่า", 1), ("มิทราบว่า", 2), ("", 1)]
verb = [("ดู", 1), ("มี", 1)]
obj1 = [("announcement", 1), ("การประกาศ", 1), ("ประกาศ", 1), ("announce", 1)]
from_word = [("จาก", 1), ("ของ", 1), ("โดย", 1)]
obj2 = [("อาจารย์", 1), ("ครู", 1), ("รายวิชา", 1), ("วิชา", 1)]
question_phrase = [("ยังไง", 1), ("อย่างไร", 2), ("ไง", 0), ("ที่ไหน", 1), ("อยู่ที่ไหน", 1), ("ไหม", 1), ("ยังงัย", 0)]
manner_phrase = [("ค่ะ", 1), ("ครับ", 1), ("ค่า", 0), ("คับ", 0), ("หรอ", 1), ("วะ", 0), ("อ่ะ", 1), ("อ่า", 0), ("", 1)]
question_mark = [("?", 1), ("", 1)]

def generateSentence(n):
    file = open("intent-4-out.txt", "w")
    a = []
    for i in range(n):
        s = []
        s.append(start_phrase[np.random.randint(0, len(start_phrase))])
        s.append(verb[np.random.randint(0, len(verb))])
        s.append(obj1[np.random.randint(0, len(obj1))])
        s.append(from_word[np.random.randint(0, len(from_word))])
        s.append(obj2[np.random.randint(0, len(obj2))])

        s.append(question_phrase[np.random.randint(0, len(question_phrase))])
        s.append(manner_phrase[np.random.randint(0, len(manner_phrase))])
        s.append(question_mark[np.random.randint(0, 2)])

        if not util.validatePoliteness(s):
          continue

        s = util.list2Sentence(s)

        if(s in D):
            i -= 1
            continue
        D[s] = True
        a.append(s)
    for line in a:
        file.writelines(line + "\n")


if __name__ == "__main__":
    generateSentence(2000)
