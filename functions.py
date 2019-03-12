def list_to(multi_dimensional_array):
    index = 0
    while index < len(multi_dimensional_array):
        while True:
            try:
                multi_dimensional_array[index:(index+1)]\
                    = multi_dimensional_array[index]
            except TypeError:
                break
        index += 1
    return multi_dimensional_array
