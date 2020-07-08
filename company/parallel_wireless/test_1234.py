# 10.010.60.30 #10.10.60.30
# 10.300.0.0


def format_ip(ip):
    ip_split = ip.split(".")
    ip_parsed = []
    if len(ip_split) != 4:
        return "invalid ip"
    for elem in ip_split:
        try:
            int_elem = int(elem)
            if int_elem <= 255:
                ip_parsed.append(int_elem)
            else:
                return "invalid ip"
        except Exception as e:
            print(e)
            return "invalid ip"
    ip_parsed_str = [str(elem) for elem in ip_parsed]
    return ".".join(ip_parsed_str)

def main():
    ipA = "10.300.0.0"
    ipB = "10.010.60.30"
    print(format_ip(ipA))
    print(format_ip(ipB))

main()
