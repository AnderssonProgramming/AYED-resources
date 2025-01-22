def listInsert(L,x):
    x.next = L.head

    if L.head != None:
        L.head.prev = x
    L.head = x
    x.prev = None

def listDelete(L,x):
    if x.prev != None:
        x.prev.next = x.next
    elif x.next != None:
        x.next.prev = x.prev
    else:
        L.head = x.next

def listSearch(L,k):
    x = L.head
    while x != None and x.key != k:
        x = x.next
    return x

