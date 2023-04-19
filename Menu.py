import main
import dif_types
import task

def menu(life=1):
    t = int(input('Какую фигуру вы хотите построить?\n1.Треугольник\n2.Прямоугольник\n3.Шестиугольник '))
    new = {1:'tr', 2:'re', 3:'h'}
    a = int(input('как? \n 1.1 ряд\n 2.перенос\n3.поворот\n4.симметрия\n5.гомометрия\n6.задание 4 '))
    if a == 1:
        main.base(new[t])
    elif a==2:
        dif_types.tr_translate(int(input('кол-во ')), int(input('расстояние ')), new[t])
    elif a==3:
        kol = int(input('сколько нужно рядов?'))
        dif_types.tr_rotate(new[t], [int(input('угол ряда')) for i in range(kol)])
    elif a==4:
        dif_types.tr_symmetry(new[t])
    elif a==5:
        dif_types.tr_homothety(new[t])
    else:
        task.task_1()
        task.task_2()
        task.task_3()
        task.task_4()
    life = 1 if input('продолжить? (y/n) ')=='y' else 0
    if life: menu(life=life)


menu()
