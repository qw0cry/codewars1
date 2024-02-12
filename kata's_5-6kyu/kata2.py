#ссылка на задачу - https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python, используйте дебаг для разбора
def make_readable(seconds):
    minuts, seconds = seconds // 60, seconds % 60 #перевод секунд в минуты целочисленным делением на 60 и остаток от деления на эти же 60 чтобы секунды не пропали
    if minuts >= 60: #если количество минут меньше 60 - нет смысла переводить их в часы
        hours, minuts = minuts // 60, minuts % 60 # точно такой же перевод, что и выше
    else:
        hours = '00' # продолжение верхнего if, присваивание 00, ибо по условию функция должна вернуть HH:MM:SS
    if len(str(hours)) == 1: #все следующие if - на случай, если число получится не в нужном формате(не 15 а 8, допустим), 8 после преобразования будет выглядеть как 08 и тд
        hours = '0' + str(hours)
    if len(str(minuts)) == 1:
        minuts = '0' + str(minuts)
    if len(str(seconds)) == 1:
        seconds = '0' + str(seconds)
    return f'{hours}:{minuts}:{seconds}' # вывод собственно
