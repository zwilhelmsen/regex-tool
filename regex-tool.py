#######################################################
#               Regular expressions tool
#######################################################

"""
Regular expressions tool 
created: zac wilhelmsen
08/31/17

Finds the regular expression used to identify patterns/strings
"""


def regex_tool(string):
    split = string.split(" ")
    regex = []
    double_space = 0
    esc_char = [r"\\", r"\'", r"\"", r"[", r"]", r"^", r"$", r".", r"|", r"?", r"*", r"+", r"(", r")", r"{", r"}"]
    for i in range(0, len(split), 1):
        # print(i,len(split))
        # print("i is:", i)
        # print(split[i])
        for k in range(0, len(split[i]), 1):
            # print(split[i][k])
            if split[i].isdigit() and len(split[i]) > 1:
                regex.append(r"\d+")
                break
            elif split[i].isalpha() and len(split[i]) > 1:
                if r'\w' in regex[-2:] or r'\w+' in regex[-2:]:
                    # print("should we add +?")
                    # print(regex)
                    if r"\w" in regex[-2:] and r"\s" in regex[-2:]:
                        # print("adding +")
                        # print(regex)
                        count = -2
                        for element in regex[-2:]:
                            if element == r"\w":
                                regex[count] = r"\w+"
                            double_space = 1
                            count += 1
                        break
                    elif r"\w+" in regex[-2:]:
                        # print("escape")
                        double_space = 1
                        break
                    # else:  # Uncomment for testing
                        # print("IDK why i'm here.")
                else:
                    regex.append(r"\w")
                    break
            # print(split[i][k])
            if split[i][k].isdigit():
                if prev_regex(regex) == r"\d" or prev_regex(regex) == r"\d+":
                    # print("second digit")
                    regex[len(regex)-1] = r"\d+"
                else:
                    # print("First digit")
                    regex.append(r"\d")
            elif split[i][k].isalpha():
                if prev_regex(regex) == r"\p{L}" or prev_regex(regex) == r"\w":
                    # print("second letter")
                    regex[len(regex)-1] = r"\w"
                else:
                    # print("first letter")
                    regex.append(r"\p{L}")
            else:
                # print("its a special!")
                # print(split[i][k])
                if not prev_regex(regex) == split[i][k]:
                    # print("it is not already present!")
                    # print(split[i][k])
                    if not split[i][k] in esc_char:
                        # print(split[i][k])
                        # print("This is a regular special character. %s is not in list" % split[i][k])
                        regex.append(split[i][k])
                    else:
                        # print("regex escape character")
                        regex.append(r"\%s" % split[i][k])
            double_space = 0
        if i+1 == len(split):
            break
        count = -2
        if double_space == 1:
            for element in regex[-2:]:
                # print(regex, count)
                if element == r"\s":
                    # print("adding +")
                    regex[count] = r"\s+"
                count += 1
                double_space = 0

        else:
            regex.append(r"\s")
        # print(regex)

    stringOfRegex = ""
    for each in regex:
        stringOfRegex += each
    print("Your regex is: %s" % stringOfRegex)


def has_number(string):
    # print("Has number!")
    return any(str.isdigit(c) for c in string)


def has_spec(string):
    # print("Has Special!")
    return any(char.isalnum() for char in string)


def prev_regex(list):
    if len(list) >= 1:
        # print(list[len(list)-1])
        return list[len(list)-1]


# def rem_space(list):
#     return r"\s" in list[-2:]


def main():
    # print(has_spec("$abc"))
    # list = ['1', 2]
    # print(len(list))
    # print("[" == r"[")
    while True:
        regex_tool(input("> Input the string you want to identify with regular expressions\n"))
        ans = input("Do you want to play again? y/n\n").lower()
        if ans == "n":
            break

if __name__ == "__main__":
    main()

