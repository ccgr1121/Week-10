import sys
from my_exceptions import NotFoundException

try:
    raise NotFoundException("cannae be bovverred m80")
except NotFoundException as e:
    print(e)
