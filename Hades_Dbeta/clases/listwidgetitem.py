import sys

from PyQt4.QtGui import QApplication, QListWidget, QListWidgetItem


class ListWidgetItem(QListWidgetItem):
    """Order items respect to the numeric value."""

    def __lt__(self, other):

        try:

            return float(self.text()) < float(other.text())

        except Exception:

            return QListWidgetItem.__lt__(self, other)


class OrdenaNumericamente(ListWidgetItem):
    """Ordena los items de un listWidget numéricamente"""
    
    def __init__(self, lst):
        
        self.lst = lst
        
    def ordena_numericamente(self):

        items = []
    
        for index in range(self.lst.count()):
            
            items.append(self.lst.item(index).text())
        
        self.lst.clear()
        
        for i in items:             
                                         
            try:                    # Si i tiene la forma 'caso : nombre' (1 : g estructura)
                                    # para que funcione la función solo puede haber cifras.
                ind = i.index(' ')  # Busca la posición del primer espacio ' '.
                caso = i[:ind]      # Selecciona los carácteres antes del primer espacio ' ' (caso).
            
                self.lst.addItem(ListWidgetItem(str(caso)))
                
                
            except:                                       # Si i tiene la forma 'caso' (1) (cuando el item procede de grupos de casos de carga).
                
                self.lst.addItem(ListWidgetItem(str(i)))  # añade directamente i.
                
            self.lst.sortItems()


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    w = QListWidget()
    for i in [1, 10, 100, 11, 110, 111, 12]:
        w.addItem(ListWidgetItem(str(i)))
    w.sortItems()
    w.show()
    sys.exit(app.exec_())
