from datetime import datetime
from logging import Formatter, getLogger, StreamHandler


class MyFormatter(Formatter):

    converter = datetime.fromtimestamp

    def formatTime(self, record, datefmt=None):
        ct = self.converter(record.created)
#         if datefmt:
        s = ct.strftime('%H:%M:%S.%f')
#         else:
#             t = ct.strftime("%H:%M:%S")
#             s = "%s,%03d" % (t, record.msecs)
        return s

logger = getLogger()
logger.setLevel('DEBUG')

console = StreamHandler()
logger.addHandler(console)

formatter = MyFormatter(fmt='[%(asctime)s] %(message)s')
console.setFormatter(formatter)
