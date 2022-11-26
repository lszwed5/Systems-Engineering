import re

address = "pythusun_toon20usun_to20@gusun_tomail.com."
pattern = "usun_to"

while re.search(pattern, address):
    search = str(re.search(pattern, address))
    found = re.findall(r"\(.*\)", search)

    found_split = found[0].split(", ")

    beginning = int(found_split[0][1:])
    end = int(found_split[1][:-1])

    address = address[:beginning] + address[end:]

print(address)
