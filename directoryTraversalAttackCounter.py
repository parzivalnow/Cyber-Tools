### Detecting the level length change of a directory traversal attack ###
def amountOfChangeInDirectoryTraversalAttack(self, logs: List[str]) -> int:
    change = 0
    for log in logs:
        if log == "../":
            change += 1
    return change