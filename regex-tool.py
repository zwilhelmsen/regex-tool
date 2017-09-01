#######################################################
#               Regular expressions tool
#######################################################

"""
Regular expressions tool 
created: zac wilhelmsen
08/31/17

Finds the regular expression used to identify patters/strings
"""


def regex_tool(string):
    split = string.split(" ")
    regex = []
    for i in range(len(split)):
        if has_number(split[i]):
            if split[i].isdigit():
                if not regex[i-1].isdigit():
                    regex.append(r"\d")
                else:
                    regex.append("+")
            num_split = split.split("\d")
            for k in num_split:
                if num_split[k].isdigit():
                    regex.append(r"\d")


def has_number(string):
    return any(str.isdigit(c) for c in string)


def has_spec(string):
    # for char in string:
    #     if not char.isalnum():
    #         return True
    # return False

    return any(char.isalnum() for char in string)


def main():
    print(has_spec("$abc"))


if __name__ == "__main__":
    main()

