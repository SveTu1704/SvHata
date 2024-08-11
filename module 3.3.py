def print_params(a = 1, b = 'строка', c = True):
 print(a,b,c)

print_params(1,5,9)
print_params()
print_params("Folse",5.2,0)
print_params(b=25,c=[1,2,3])

values_list=[True,5.8,"Urban"]

print_params(*values_list)

values_dict_ = {"a":5456625, "b":852555445, "c":654652954}
print_params(**values_dict_)

values_list_2=["Svetlana",True]
print_params(*values_list_2, 42)