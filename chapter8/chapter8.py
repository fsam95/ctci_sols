def get_subsets(big_set):
    if big_set == set():
        return [set()]
    else:
        subsets = [big_set]
        for element in big_set:
            subsets.extend(get_all_subsets(big_set.difference(set([element]))))
        return subsets

def get_all_subsets(big_set):
    list_of_subsets = get_subsets(big_set)
    all_subsets = set()
    for subset in list_of_subsets:
        all_subsets.add(frozenset(subset))
    return all_subsets



if __name__ == '__main__':
    print(get_all_subsets(set([1,2,3])))
        



