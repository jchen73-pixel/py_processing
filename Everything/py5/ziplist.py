# def zipLists(a, b) -> list
# a,b: list
# Returns a list of the contents of a & b intercalated,
# adding the rest of the longer list (if any) at the end.
# Assumes valid inputsdef zipLists(a, b):
def zipLists(a, b):
     new = []
     i = 0
     while len(a) > i and len(b) > i:
        new += [a[i], b[i]]
        i += 1
     new += a[i:] + b[i:]
     return new
