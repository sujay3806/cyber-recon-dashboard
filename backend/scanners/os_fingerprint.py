import subprocess
import platform

def detect_os(ip:str):
    
    try:
        param = "-n" if platform.system().lower() == "windows" else "-c"
        
        command = ["ping",param,"1",ip]
        output= subprocess.check_output(command).decode()
        
        ttl_value = int(output.lower().split("ttl=")[1].split()[0])
        
        if ttl_value<= 64:
            return "Linux/Unix"
        elif ttl_value<= 128:
            return "Windows"
        else:
            return "Network Device"
        
    except Exception as e:
        print("OS Detection failed",e)
        return "Unknown (ICMP Blocked or Filtered)"