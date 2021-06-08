
import re


def welcom_text():
    print(f"""
    *************************************************
            ༼ಠ ل ಠ༽༼ಠ ل ಠ༽༼ಠ ل ಠ༽༼ಠ ل ಠ༽༼ಠ ل ಠ༽༼ಠ ل ಠ༽༼ಠ ل ಠ༽༼ಠ ل ಠ༽༼ಠ ل ಠ༽༼ಠ ل ಠ༽༼ಠ ل ಠ༽


     hello there i wanna play a game
     i will be asking you some quetion that will
     detrmind what am going to do to you 
    ready or not here we go .......


     ༼ಠ ل ಠ༽༼ಠ ل ಠ༽༼ಠ ل ಠ༽༼ಠ ل ಠ༽༼ಠ ل ಠ༽༼ಠ ل ಠ༽༼ಠ ل ಠ༽༼ಠ ل ಠ༽༼ಠ ل ಠ༽༼ಠ ل ಠ༽༼ಠ ل ಠ༽
    *************************************************
    """)

welcom_text() 


def read(path):
    with open(path,'r') as file:
     content = file.read()
    return contenthumanty

read('assets/madlib_source.txt')


def questions():
    questions=['i will give you a lesson about...',"also about ....","what you did wroung  ....",
    "but theres a way out :P ....","your name is ^.^  ...."
    ]
    values=[]
    
    for i in questions:
        question= input(i)
        values.append(question)
    return values

def merge(text,answers):
    dataText = text
    answer=dataText.format(*answers)
    print(answer)  
    return answer

with open('assets/madlib_result.txt', 'w') as file:
    file.write(merge(read('assets/madlib_source.txt'),questions()))


def parse(path):
    data=re.findall(r"\{(.*?)\}",read(path))  
    return data
print(parse('assets/madlib_source.txt'))