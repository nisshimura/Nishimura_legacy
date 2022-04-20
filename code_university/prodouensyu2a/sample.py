import nnabla as nn
import nnabla.functions as F
import nnabla.parametric_functions as PF

def network(x, y, test=False):
    # Input:x -> 1,28,28
    # Affine -> 100
    h = PF.affine(x, (100,), name='Affine')
    # Softmax
    h = F.softmax(h)
    # CategoricalCrossEntropy -> 1
    h = F.categorical_cross_entropy(h, y)
    return h
