# -*- coding: utf-8 -*-
from hashids import Hashids

# from media.db import get_db
# from werkzeug.exceptions import abort

user_id_hashids = Hashids(salt="test", min_length=5)
# hashing and decoding user_id of length 16
def update_user_id_hashids(user_id, day):
    global user_id_hashids
    user_id_hashids = Hashids(salt=str(10 * user_id + day) + "user_id", min_length=16)

def create_user_id_hashid(user_id, day):
    update_user_id_hashids(user_id, day)
    hashed_user_id = user_id_hashids.encrypt(user_id)
    return hashed_user_id

def decode_user_id_hashid(hashed_user_id):
    user_id = user_id_hashids.decrypt(hashed_user_id)
    return user_id


day_hashids = Hashids(salt="test", min_length=7)
# hashing and decoding day of length 10
def update_day_hashids(user_id, day):
    global day_hashids
    day_hashids = Hashids(salt=str(10 * user_id + day) + "day", min_length=10)

def create_day_hashid(user_id, day):
    update_day_hashids(user_id, day)
    hashed_day = day_hashids.encrypt(day)
    return hashed_day

def decode_day_hashid(hashed_day):
    day = day_hashids.decrypt(hashed_day)
    return day

# if __name__== "__main__":
#     my_user_id = input("user_id: ")
#     my_day = input("day: ")
#     print("encoding:" + my_user_id + "/" + my_user_id)
#
#     my_hashed_user_id = create_user_id_hashid(int(my_user_id), int(my_day))
#     my_hashed_day = create_day_hashid(int(my_user_id), int(my_day))
#     print("encoded:" + my_hashed_user_id + "/" + my_hashed_day)
#
#     decoded_my_user_id = decode_user_id_hashid(my_hashed_user_id)
#     decoded_my_day = decode_day_hashid(my_hashed_day)
#     print("decoded:" + str(decoded_my_user_id[0]) + "/" + str(decoded_my_day[0]))
