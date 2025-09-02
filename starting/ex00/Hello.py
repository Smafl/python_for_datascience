ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
#your code here

# changeable by index
ft_list[1] = "World"

# unchangeable
ft_tuple = ("Hello", "Germany")

# unordered, unchangeable, unindexed
ft_set.remove("tutu!")
ft_set.add("Heilbronn")

# ordered, changeable
ft_dict["Hello"] = "42Heilbronn"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)