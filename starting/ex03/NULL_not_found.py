def NULL_not_found(object: any) -> int:
    #your code here

    object_type = type(object)

    if object is None:
        print(f"Nothing: {object} {object_type}")
        return 0
    elif (object_type == float) and (object != object):
        print(f"Cheese: {object} {object_type}")
        return 0
    elif (object_type == int) and (object == 0):
        print(f"Zero: {object} {object_type}")
        return 0
    elif object == '':
        print(f"Empty: {object} {object_type}")
        return 0
    elif object is False:
        print(f"Fake: {object} {object_type}")
        return 0
    else:
        print("Type not Found")
        return 1