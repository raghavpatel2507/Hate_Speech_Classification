from hate.logger import logging
from hate.exception import CustomException
import sys
#logging.info('hello welcome to my project')

try:
    a=25/"2"
except Exception as e:
    raise CustomException(e,sys) from e