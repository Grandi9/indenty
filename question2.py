

import numpy as np

nums = np.random.rand(4,3)
print(nums)
#input check

#output here
print np.where(nums > 0.2, 0, nums)
