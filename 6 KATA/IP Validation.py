from ipaddress import ip_address

def is_valid_IP(strng):
    try:
        return True if ip_address(strng) else False
    except:
        return False