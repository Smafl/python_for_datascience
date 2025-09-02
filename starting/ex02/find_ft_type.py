def all_thing_is_obj(object: any) -> int:
	#your code here
	data_types = {
		list : "List",
		set : "Set",
		dict : "Dict",
		tuple : "Tuple",
		str : "Str"
	}

	object_type = type(object)
	type_name = data_types.get(object_type, "Type not found")

	if object_type == str:
		print(f"{object} is in the kitchen : {object_type}")
	elif type_name == "Type not found":
		print("Type not found")
	else:
		print(f"{type_name} : {object_type}")

	return 42