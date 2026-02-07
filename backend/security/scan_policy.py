import ipaddress

def is_safe_target(ip: str):
    """
    Allow only:
    - Localhost
    - Private networks
    """

    try:
        ip_obj = ipaddress.ip_address(ip)

        return (
            ip_obj.is_private or
            ip_obj.is_loopback
        )

    except:
        return False
