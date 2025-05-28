#creating a place for valid status codes, http methods.

valid_status_codes = ["200", "301", "302", "400", "401", "403", "404", "500", "502", "503"]
valid_http_methods = ["GET", "POST"]

#prompt the user to enter their log file path they want to analyze
log_path = input("Enter the log file path here: ").strip()


#have the user enter what they're searching for or if they want to skip

target_ip = input("Type in the IP address you wish to filter for (or press Enter to skip): ").strip()
target_status_code = input(f"Please enter the Status Code you wish to filter by {valid_status_codes} (or press Enter to skip): ").strip( )
target_http_method = input(f"Please enter the HTTP method you wish to filter by {valid_http_methods} (or press Enter to skip): ").upper().strip()

#compares user input to valid inputs and if matched, opens the log provided and searches for matches

if target_status_code and target_status_code not in valid_status_codes:
    print(f"Invalid Status Code entry. Please enter one of the valid options {valid_status_codes}")
    exit()

if target_http_method and target_http_method not in valid_http_methods:
    print(f"Invalid HTTP Method entry. Please enter of of the valid options {valid_http_methods}")
    exit()


try:
    with open(log_path, "r") as file:
        print("\n Matching log entries:\n" + "-" * 40)
        found = False
        for line in file:
            cleaned_line = line.strip()
            if cleaned_line:
                if not cleaned_line:
                    continue


                log_part = cleaned_line.split(" ")
                if len(log_part) >= 9:
                    ip_address = log_part[0]
                    timestamp = log_part[3].strip("[]")
                    request_method = log_part[4].strip('"')
                    resource = log_part[5]
                    protocol = log_part[6].strip('"')
                    status_code = log_part[7]
                    response_size = log_part[8]

#once matched it will print out results unless entry was skipped

                if (
                    (not target_ip or ip_address == target_ip) and
                    (not target_status_code or status_code == target_status_code) and
                    (not target_http_method or request_method == target_http_method)
                ):
                    print(cleaned_line)
                    found = True
        if not found:
            print("No matching entries found.")
except FileNotFoundError:
    print(f"Error: Log file not found in path provided: {log_path}")
except Exception as e:
    print(f"An error occured: {e}")
