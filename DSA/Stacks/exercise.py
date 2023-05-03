from DSA.Stacks.stacksonstacks import Stack

# Divide the number by 2
# store the remainder as binary
# Once the number gets to < 1 store that remainder as binary
# Use your binaries to return an integer
# They will be in reverse order so you'll need to reverse them 

bin_list = Stack()



def convert_int_to_bin(dec_num):
    reverse_bin_list = ""
    while dec_num >= 1:
        rem = bin(dec_num  % 2)[2:]
        bin_list.push(rem)
        dec_num = dec_num // 2
        print(rem)
    while not bin_list.check_stack():
        reverse_bin_list += bin_list.pop()
  



    return reverse_bin_list





convert_int_to_bin(242)