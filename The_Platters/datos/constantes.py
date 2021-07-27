# -*- coding: utf-8 -*-
"""
Constantes de la aplicación

Created on Wed Nov 26 11:49:16 2019

__author__ = Pedro Biel
__version__ = 0.0
__email__ = pbiel@taimweser.com
"""


class Constantes:
    """Valores constantes de la aplicación."""

    EXISTING_DIRECTORY = [
        'Seleccionar carpeta',
        r'H:\COMUN MANUTENCION\5.CE\SQLite'
        ]

    GUARDAR_PROYECTO = 'Guardar proyecto'

    ABRIR_PROYECTO = 'Abrir proyecto'

    n_pernos = (
            '2 pernos int.',
            '4 pernos int.',
            '4 pernos ext.',
            '6 pernos; 2 int, 4 ext.'
            )

    d_pernos = (
            'Diámetro 16 mm',
            'Diámetro 20 mm',
            'Diámetro 24 mm',
            'Diámetro 27 mm',
            'Diámetro 30 mm',
            'Diámetro 36 mm',
            'Diámetro 42 mm'
            )  # Diaémtro de los pernos para QTreeView.

    d = (
            16,
            20,
            24,
            27,
            30,
            36,
            42
            )  # [mm] Diámetro de los pernos.

    d0 = (
            50,
            50,
            50,
            50,
            50,
            60,
            70
            )  # [mm] Diámetro de los agujeros.

    As = (
            1.566,
            2.449,
            3.527,
            4.596,
            5.609,
            8.172,
            11.21
            )  # [cm²] Área de tensión de los pernos de anclaje.

    mn = (
            50,
            75,
            75,
            75,
            75,
            100,
            100
            )  # [mm] Espesor del mortero de nivelación.

    REDONDEO_5 = 5  # Redondeo a 5.

    REDONDEO_10 = 10  # Redondeo a 10.
