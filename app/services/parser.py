# Here I have to implement the Parser class which will be responsible for parsing log files and extracting relevant information for analysis.
def parse_logs(log_text):

    logs = []

    for line in log_text.split("\n"):

        parts = line.split(" - ")

        if len(parts) == 2:
            logs.append({
                "ip": parts[0],
                "event": parts[1]
            })

    return logs