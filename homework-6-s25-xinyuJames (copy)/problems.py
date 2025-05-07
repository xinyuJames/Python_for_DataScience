import re


def problem1(searchstring):
    """
    Match emails.

    :param searchstring: string
    :return: string
    """
    pattern = r'^[A-Za-z]{1,10}\.[1-7]\d{2}[A-Za-z]*@(shield\.gov|starkindustries\.com)$'

    if re.fullmatch(pattern, searchstring):
        return 'valid'
    else:
        return 'invalid'


def problem2(searchstring):
    """
    Extract author and book.

    :param searchstring: string
    :return: tuple
    """

    pattern = re.compile(
            r'([A-Z][a-zA-Z]+(?: [A-Z][a-zA-Z]+)?)\s+'
            r'wrote\s+'
            r'((?:[A-Z0-9][a-zA-Z0-9]*)(?: [A-Z0-9][a-zA-Z0-9]*){0,2}|books)'
            )
    
    matches = pattern.finditer(searchstring)
    isvalid = None

    for match in matches:
        author = match.group(1).strip()
        book = match.group(2).strip()
        isvalid = (author, book)

    if isvalid:
        return isvalid
    else:
        return ('noauthor', 'noname')


def problem3(searchstring):
    """
    Replace Boy/Girl or boy/girl with Man/Woman or man/woman respectively.

    :param searchstring: string
    :return: string
    """

    pattern = r'\b([A-Z][a-zA-Z]*)\s+(Boy|boy|Girl|girl)\b'
    matches = re.findall(pattern, searchstring)

    if not matches:
        return 'nomatch'
    
    for match in matches:
        hero, gender = match

        if gender == 'Boy':
            subs = 'Man'
        elif gender == 'boy':
            subs = 'man'
        elif gender == "Girl":
            subs = 'Woman'
        elif gender == 'girl':
            subs = 'woman'

        searchstring = searchstring.replace(hero + ' ' + gender, hero + ' ' + subs)

    return searchstring
    
    


if __name__ == '__main__':

    print("\nProblem 1:")
    testcase11 = 'iamironman.123@starkindustries.com'
    print("Student answer: ",problem1(testcase11),"\tAnswer correct?", problem1(testcase11) == 'valid')

    testcase12 = 'Srogers.250captainA@starkindustries.com'
    print("Student answer: ",problem1(testcase12),"\tAnswer correct?", problem1(testcase12) == 'valid')

    testcase13 = 'nickfury.100@shield.gov'
    print("Student answer: ",problem1(testcase13),"\tAnswer correct?", problem1(testcase13) == 'valid')

    testcase14 = 'venom.144@starkindustries.comasdf'
    print("Student answer: ",problem1(testcase14),"\tAnswer correct?", problem1(testcase14) == 'invalid')

    testcase15 = 'hyperion.942@starkindustries.com'
    print("Student answer: ",problem1(testcase15),"\tAnswer correct?", problem1(testcase15) == 'invalid')

    testcase16 = 'greengoblin.567@shield.gov'
    print("Student answer: ",problem1(testcase16),"\tAnswer correct?", problem1(testcase16) == 'invalid')

    testcase17 = 'drdoom324@starkindustries.com'
    print("Student answer: ",problem1(testcase17),"\tAnswer correct?", problem1(testcase17) == 'invalid')

    testcase18 = 'Hosborn.765*abc@shield.gov'
    print("Student answer: ",problem1(testcase18),"\tAnswer correct?", problem1(testcase18) == 'invalid')

    testcase19 = 'vulture.123@shield.com'
    print("Student answer: ",problem1(testcase19),"\tAnswer correct?", problem1(testcase19) == 'invalid')


    print("\nProblem 2:")
    testcase21 = "George Orwell wrote 1984"
    print("Student answer: ",problem2(testcase21),"\tAnswer correct?", problem2(testcase21) == ("George Orwell","1984"))

    testcase22 = "In the 1930s, a Mystery writer wrote Mary Westmacotts. Later it was found that Agatha Christie wrote The Westmacott Novels"
    print("Student answer: ",problem2(testcase22),"\tAnswer correct?", problem2(testcase22) == ("Agatha Christie", "The Westmacott Novels"))

    testcase23 = "Roxette wrote books"
    print("Student answer: ", problem2(testcase23), "\tAnswer correct?", problem2(testcase23) == ("Roxette", "books"))

    testcase24 = "Erin Morgenstern wrote The Starless Sea Book and The Night Circus"
    print("Student answer: ",problem2(testcase24),"\tAnswer correct?", problem2(testcase24) == ("Erin Morgenstern", "The Starless Sea"))

    testcase25 = "Haruki Murakami wrote 1Q84"
    print("Student answer: ",problem2(testcase25),"\tAnswer correct?", problem2(testcase25) == ("Haruki Murakami", "1Q84"))

    testcase26 = "Khaled Hosseini wrote sad books"
    print("Student answer: ",problem2(testcase26),"\tAnswer correct?", problem2(testcase26) == ("noauthor", "noname"))

    testcase27 = "Haruki Murakami wrote Norwegian Wood"
    print("Student answer: ",problem2(testcase27),"\tAnswer correct?", problem2(testcase27) == ("Haruki Murakami", "Norwegian Wood"))


    print("\nProblem 3:")
    testcase31 = 'Spider Boy, I need help!'
    print("Student answer: ",problem3(testcase31),"\tAnswer correct?", problem3(testcase31) == "Spider Man, I need help!")

    testcase32 = 'There is a boy trapped in a burning building Iron Boy'
    print("Student answer: ",problem3(testcase32),"\tAnswer correct?", problem3(testcase32) == "There is a boy trapped in a burning building Iron Man")

    testcase33 = 'Spider Girl, I need help!'
    print("Student answer: ",problem3(testcase33),"\tAnswer correct?", problem3(testcase33) == "Spider Woman, I need help!")

    testcase34 = 'The Invisible girl is a member of the Fantastic Four'
    print("Student answer: ",problem3(testcase34),"\tAnswer correct?", problem3(testcase34) == "The Invisible woman is a member of the Fantastic Four")

    testcase35 = 'There is a boy that needs to be saved from the alien!'
    print("Student answer: ",problem3(testcase35),"\tAnswer correct?", problem3(testcase35) == "nomatch")
