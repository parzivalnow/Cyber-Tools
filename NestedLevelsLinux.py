def minOperations2RootDirectory(self, logs: List[str]) -> int:
    change = 0
    for log in logs:
        if log == "../" and change > 0:
            change -= 1
        elif log != "../" and log != "./":
            change += 1
    return change