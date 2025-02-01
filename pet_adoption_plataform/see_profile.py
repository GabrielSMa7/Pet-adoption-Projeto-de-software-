def profile(list, name):
    
    newlist = {}
    for item, item_info in list.items():
        if item == name:
          newlist[item] = list[item].copy()
    return newlist