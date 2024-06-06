print("выбери имя[1]/фамилия[2]/имя и фамилия[3]")
a=input()
def razbor(word):
    gl=["а","у","о","и","э","ы","я","ю","е","ё"]
    countgl=0
    countsogl=0
    for letter in word:
        for letmass in gl:
            if letter == letmass:
                countgl=countgl+1
            else:
                ["б","в","г","д","ж","з","й","к","л","м","н","п","р","с","т","ф","х","ц","ч","ш",
                "щ","ъ","ь","э","ю","я"]
                countsogl=countsogl+1
    return countgl,countsogl
if a=="1":
    print("ты выбрал имя,теперь напиши его")
    name=input()
    b = razbor(name)
if a=="2":
    print("ты выбрал фамилию,теперь напиши ее")
    surname=input()
    b = razbor(surname)
if a == "3":
    print("ты выбрал имя и фамилию,теперь напиши их")
    both = input()
    b = razbor(both)
print("согласные")
print(b[1])
print("гласные")
print(b[0])





