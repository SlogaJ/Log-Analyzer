<<<<<<< HEAD
target_ip = input("Type in the IP address you wish to filter for: ")

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
                protocol = log_part[6].strip('"')
                status_code = log_part[7]
                response_size = log_part[8]
            if ip_address == target_ip:
=======
target_ip = input("Type in the IP address you wish to filter for: ")

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
                protocol = parts[6].strip('"')
                status_code = parts[7]
                response_size = parts[8]
            if ip_address == target_ip:
>>>>>>> 2320b8bc65d89e2d3b271e2ba7040b297fd7bb7a
                print(cleaned_line)