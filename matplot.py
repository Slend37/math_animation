import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import pandas as pd

# Необходимые переменные
fig, ax = plt.subplots() # создание графика
last = [] # массив для предыдущей стадии
x = [] # массив для кол-ва строк в графике
data = [] # обновляемые данные на экране

# Для внесения данных вручную
def hand_import():
    players = {
        'Петров':[70,60,50,30,50,40,50,45,65,76,80],
        'Иванов':[30,50,65,80,55,65,76,45,75,32,45],
        'Сидоров':[50,80,90,100,89,92,91,90,66,65,74],
    }

    # Обработка данных в виде таблицы (на всякий случай)
    imp = pd.DataFrame({})
    for i in players:
        imp.insert(0,i,players[i])
    return players

# Для импорта данных из таблицы excel
def excel_import():
    players = {} # Пустой список для внесения туда игроков
    imp = pd.read_excel("") # Путь к таблице excel
    imp = pd.DataFrame(imp)

    # Добавление данных из таблицы с помощью цикла
    for i in range(imp.shape[0]): # Добавление строк
        add_list = [] # Вспомогательный лист для следующего цикла
        for j in range(1,imp.shape[1]): # Добавление столбцов
            try:
                add_list.append(int(imp.at[i,imp.columns.tolist()[j]]))
            except:
                add_list.append(0)
            players[imp.at[i,imp.columns.tolist()[0]]] = add_list # Добавляем в словарь Имя Игрока и по очередно вносим столбцы из вспомогательного листа
    return players

# Выбор метода импорта
players = hand_import()
#players = excel_import()
# Работа с необходимыми листами
for i in range(len(players)):
    last.append(1) # Заполнение начальным значением
    x.append(i) # Высота строк
    data.append(0) # Нулевые значения, в последствие обновятся

# Преобразование в формат array для работы с matplotlib
last = np.array(last)
x = np.array(x)
data = np.array(data)

# Создание стадий. Преобразование данных в другой формат
stages = []
for j in range(len(players[list(players.keys())[0]])):
    add=[]
    for i in players:
        add.append(players[i][j])
    stages.append(add)
print(players)
# Листы для графика
artists = [] # Контейнеры с графиком
labels = [i for i in players] # Названия строк

colors_list = ['tab:blue', 'tab:red', 'tab:green', 'tab:purple', 'tab:orange', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan'] # Цвета
colors = [] # Массив цветов для графика
for i in range(len(labels)): # Заполение массива цветов
    if i > len(colors_list) - 1:
        i = i%(len(colors_list) - 1)
    colors.append(colors_list[i])

print("Рисовка начата")
# Рисовка графика
frames = 20
for k in range(len(stages)): # Цикл стадий
    print(k)
    next_stage = stages[k] # Переход на следующую стадию
    for i in range(frames): # Цикл фреймов для анимации
        for j in range(len(data)): # Цикл кол-ва отметок
            data[j] = last[j]+(next_stage[j]-last[j])/frames*(i+1)
        # print(k,i, data, colors,labels)
        container = ax.barh(x, data, color=colors,tick_label = labels)
        artists.append(container)
    last = next_stage # смена последней стадии
        
# Вывод анимации
ani = animation.ArtistAnimation(fig=fig, artists=artists, interval=10)
plt.show()