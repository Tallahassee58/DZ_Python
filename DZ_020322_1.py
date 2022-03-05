hours = 0
days = 0
minutes = 0
seconds = int(input('ведите количество секунд:'))
if seconds > 59:
    minutes = seconds // 60
    seconds = seconds - minutes * 60
if minutes > 59:
    hours = minutes // 60
    minutes = minutes - hours * 60
if hours > 23:
    days = hours // 24
    hours = hours - days * 24
if days > 0:
    print(days, 'дн ', end='')
if hours > 0:
    print(hours, 'чаc ', end='')
if minutes > 0:
    print(minutes, 'мин ', end='')
print(seconds, 'сек', end='')
