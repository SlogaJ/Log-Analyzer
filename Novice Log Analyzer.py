#creating a place for valid status codes, http methods.

valid_status_code = ["200", "301", "302", "400", "401", "403", "404", "500", "502", "503"]
valid_http_method = ["GET", "POST"]

#have the user enter their search requests

target_ip = input("Type in the IP address you wish to filter for: ").strip()
target_status_code = input("Please enter the Status Code you wish to filter by: ").strip()
target_http_method = input("Please enter the HTTP method you wish to filter for: ").upper().strip()

#compares user input to valid inputs and if matched, opens the log provided and searches for matches

if target_status_code not in valid_status_code or target_http_method not in valid_http_method:
    print("Invalid input, please try again.")
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

#once matched it will print out results

                if status_code == target_status_code or request_method == target_http_method or ip_address == target_ip:
                    print(cleaned_line)