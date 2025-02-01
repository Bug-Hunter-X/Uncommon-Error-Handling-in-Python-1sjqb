def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        if isinstance(a,(int,float)) and isinstance(b,(int,float)):
            return "Error:Unknown error"
        else:
            return "Error:Type Error"

# Example usage
print(function_with_uncommon_error(10, 0))  # Output: Error: Division by zero
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error("10", 2)) # Output: Error:Type Error
print(function_with_uncommon_error(10, "2")) # Output: Error:Type Error
print(function_with_uncommon_error("10","2")) # Output:Error:Type Error
