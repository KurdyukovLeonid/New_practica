team1_num = 5
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'


print('В команде Мастера кода участников %s!' % team1_num)
print('Итого сегодня в командах участников: %(num_1)s и %(num_2)s!' % {'num_1': team1_num, 'num_2': team2_num})

print('Команда Волшебники данных решила задач: {}!'.format(score2))
print('Волшебники данных решили задачи за {}!'.format(team1_time))

print(f'Команды решили {score1} и {score2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')








