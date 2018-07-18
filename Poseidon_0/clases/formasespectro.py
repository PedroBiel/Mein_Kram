import matplotlib.pyplot as plt


class FormasEspectro:

    def __init__(self, chkbx_X, chkbx_Y, chkbx_Z, T, SdTx, SdTy, SdTz):

        self.chkbx_X = chkbx_X
        self.chkbx_Y = chkbx_Y
        self.chkbx_Z = chkbx_Z
        self.T = T
        self.SdTx = SdTx
        self.SdTy = SdTy
        self.SdTz = SdTz

        self.etiqueta = ''
        self.etiqueta_x = '$S_d(T)_x$'
        self.etiqueta_y = '$S_d(T)_y$'
        self.etiqueta_z = '$S_d(T)_z$'
        self.color = ''

        self.x = self.T
        self.max_y = 0

        plt.style.use('seaborn-darkgrid')


    def plt_show(self):

        fig, self.ax = plt.subplots()

        if self.chkbx_Z.isChecked() is True:

            self.y = self.SdTz
            self.etiqueta = '$S_d(T)_z$'
            self.color = 'b'
            self.ax_plot()

            # ax.plot(x, y3, color='b', linewidth=2, label=etiqueta)
            #
            # if self.max_y < max(y3):
            #
            #     max_y = max(y3)

        if self.chkbx_Y.isChecked() is True:

            self.y = self.SdTy
            self.etiqueta = '$S_d(T)_y$'
            self.color = 'g'
            self.ax_plot()

        if self.chkbx_X.isChecked() is True:

            self.y = self.SdTx
            self.etiqueta = '$S_d(T)_y$'
            self.color = 'g'
            self.ax_plot()

        # self.ax.axis([0, 4, 0, self.max_y + 0.5])
        self.plt.ylim(self.max_y + 0.5)
        self.ax.set_xlabel('$T$ [s]', fontsize=14)
        self.ax.set_ylabel('$S_e(T)$ [g]', fontsize=14)
        self.ax.legend(prop={'size': 14})
        self.ax.set_title('Shapes of the design spectrum for the elastic analysis', fontsize=16)
        plt.show()

    def ax_plot(self):

        self.ax.plot(self.x, self.y, color=self.color, linewidth=2, label=self.etiqueta)

        if self.max_y < max(self.y):

            self.max_y = max(self.y)


