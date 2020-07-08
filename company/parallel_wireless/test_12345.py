# st1 = "I own one iPhone and two SamSung , I bought it from USA"

# # output = "I own 1 i_phone and 2 Sam_sung , I bought it from USA"

num_map = {"one" : 1, "two": 2, "three": 3}

def parse_convert(st1):
    st_list = st1.split()
    for i in range(len(st_list)):
        if st_list[i] in num_map:
            value = num_map[st_list[i]]
            st_list[i] = str(value)
        
        else:
            # for j in range(len(st_list[i])):
            el_list = [ch for ch in st_list[i]]
            if all(elem.isupper() for elem in el_list):
                pass
            else:
                for j in range(len(el_list)):
                    if j!=0 and el_list[j].isupper():
                        el = el_list[j].lower()
                        # print(el)
                        el_list[j] = "_" + el
            st_list[i] = "".join(el_list)
    return " ".join(st_list)

def main():
    st1 = "I own one iPhone and two SamSung , I bought it from USA"
    print(parse_convert(st1))

main()