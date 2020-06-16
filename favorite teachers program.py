print('Welcome to the Favorite Teachers program')
favorites=[]
teacher=input('Who is your first favourite teacher: ').title().strip()
favorites.append(teacher)
teacher=input('Who is your second favourite teacher: ').title().strip()
favorites.append(teacher)
teacher=input('Who is your third favourite teacher: ').title().strip()
favorites.append(teacher)
teacher=input('Who is your fourth favourite teacher: ').title().strip()
favorites.append(teacher)

print('Your favprites teachers ranked are: ' + str(favorites))
print('Your favpurites teachers alphabetically are: ' + str(sorted(favorites)))
print('Your favpurites teachers in reversed alphabetical order are: ' + str(sorted(favorites, reverse=True)))

print('\nYour top two teachers are: ' + str(favorites[0:2]))
print('Your next two teachers are: ' + str(favorites[2:4]))
print('Your last favourite teacher is :' + str(favorites[-1]))
print('\nYou have a total of ' + str(len(favorites)) + ' teachers.')

new_teacher= input('\nOops, ' + str(favorites[0]) + ' is no longer your first favourite teacher. Who is your new FAVOURITE teacher: ').title().strip()
favorites.insert(0, new_teacher)
print('Your favpurites teachers ranked are: ' + str(favorites))
print('Your favpurites teachers alphabetically are: ' + str(sorted(favorites)))
print('Your favpurites teachers in reversed alphabetical order are: ' + str(sorted(favorites, reverse=True)))

print('\nYour top two teachers are: ' + str(favorites[0:2]))
print('Your next two teachers are: ' + str(favorites[2:4]))
print('Your last favourite teacher is :' + str(favorites[-1]))
print('\nYou have a total of ' + str(len(favorites)) + ' teachers.')

bad=input("\nYou've decided you no longer like a teacher. Which teacher would you like to remove from your list: ").title().strip()
favorites.remove(bad)

print('Your favpurites teachers ranked are: ' + str(favorites))
print('Your favpurites teachers alphabetically are: ' + str(sorted(favorites)))
print('Your favpurites teachers in reversed alphabetical order are: ' + str(sorted(favorites, reverse=True)))

print('\nYour top two teachers are: ' + str(favorites[0:2]))
print('Your next two teachers are: ' + str(favorites[2:4]))
print('Your last favourite teacher is :' + str(favorites[-1]))
print('\nYou have a total of ' + str(len(favorites)) + ' teachers.')
