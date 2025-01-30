def filtr(list, fltrs, sps):
    
    newlist = {}
    for item, item_info in list.items():
        if sps == item_info[fltrs]:
          newlist[item] = list[item].copy()
    print(f"{len(newlist)} itens available!\n")
    return newlist