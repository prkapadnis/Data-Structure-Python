def check_sum(num_list):
    for i in num_list:
        for j in num_list:
            if i+j == 0:
                return True
    return False


num_list = [10, -14, 26, 5, -3, 13, -5]
print(check_sum(num_list))
