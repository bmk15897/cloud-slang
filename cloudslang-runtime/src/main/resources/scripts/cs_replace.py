def cs_replace(string, old_val, new_val, count=-1):

    if type(string).__name__ != "str" and type(string).__name__ != "unicode":
        raise Exception("Expected a string for parameter 'string', got " + str(string))

    if type(old_val).__name__ != "str" and type(old_val).__name__ != "unicode":
        raise Exception("Expected a string for parameter 'old_val', got " + str(old_val))

    if type(new_val).__name__ != "str" and type(new_val).__name__ != "unicode":
        raise Exception("Expected a string for parameter 'new_val', got " + str(new_val))

    count_int_value = validate_input(count, "count", -1)

    return (
        string.replace(old_val, new_val)
        if count_int_value < 0
        else string.replace(old_val, new_val, count_int_value)
    )


def validate_input(input_value, parameter_name, default_value):
    if type(input_value).__name__ == "NoneType":
        return default_value
    elif type(input_value).__name__ == "int":
        return input_value
    elif type(input_value).__name__ == "float" or type(input_value).__name__ == "bool":
        return int(input_value)
    elif type(input_value).__name__ == "str":
        return convert_string_to_int(input_value, parameter_name, default_value)
    elif type(input_value).__name__ == "bytes":
        return convert_string_to_int(input_value.decode(), parameter_name, default_value)
    else:
        raise Exception("Type of parameter '" + parameter_name + "' is not valid, got " + str(input_value)
            + " of type " + str(type(input_value).__name__))


def convert_string_to_int(input_value, parameter_name, default_value):
    if is_string_of_type_int(input_value):
        return int(input_value)
    elif is_string_of_type_float(input_value):
        return int(float(input_value))
    elif is_string_of_type_none(input_value):
        return default_value
    else:
        return check_bool_in_string(input_value, parameter_name)


def is_string_of_type_int(input_value):
    try:
        int(input_value)
        return True
    except ValueError:
        return False


def is_string_of_type_float(input_value):
    try:
        float(input_value)
        return True
    except ValueError:
        return False

def is_string_of_type_none(input_value):
    if input_value.lower() == 'none':
        return True
    else:
        return False


def check_bool_in_string(input_value, parameter_name):
    if input_value.lower() == 'true':
        return int(True)
    elif input_value.lower() == 'false':
        return int(False)
    else:
        raise Exception("Value of the parameter '" + parameter_name + "' is not valid, got " + str(input_value))