# Copyright (c) 2020 Jonas Thorsell
import sys

def cls(pk, sn=7):
    ls = 0
    v = 1
    while not v == pk:
        ls += 1
        v = (v * sn) % 20201227
    return ls

def cek(ls, sn):
    v = 1
    for i in range(ls):
        v = (v * sn) % 20201227
    return v


card_pk = int(sys.stdin.readline())
door_pk = int(sys.stdin.readline())

card_ls = cls(card_pk)
door_ls = cls(door_pk)

print(f'card pk: {card_pk} ls: {card_ls}')
print(f'door pk: {door_pk} ls: {door_ls}')
print(cek(card_ls, door_pk))
print(cek(door_ls, card_pk))
