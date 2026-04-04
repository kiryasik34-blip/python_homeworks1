def errors_logs (logs):
    errors =[]

    for log in logs:
        if "ERROR" in log:
            errors.append(log)
    return errors

def counts_errors(logs):
    return len(errors_logs(logs))

logs = [
    "INFO: start",
    "ERROR: file not found",
    "INFO: retry",
    "ERROR: timeout",
]

errors = errors_logs(logs)

print("Oshibki")
for e in errors:
    print(e)
print(f'KOLVO: {counts_errors(logs)}')
