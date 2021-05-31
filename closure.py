def sentence(name):
    age = 36
    lol = 30

    def full_sentence(city):
        return f"I am {name}, {age} years old, from {city}."

    return full_sentence


# s = sentence("Pawel")
# print(s("Krakow"))
# print(s("Warsaw"))


# uuid - universal unique identifer
def get_uuid():
    idx = 0
    def inner():
        nonlocal idx
        result = idx
        idx += 1
        return inner

    return inner


uuid = get_uuid()

# for _ in range(10):
#     print(uuid)


def my_power(exponent):
    def inner(digit):
        return digit ** exponent

    return inner


power_3 = my_power(3)
power_4 = my_power(4)
power_7 = my_power(7)

print(power_3(2))
print("power_3 what is in closure", power_3.__closure__[0].cell_contents)
print(power_4(2))
print("power_3 what is in closure", power_4.__closure__[0].cell_contents)
print(power_7(2))
print("power_3 what is in closure", power_7.__closure__[0].cell_contents)