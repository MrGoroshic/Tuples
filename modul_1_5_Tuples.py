immutable_var = [5, 4, 2], 1, 3, True, "String"
print(immutable_var)

immutable_var[0][1] = 9 # Можно изменить так как это изменяемый внутренний список
# immutable_var[3] = False # НЕльзя изменить так как это НЕизменяемый элемент основного списка не изменяемого кортежа
print(immutable_var)

mutable_list = [1,2,3,4,5]
print(mutable_list)
mutable_list[0:3] = 5,4,3
print(mutable_list)