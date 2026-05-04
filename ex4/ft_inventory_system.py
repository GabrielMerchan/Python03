#!/usr/bin/env python3

import sys

def parser() -> dict:
    inventory = {}
    for i in sys.argv[1:]:
            command = i.split(':')
            inventory[command[0]] = int(command[1])
    return inventory


def count_item(inventory: dict) -> int:
    sum(inventory.values())


def maxmin_item(inventory: dict, order: str) -> list:
    cont_lst = list(inventory.values())
    cont = cont_lst[0]
    key_lst = list(inventory.keys())
    key = key_lst[0]
    if order == "max":
        for i in inventory:
            if inventory[i] > cont:
                cont = inventory[i]
                key = i
    elif order == 'min':
        for i in inventory:
            if inventory[i] < cont:
                cont = inventory[i]
                key = i        
    maxmin_item = {key:cont}
    return maxmin_item


def display() -> None:
    invent = parser()
    print("=== Inventory System Analysis ===")
    print(f"Got inventory: {invent}")
    keys_lst = list(invent.keys())
    print(f"Item list: {keys_lst}")
    val_sum = sum(invent.values())
    print(f"Total quantity of the {len(invent)} items: {val_sum}")
    for i in keys_lst:
        print(f"Item {i} represents {round(float((invent[i] / val_sum)*100), 1)}%")
    cont_invent = maxmin_item(invent, 'max')
    keys_lst = list(cont_invent.keys())
    val_lst = list(cont_invent.values())
    print(f"Item most abundant: {keys_lst[0]} with quantity {val_lst[0]}")
    cont_invent = maxmin_item(invent, 'min')
    keys_lst = list(cont_invent.keys())
    val_lst = list(cont_invent.values())
    print(f"Item least abundant: {keys_lst[0]} with quantity {val_lst[0]}")
    invent.update({'bow':2, 'arrow':10})
    print(f"Updated inventory: {invent}")


if __name__ == "__main__":
    display()