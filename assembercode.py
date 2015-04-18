import sys
from PyQt4 import QtCore, QtGui

import assember


class AssemberWindow(QtGui.QMainWindow, assember.Ui_AssemBER):
    def __init__(self, parent=None):
        super(AssemberWindow, self).__init__(parent)
        self.setupUi(self)

        self.connect(self.convertasm, QtCore.SIGNAL("clicked()"), self.convertasmcode)

    def convertasmcode(self):
        code = self.asmtextedit.toPlainText()
        print code
        self.mlecode.setText(code)

app = QtGui.QApplication(sys.argv)
form = AssemberWindow()
form.show()
app.exec_()