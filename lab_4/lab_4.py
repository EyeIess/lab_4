import os
import csv
class Place:

    def __init__(self, place, width, height, par):
        self.place = place
        self.width = width
        self.height = height
        self.par = par

    def __getitem__(self, i):
        try:
            return self.place[i], self.width[i], self.height[i]
        except:
            printf("Введён не правильный индекс")

    def __repr__(self):
        pass

class Temperature(Place):

    def __init__(self, number, temp, time, date, place, width, height, par):
        self.number = number
        self.temp = temp
        self.time = time
        self.date = date
        super().__init__(place, width, height, par)

    def __setattr__(self, name, value):
        if name in ['place', 'time', 'date']:
            for i in value:
                try:
                    str(i)
                except:
                    print('в таблице в поле ' + name + ' введены неверные данные!!!')
        else:
            for i in value:
                try:
                    int(i)
                except:
                    print('в таблице в поле ' + name + ' введены неверные данные!!!')
        return super().__setattr__(name, value)

    def __getitem__(self, i):
        for j in range(len(self.par)):
            if i < self.par[j]:
                return self.number[i], self.place[j - 1], self.width[j - 1], self.height[j - 1], self.temp[i], self.time[i], self.date[i] 
        return self.number[i], self.place[self.par[len - 1]], self.width[self.par[len - 1]], self.height[self.par[len - 1]], self.temp[i], self.time[i], self.date[i]

    def __repr__(self):
        return repr(self.place)

class Processing():
    
    dict_outputing = {}
    dict_reading = {}

    def __init__(self):
        with open('C:\\Users\\Mikhail\\Desktop\\data.csv', 'r') as F:
            reading_file = csv.DictReader(F, delimiter=';')
            dict_copy = dict.fromkeys(reading_file.fieldnames)
            for i in reading_file:
                dict_copy.update(i)
                self.dict_reading[reading_file.line_num - 2] = dict_copy.copy()
            self.copy_class = ''
            y = {0:[],1:[],2:[],3:[],4:[],5:[],6:[]}
            par = []
            for i in iter(self.dict_reading):
                if not self.copy_class == self.dict_reading[i]['Место']:
                    self.copy_class = self.dict_reading[i]['Место']
                    y[0].append(self.copy_class)
                    y[1].append(int(self.dict_reading[i]['Широта']))
                    y[2].append(int(self.dict_reading[i]['Долгота']))
                    par.append(i)
                y[3].append(int(self.dict_reading[i]['№']))
                y[4].append(int(self.dict_reading[i]['Температура']))
                y[5].append(self.dict_reading[i]['Время'])
                y[6].append(self.dict_reading[i]['Дата'])
            self.copy_class = Temperature(y[3], y[4], y[5], y[6], y[0], y[1], y[2], par)
            self.copy_class[0]

    @staticmethod
    def file_count(adres):
        try:
            name = os.listdir(adres)
        except:
            print("Вы не правильно ввели адрес каталога\nПоэтому он был заменён на адрес каталога программы")
            adres = None
            name = os.listdir(adres)
        cnt = 0
        for i in name:
            try:
               os.listdir(adres + "\\" + i)
            except:
                cnt += 1
        print("Количество файлов в введённом катологе: " + str(cnt))

    def iterat(self):
        iterator_dict = iter(self.dict_reading)
        return iterator_dict

    def sort_string(self):
        j = {i: self.dict_reading[i]['Дата'] for i in self.iterat()}
        j = sorted(j, key = j.get)
        j = {i: self.dict_reading[j[i]] for i in self.iterat()}
        output_in_console(self.iterat(), j)

    def sort_int(self):
        j = {i: self.dict_reading[i]['Температура'] for i in self.iterat()}
        j = sorted(j, key = j.get)
        j = {i: self.dict_reading[j[i]] for i in self.iterat()}
        output_in_console(self.iterat(), j)

    def sort_criterion(self):
        try:
            n = int(input("Введите минимальное значение долготы в приделе от -180 до 180"))
            if(-180 > n or n > 180):
                n = -120
                print("Вы не правильно ввели долготу\nПоэтому минимальное значение долготы стало равно стандартному, а именно -120")
        except:
            n = -120
            print("Вы не правильно ввели долготу\nПоэтому минимальное значение долготы стало равно стандартному, а именно -120")
        j = [i for i in self.iterat() if int(self.dict_reading[i]['Долгота']) >= n]
        if j == []:
            print("Таких значений в поле 'Долгота' нет")
        else:
            m = j.copy()
            j = {i: self.dict_reading[i] for i in m}
            output_in_console(m, j)

    def output_in_console(self, m, j):
        print(" ".join(self.dict_reading[0].keys()))
        for i in m:
            print("{:<3}{:>3}{:>6}{:>8}{:>10}{:>10}{:>11}".format(*j[i].values()))
        self.dict_outputing = j

    def output_in_file(self):

        with open('C:\\Users\\Mikhail\\Desktop\\data1.csv', 'w') as F:
            output_file = csv.DictWriter(F, fieldnames = list(self.dict_outputing[7].keys()), delimiter=';')
            output_file.writeheader()
            for i in self.dict_outputing:
                output_file.writerow(self.dict_outputing[i])
        print("В файл data1.csv были записанно новые данные ")

def main_code():

    tabl =  Processing()
    print("Метод №1 выводит количество файлов в каталоге")
    print("Метод №2 выводит таблицу отсортированную по полю 'Дата'")
    print("Метод №3 выводит таблицу отсортированную по возрастанию в поле 'Температура'")
    print("Метод №4 выводит таблицу отсортированную по критерию значение поля 'Долгота', больше или равно введённому числу в пределах от [-180;180]")
    print("Метод №5 сохраняет изменённую таблицу в файл data1.csv")
    print("Метод №6 получение значений классов по индексу")
    print("Метод №0 закрывает программу")
    while True:
        while True:
            try:
                choice_of_method = int(input('Введите номер метода '))
                if (choice_of_method < 0 or choice_of_method >6):
                    print("Вы не правильно ввели номер метода\nПопробуйте ввести ещё раз")
                else:
                    break
            except:
                print("Вы не правильно ввели номер метода\nПопробуйте ввести ещё раз")
        if choice_of_method == 0:
            break
        elif choice_of_method == 1:
            adres = input('Введите адрес каталога')
            tabl.file_count(adres)
        elif choice_of_method == 2:
            tabl.sort_string()
        elif choice_of_method == 3:
            tabl.sort_int()
        elif choice_of_method == 4:
            tabl.sort_criterion()
        elif choice_of_method == 5:
            if not(tabl.dict_outputing == {}):
                tabl.output_in_file()
            else:
                print('Вы не изменили изначальную таблицу, поэтому нечего сохранять')
        else:
            while True:
                try:
                    i = int(input('Введите индекс '))
                    print(str(tabl.copy_class[i]))
                    break
                except:
                    print('Вы не правильно ввели индекс')
main_code()
