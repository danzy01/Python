# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from abc import ABC, abstractmethod



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    class figura:
        def __init__(self,obwod,pole):
            self.obwod = obwod
            self.pole = pole

        @abstractmethod
        def print_c(self):
            print('Obw:', self.obwod, '\nPole:', self.pole)

    class kwadrat(figura):
        def __init__(self,bok,obwod,pole):
            super().__init__(obwod,pole)
            self.bok = bok

        def print_c(self):
            figura.print_c(self)
            print('Bok:',self.bok)


    a = kwadrat(10,40,100)
    a.print_c()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
