from torch import nn, Tensor

from . import register_act_fn


@register_act_fn(name="relu")
class ReLU(nn.ReLU):
    def __init__(self, inplace: bool = False):
        super(ReLU, self).__init__(inplace=inplace)

    def profile_module(self, input: Tensor) -> (Tensor, float, float):
        return input, 0.0, 0.0
