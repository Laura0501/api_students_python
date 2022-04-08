from .node import Node

class ListSE:
    def __init__(self):
        self.head= None

    def add(self, data):
        if self.head== None:
            self.head = Node(data)

        else:
            if self.validate_exist(data.identification):
                raise Exception("Ya existe un estudiante con la identificacion")
            temp=self.head

            while temp.next != None:
                temp=temp.next
            #posicionandonos en el ultimo

            temp.next=Node(data)

    def validate_exist(self,id):
            temp=self.head
            while temp != None:
                if temp.data.identification==id:
                    return True
                temp=temp.next
            return False












