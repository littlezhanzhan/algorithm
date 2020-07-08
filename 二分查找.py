def main(SearchList , Value):
    if Value > SearchList[-1] or Value < SearchList[0]:
        return 0
    position = BaseSearch(len(SearchList)-1, 0, SearchList, Value)
    return position

def BaseSearch(high, low , List, Value):
    if low > high:
        return -1
    Mid = low+int((high-low)/2)
    if List[Mid] > Value:
        return BaseSearch(Mid-1, low, List, Value)
    elif List[Mid] < Value:
        return BaseSearch(high, Mid+1, List, Value)
    else:
        return Mid

a = [1,2,3,4,5,6,7,10,11,12,14,22,34]
value = 4
print(main(a, 15))