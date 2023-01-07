ul_str = "altERnaTIng cAsE"

# printing original string
print("The original string is : " + str(ul_str))

# Using upper() + lower() + loop
# Alternate cases in String
result = ""
for idx in range(len(ul_str)):
    if not idx % 2:
        result = result + ul_str[idx].upper()
    else:
        result = result + ul_str[idx].lower()

# printing result
print("The converted string is : " + str(result))