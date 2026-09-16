import socket
from datetime import datetime
target=input(" enter website name | enter IP adress  ")
allowed_targets = ["scanme.nmap.org", "127.0.0.1", "localhost"]
if target not in allowed_targets:
    print("ACCESS DENIED: You do not have permission to scan that target!")
    exit()
target_ip= socket.gethostbyname(target)
print(target_ip)
print("-"*50)
print(f"Scanning-Target {target}")
print("-"*50)
A=int(input(" enter port range "))
B=int(input(" enter port range "))
start_time = datetime.now()
for  port in range(A,B+1):
    print(f"Scanning port {port}...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target_ip, port))
    if result==0:
        print(f"port {port} is open !")
    s.close()
end_time = datetime.now()
print(f"Scan completed in: {end_time - start_time}")
