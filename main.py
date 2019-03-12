from functions import list_to


def main():
    multi_dimensional_array = [1, [9, [[[[[2]]]]]], [[[2], [12, [2]], [10]]]]
    print(list_to(multi_dimensional_array))


main()
