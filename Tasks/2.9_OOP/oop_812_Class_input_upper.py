# 812
# Напишіть клас, який має як мінімум два методи:
# перший - отримати рядок з вводу консолі,
# другий - друкувати рядок у верхньому регістрі.
class Upp:
    '''Convert all letters to uppercase'''

    def input(self):
        self.word = input()

    def output(self):
        return self.word.upper()

word1 = Upp()
word1.input()
print(word1.output())





