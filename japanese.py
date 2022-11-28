from random import randrange
import random

class Japanese:
    def __init__(self):
        self.roman = ('a','i','u','e','o','ka','ki','ku','ke','ko','sa','shi','su','se','so','ta','chi','tsu','te','to','na','ni','nu','ne','no')
        self.hiragana = ('あ','い','う','え','お','か','き','く','け','こ','さ','し','す','せ','そ','た','ち','つ','て','と','な','に','ぬ','ね','の')
        self.katakana = ('ア','イ','ウ','エ','オ','カ','キ','ク','ケ','コ','サ','シ','ス','セ','ソ','タ','チ','ツ','テ','ト','ナ','ニ','ヌ','ネ','ノ')
        self.dictionary = {r:(h,k) for r,h,k in zip(self.roman,self.hiragana,self.katakana)}
        self.counterReset(2)
        self.test()

    def counterReset(self, counter):
        self.dictionaryHiraCount = [[c,counter] for c,h in enumerate(self.hiragana)]
        self.dictionaryKataCount = [[c,counter] for c,k in enumerate(self.katakana)]

    def randomSingleHira(self):
        hira = random.choice(self.dictionaryHiraCount)
        hiraChar = self.hiragana[hira[0]]
        self.dictionaryHiraCount.remove(hira)
        if hira[1]-1 > 0:
            self.dictionaryHiraCount.append([hira[0],hira[1]-1])
        return hiraChar, hira[0]

    def randomSingleKata(self):
        kata = random.choice(self.dictionaryKataCount)
        kataChar = self.katakana[kata[0]]
        self.dictionaryKataCount.remove(kata)
        if kata[1]-1 > 0:
            self.dictionaryKataCount.append([kata[0],kata[1]-1])
        return kataChar, kata[0]

    def writing(self):
        word = ''
        wordAnswer = ''
        wordKataAnswer = ''
        for a in range(5):
            randomChar = self.randomSingleHira()
            wordAnswer += randomChar[0]
            wordAnswer += ' '
            wordKataAnswer += self.katakana[randomChar[1]]
            wordKataAnswer += ' '
            char = self.roman[randomChar[1]]
            word += char
            word += ' '
        print(word)
        answer = input('Enter to show answer')
        print(wordAnswer)
        print(wordKataAnswer)
        print('---------------------------')

    def reading(self):
        word = ''
        wordPron = ''
        for a in range(5):
            randomChar = random.choice([self.randomSingleHira(),self.randomSingleKata()])
            char = self.roman[randomChar[1]]
            wordPron += char
            wordPron += ' '
            word += randomChar[0]
            word += ' '
        print(word)
        answer = str(input('Enter the answer:'))
        if answer.strip() == wordPron.strip():
            print('Correct')
        else:
            print(f'Wrong\nAnswer is:{wordPron}')
        print('----------------------------')

    def test(self):
        exit = False
        while exit == False:
            choice = input('Choose writing(w) or reading(r) test:')
            back = False
            if choice == 'w':
                while back == False:
                    try:
                        self.writing()
                        change = input('Next or Back(b)>>>>>>>>>>>>')
                        if change == 'b':
                            back = True
                    except Exception as e:
                        print(e)
                        print('Test finished')
                        break
            if choice == 'r':
                while back == False:
                    try:
                        self.reading()
                        change = input('Next or Back(b)>>>>>>>>>>>>')
                        if change == 'b':
                            back = True
                    except Exception as e:
                        print(e)
                        print('Test finished')
                        break
            self.counterReset(2)
            change = input('Next test or exit(e)')
            if change == 'e':
                exit = True
            

a = Japanese()