from random import randrange
import random

class Japanese:
    def __init__(self):
        self.roman = ('a','i','u','e','o','ka','ki','ku','ke','ko','sa','shi','su','se','so','ta','chi','tsu','te','to',
        'na','ni','nu','ne','no','ha','hi','hu','he','ho','ma','mi','mu','me','mo','ya','yu','yo','ra','ri','ru','re','ro','wa','wo',
        'n','ga','gi','gu','ge','go','za','ji','zu','ze','zo','da','di','du','de','do','ba','bi','bu','be','bo','pa','pi','pu','pe','po','ja','ju','jo')
        self.hiragana = ('あ','い','う','え','お','か','き','く','け','こ','さ','し','す','せ','そ','た','ち','つ','て','と',
        'な','に','ぬ','ね','の','は','ひ','ふ','へ','ほ','ま','み','む','め','も','や','ゆ','よ','ら','り','る','れ','ろ','わ','を','ん',
        'が','ぎ','ぐ','げ','ご','ざ','じ','ず','ぜ','ぞ','だ','ぢ','づ','で','ど','ば','び','ぶ','べ','ぼ','ぱ','ぴ','ぷ','ぺ','ぽ','じゃ','じゅ','じょ')
        self.katakana = ('ア','イ','ウ','エ','オ','カ','キ','ク','ケ','コ','サ','シ','ス','セ','ソ','タ','チ','ツ','テ','ト',
        'ナ','ニ','ヌ','ネ','ノ','ハ','ヒ','フ','ヘ','ホ','マ','ミ','ム','メ','モ','ヤ','ユ','ヨ','ラ','リ','ル','レ','ロ','ワ','ヲ','ン',
        'ガ','ギ','グ','ゲ','ゴ','ザ','ジ','ズ','ゼ','ゾ','ダ','ヂ','ヅ','デ','ド','バ','ビ','ブ','ベ','ボ','パ','ピ','プ','ペ','ポ','ジャ','ジュ','ジョ')
        self.unfamiliar = [6,8,9,10,11,12,14,16,17,18,19,20,23,25,27,29,30,32,33,38,40,41,42,43,44]
        dakuon = [num for num in range(46,68)]
        self.unfamiliar = self.unfamiliar + dakuon
        self.roman = ( self.roman[num] for num in self.unfamiliar )
        self.hiragana = ( self.hiragana[num] for num in self.unfamiliar )
        self.katakana = ( self.katakana[num] for num in self.unfamiliar )
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