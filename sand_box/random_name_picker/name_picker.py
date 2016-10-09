import random
names_list = 'names_list.txt'
picked_names_list = 'picked_names_list.txt'
new_names = open(names_list, 'r')
new_names = new_names.read().split(',')
picked_names = open(picked_names_list, 'r')
picked_names = picked_names.read().split(',')

diff_names = list(set(new_names).difference(picked_names))
first_name = random.choice(diff_names)
diff_names.remove(first_name)
seconds_name = random.choice(diff_names)
print(first_name, seconds_name)

# send automatic email to the selected user

# save new diff_names list to 'picked_names_list' file



