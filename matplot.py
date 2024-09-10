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
        'spaceuk':[70,100,115,130],
        'lord':[30,50,65,80],
        'dro9':[50,80,90,100],
        'Slend': [20,60,110,145],
        'niko': [40,50,60,150],
        'vaiber': [10,20,30,40],
        'lux': [15,35,65,79],
        'Dead': [20,20,50,50],
        'night': [60,80,120,135],
        'Ryzh': [25,10,15,5],
        'alexander09-2':[30,30,30,30]
    }

    titles = []

    # Обработка данных в виде таблицы (на всякий случай)
    imp = pd.DataFrame({})
    for i in players:
        imp.insert(0,i,players[i])
    return players, titles

# Для импорта данных из таблицы excel
def excel_import():
    players = {} # Пустой список для внесения туда игроков
    imp = pd.read_excel("") # Путь к таблице excel
    imp = pd.DataFrame(imp)
    titles = [] 

    # Добавление данных из таблицы с помощью цикла
    for i in range(imp.shape[0]): # Добавление строк
        add_list = [] # Вспомогательный лист для следующего цикла
        for j in range(1,imp.shape[1]): # Добавление столбцов
            try:
                add_list.append(int(imp.at[i,imp.columns.tolist()[j]]))
            except:
                add_list.append(0)
            players[imp.at[i,imp.columns.tolist()[0]]] = add_list # Добавляем в словарь Имя Игрока и по очередно вносим столбцы из вспомогательного листа

    for i in range(1,imp.shape[1]):
        titles.append(imp.columns.tolist()[i])

    return players, titles

# Выбор метода импорта
players, titles = excel_import()
print(titles)
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