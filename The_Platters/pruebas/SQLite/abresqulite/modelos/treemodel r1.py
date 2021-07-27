import sys

from PyQt5 import uic
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication


class Node:

    def __init__(self, name, parent=None):

        self._name = name
        self._children = []
        self._parent = parent

        if parent is not None:

            parent.addChild(self)

    def typeInfo(self):

        return 'NODE'

    def addChild(self, child):

        self._children.append(child)

    def insertChild(self, position, child):

        if position < 0 or position > len(self._children):

            return False

        self._children.insert(position, child)
        child._parent = self

        return True

    def removeChild(self, position):

        if position < 0 or position > len(self._children):

            return False

        child = self._children.pop(position)
        child._parent = Node

        return True

    def name(self):

        return self._name

    def setName(self, name):

        self._name = name

    def child(self, row):

        return self._children[row]

    def childCount(self):

        return len(self._children)

    def parent(self):

        return self._parent

    def row(self):

        if self._parent is not None:

            return self._parent._children.index(self)

    def log(self, tabLevel=-1):

        output = ''
        tabLevel += 1

        for i in range(tabLevel):

            output += '\t'

        output += '|------' + self._name + '\n'

        for child in self._children:

            output += child.log(tabLevel)

        tabLevel -= 1
        output += '\n'

        return output

    def __repr__(self):

        return self.log()


class SceneGraphModel(QtCore.QAbstractItemModel):

    def __init__(self, root, parent=None):

        super(SceneGraphModel, self).__init__(parent)
        self._rootNode = root

    def rowCount(self, parent):
        """
        Returns the number of rows under the given parent. When the parent is
        valid it means that rowCount is returning the number of children of
        parent.

        https://doc.qt.io/qt-5/qabstractitemmodel.html#rowCount
        """

        if not parent.isValid():

            parentNode = self._rootNode

        else:

            parentNode = parent.internalPointer()

        return parentNode.childCount()

    def columnCount(self, parent):
        """
        Returns the number of columns for the children of the given parent.

        https://doc.qt.io/qt-5/qabstractitemmodel.html#columnCount
        """

        return 1

    def data(self, index, role):
        """
        Returns the data stored under the given role for the item referred to
        by the index.

        https://doc.qt.io/qt-5/qabstractitemmodel.html#data
        """

        if not index.isValid():

            return None

        node = index.internalPointer()

        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:

            if index.column() == 0:

                return node.name()

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        """
        Sets the role data for the item at index to value.
        """

        if index.isValid():

            if role == QtCore.Qt.EditRole:

                node = index.internalPointer()
                node.setName(value)

                return True

        return False

    def headerData(self, section, orientation, role):
        """
        Returns the data for the given role and section in the header with the
        specified orientation.
        For horizontal headers, the section number corresponds to the column
        number. Similarly, for vertical headers, the section number corresponds
        to the row number.

        https://doc.qt.io/qt-5/qabstractitemmodel.html#headerData
        """

        if role == QtCore.Qt.DisplayRole:

            if section == 0:

                return 'Perfiles'

            else:

                return 'Typeinfo'

    def flags(self, index):
        """
        Returns the item flags for the given index.
        The base class implementation returns a combination of flags that
        enables the item (ItemIsEnabled) and allows it to be selected
        (ItemIsSelectable).

        https://doc.qt.io/qt-5/qabstractitemmodel.html#flags
        """

        return \
            QtCore.Qt.ItemIsEnabled | \
            QtCore.Qt.ItemIsSelectable | \
            QtCore.Qt.ItemIsEditable

    def parent(self, index):
        """
        Returns the parent of the model item with the given index. If the item
        has no parent, an invalid QModelIndex is returned.

        https://doc.qt.io/qt-5/qabstractitemmodel.html#parent
        """

        node = self.getNode(index)
        parentNode = node.parent()

        if parentNode == self._rootNode:

            return QtCore.QModelIndex()

        return self.createIndex(parentNode.row(), 0, parentNode)
        """
        Creates a model index for the given row and column with the internal
        pointer ptr.

        https://doc.qt.io/qt-5/qabstractitemmodel.html#createIndex
        """

    def index(self, row, column, parent):
        """
        Returns the index of the item in the model specified by the given row,
        column and parent index.

        https://doc.qt.io/qt-5/qabstractitemmodel.html#index
        """

        parentNode = self.getNode(parent)
        childItem = parentNode.child(row)

        if childItem:

            return self.createIndex(row, column, childItem)
            """
            Creates a model index for the given row and column with the
            internal pointer ptr.

            https://doc.qt.io/qt-5/qabstractitemmodel.html#createIndex
            """

        else:

            return QtCore.QModelIndex()
            """
            This class is used as an index into item models derived from
            QAbstractItemModel. The index is used by item views, delegates, and
            selection models to locate an item in the model.

            https://doc.qt.io/qt-5/qmodelindex.html
            """

    def getNode(self, index):

        if index.isValid():

            node = index.internalPointer()

            if node:

                return node

        return self._rootNode

    def insertRows(self, position, rows, parent=QtCore.QModelIndex()):

        parentNode = self.getNode(parent)
        self.beginInsertRows(parent, position, position + rows - 1)

        for row in range(rows):

            childCount = parentNode.childCount()
            childNode = Node('untitled' + str(childCount))
            success = parentNode.insertChild(position, childNode)

        self.endInsertRows()

        return success

    def removeRows(self, position, rows, parent=QtCore.QModelIndex()):

        parentNode = self.getNode(parent)
        self.beginRemoveRows(parent, position, position + rows - 1)

        for row in range(rows):

            success = parentNode.removeChild(position)

        self.endRemoveRows()

        return success


class WndTutorial05(QMainWindow):

    def __init__(self):

        QMainWindow.__init__(self)
        uic.loadUi('Tutorial05.ui', self)

        rootNode = Node("Root: db")
        childNode0 = Node("EUROPA", rootNode)
        childNode1 = Node("HEA", childNode0)
        childNode2 = Node("HEB", childNode0)
        childNode3 = Node("HEM", childNode0)
        childNode4 = Node("UPN", childNode0)
        childNode5 = Node("AMÉRICA", rootNode)
        childNode6 = Node("C", childNode0)
        childNode7 = Node("W", childNode0)


        self._proxyModel = QtCore.QSortFilterProxyModel()
        '''
        VIEW <------> PROXY MODEL <------> DATA MODEL
        
        QSortFilterProxyModel can be used for sorting items, filtering out
        items, or both. The model transforms the structure of a source model by
        mapping the model indexes it supplies to new indexes, corresponding to
        different locations, for views to use. This approach allows a given
        source model to be restructured as far as views are concerned without
        requiring any transformations on the underlying data, and without
        duplicating the data in memory.
        
        https://doc.qt.io/qt-5/qsortfilterproxymodel.html
        '''

        self._model = SceneGraphModel(rootNode)
#        self._model.insertLights(0, 10)

        self._proxyModel.setSourceModel(self._model)
        '''
        Sets the given sourceModel to be processed by the proxy model.
        
        https://doc.qt.io/qt-5/qabstractproxymodel.html#setSourceModel
        '''
        
        self._proxyModel.setDynamicSortFilter(True)
        '''
        This property holds whether the proxy model is dynamically sorted and
        filtered whenever the contents of the source model change.
        
        https://doc.qt.io/qt-5/qsortfilterproxymodel.html#dynamicSortFilter-prop
        '''
        
        self._proxyModel.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        '''
        This property holds the case sensitivity of the QRegExp pattern used to
        filter the contents of the source model.

        https://doc.qt.io/qt-5/qsortfilterproxymodel.html#filterCaseSensitivity-prop
        '''
        
        self.uiTree.setModel(self._proxyModel)

        self.uiFilter.textChanged.connect(self._proxyModel.setFilterRegExp)

        self.uiTree.setSortingEnabled(True)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyle("cleanlooks")

    wnd = WndTutorial05()
    wnd.show()

    sys.exit(app.exec_())
