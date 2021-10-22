def swap(f):
    def new_f(*a, **b):
        a = a[:: -1]
        res = f(*a, **b)
        return res
    return new_f

