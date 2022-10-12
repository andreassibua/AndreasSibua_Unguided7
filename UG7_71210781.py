class StackList:
def __init__(self):


self.stack_data = list()
def push(self, new_data):


self.stack_data.append(new_data)
def top(self):


if len(self.stack_data) == 0:
return None
else:
return self.stack_data[-1]
def pop(self):


if len(self.stack_data) == 0:
return None
else:
pop_data = self.stack_data.pop()
return pop_data
def size(self):


return len(self.stack_data)
class UndoRedo:
def __init__(self):


self.mainStack = StackList()  # stack ini sebagai tempat menyimpan
data pertama kali
self.backupStack = StackList()  # stack ini sebagai tempat menyimpan
data yang di hapus


def write(self, data):
    # Tuliskan Code Anda Disini


def undo(self):
    # Tuliskan Code Anda Disini


def redo(self):
    # Tuliskan Code Anda Disini


def printInfo(self):

    # Tuliskan Code Anda Disini
Test Case
if __name__ == '__main__':
obj_undoredo = UndoRedo()
obj_undoredo.undo()  # Test case Jika belum ada data yang ditambahkan
obj_undoredo.redo()  # Test case jika belum ada data yang di undo
obj_undoredo.write('Pada Suatu Hari hiduplah seorang kakek-kakek')
obj_undoredo.write("Dia tinggal sebatang kara di pegunungan")
obj_undoredo.write("Dia kemudian turun gunung buat kuliah")
obj_undoredo.write("SEMESTER 5 BANYAK TUGASSSSSSS !!!")
obj_undoredo.printInfo()
obj_undoredo.undo()
obj_undoredo.undo()
obj_undoredo.undo()
obj_undoredo.undo()
obj_undoredo.redo()
obj_undoredo.redo()
obj_undoredo.redo()
