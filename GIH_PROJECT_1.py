import pandas as pd

output = pd.DataFrame()
df = pd.DataFrame()

while True:
    name = input("name:")
    surname = input("surname:")
    school_no = input("no:")
    score = int(input("score: "))
    letter_grade = ''
    if score > 89 :
        print("geçme notunuz : AA ")
        letter_grade = 'AA'
    elif score > 79 :
        print("geçme notunuz : BA ")
        letter_grade = 'BA'
    elif score > 69:
        print("geçme notunuz : BB ")
        letter_grade = 'BB'
    elif score > 59 :
        print("geçme notunuz : CB ")
        letter_grade = 'CB'
    elif score > 49:
        print("geçme notunuz : CC ")
        letter_grade = 'CC'
    else :
        print("KALDINIZ!")
        letter_grade = 'FF'

    df_new_row = pd.DataFrame({ 'a': [1], 'b': [2] })
    df = pd.concat([df, df_new_row])


    print("Press 0 to exit...\nor press any key to continue")
    process = input()
    if process == '0':
        break

df.to_excel(r'results.xlsx', index = False)