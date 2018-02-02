mass = float(input('Введите свой вес в килограммах, пожалуйста: '))
height = float(input('Теперь введите свой рост в сантиметрах: '))
index = mass / ((height / 100) * (height / 100))
count = float(index)
print('Индекс вашего тела:', count)
#на всякий случай еще запринтил сам индекс, если человеку интересно.

if count < 16:
    print('У вас выраженный дефицит массы тела.')
elif count >= 16 and count < 18.5:
    print('У вас недостаточный вес тела.')
elif count >= 18.5 and count < 25:
    print('У вас нормальный вес тела.')
elif count >= 25 and count < 30:
    print('У вас слегка избыточная масса тела.')
elif count >= 30 and count < 35:
    print('У вас ожирение первой степени')
elif count >= 35 and count < 40:
    print('У вас ожирение второй степени.')
else:
    print('У вас ожирение третьей степени (морбидное)')