"""fruit = "apple orange pear"
list_of_fruit = fruit.split()
print (list_of_fruit)

log_entry = "192.168.1.1 - - [16/May/2025:13:45:00] GET /index.html"
parts = log_entry.split()
print(parts)

C:\\Users\\Jeremiah\\VS Code\\Python Projects\\FirstProjects.py\\access.log
"""

with open("C:\\Users\\Jeremiah\\VS Code\\Python Projects\\FirstProjects\\access.log", "r") as file:
    for line in file:
        cleaned_line = line.strip()
        if cleaned_line:
            parts = cleaned_line.split(" ")
            if len(parts) >= 9:
                ip_address = parts[0]
                timestamp = parts[3].strip("[]")
                request_method = parts[4].strip('"')
                resource = parts[5]
                protocol = parts[6].split()
                status_code = parts[7]
                response_size = parts[8]

                print(f"IP Address: {ip_address}")
                print(f"Timestamp: {timestamp}")
                print(f"Request Method: {request_method}")
                print(f"Resource: {resource}")
                print(f"Protocol: {protocol}")
                print(f"Status Code: {status_code}")
                print(f"Response Size: {response_size}")
                print("---")



