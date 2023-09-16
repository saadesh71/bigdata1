import fileinput

with fileinput.input(files=('input.txt')) as f:
    key_value_pairs = []
    for line in f:
        person, friends = line.split('   ')
        friends_list = friends.split(',')
        friends_list[-1] = friends_list[-1].strip()
        # friends_list = set(friends_list)
        for friend in friends_list:
            key = tuple(sorted((person, friend)))
            value = friends_list
            key_value_pairs.append((key, tuple(value)))
    # print(key_value_pairs)
    # print('----------------')

    pairs1 = []
    keys = []
    for i in range(0, len(key_value_pairs)):
        if key_value_pairs[i][0] not in keys:
            key = key_value_pairs[i][0]
            values = [key_value_pairs[i][1]]
            for j in range(i+1, len(key_value_pairs)):
                if key_value_pairs[i][0] == key_value_pairs[j][0]:
                    values.append(key_value_pairs[j][1])
            pairs1.append([key, values])
            keys.append(key)

    for pair in pairs1:
        out = str(pair[0]) + '   '
        for val in pair[1]:
            out += str(val) + ';'
        print(out)
