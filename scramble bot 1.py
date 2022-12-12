import enchant
import random

d = enchant.Dict("en_US")

all_letters = ['A','A','A','A','A','A','A','A','A','B','B','C','C','D','D','D','D','E','E','E','E','E',
               'E','E','E','E','E','E','E','F','F','G','G','G','H','H','H','I','I','I','I','I','I','I','I','I',
               'J','K','L','L','L','L','M','M','N','N','N','N','N','N','O','O','O','O','O','O','O','O','P','P'
               'Q','R','R','R','R','R','R','S','S','S','S','T','T','T','T','T','T','U','U','U','U','V','V','W',
               'W','X','Y','Y','Z']


def word_generator(my_letter_list1, fix_letters, space_for_letters):
    word_list = []
    for i in range(7):
        my_letter_list = my_letter_list1.copy()
        new_word = ""
        # temp = 'let' + str(i)
        new_word += my_letter_list.pop(i)
        # print("i",my_letter_list)
        j_list = my_letter_list.copy()
        for j in range(6):

            j_list_copy = j_list.copy()
            new_word_j = new_word + j_list_copy.pop(j)
            k_list = j_list_copy.copy()
            if space_for_letters == 2:
                if d.check(str(new_word_j + fix_letters)) == True:
                    word_list.append(new_word_j + fix_letters)
                continue

            for k in range(5):
                k_list_copy = k_list.copy()
                new_word_k = new_word_j + k_list_copy.pop(k)

                l_list = k_list_copy.copy()
                if space_for_letters == 3:
                    if d.check(str(new_word_k + fix_letters)) == True:
                        word_list.append(new_word_k + fix_letters)
                    continue

                for l in range(4):
                    l_list_copy = l_list.copy()
                    new_word_l = new_word_k + l_list_copy.pop(l)
                    m_list = l_list_copy.copy()
                    if space_for_letters == 4:
                        if d.check(str(new_word_l + fix_letters)) == True:
                            word_list.append(new_word_l + fix_letters)
                        continue
                    for m in range(3):
                        m_list_copy = m_list.copy()
                        new_word_m = new_word_l + m_list_copy.pop(m)

                        n_list = m_list_copy.copy()

                        if space_for_letters == 5:
                            if d.check(str(new_word_m + fix_letters)) == True:
                                word_list.append(new_word_m + fix_letters)
                            continue

                        for n in range(2):
                            n_list_copy = n_list.copy()
                            new_word_n = new_word_m + n_list_copy.pop(n)

                            o_list = n_list_copy.copy()

                            if space_for_letters == 6:
                                if d.check(str(new_word_n + fix_letters)) == True:
                                    word_list.append(new_word_n + fix_letters)
                                continue
                            for o in range(1):

                                o_list_copy = o_list.copy()
                                new_word_o = new_word_n + o_list_copy.pop(o)
                                if space_for_letters >= 7:
                                    if d.check(str(new_word_o + fix_letters)) == True:
                                        word_list.append(new_word_o + fix_letters)

    return word_list


def word_generator_back(my_letter_list1, fix_letters, space_for_letters):
    word_list = []
    for i in range(7):
        my_letter_list = my_letter_list1.copy()
        new_word = ""
        # temp = 'let' + str(i)
        new_word += my_letter_list.pop(i)

        # print("i",my_letter_list)
        j_list = my_letter_list.copy()
        if space_for_letters == 1:
            if d.check(str(fix_letters + new_word)) == True:
                word_list.append(fix_letters + str(new_word))
            continue
        for j in range(6):

            j_list_copy = j_list.copy()
            new_word_j = new_word + j_list_copy.pop(j)
            k_list = j_list_copy.copy()
            if space_for_letters == 2:
                if d.check(str(fix_letters + new_word_j)) == True:
                    word_list.append(fix_letters + new_word_j)
                continue

            for k in range(5):
                k_list_copy = k_list.copy()
                new_word_k = new_word_j + k_list_copy.pop(k)

                l_list = k_list_copy.copy()
                if space_for_letters == 3:
                    if d.check(str(fix_letters + new_word_k)) == True:
                        word_list.append(fix_letters + new_word_k)
                    continue

                for l in range(4):
                    l_list_copy = l_list.copy()
                    new_word_l = new_word_k + l_list_copy.pop(l)
                    m_list = l_list_copy.copy()
                    if space_for_letters == 4:
                        if d.check(str(fix_letters + new_word_l)) == True:
                            word_list.append(fix_letters + new_word_l)
                        continue
                    for m in range(3):
                        m_list_copy = m_list.copy()
                        new_word_m = new_word_l + m_list_copy.pop(m)

                        n_list = m_list_copy.copy()

                        if space_for_letters == 5:
                            if d.check(str(fix_letters + new_word_m)) == True:
                                word_list.append(fix_letters + new_word_m)
                            continue

                        for n in range(2):
                            n_list_copy = n_list.copy()
                            new_word_n = new_word_m + n_list_copy.pop(n)

                            o_list = n_list_copy.copy()

                            if space_for_letters == 6:
                                if d.check(str(fix_letters + new_word_n)) == True:
                                    word_list.append(fix_letters + new_word_n)
                                continue
                            for o in range(1):

                                o_list_copy = o_list.copy()
                                new_word_o = new_word_n + o_list_copy.pop(o)
                                if space_for_letters >= 7:
                                    if d.check(str(fix_letters + new_word_o)) == True:
                                        word_list.append(fix_letters + new_word_o)

    return word_list


def word_generator_mid(my_letter_list1, fix_letters, front_space, back_space):
    word_list = []
    for i in range(7):
        my_letter_list = my_letter_list1.copy()
        new_word = ""
        # temp = 'let' + str(i)
        new_word += my_letter_list.pop(i)

        # print("i",my_letter_list)
        j_list = my_letter_list.copy()
        for j in range(6):

            j_list_copy = j_list.copy()
            new_word_j = new_word + j_list_copy.pop(j)
            k_list = j_list_copy.copy()
            if front_space + back_space == 2:


                word_list.append(str(new_word_j[:1] + fix_letters + new_word_j[1:]))
                continue

            for k in range(5):
                k_list_copy = k_list.copy()
                new_word_k = new_word_j + k_list_copy.pop(k)

                l_list = k_list_copy.copy()
                if front_space + back_space == 3:

                    word_list.append(str(new_word_k[:front_space] + fix_letters + new_word_k[front_space:]))
                    continue

                for l in range(4):
                    l_list_copy = l_list.copy()
                    new_word_l = new_word_k + l_list_copy.pop(l)
                    m_list = l_list_copy.copy()
                    if front_space + back_space == 4:

                        word_list.append(str(new_word_l[:front_space] + fix_letters + new_word_l[front_space:]))
                        continue
                    for m in range(3):
                        m_list_copy = m_list.copy()
                        new_word_m = new_word_l + m_list_copy.pop(m)

                        n_list = m_list_copy.copy()

                        if front_space + back_space == 5:

                            word_list.append(str(new_word_m[:front_space] + fix_letters + new_word_m[front_space:]))
                            continue

                        for n in range(2):
                            n_list_copy = n_list.copy()
                            new_word_n = new_word_m + n_list_copy.pop(n)

                            o_list = n_list_copy.copy()

                            if front_space + back_space == 6:
                                word_list.append(
                                    str(new_word_n[:front_space] + fix_letters + new_word_n[front_space:]))
                                continue
                            for o in range(1):

                                o_list_copy = o_list.copy()
                                new_word_o = new_word_n + o_list_copy.pop(o)
                                if front_space + back_space >= 7:

                                    word_list.append(
                                        str(new_word_o[:front_space] + fix_letters + new_word_o[front_space:]))



    return word_list


def test_case1(my_letters_list, fix_letters, space_for_letters):
    word_list = []

    for r in range(1, len(fix_letters) + 1):
        temp_fix_letters = fix_letters[0:r]

        for i in range(1, space_for_letters + 1):
            if i == 8:
                break
            temp = word_generator(my_letters_list, str(temp_fix_letters), i)
            word_list.extend(temp)

    print(word_list)


def test_case2(my_letters_list, fix_letters, space_for_letters):
    word_list = []

    for r in range(0, len(fix_letters)):
        temp_fix_letters = fix_letters[r:len(fix_letters)]

        for i in range(1, space_for_letters + 1):
            if i == 8:
                break
            temp = word_generator_back(my_letters_list, str(temp_fix_letters), i)
            word_list.extend(temp)

    print(word_list)


def test_case3(my_letters_list, fix_letters, front_space, back_space):
    word_list = []
    a = back_space

    b = front_space

    if back_space >= 7:
        back_space = 6
    if front_space >= 7:
        front_space = 6

    for i in range(1, front_space + 1):
        if i + back_space > 7:
            back_space = 7 - i

        for j in range(1, back_space + 1):
            temp = word_generator_mid(my_letters_list, fix_letters, i, j)
            word_list.extend(temp)

    back_space = a
    front_space = b

    if back_space >= 7:
        back_space = 6
    if front_space >= 7:
        front_space = 6

    for i in range(1, back_space + 1):
        if i + front_space > 7:
            front_space = 7 - i

        for j in range(1, front_space + 1):
            temp = word_generator_mid(my_letters_list, fix_letters, j, i)
            word_list.extend(temp)
    word_set = set(word_list)
    word_list2 = []
    for i in word_set:
        if d.check(str(i)) == True:
            word_list2.append(i)
    print(word_list2)

def letter_picker(n):
    lis = []
    global all_letters
    for i in range (n):
        pos = random.randrange(1,len(all_letters))
        lis.append(all_letters.pop(pos))
    print(lis)
    print(len(all_letters))


let1 = 'l'
let2 = 'y'
let3 = 'g'
let4 = 'p'
let5 = 'y'
let6 = 'o'
let7 = 's'
# psychology
my_letters_list = [let1, let2, let3, let4, let5, let6, let7]

fix_letters = 'cho'

front_space = 8
back_space = 8

# test_case1(my_letters_list,fix_letters,front_space)

#test_case3(my_letters_list, fix_letters, front_space, back_space)

letter_picker(7)
letter_picker(7)