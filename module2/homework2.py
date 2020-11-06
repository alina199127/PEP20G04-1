# Prove "and" operation takes precedence over "or" operation
print((False or (False and True) or True)==(False or False and True or True))
print((False or False) and (True or True)==(False or False and True or True))
