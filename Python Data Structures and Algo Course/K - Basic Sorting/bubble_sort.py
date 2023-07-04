# bubble sort 

def bubble_sort(my_list):
    # this for loop controls the number of iterations by len() function
    for i in range(len(my_list) - 1, 0, -1): # -1 time step because we start from the last 
        for j in range(i):
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j+1] = temp 
    return my_list 

print(bubble_sort([3, 5, 1, 10, 49]))