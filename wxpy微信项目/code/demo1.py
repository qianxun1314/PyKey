import wxpy
bot = wxpy.Bot(console_qr=-1, cache_path=True)

my_friends = bot.friends()
male = 0
female = 0
other = 0
for friend in my_friends:
    if friend.sex == 1:
        male += 1
    elif friend.sex == 2:
        female += 1
    else:
        other += 1
print("male = ", male)
print("female = ", female)
print("total numbers = ", len(my_friends))
