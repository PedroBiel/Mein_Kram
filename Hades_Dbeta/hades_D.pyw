import os
import sys

import pandas as pd

#from PyQt4 import QtCore, QtGui

from qtdesigner.hades_D import *

from clases.apoyos import Apoyos
from clases.casoscarga import CasosCarga
from clases.casonombre import CasoNombre
from clases.creagrupo import CreaGrupo
from clases.cuadroimplantacion import CuadroImplantacion
from clases.datos import Datos
from clases.gruposimplantacion import GruposImplantacion
from clases.listwidgetitem import OrdenaNumericamente
from clases.messagebox import MessageBox
from clases.nudosapoyo import NudosApoyo
from clases.pasaitems import PasaItems
from clases.puebladialogo import PueblaDialogoRSA, PueblaDialogoImpl
from clases.puntos import Puntos

from dialogos.propiedades import DialogPropiedades
from dialogos.proyecto import DialogProyecto
from dialogos.reaccionesimpl import DialogReaccionesImpl
from dialogos.reaccionesrsa import DialogReaccionesRSA

pd.set_option('display.width', 150)
pd.set_option('precision', 0)


class Window(QtGui.QMainWindow):

    def __init__(self, parent=None):

        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #self.reacciones = pd.DataFrame()
        
        # Menú.
        # -----
        
        # Datos de proyecto
        
        self.proyecto = '12345'
        self.elemento = 'GANGSEONGDAEGUK'
        self.empresa = 'JOSEON MINJUJUEUI INMIN GONGHWAGUK'
        self.autor = 'KIM JONG-UN'
        self.comentarios = 'No comment.'

        self.acn_datos_proyecto = self.ui.actionDatos_de_proyecto
        self.acn_datos_proyecto.triggered.connect(self.datos_proyecto)
        
        # Propiedades
        
        self.cuadro = 'Cintas'
        self.idioma = 'Español'
        self.redondeo = '1'
        self.filas_columnas = 'Puntos/Grupos'
        
        self.acn_propiedades_impl = self.ui.actionPropiedades
        self.acn_propiedades_impl.triggered.connect(self.propiedades_implantacion)

        # Archivos csv.
        # -------------

        self.ruta = self.ui.lineEdit_ruta
        self.btn_ruta = self.ui.pushButton_importar_ruta

        self.lst_archivos_ruta = self.ui.listWidget_archivos_ruta
        self.lst_archivos_ruta.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)  # Permite selección múltiple.
#        self.lst_archivos_ruta.setAcceptDrops(True)
#        self.lst_archivos_ruta.setDragEnabled(True)

        self.lst_archivos_implantacion = self.ui.listWidget_archivos_implantacion
        self.lst_archivos_implantacion.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)  # Permite selección múltiple.
#        self.lst_archivos_implantacion.setAcceptDrops(True)
#        self.lst_archivos_implantacion.setDragEnabled(True)

        self.btn_selecciona_csv = self.ui.pushButton_selecciona_csv
        self.btn_selecciona_todos_csv = self.ui.pushButton_selecciona_todos_csv
        self.btn_deselecciona_csv = self.ui.pushButton_deselecciona_csv
        self.btn_deselecciona_todos_csv = self.ui.pushButton_deselecciona_todos_csv

        # Importa ruta con archivos csv.
        self.btn_ruta.clicked.connect(self.importa_ruta)

        # Selecciona archivos csv de la ruta.
        self.btn_selecciona_csv.clicked.connect(self.selecciona_csv)

        # Selecciona todos los archivos csv de la ruta.
        self.btn_selecciona_todos_csv.clicked.connect(self.selecciona_todos_csv)

        # Deselecciona archivos csv de la implantación.
        self.btn_deselecciona_csv.clicked.connect(self.deselecciona_csv)

        # Deselecciona todos los archivos csv de la implantación.
        self.btn_deselecciona_todos_csv.clicked.connect(self.deselecciona_todos_csv)

        # Casos de carga.
        # ---------------

        self.lst_casos_carga = self.ui.listWidget_casos_carga
        self.lst_casos_carga.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)  # Permite selección múltiple.
#        self.lst_casos_carga.setAcceptDrops(True)
#        self.lst_casos_carga.setDragEnabled(True)
        
        self.rbt_Y = self.ui.radioButton_Y
        self.rbt_YO = self.ui.radioButton_YO
        self.rbt_O = self.ui.radioButton_O
        self.btn_selecciona_cc = self.ui.pushButton_selecciona_cc
        self.btn_selecciona_todos_cc = self.ui.pushButton_selecciona_todos_cc
        self.btn_deselecciona_cc = self.ui.pushButton_deselecciona_cc
        self.btn_deselecciona_todos_cc = self.ui.pushButton_deselecciona_todos_cc        
        
        self.lst_casos_carga_grupo = self.ui.listWidget_casos_carga_grupo
        self.lst_casos_carga_grupo.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)  # Permite selección múltiple.
#        self.lst_casos_carga_grupo.setAcceptDrops(True)
#        self.lst_casos_carga_grupo.setDragEnabled(True)
        
        self.nuevo_grupo = self.ui.lineEdit_nuevo_grupo
        self.btn_crea_grupo = self.ui.pushButton_crear_nuevo_grupo
        self.lst_grupos = self.ui.listWidget_grupos_casos_carga
        self.lst_grupos.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)  # Permite selección múltiple.
        self.lst_grupos.setAcceptDrops(True)
        self.lst_grupos.setDragEnabled(True)
        self.lst_grupos.setDragDropMode(QtGui.QAbstractItemView.InternalMove)  # Permite el desplazamiento detro de la listWigdet.
        
        self.btn_deselecciona_grp = self.ui.pushButton_deselecciona_grp
        self.btn_deselecciona_todos_grp = self.ui.pushButton_deselecciona_todos_grp
        
        self.grupos = {}
        
        # Selecciona casos de carga.
        self.btn_selecciona_cc.clicked.connect(self.selecciona_cc)

        # Selecciona todos los casos de carga.
        self.btn_selecciona_todos_cc.clicked.connect(self.selecciona_todos_cc)

        # Deselecciona casos de carga en grupo.
        self.btn_deselecciona_cc.clicked.connect(self.deselecciona_cc)

        # Deselecciona todos los casos de carga en grupo.
        self.btn_deselecciona_todos_cc.clicked.connect(self.deselecciona_todos_cc)
        
        # Crea un nuevo grupo de casos de carga.
        self.btn_crea_grupo.clicked.connect(self.crea_grupo)
        
        # Deselecciona grupos de casos de carga.
        self.btn_deselecciona_grp.clicked.connect(self.deselecciona_grp)
        
        # Deselecciona todos los grupos de casos de carga.
        self.btn_deselecciona_todos_grp.clicked.connect(self.deselecciona_todos_grp)
        
        # Apoyos.
        # -------
        
        self.lst_nudos_apoyo = self.ui.listWidget_nudos_apoyo
        self.lst_nudos_apoyo.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)  # Permite selección múltiple.
        
        self.btn_nudos = self.ui.pushButton_nudos
        self.btn_deselecc_nudos = self.ui.pushButton_deseleccionar_nudos
        self.nudos = self.ui.lineEdit_nudos
        self.apoyo = self.ui.lineEdit_apoyo
        self.btn_apoyo = self.ui.pushButton_apoyo
        self.btn_deselecciona_apy = self.ui.pushButton_deselecciona_apy
        self.btn_deselecciona_todos_apy = self.ui.pushButton_deselecciona_todos_apy
        
        self.lst_apoyos_implantacion = self.ui.listWidget_apoyos_implantacion
        self.lst_apoyos_implantacion.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)  # Permite selección múltiple.
        self.lst_apoyos_implantacion.setAcceptDrops(True)
        self.lst_apoyos_implantacion.setDragEnabled(True)
        
        self.apoyos = {}
        
        # Selecciona nudos.
        self.btn_nudos.clicked.connect(self.selecciona_nudos)
        
        # Deselecciona nudos.
        self.btn_deselecc_nudos.clicked.connect(self.deselecciona_nudos)
        
        # Crea apoyo.
        self.btn_apoyo.clicked.connect(self.crea_apoyo)
        
        # Deselecciona apoyo para el cuadro de implantación.
        self.btn_deselecciona_apy.clicked.connect(self.deselecciona_apoyo)
        
        # Deselecciona todos los apoyos para el cuadro de implantación.
        self.btn_deselecciona_todos_apy.clicked.connect(self.deselecciona_todos_apoyos)
        
        # Nº de puntos.
        # -------------
        
        self.lst_apoyos = self.ui.listWidget_apoyos
        self.lst_apoyos.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)  # Permite selección múltiple.
        
        self.btn_apoyos = self.ui.pushButton_apoyos
        self.btn_deselecc_apoyos = self.ui.pushButton_deseleccionar_apoyos
        self.apoyos_seleccionados = self.ui.lineEdit_apoyos_seleccionados
        self.puntos_apoyo = self.ui.lineEdit_puntos_apoyo
        self.btn_puntos = self.ui.pushButton_puntos
        self.btn_deselecciona_pto = self.ui.pushButton_deselecciona_pto
        self.btn_deselecciona_todos_pto = self.ui.pushButton_deselecciona_todos_pto
        
        self.lst_puntos_apoyo = self.ui.listWidget_puntos_apoyo
        self.lst_puntos_apoyo.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)  # Permite selección múltiple.
        self.lst_puntos_apoyo.setAcceptDrops(True)
        self.lst_puntos_apoyo.setDragEnabled(True)
        
        self.puntos = {}
        
        # Selecciona apoyos.
        self.btn_apoyos.clicked.connect(self.selecciona_apoyos)
        
        
        
        
        
        
        
        
        
        
        
        # Implantaciones.
        # ---------------
                      
        self.lst_grupos_impl = self.ui.listWidget_grupos_implantacion
        self.lst_grupos_impl.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)  # Permite selección múltiple.
        self.cbx_coeficiente_impl = self.ui.comboBox_coeficiente_implantacion
        self.btn_selecciona_gc = self.ui.pushButton_selecciona_grp_coef
        self.btn_selecciona_todos_gc = self.ui.pushButton_selecciona_todos_grp_coef
        self.btn_deselecciona_gc = self.ui.pushButton_deselecciona_grp_coef
        self.btn_deselecciona_todos_gc = self.ui.pushButton_deselecciona_todos_grp_coef
        self.lst_coeficientes_impl = self.ui.listWidget_coeficientes_implantacion
        self.lst_coeficientes_impl.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)  # Permite selección múltiple.
        self.lst_coeficientes_impl.setAcceptDrops(True)
        self.lst_coeficientes_impl.setDragEnabled(True)
        self.lst_coeficientes_impl.setDragDropMode(QtGui.QAbstractItemView.InternalMove)  # Permite el desplazamiento detro de la listWigdet.
        
        self.btn_reacciones_rsa = self.ui.pushButton_reacciones_rsa
        self.btn_reacciones_impl = self.ui.pushButton_reacciones_implantacion
        self.btn_cuadro_implantacion = self.ui.pushButton_cuadro_implantacion
        
        lst_coeficientes_implantacion = ['1,0', '1,05', '1,1', '1,15', '1,2']
        self.cbx_coeficiente_impl.addItems(lst_coeficientes_implantacion)

        self.coeficientes_impl = {}
        
        # Muestra reacciones RSA.
        self.btn_reacciones_rsa.clicked.connect(self.reacciones_rsa)
        
        # Muestra reacciones Iplantación.
        self.btn_reacciones_impl.clicked.connect(self.reacciones_impl)
        
        # Aplica coeficiente de implantación a grupo(s) seleccionado(s).
        self.btn_selecciona_gc.clicked.connect(self.aplica_coeficiente_grp)
        
        # Aplica coeficiente de implantación a todos los grupos.
        self.btn_selecciona_todos_gc.clicked.connect(self.aplica_coeficiente_todos_grp)
        
        # Deselecciona coeficientes para cuadro de implantación.
        self.btn_deselecciona_gc.clicked.connect(self.desaplica_coeficiente_grp)
        
        # Deselecciona todos los coeficientes para cuadro de implantación.
        self.btn_deselecciona_todos_gc.clicked.connect(self.desaplica_coeficiente_todos_grp)
        
        # Crea lista con el orden de los grupos de implantación.
        self.lst_coeficientes_impl.model().rowsMoved.connect(self.filas_movidas)
        
        # Crea el cuadro de implantación.
        self.btn_cuadro_implantacion.clicked.connect(self.cuadro_implantacion)
        
    
    # Menú.
    # =====
    
    def datos_proyecto(self):
        
        datos_hades = Datos()
        datos_hades.var1 = self.proyecto
        datos_hades.var2 = self.elemento
        datos_hades.var3 = self.empresa
        datos_hades.var4 = self.autor
        datos_hades.var5 = self.comentarios
        
        self.dialogo = DialogProyecto()
        self.dialogo.datos_proyecto = datos_hades
        
        # Nota:
        # Al crear la instancia de la clase Datos
        #     datos_hades = Datos()
        # se ejecuta el método __init__, pero todavía no se han pasado los 
        # objetos por referencia, por lo que el DataFrame 
        # self.dialogo.datos_reacciones.df todavía no se ha poblado y en el 
        # textEdit de self.dialogo no se muestra nada.
        # Para evitar este problema entre las líneas
        #     self.dialogo.datos_proyecto = datos_hades
        #     self.dialogo.exec_()
        # se incluye el código para que cuando se abra el diálogo se muestren
        # los pirmeros datos (Reacciones RSA por modelo).
        
        self.dialogo.proyecto.setText(datos_hades.var1)
        self.dialogo.elemento.setText(datos_hades.var2)
        self.dialogo.empresa.setText(datos_hades.var3)
        self.dialogo.autor.setText(datos_hades.var4)
        self.dialogo.comentarios.setPlainText(datos_hades.var5)
        
        self.dialogo.exec_()

        datos_hades = self.dialogo.datos_proyecto
        
        self.proyecto = datos_hades.var1
        self.elemento = datos_hades.var2
        self.empresa = datos_hades.var3
        self.autor = datos_hades.var4
        self.comentarios = datos_hades.var5
        print('self.proyecto:', self.proyecto)
        print('self.elemento:', self.elemento)
        print('self.empresa:', self.empresa)
        print('self.autor:', self.autor)
        print('self.comentarios:', self.comentarios, '\n')
        
    def propiedades_implantacion(self):
        
        datos_hades = Datos()

        self.dialogo = DialogPropiedades()
        self.dialogo.datos_propiedades = datos_hades
        self.dialogo.exec_()
        
        self.cuadro = datos_hades.var1
        self.idioma = datos_hades.var2
        self.redondeo = datos_hades.var3
        self.filas_columnas = datos_hades.var4
        print(self.cuadro)
        print(self.idioma)
        print(self.redondeo)
        print(self.filas_columnas)
        

        
        
        
        
        
    # Archivos csv.
    # =============

    def importa_ruta(self):

        #self.pfad = QtGui.QFileDialog.getExistingDirectory(self)
        self.pfad = 'H:\COMUN\Cálculo Estructural\VB\TEMP'
        #self.pfad = r'H:\79.XXX\79750 - SAIPEM- KNPC\CE\03 Máquinas\Robot\r11'
        self.ruta.setText(self.pfad)

        os.chdir(self.pfad)
        os.getcwd()
        list_csv = [fichero for fichero in os.listdir(self.pfad) if 'csv' in fichero]

        self.lst_archivos_ruta.clear()
        self.lst_archivos_implantacion.clear()
        self.lst_casos_carga.clear()
        self.lst_casos_carga_grupo.clear()
        self.nuevo_grupo.clear()
        self.lst_grupos.clear()
        self.grupos.clear()  # Limipia dicionario.
        
        for csv in list_csv:

            self.lst_archivos_ruta.addItem(csv)
    
    def selecciona_csv(self):
        
        PasaItems(self.lst_archivos_ruta, self.lst_archivos_implantacion).pasa_items()
        cas_carg = CasosCarga(self.lst_archivos_implantacion, self.lst_casos_carga, self.lst_casos_carga_grupo, self.pfad)
        cas_carg.casos_carga()
        self.reacciones = cas_carg.df_reacciones()
        NudosApoyo(self.lst_archivos_ruta, self.lst_nudos_apoyo, self.lst_apoyos_implantacion, self.reacciones).nudos_apoyo()

    def selecciona_todos_csv(self):

        PasaItems(self.lst_archivos_ruta, self.lst_archivos_implantacion).pasa_todos_items()
        cas_carg = CasosCarga(self.lst_archivos_implantacion, self.lst_casos_carga, self.lst_casos_carga_grupo, self.pfad)
        cas_carg.casos_carga()
        self.reacciones = cas_carg.df_reacciones()
        NudosApoyo(self.lst_archivos_ruta, self.lst_nudos_apoyo, self.lst_apoyos_implantacion, self.reacciones).nudos_apoyo()


    def deselecciona_csv(self):

        PasaItems(self.lst_archivos_implantacion, self.lst_archivos_ruta).pasa_items()
        cas_carg = CasosCarga(self.lst_archivos_implantacion, self.lst_casos_carga, self.lst_casos_carga_grupo, self.pfad)
        cas_carg.casos_carga()
        self.reacciones = cas_carg.df_reacciones()
        NudosApoyo(self.lst_archivos_ruta, self.lst_nudos_apoyo, self.lst_apoyos_implantacion, self.reacciones).nudos_apoyo()

    def deselecciona_todos_csv(self):

        PasaItems(self.lst_archivos_implantacion, self.lst_archivos_ruta).pasa_todos_items()
        cas_carg = CasosCarga(self.lst_archivos_implantacion, self.lst_casos_carga, self.lst_casos_carga_grupo, self.pfad)
        cas_carg.casos_carga()
        self.reacciones = cas_carg.df_reacciones()
        NudosApoyo(self.lst_archivos_ruta, self.lst_nudos_apoyo, self.lst_apoyos_implantacion, self.reacciones).nudos_apoyo()

        self.grupos = {}  # Limpia diccionario de grupos.
        self.apoyos = {}  # Limpia diccionario de apoyos.
        self.coeficientes_impl = {}  # Limpia diccionario de coeficientes de implantación.
        
        self.lst_grupos.clear()  # Limpia la lista con los grupos de casos de carga.
        self.lst_apoyos_implantacion.clear()  # Limpia la lista con los apoyos para cuadro de implantación.
        self.lst_grupos_impl.clear()  # Limpia la lista con los grupos para la implantación.
        self.lst_coeficientes_impl.clear()  # Limpia la lista con los coeficientes de implantación. 
        

    # Casos de carga.
    # ===============
            
    def selecciona_cc(self):
        
        self.ui.statusbar.showMessage('Seleccionando los casos de carga para las implantaciones...')
        
        PasaItems(self.lst_casos_carga, self.lst_casos_carga_grupo).pasa_items()
        OrdenaNumericamente(self.lst_casos_carga_grupo).ordena_numericamente()
        CasoNombre(self.lst_casos_carga_grupo, self.reacciones).caso_nombre()
        
        self.ui.statusbar.clearMessage()

    def selecciona_todos_cc(self):
        
        self.ui.statusbar.showMessage('Seleccionando todos los casos de carga para las implantaciones...')
        
        PasaItems(self.lst_casos_carga, self.lst_casos_carga_grupo).pasa_todos_items()
        OrdenaNumericamente(self.lst_casos_carga_grupo).ordena_numericamente()
        CasoNombre(self.lst_casos_carga_grupo, self.reacciones).caso_nombre()
        
        self.ui.statusbar.clearMessage()

    def deselecciona_cc(self):
        
        self.ui.statusbar.showMessage('Eliminando los casos de carga para las implantaciones...')

        PasaItems(self.lst_casos_carga_grupo, self.lst_casos_carga).pasa_items()
        OrdenaNumericamente(self.lst_casos_carga).ordena_numericamente()
        CasoNombre(self.lst_casos_carga, self.reacciones).caso_nombre()
        
        self.ui.statusbar.clearMessage()

    def deselecciona_todos_cc(self):
        
        self.ui.statusbar.showMessage('Eliminando todos los casos de carga para las implantaciones...')

        PasaItems(self.lst_casos_carga_grupo, self.lst_casos_carga).pasa_todos_items()
        OrdenaNumericamente(self.lst_casos_carga).ordena_numericamente()
        CasoNombre(self.lst_casos_carga, self.reacciones).caso_nombre()
        
        self.ui.statusbar.clearMessage()
        
    def crea_grupo(self):
        
        self.crea_grp = CreaGrupo(self.lst_casos_carga_grupo, self.lst_grupos, self.nuevo_grupo, self.grupos, self.rbt_Y, self.rbt_O)
        self.crea_grp.crea_grupo()
        GruposImplantacion(self.grupos, self.lst_grupos_impl, self.lst_coeficientes_impl, self.cbx_coeficiente_impl, self.coeficientes_impl).grupos_implantacion()
        GruposImplantacion(self.grupos, self.lst_apoyos, self.lst_coeficientes_impl, self.cbx_coeficiente_impl, self.coeficientes_impl).grupos_implantacion()
               
    def deselecciona_grp(self):
        
        pasa_items = PasaItems(self.lst_grupos, self.lst_casos_carga)
        pasa_items.pasa_items_grupo()
        pasa_items.claves()
        OrdenaNumericamente(self.lst_casos_carga).ordena_numericamente()
        CasoNombre(self.lst_casos_carga, self.reacciones).caso_nombre()
        
        for clv in pasa_items.claves():  # Elimina los grupos del diccionario de grupos.
        
            del self.grupos[clv]
        
        self.coeficientes_impl = {}  # Limpia diccionario de coeficientes de implantación.
        self.lst_grupos_impl.clear()  # Limpia la lista con los grupos para la implantación.
        self.lst_coeficientes_impl.clear()  # Limpia la lista con los coeficientes de implantación. 
    
    def deselecciona_todos_grp(self):
        
        PasaItems(self.lst_grupos, self.lst_casos_carga).pasa_todos_items_grupo()
        OrdenaNumericamente(self.lst_casos_carga).ordena_numericamente()
        CasoNombre(self.lst_casos_carga, self.reacciones).caso_nombre()
        
        self.grupos = {}  # Limpia diccionario de grupos.
        self.coeficientes_impl = {}  # Limpia diccionario de coeficientes de implantación.
        self.lst_grupos_impl.clear()  # Limpia la lista con los grupos para la implantación.
        self.lst_coeficientes_impl.clear()  # Limpia la lista con los coeficientes de implantación. 
        

    # Apoyos.
    # =======

    def selecciona_nudos(self):
        
        Apoyos(self.lst_nudos_apoyo, self.lst_apoyos_implantacion, self.nudos, self.apoyo, self.btn_nudos, self.btn_apoyo, self.apoyos).selecciona_nudos()
        OrdenaNumericamente(self.lst_nudos_apoyo).ordena_numericamente()
             
    def deselecciona_nudos(self):
        
        Apoyos(self.lst_nudos_apoyo, self.lst_apoyos_implantacion, self.nudos, self.apoyo, self.btn_nudos, self.btn_apoyo, self.apoyos).deselecciona_nudos()
        OrdenaNumericamente(self.lst_nudos_apoyo).ordena_numericamente()
          
    def crea_apoyo(self):
              
        self.crea_apy = Apoyos(self.lst_nudos_apoyo, self.lst_apoyos_implantacion, self.nudos, self.apoyo, self.btn_nudos, self.btn_apoyo, self.apoyos)
        self.crea_apy.crea_apoyo()
        
    def deselecciona_apoyo(self):
        
        pasa_items = PasaItems(self.lst_apoyos_implantacion, self.lst_nudos_apoyo)
        pasa_items.pasa_items_apoyo()
        OrdenaNumericamente(self.lst_nudos_apoyo).ordena_numericamente()
        
        for clv in pasa_items.claves():  # Elimina los apoyos del diccionario de apoyos.
        
            del self.apoyos[clv]
            
    def deselecciona_todos_apoyos(self):
        
        PasaItems(self.lst_apoyos_implantacion, self.lst_nudos_apoyo).pasa_todos_items_grupo()
        OrdenaNumericamente(self.lst_nudos_apoyo).ordena_numericamente()
        
        self.apoyos = {}  # Limpia diccionario de apoyos.
        

    # Puntos.
    # =======
        
    def selecciona_apoyos(self):
        
        Puntos(self.lst_apoyos, self.lst_puntos_apoyo, self.apoyos_seleccionados, self.puntos_apoyo, self.btn_apoyos, self.btn_puntos, self.puntos).selecciona_apoyos()
        OrdenaNumericamente(self.lst_nudos_apoyo).ordena_numericamente()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

    # Implantaciones.
    # ===============

    def reacciones_rsa(self):
        
        try:
        
            datos_hades = Datos()  # Los objetos entre formularios (con sus datos) se pasan por referencia.
            datos_hades.df = self.reacciones
    
            self.dialogo = DialogReaccionesRSA()
            self.dialogo.datos_reacciones_rsa = datos_hades
            
            # Nota:
            # Al crear la instancia de la clase Datos
            #     datos_hades = Datos()
            # se ejecuta el método __init__, pero todavía no se han pasado los 
            # objetos por referencia, por lo que el DataFrame 
            # self.dialogo.datos_reacciones.df todavía no se ha poblado y en el 
            # textEdit de self.dialogo no se muestra nada.
            # Para evitar este problema entre las líneas
            #     self.dialogo.datos_reacciones = datos_hades
            #     self.dialogo.show()
            # se incluye el código para que cuando se abra el diálogo se muestren
            # los pirmeros datos (Reacciones RSA por modelo).
            
            reacciones_rsa_ = PueblaDialogoRSA(self.reacciones).reacciones_rsa()
            self.dialogo.txt_reacciones.setText(str(reacciones_rsa_))
            
            self.dialogo.show()
            
        except:
            
            msg = MessageBox('Warning', 'Faltan datos por introducir.')
            msg.show_message_box()
               
    def reacciones_impl(self):
        
        try:
        
            datos_hades = Datos()  # Los objetos entre formularios (con sus datos) se pasan por referencia.
    
            dicc_grupos = self.crea_grp.dicc_grupos()
            dicc_apoyos = self.crea_apy.dicc_apoyos()
            
            datos_hades.df = self.reacciones
            datos_hades.dcc = dicc_grupos
            datos_hades.dcc1 = dicc_apoyos        
            
            self.dialogo = DialogReaccionesImpl()
            self.dialogo.datos_reacciones_impl = datos_hades
                   
            reacciones_impl_ = PueblaDialogoImpl(self.reacciones, self.grupos, dicc_grupos, dicc_apoyos).reacciones_impl()
            self.cols = ['Fx', 'Fy', 'Fz', 'Mx', 'My', 'Mz']
            self.dialogo.txt_reacciones.setText(str(reacciones_impl_[self.cols]))
            
            self.dialogo.show()
            
        except:
            
            msg = MessageBox('Warning', 'Faltan datos por introducir.')
            msg.show_message_box()
        
    def aplica_coeficiente_grp(self):
        
        GruposImplantacion(self.grupos, self.lst_grupos_impl, self.lst_coeficientes_impl, self.cbx_coeficiente_impl, self.coeficientes_impl).aplica_coeficiente()

    def aplica_coeficiente_todos_grp(self):
        
        GruposImplantacion(self.grupos, self.lst_grupos_impl, self.lst_coeficientes_impl, self.cbx_coeficiente_impl, self.coeficientes_impl).aplica_coeficiente_todos()

    def desaplica_coeficiente_grp(self):
        
        pasa_items = PasaItems(self.lst_coeficientes_impl, self.lst_grupos_impl)
        pasa_items.pasa_items_coeficiente()
        pasa_items.claves()
        self.lst_grupos_impl.sortItems()
              
        for clv in pasa_items.claves():  # Elimina los grupos del diccionario de coeficientes.
            print(clv)
            del self.coeficientes_impl[clv]
        print(self.coeficientes_impl)
        
    def desaplica_coeficiente_todos_grp(self):
        
        pasa_items = PasaItems(self.lst_coeficientes_impl, self.lst_grupos_impl)
        pasa_items.pasa_todos_items_coeficiente()
        
        self.coeficientes_impl = {}  # Limpia diccionario de coeficientes de implantación.
        
    def filas_movidas(self, *args):
    
        GruposImplantacion(self.grupos, self.lst_grupos_impl, self.lst_coeficientes_impl, self.cbx_coeficiente_impl, self.coeficientes_impl).orden_grupos_modificado()
        
    def cuadro_implantacion(self):
     
        CuadroImplantacion(
        self.proyecto, self.elemento, self.autor, self.cuadro, self.idioma, 
        self.redondeo, self.filas_columnas, self.apoyos
        ).crea_xlsx()
     
        
        



if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    myapp = Window()
    myapp.show()
    sys.exit(app.exec_())
