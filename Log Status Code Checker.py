valid_status_code = ["200", "301", "302", "400", "401", "403", "404", "500", "502", "503"]
target_status_code = input("Please enter the Status Code you wish to filter by: ")

if target_status_code not in valid_status_code:
    print("Invalid Status Code input, please enter a valid Status Code.")
else:
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
                if status_code == target_status_code:
                    print(cleaned_line)
