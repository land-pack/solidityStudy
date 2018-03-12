#!/usr/bin/python

import MySQLdb


class DBS(object):

    def __enter__(self):
        # Open database connection
        self.db = MySQLdb.connect("localhost",
                                "root",
                                "openmysql",
                                "test")
        # Prepare a cursor object using cursor() method
        self.cursor = self.db.cursor()
        return self


    def __exit__(self, exception_type, exception_value, traceback):
        print 'Close database connection'
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
                f_result, f_status, f_trade_addr):
        """
        if f_status is win and then read the `f_result` else just output `f_status`.
        """
        sql = """
            INSERT INTO t_trade(f_user_addr, f_expect_id, f_lucky_num, f_digit_curreny,
            f_result, f_status, f_trade_addr)VALUE(%s, %s, %s, %s, %s, %s, %s)
        """
        try:
            self.cursor.execute(sql, (f_user_addr, f_expect_id, f_lucky_num,
                f_digit_curreny, f_result, f_status, f_trade_addr))
            self.db.commit()
        except:
            # Rollback  in case there is any error
            self.db.commit()





if __name__ == '__main__':
    
    with Luckyeleven() as dbs:
        print dbs.fetch_version()


    with Luckyeleven() as dbs:
        dbs.save(1803120252, 102, 1)



    with Luckyeleven() as dbs:
        dbs.place('012x23712aawdmqmdwqww',
                1803120252, '1|3|6|8|10',
                0.00021, 0, 0,
                '012akmsdl3l2m2mm2m2l2m2')

