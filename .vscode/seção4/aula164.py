def concatenate(string):
    final_value = string
    def internal(internal_string):
        nonlocal final_value
        final_value += internal_string
        return final_value

    return internal

f = concatenate('oi')

print(f('tudobem'))

