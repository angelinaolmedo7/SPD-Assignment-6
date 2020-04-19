
def raindrop(num):
    # Convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    if type(num) is not int:
        # raise Exception("Wrong type.")
        return "Wrong type :/"

    rtn = ""
    if num % 3 == 0:
        rtn += "Pling"
    if num % 5 == 0:
        rtn += "Plang"
    if num % 7 == 0:
        rtn += "Plong"

    if rtn == "":
        rtn = num

    return rtn


# Good input
print(raindrop(50))  # Plang
print(raindrop(21))  # PlingPlong
print(raindrop(105))  # PlingPlangPlong
print(raindrop(1))  # 1

# Bad input
print(raindrop("hooty hoo"))
print(raindrop([1, 2, 3]))

# Edge cases
print(raindrop(0))  # PlingPlangPlong
print(raindrop(15))  # PlingPlang
