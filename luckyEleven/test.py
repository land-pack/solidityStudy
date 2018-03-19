#from pysol.wallet import create_account
#from pysol.watch import watching
#from pysol.rpc import get_balance
from pysol.rpc import get_result_num
from pysol.rpc import submit_block_hash

# Test model
#from model.order import Luckyeleven


from utils.cache import push_block, top_block
from utils.cache import push_user_place_hash, pop_by_hx, left_hx, is_finish_order



if __name__ == '__main__':
    #print("Test create_account(12345) == {}".format(create_account('12345')))
    #watching()
    #while(1):
    #    pass
    #print(get_balance())

    #with Luckyeleven() as db:
    #    db.update_succ('0xde1ce69f800cab6451f1e50aeb4c6b088a8f106533e4b121c719f208b4e0bb27')


#    push_block(1123, 122)
#    push_block(1123, 12)
#    push_block(1123, 182)
#    print(top_block(1123))
#
#    set_win_num()
#
    print(left_hx(1001))
#    push_user_place_hash(1001, 123)
#    push_user_place_hash(1001, 13)
#    push_user_place_hash(1001, 23)
    print(left_hx(1001))
    pop_by_hx(1001, 123)
    print(is_finish_order(1001))
    pop_by_hx(1001, 13)
    print(left_hx(1001))
    print(is_finish_order(1001))


    submit_block_hash('1803161918')
    get_result_num('1803161918')
