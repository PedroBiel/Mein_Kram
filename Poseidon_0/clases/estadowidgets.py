class EstadoWidgets:
    """Color y activación iniciales de los widgets Checkbox, Label y LineEdit"""

    def __init__(self, cb, lb, le):

        self.chkbx = cb  # Checkbox.
        self.lbl = lb    # Label.
        self.lndt = le   # LineEdit.

    # Color inicial de chekbox.

    def chkbx_activado(self):

        self.chkbx.setStyleSheet('color: black')

    def chkbx_desactivado(self):

        self.chkbx.setStyleSheet('color: gray')

    # Color inicial de label.

    def lbl_activado(self):

        self.lbl.setStyleSheet('color: black')

    def lbl_desactivado(self):

        self.lbl.setStyleSheet('color: gray')

    # Activación inicial de lineEdit.

    def lndt_activado(self):

        self.lndt.setEnabled(True)

    def lndt_desactivado(self):

            self.lndt.setEnabled(False)

    # Activa widgets.

    def activa_widgets(self):
        """Activa los widgets si CheckBox ischecked."""

        if self.chkbx.isChecked() is True:

            self.chkbx.setStyleSheet('color: black')
            self.lbl.setStyleSheet('color: black')
            self.lndt.setEnabled(True)

        else:

            self.chkbx.setStyleSheet('color: gray')
            self.lbl.setStyleSheet('color: gray')
            self.lndt.setEnabled(False)
            self.lndt.clear()