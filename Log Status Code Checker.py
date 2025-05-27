valid_status_code = ["200", "301", "302", "400", "401", "403", "404", "500", "502", "503"]
target_status_code = input("Please enter the Status Code you wish to filter by: ")

if target_status_code not in valid_status_code:
    print("Invalid Status Code input, please enter a valid Status Code.")
else:
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
                if status_code == target_status_code:
                    print(cleaned_line)
