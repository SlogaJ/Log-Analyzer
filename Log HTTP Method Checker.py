valid_http_method = ["GET", "POST"]
target_http_method = input("Please enter the HTTP method you wish to filter for: ").upper()

if target_http_method not in valid_http_method:
        print("Invalid Input, please enter either GET or POST")
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

                    method_parts = request_method.split(" ")
                    if len(method_parts) > 0:
                         method = method_parts[0]
                         if method == target_http_method:
                              print(cleaned_line)