"""fruit = "apple orange pear"
list_of_fruit = fruit.split()
print (list_of_fruit)

log_entry = "192.168.1.1 - - [16/May/2025:13:45:00] GET /index.html"
log_parts = log_entry.split()
print(log_parts)

C:\\Users\\Jeremiah\\VS Code\\Python Projects\\FirstProjects.py\\access.log
"""

with open("C:\\Users\\Jeremiah\\VS Code\\Python Projects\\FirstProjects\\access.log", "r") as file:
    for line in file:
        cleaned_line = line.strip()
        if cleaned_line:
            log_part = cleaned_line.split(" ")
            if len(log_part) >= 9:
                ip_address = log_part[0]
                timestamp = log_part[3].strip("[]")
                request_method = log_part[4].strip('"')
                resource = log_part[5]
                protocol = log_part[6].split()
                status_code = log_part[7]
                response_size = log_part[8]

                print(f"IP Address: {ip_address}")
                print(f"Timestamp: {timestamp}")
                print(f"Request Method: {request_method}")
                print(f"Resource: {resource}")
                print(f"Protocol: {protocol}")
                print(f"Status Code: {status_code}")
                print(f"Response Size: {response_size}")
                print("---")
