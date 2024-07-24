# class A:
#     def __init__(self):
#         self.speek()
#     def speek(self):
#         print("Hello")

# class B(A):
#     def speek(self):
#         print("world")

# a=A()

# b=B()


# class C:
#     def x(self):
#         print('x: C')


# class D:
#     def x(self):
#         print('x: D')


# class E(C, D):
#     pass


# e = E()
# e.x()
# print(E.mro())


# myset={"Geeks","for","geeks","boat"}
# newset={"risky","business","for"}

# myset.update({"Geeks"})
# print(myset)
# myset.add("a")
# print(myset)

# myset=myset.difference(newset)
# print(myset)


## Diamond Problem without confusion

# class Tokenizer:
#     """Tokenize text"""
#     def __init__(self, text):
#         print('Start Tokenizer.__init__()')
#         self.tokens = text.split()
#         print('End Tokenizer.__init__()')


# class WordCounter(Tokenizer):
#     """Count words in text"""
#     def __init__(self, text):
#         print('Start WordCounter.__init__()')
#         super().__init__(text)
#         self.word_count = len(self.tokens)
#         print('End WordCounter.__init__()')


# class Vocabulary(Tokenizer):
#     """Find unique words in text"""
#     def __init__(self, text):
#         print('Start init Vocabulary.__init__()')
#         super().__init__(text)
#         self.vocab = set(self.tokens)
#         print('End init Vocabulary.__init__()')


# class TextDescriber(WordCounter, Vocabulary):
#     """Describe text with multiple metrics"""
#     def __init__(self, text):
#         print('Start init TextDescriber.__init__()')
#         super().__init__(text)
#         print('End init TextDescriber.__init__()')


# td = TextDescriber('row row row your boat')
# print('--------')
# print(td.tokens)
# print(td.vocab)
# print(td.word_count)


# Diamond Problem with confusion

# class Tokenizer:
#     """Tokenize text"""
#     def __init__(self, text):
#         print('Start Tokenizer.__init__()')
#         self.tokens = text.split()
#         self.val='Token'
#         print('End Tokenizer.__init__()')

#     def sayHi(self):
#         print("Hi From Token")


# class WordCounter(Tokenizer):
#     """Count words in text"""
#     def __init__(self, text):
#         print('Start WordCounter.__init__()')
#         super().__init__(text)
#         self.word_count = len(self.tokens)
#         self.val='Word Count'
#         print('End WordCounter.__init__()')

#     def sayHi(self):
#         print("Hi From word count")


# class Vocabulary(Tokenizer):
#     """Find unique words in text"""
#     def __init__(self, text):
#         print('Start init Vocabulary.__init__()')
#         super().__init__(text)
#         self.vocab = set(self.tokens)
#         self.val='Vocab'
#         print('End init Vocabulary.__init__()')

#     def sayHi(self):
#         print("Hi From vocabulary")


# class TextDescriber(Vocabulary,WordCounter):
#     """Describe text with multiple metrics"""
#     def __init__(self, text):
#         print('Start init TextDescriber.__init__()')
#         super().__init__(text)
#         print('End init TextDescriber.__init__()')


# td = TextDescriber('Anything but nothing')
# print('--------')
# print(td.val)
# td.sayHi()


class Art:
    def __init__(self, art_type):
        self.__art_type = art_type

    def message(self):
        print("I'm a piece of art.")


class Painting(Art):
    def __init__(self):
        Art.__init__(self, "painting")

    def message(self):
        print("I'm a painting.")


a = Art("sculpture")
p = Painting()
a.message()
p.message()
