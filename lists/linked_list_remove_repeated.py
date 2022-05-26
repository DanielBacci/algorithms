class Linked(object):
    
    def __init__(self, data, next_linked):
        super(Linked, self).__init__()
        self.data = data
        self.next = next_linked


linked = Linked(data=1, next_linked=Linked(data=2, next_linked=Linked(data=1, next_linked=Linked(data=4, next_linked=None))))

def remove_duplicated(linked):
    import ipdb; ipdb.set_trace()
    _previous = linked
    current = linked

    while current:
    
        while _previous.next:
            if _previous.next.data != current.data:
                _previous = _previous.next
                continue
            
            _previous.next = _previous.next.next

        current = current.next

remove_duplicated(linked)
