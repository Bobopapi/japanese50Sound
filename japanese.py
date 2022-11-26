from random import randrange
import random

class Japanese:
    def __init__(self):
        self.roman = ['a','i','u','e','o','ka','ki','ku','ke','ko','sa','shi','su','se','so','ta','chi','tsu','te','to','na','ni','nu','ne','no']
        self.hiragana = ['あ','い','う','え','お','か','き','く','け','こ','さ','し','す','せ','そ','た','ち','つ','て','と','な','に','ぬ','ね','の']
        self.katakana = ['ア','イ','ウ','エ','オ','カ','キ','ク','ケ','コ','サ','シ','ス','セ','ソ','タ','チ','ツ','テ','ト','ナ','ニ','ヌ','ネ','ノ']
        self.dictionary = {r:[h,k] for r,h,k in zip(self.roman,self.hiragana,self.katakana)}
        self.test()

    def singleHira(self, roman):
        return self.dictionary.get(roman)[0]

    def singleKata(self, roman):
        return self.dictionary.get(roman)[1]

    def writing(self):
        word = ''
        wordAnswer = ''
        wordKataAnswer = ''
        for a in range(5):
            char = random.choice(self.roman)
            word += char
            word += ' '
            wordAnswer += self.singleHira(char)
            wordAnswer += ' '
            wordKataAnswer += self.singleKata(char)
            wordKataAnswer += ' '
        print(word)
        answer = input('Enter to show answer')
        print(wordAnswer)
        print(wordKataAnswer)
        print('---------------------------')

    def reading(self):
        word = ''
        wordPron = ''
        for a in range(5):
            char = self.roman[random.randrange(len(self.dictionary))]
            wordPron += char
            wordPron += ' '
            word += random.choice([self.singleHira(char),self.singleKata(char)])
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
                    self.writing()
                    change = input('Next or Back(b)>>>>>>>>>>>>')
                    if change == 'b':
                        back = True
            if choice == 'r':
                while back == False:
                    self.reading()
                    change = input('Next or Back(b)>>>>>>>>>>>>')
                    if change == 'b':
                        back = True
            change = input('Next test or exit(e)')
            if change == 'e':
                exit = True
            

a = Japanese()