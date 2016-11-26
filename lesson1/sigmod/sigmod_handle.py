from math import exp
# import numpy as np


#def sigmod(x):
#    return 1/(1 + math.exp(-x))

def sigmod(x):
    #Numerically-stable sigmod function
    if x >= 0:
        z = exp(-x)
        return 1 / (1 + z)
    else:
        z = exp(x)
        return z / (1 + z)

# def nat_to_exp(q):
#     max_q = max(0.0, np.max(q))
#     rebased_q = q - max_q
#     return np.exp(rebased_q - np.logaddexp(-max_q, np.logaddexp.__reduce__(rebased_q)))
def sigmod_range():
    for val in range(0, 710, 1):
        try:
            # print val
            y = exp(val)
        except:
            print  val, y
            break

if __name__ == "__main__":
    sigmod_range()

