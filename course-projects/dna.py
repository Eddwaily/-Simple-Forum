


def DNA_trans(origin):
    i = 0
    new_dna=""
    list_of_letters=['A','C','G','T']

    while i < len(origin) :
        j = 0
        find_flag = 0

        while j < len(list_of_letters) :
            if origin[i] == list_of_letters[j] :
                new_dna += list_of_letters[3-j]
                find_flag = 1
                break
            j += 1
        if not find_flag :
            new_dna += origin[i]
        i += 1
    return new_dna

print DNA_trans("AACCGT")
print DNA_trans("AACCBFG")
