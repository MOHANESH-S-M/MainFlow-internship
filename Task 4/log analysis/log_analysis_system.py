# This is Task 4 project
"""4. Log Analysis System
 ● Description    : Write a program to parse large log files (e.g., web server logs) and extract 
                    insights like the most frequent IP addresses, response codes, or URLs accessed.
 ● Challenges     :
                    ○ Efficiently process large text files.
                    ○ Handle various formats and error cases in logs.
                    ○ Summarize and display data meaningfully.
 ● Skills         : File I/O, data parsing, and data aggregation.
 ● Restriction    : File size must be limited to 100 MB for log files.

 ● Reason         : Log analysis is important for many real-world applications, but dealing with
                        large datasets can become cumbersome. Limiting file size helps students focus on data
                        parsing and insight extraction, allowing them to develop efficient file handling techniques
                        without being overwhelmed. It also simulates real-world constraints like processing time
                        and memory limits.
 ● Learning Outcome: Students will learn how to efficiently process large datasets, extract
                        meaningful insights, and handle file-based data using basic algorithms and data
                        structures like dictionaries and lists."""
from collections import defaultdict

with open(r"d:\pythonprgms\Mainflow internship tasks\MainFlow-internship\Task 4\log analysis\logs_apache_logs.txt", 'r') as file:
    logs = file.readlines()

ip_address_count = defaultdict(int)
url_count = defaultdict(int)
response_code_count = defaultdict(int)

for line in logs:
    # for getting ip address
    ip = line.split(' ')[0]
    ip_address_count[ip] += 1
    # for getting url
    try :
        quotation_starting = line.index('"') + 1
        quotation_ending = line.index('"',quotation_starting)
        request_made = line[quotation_starting:quotation_ending]
        url = request_made.split(' ')[1]
    except (ValueError,IndexError):
        url = 'INVALID'
    url_count[url]+=1
    #for getting response code
    parts = line[quotation_ending+1:].strip().split(' ',1)
    request_code = parts[0] if parts else 'UNKNOWN'
    response_code_count[request_code] += 1

def frequent_ip_addr():
    max_key = None
    max_count = -1
    for k,v in ip_address_count.items():
        if v > max_count:
            max_count = v
            max_key = k
    return max_key

def frequent_url_addr():
    max_key = None
    max_count = -1
    for k,v in url_count.items():
        if v > max_count:
            max_count = v
            max_key = k
    return max_key

def frequent_response_code():
    max_key = None
    max_count = -1
    for k,v in response_code_count.items():
        if v > max_count:
            max_count = v
            max_key = k
    return max_key
print("frequent IP Address",frequent_ip_addr())
print("frequent URL Address",frequent_url_addr())
print("frequent Response Code",frequent_response_code())