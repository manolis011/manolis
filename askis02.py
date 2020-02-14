with open('text.txt') as my_file:
    # I already have file open at this point... fix yours!!!
    my_file.seek(0)
    first_char = my_file.read(1)
    if not first_char:
        print("Text file is empty!")
    else:
        my_file.seek(0)
        f = {}
        def freq(str):
            str = str.split()
            str2 = []
            for i in str:
                if i not in str2:
                    str2.append(i)
            for i in range(0, len(str2)):
                word_letters_number = 0
                for j in str2[i]:
                    f[i] = f.get(i, 0) + 1
                    word_letters_number = word_letters_number + 1
                    f_number = int(str2[i].count('f'))  # number of f
                    c_number = int(str2[i].count('c'))  # number of c
                    k_number = int(str2[i].count('k'))  # number of k
                    r_number = int(str2[i].count('r'))  # number of r
                    F_number = int(str2[i].count('F'))  # number of F
                    C_number = int(str2[i].count('C'))  # number of C
                    K_number = int(str2[i].count('K'))  # number of K
                    R_number = int(str2[i].count('R'))  # number of R
                    total_bad_letters = f_number + c_number + k_number + r_number + F_number + C_number + K_number + R_number
                    total_good_letters = int(word_letters_number - total_bad_letters)
                if total_good_letters > total_bad_letters:
                    print(str2[i], 'is : Good word')
                else:
                    print(str2[i], 'is : Bad word! Pepper on your tongue!')
        def main():
            with open('text.txt', 'r') as myfile:
                str = myfile.read().replace(',', '\n').replace('\n', ' ', ).replace('.', '').replace('!', '').replace(
                    '-', '').replace('_', '').replace('(', '').replace(')', '')  # replace \n and delete , ! - _ and dot
            freq(str)
        if __name__ == "__main__":
            main()

