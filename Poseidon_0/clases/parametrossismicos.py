from PyQt4 import QtGui

from classes.EN_1998.part_1._3_ground_conditions_and_seismic_action._3_2_seismic_action_0_0_171106 import SeismicAction


class ParametrosSismicos:

    def __init__(self, chkbx_eje, direcc, agR, gI, ground_type, type_of_spectra, T, m, q, b):

        self.chkbx_eje = chkbx_eje              # checkBox de la dirección de la aceleración símica.
        self.direccion = direcc                 # Dirección de la aceleración sísmica.
        self.agR = agR                          # Aceleración máxima de referencia del suelo en un terreno tipo A
        self.gI = gI                            # Coeficiente de importancia.
        self.ground_type = ground_type          # Tipo de terreno.
        self.type_of_spectra = type_of_spectra  # Tipo de espectro.
        self.T = T                              # Rango del periodo.
        self.m = m                              # Coeficiente de corrección del amortiguamiento.
        self.q = q                              # Coeficiente de comportamiento.
        self.b = b                              # Coeficiente correspondiente al umbral inferior del espectro de cálculo horizontal.

    def parametros_sismicos(self):

        if self.chkbx_eje.isChecked() is True:

            agR = float(self.agR.text())
            gI = float(self.gI.text())
            ground_type = self.ground_type.currentText()
            type_of_spectra = self.type_of_spectra.currentText()
            T = self.T
            m = float(self.m.text())
            q = float(self.q.text())
            b = float(self.b.text())

            accion_sismica = SeismicAction(agR, gI, ground_type, type_of_spectra, T, m, q, b)
            return accion_sismica

    def type_spectra(self):

        return self.type_of_spectra.currentText()

    def ground_typ(self):

        return self.ground_type.currentText()

    def S(self):

        return str(self.parametros_sismicos().soil_factor())

    # Parámetros horizontales.

    def ag(self):

        ag = self.parametros_sismicos().vertical_design_ground_acceleration()
        ag = '{:.4g}'.format(ag)

        return ag

    def TB(self):

        return str(self.parametros_sismicos().lower_limit_of_the_period())

    def TC(self):

        return str(self.parametros_sismicos().upper_limit_of_the_period())

    def TD(self):

        return str(self.parametros_sismicos().beginnig_of_the_constant_displacement())

    def SeT(self):

        return self.parametros_sismicos().horizontal_elastic_response_spectrum()

    def SdT(self):

        return self.parametros_sismicos().horizontal_design_spectrum()

    # Parámetros verticales.

    def avg(self):

        avg = self.parametros_sismicos().vertical_design_ground_acceleration()
        avg = '{:.4g}'.format(avg)

        return avg

    def TBv(self):

        return str(self.parametros_sismicos().vertical_lower_limit_of_the_period())

    def TCv(self):

        return str(self.parametros_sismicos().vertical_upper_limit_of_the_period())

    def TDv(self):

        return str(self.parametros_sismicos().vertical_beginnig_of_the_constant_displacement())

    def SveT(self):

        return self.parametros_sismicos().vertical_elastic_response_spectrum()

    def SvdT(self):

        return self.parametros_sismicos().vertical_design_spectrum()

    # Parámetros.

    def parametros_horizontales(self):

        return (
            self.direccion, self.type_spectra(), self.ground_typ(), self.ag(), self.S(), self.TB(), self.TC(),
            self.TD()
        )

    def parametros_verticales(self):

        return (
            self.direccion, self.type_spectra(), self.ground_typ(), self.avg(), self.S(), self.TBv(), self.TCv(),
            self.TDv()
        )
