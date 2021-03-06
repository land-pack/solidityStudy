#!/usr/bin/python

import traceback

try:
    import MySQLdb  as DBMS
except:
    import _mysql as DBMS

from pysol import rpc
from utils.cache import push_user_place_hash, pop_by_hx, get_current_expect_id

class DBS(object):

    def __enter__(self):
        # Open database connection
        self.db = DBMS.connect("localhost",
                                "root",
                                "openmysql",
                                "test"
                                )


        # Prepare a cursor object using cursor() method
    
        self.cursor = self.db.cursor(DBMS.cursors.DictCursor)
        return self


    def __exit__(self, exception_type, exception_value, traceback):
        print('Close database connection')
        # disconnect from server
        self.db.close()


    def fetch_version(self):
        # Fetch a single row using fetchone() method
        # execute SQL query using execute() method.
        self.cursor.execute("SELECT VERSION()")
        data = self.cursor.fetchone()
        return data


class Luckyeleven(DBS):
    """
    create table magnet_account(id int auto_increment, expect_id int, create_time timestamp, player_total int, status int, primary key (id));
    create table t_trade(f_id int auto_increment, f_create_time timestamp, f_user_addr char(128), f_expect_id int, f_lucky_num char(128), f_digit_curreny decimal(12,6), f_result decimal(12, 6), f_status int, f_trade_addr char(128),  primary key (f_id));
    """
    def save(self, expect_id, player_total, status):
        """
        expect_id:      lottery expect id
        player_total:   player total numbers
        status:         status of the current expect id
                         -1: failure;
                         0:default open;  
                         1:close; 
                         2: have result;
        """
        sql = """
            INSERT INTO magnet_account(expect_id, player_total, status)
            VALUE(%s, %s, %s)
        """

        try:
            self.cursor.execute(sql, (expect_id, player_total, status))
            self.db.commit()
        except:
            # Rollback in case there is any error
            self.db.rollback()


       
    def place(self, f_user_addr, f_expect_id, f_lucky_num, f_digit_curreny,
                f_result, f_status):
        """
        if f_status is win and then read the `f_result` else just output `f_status`.
        """
        sql = """
            INSERT INTO t_trade(f_user_addr, f_expect_id, f_lucky_num, f_digit_curreny,
            f_result, f_status, f_trade_addr)VALUE(%s, %s, %s, %s, %s, %s, %s)
        """
        try:
            number = f_lucky_num.split('|')
            tx = rpc.place(f_user_addr, f_digit_curreny, f_expect_id, number)
            self.cursor.execute(sql, (f_user_addr, f_expect_id, f_lucky_num,
                f_digit_curreny, f_result, f_status, tx))
            push_user_place_hash(f_expect_id, tx)
            self.db.commit()
        except:
            # Rollback  in case there is any error
            self.db.rollback()
            print(traceback.format_exc())
            raise
        else:
            return tx

    def fetch_place(self, filer_by_status=0, filer_by_day=7):
        sql = """
            SELECT f_user_addr as user_addr, f_expect_id as expect_id, f_lucky_num as lucky_num,
            f_digit_curreny as curreny, f_result as result, f_trade_addr as trade_addr
            FROM t_trade
            WHERE f_status=%s AND  datediff(current_date(), f_create_time) < %s;
        """
        try:
            self.cursor.execute(sql, (filer_by_status, filer_by_day))
            data = self.cursor.fetchall()
        except:
            raise
        else:
            return data
    



    def update_succ(self, trade_hash, blockNumber=-1, result=None):
        """
        If callback return with successful status
        Will update the trade status to place successful!
        status :
           -1 : failure 
            0 : pending  (default)
            1 : success
            2 : bingo (get prize)
            3 : no-prize

        """
        sql_succ = """
            UPDATE t_trade
            SET f_status=1, f_block_id=%s
            WHERE f_trade_addr=%s
        """

        sql_set_result = """
            UPDATE t_trade
            SET f_status=2, f_result=%s
            WHERE f_trade_addr=%s

        """

        current_expect_id = get_current_expect_id()
        try:
            if result:
                self.cursor.execute(sql_set_result, (trade_hash, result))
            else:
                push_user_place_hash(current_expect_id, trade_hash)
                self.cursor.execute(sql_succ, (blockNumber, trade_hash))
            self.db.commit()
        except:
            self.db.rollback()
            raise
        else:
            print("Oder update successful!")

    def fetch_order_by_addr(self, addr):
        sql = """
            SELECT f_expect_id as expect_id, f_lucky_num as lucky_num,
            f_digit_curreny as digit_curreny, f_result as prize_result, f_trade_addr as trade_addr,
            f_lucky_result as lucky_result, f_status as status
            FROM t_trade
            WHERE f_user_addr=%s
            ORDER BY f_create_time DESC 
            LIMIT 4
        """

        check_count = """
            SELECT count(*) as counter
            FROM t_trade
            WHERE f_user_addr=%s
        """


        try:
            self.cursor.execute(sql, (addr, ))
            data = self.cursor.fetchall()
            
            self.cursor.execute(check_count, (addr, ))
            counter = self.cursor.fetchone()

        except:
            raise
        else:
            return {
                "data": data,
                "counter": counter
            }

            
    def top_20(self):
        sql = """
            SELECT f_user_addr as user_addr, f_expect_id as expect_id, f_lucky_num as lucky_num,
            f_digit_curreny as digit_curreny, f_result as prize_result, f_trade_addr as trade_addr,
            f_lucky_result as lucky_result, f_create_time as place_time, f_status as status
            FROM t_trade
            ORDER BY f_create_time DESC 
            LIMIT 20
        """
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
        except:
            raise
        else:
            return data



if __name__ == '__main__':
    
    with Luckyeleven() as dbs:
        print(dbs.fetch_version())


    with Luckyeleven() as dbs:
        dbs.save(1803120252, 102, 1)



    with Luckyeleven() as dbs:
        dbs.place('012x23712aawdmqmdwqww',
                1803120252, '1|3|6|8|10',
                0.00021, 0, 0,
                '012akmsdl3l2m2mm2m2l2m2')

    with Luckyeleven() as dbs:
        print(list(dbs.fetch_place()))
