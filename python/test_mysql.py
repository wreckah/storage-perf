from datetime import datetime, timedelta
from itertools import chain
from math import ceil
from os.path import dirname
from random import randint, shuffle
from time import time

import MySQLdb as db

from records import MID_RECORD
from utils import logger

DB_PARAMS = {
    'user': 'root',
    'passwd': 'croot',
#     'db': 'test',
#     'cursorclass': db.cursors.DictCursor
}


class MysqlTest(object):
    ITER_NUM = 1000
    RECORDS = [100, 10000, 1000000]
    CHUNK_SIZE = 1000
    CREATED_INTERVAL = 10  # sec

    def __enter__(self):
        self.connection = db.connect(**DB_PARAMS)
        self.cursor = self.connection.cursor()

        self.cursor.execute('SHOW DATABASES LIKE %s', ['test'])
        if self.cursor.fetchone():
            self.cursor.execute('USE `test`')
            return self

        self.cursor.execute(
            'CREATE DATABASE `test` CHARACTER SET utf8 COLLATE utf8_general_ci'
        )
        self.cursor.execute('USE `test`')

        return self

    def __exit__(self, *args, **kwargs):
        del self.cursor
        self.connection.close()

    def setup_table(self, num):
        table = 'test_%s' % num
        self.cursor.execute('SHOW TABLES LIKE %s', [table])
        if self.cursor.fetchone():
            # Table already exists.
            return table

        logger.debug('Creating table "%s"' % table)

        _dir = dirname(__file__) or '.'
        with open(_dir + '/mysql_mid_table.sql', 'rb') as f:
            sql = f.read() % num
        self.cursor.execute(sql.strip(' ;\r\n'))

        delta = timedelta(seconds=self.CREATED_INTERVAL)
        start_dt = datetime.now() - delta * num
        for chunk in xrange(int(ceil(float(num) / self.CHUNK_SIZE))):
            values = list(chain(*[[
                MID_RECORD['name'] % (i + chunk * self.CHUNK_SIZE),
                MID_RECORD['data'],
                start_dt + delta * i,
            ] for i in xrange(self.CHUNK_SIZE)]))
            sql = (
                'INSERT INTO `%s` (`name`, `data`, `created`) VALUES ' % table
            ) + ('(%s, %s, %s), ' * self.CHUNK_SIZE)[:-2]
            self.cursor.execute('BEGIN')
            self.cursor.execute(sql, values)
            self.cursor.execute('COMMIT')
#             logger.debug(
#                 'Inserted chunk #%s with %s middle sized records',
#                 chunk + 1, self.CHUNK_SIZE
#             )
        logger.debug('Created with %s records' % num)
        return table

    def test_getting_mid_record_wo_cache(self):
        logger.debug('')
        for REC_NUM in self.RECORDS:
            logger.debug('-' * 80)
            logger.debug('Testing getting %s middle sized objects from MySQL () from table with %s records', self.ITER_NUM, REC_NUM)
            logger.debug('This test also prevents heating MySQL cache by querying the same objects.')

            table = self.setup_table(REC_NUM)

            # Prevents using cache.
            keys = range(REC_NUM)
            shuffle(keys)
            keys = keys[:self.ITER_NUM]

            res = []
            sql = 'SELECT * FROM `%s` WHERE id=%%s' % table

            for key in keys:
                t = time()
                self.cursor.execute(sql, [key])
                _ = self.cursor.fetchall()
                res.append(time() - t)

            self.report(res, len(keys))

    def test_getting_mid_record_with_cache(self):
        logger.debug('')
        for REC_NUM in self.RECORDS:
            logger.debug('-' * 80)
            logger.debug('Testing getting %s middle sized objects from MySQL () from table with %s records', self.ITER_NUM, REC_NUM)
            logger.debug('Using MySQL cache.')

            table = self.setup_table(REC_NUM)

            res = []
            sql = 'SELECT * FROM `%s` WHERE id=%%s' % table

            for _ in xrange(self.ITER_NUM):
                key = randint(1, REC_NUM)
                t = time()
                self.cursor.execute(sql, [key])
                _ = self.cursor.fetchall()
                res.append(time() - t)

            self.report(res, self.ITER_NUM)

    def report(self, res, num):
        logger.debug('Min query time: %.3f msec', min(res) * 1000)
        avg = sum(res) / num * 1000
        logger.debug('Avg query time: %.3f msec', avg)
        res = sorted(res)
        perc_90 = res[int(ceil(len(res) * .9))] * 1000
        logger.debug('90%% of queries were faster than: %.3f msec', perc_90)
        perc_99 = res[int(ceil(len(res) * .99))] * 1000
        logger.debug('99%% of queries were faster than: %.3f msec', perc_99)
        logger.debug('Max query time: %.3f msec', max(res) * 1000)


if __name__ == '__main__':
    with MysqlTest() as test:
        test.test_getting_mid_record_wo_cache()
        test.test_getting_mid_record_with_cache()
