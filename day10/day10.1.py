def formatName(f_name, l_name):
    first = f_name.title()
    last = l_name.title()
    return (f"{first} {last}")

formattedString = formatName("zeynep", "KARAKAYALI")
print(formattedString)