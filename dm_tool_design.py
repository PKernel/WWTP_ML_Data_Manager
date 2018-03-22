from __future__ import print_function
from PyQt4 import QtCore, QtGui
import sys,re,glob,csv,pickle,os,time,pandas as pd,numpy as np,scipy.stats as stats,matplotlib.pyplot as plt,matplotlib.mlab as mlab,matplotlib.pylab as pylab
from pandas import read_csv
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.widgets import SpanSelector
from matplotlib.widgets import RectangleSelector
from matplotlib import style
import multiprocessing
import pathlib
import shutil
import weka.core.jvm as jvm
jvm.start(packages=True,max_heap_size="13500m")

print(multiprocessing.cpu_count())

try:
    
    _fromUtf8 = QtCore.QString.fromUtf8
    
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class ApplicationWindow(QtGui.QMainWindow):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1257, 905)
        Form.setMouseTracking(False)
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 5, 1261, 921))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(236, 236, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(226, 226, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 236, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(226, 226, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 236, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.tabWidget.setPalette(palette)
        font = QtGui.QFont()
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.t1_pushButton_exit = QtGui.QPushButton(self.tab_1)
        self.t1_pushButton_exit.setGeometry(QtCore.QRect(1170, 850, 71, 23))
        self.t1_pushButton_exit.setObjectName("t1_pushButton_exit")
        self.t1_label_1 = QtGui.QLabel(self.tab_1)
        self.t1_label_1.setGeometry(QtCore.QRect(10, 10, 161, 20))
        self.t1_label_1.setObjectName("t1_label_1")
        self.t1_pushButton_merge_combi = QtGui.QPushButton(self.tab_1)
        self.t1_pushButton_merge_combi.setGeometry(QtCore.QRect(850, 310, 71, 23))
        self.t1_pushButton_merge_combi.setObjectName("t1_pushButton_merge_combi")
        self.t1_pushButton_1 = QtGui.QPushButton(self.tab_1)
        self.t1_pushButton_1.setGeometry(QtCore.QRect(10, 60, 31, 23))
        self.t1_pushButton_1.setObjectName("t1_pushButton_1")
        self.t1_pushButton_selectfile = QtGui.QPushButton(self.tab_1)
        self.t1_pushButton_selectfile.setGeometry(QtCore.QRect(180, 430, 31, 23))
        self.t1_pushButton_selectfile.setObjectName("t1_pushButton_selectfile")
        self.t1_comboBox_1 = QtGui.QComboBox(self.tab_1)
        self.t1_comboBox_1.setGeometry(QtCore.QRect(50, 60, 181, 22))
        self.t1_comboBox_1.setObjectName("t1_comboBox_1")
        self.t1_comboBox_1.addItem("")
        self.t1_comboBox_1.addItem("")
        self.t1_comboBox_1.addItem("")
        self.t1_comboBox_1.addItem("")
        self.t1_pushButton_6 = QtGui.QPushButton(self.tab_1)
        self.t1_pushButton_6.setGeometry(QtCore.QRect(10, 620, 101, 23))
        self.t1_pushButton_6.setObjectName("t1_pushButton_6")
        self.t1_pushButton_apply_trans = QtGui.QPushButton(self.tab_1)
        self.t1_pushButton_apply_trans.setGeometry(QtCore.QRect(180, 530, 651, 23))
        self.t1_pushButton_apply_trans.setObjectName("t1_pushButton_apply_trans")
        self.t1_pushButton_7 = QtGui.QPushButton(self.tab_1)
        self.t1_pushButton_7.setGeometry(QtCore.QRect(10, 650, 191, 23))
        self.t1_pushButton_7.setObjectName("t1_pushButton_7")
        self.t1_listWidget_1 = QtGui.QListWidget(self.tab_1)
        self.t1_listWidget_1.setGeometry(QtCore.QRect(260, 60, 256, 131))
        self.t1_listWidget_1.setObjectName("t1_listWidget_1")
        self.t1_pushButton_submergeleft = QtGui.QPushButton(self.tab_1)
        self.t1_pushButton_submergeleft.setGeometry(QtCore.QRect(130, 200, 101, 23))
        self.t1_pushButton_submergeleft.setObjectName("t1_pushButton_submergeleft")
        self.t1_pushButton_submergeright = QtGui.QPushButton(self.tab_1)
        self.t1_pushButton_submergeright.setGeometry(QtCore.QRect(710, 200, 101, 23))
        self.t1_pushButton_submergeright.setObjectName("t1_pushButton_submergeright")
        self.t1_comboBox_2 = QtGui.QComboBox(self.tab_1)
        self.t1_comboBox_2.setGeometry(QtCore.QRect(630, 60, 181, 22))
        self.t1_comboBox_2.setObjectName("t1_comboBox_2")
        self.t1_comboBox_2.addItem("")
        self.t1_comboBox_2.addItem("")
        self.t1_comboBox_2.addItem("")
        self.t1_comboBox_2.addItem("")
        self.t1_pushButton_2 = QtGui.QPushButton(self.tab_1)
        self.t1_pushButton_2.setGeometry(QtCore.QRect(590, 60, 31, 23))
        self.t1_pushButton_2.setObjectName("t1_pushButton_2")
        self.t1_listWidget_2 = QtGui.QListWidget(self.tab_1)
        self.t1_listWidget_2.setGeometry(QtCore.QRect(840, 60, 256, 131))
        self.t1_listWidget_2.setObjectName("t1_listWidget_2")
        self.t1_lineEdit_1 = QtGui.QLineEdit(self.tab_1)
        self.t1_lineEdit_1.setGeometry(QtCore.QRect(10, 200, 113, 20))
        self.t1_lineEdit_1.setObjectName("t1_lineEdit_1")
        self.t1_lineEdit_2 = QtGui.QLineEdit(self.tab_1)
        self.t1_lineEdit_2.setGeometry(QtCore.QRect(590, 200, 113, 20))
        self.t1_lineEdit_2.setObjectName("t1_lineEdit_2")
        self.t1_label_2 = QtGui.QLabel(self.tab_1)
        self.t1_label_2.setGeometry(QtCore.QRect(10, 260, 211, 20))
        self.t1_label_2.setObjectName("t1_label_2")
        self.t1_lineEdit_merge_combi = QtGui.QLineEdit(self.tab_1)
        self.t1_lineEdit_merge_combi.setGeometry(QtCore.QRect(752, 310, 91, 20))
        self.t1_lineEdit_merge_combi.setObjectName("t1_lineEdit_merge_combi")
        self.t1_line_1 = QtGui.QFrame(self.tab_1)
        self.t1_line_1.setGeometry(QtCore.QRect(0, 240, 1251, 20))
        self.t1_line_1.setFrameShape(QtGui.QFrame.HLine)
        self.t1_line_1.setFrameShadow(QtGui.QFrame.Sunken)
        self.t1_line_1.setObjectName("t1_line_1")
        self.t1_line_2 = QtGui.QFrame(self.tab_1)
        self.t1_line_2.setGeometry(QtCore.QRect(0, 360, 1251, 20))
        self.t1_line_2.setFrameShape(QtGui.QFrame.HLine)
        self.t1_line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.t1_line_2.setObjectName("t1_line_2")
        self.t1_line_3 = QtGui.QFrame(self.tab_1)
        self.t1_line_3.setGeometry(QtCore.QRect(0, 560, 1251, 20))
        self.t1_line_3.setFrameShape(QtGui.QFrame.HLine)
        self.t1_line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.t1_line_3.setObjectName("t1_line_3")
        self.t1_label_3 = QtGui.QLabel(self.tab_1)
        self.t1_label_3.setGeometry(QtCore.QRect(10, 380, 211, 20))
        self.t1_label_3.setObjectName("t1_label_3")
        self.t1_pushButton_selecttransdic = QtGui.QPushButton(self.tab_1)
        self.t1_pushButton_selecttransdic.setGeometry(QtCore.QRect(180, 460, 31, 23))
        self.t1_pushButton_selecttransdic.setObjectName("t1_pushButton_selecttransdic")
        self.t1_label_5 = QtGui.QLabel(self.tab_1)
        self.t1_label_5.setGeometry(QtCore.QRect(10, 580, 211, 20))
        self.t1_label_5.setObjectName("t1_label_5")
        self.t1_lineEdit_targetpath = QtGui.QLineEdit(self.tab_1)
        self.t1_lineEdit_targetpath.setGeometry(QtCore.QRect(220, 490, 181, 20))
        self.t1_lineEdit_targetpath.setObjectName("t1_lineEdit_targetpath")
        self.t1_label_6 = QtGui.QLabel(self.tab_1)
        self.t1_label_6.setGeometry(QtCore.QRect(10, 430, 51, 20))
        self.t1_label_6.setObjectName("t1_label_6")
        self.t1_label_13 = QtGui.QLabel(self.tab_1)
        self.t1_label_13.setGeometry(QtCore.QRect(10, 460, 141, 20))
        self.t1_label_13.setObjectName("t1_label_13")
        self.t1_label_14 = QtGui.QLabel(self.tab_1)
        self.t1_label_14.setGeometry(QtCore.QRect(10, 490, 141, 20))
        self.t1_label_14.setObjectName("t1_label_14")
        self.t1_lineEdit_selectfile = QtGui.QLineEdit(self.tab_1)
        self.t1_lineEdit_selectfile.setGeometry(QtCore.QRect(220, 430, 611, 20))
        self.t1_lineEdit_selectfile.setObjectName("t1_lineEdit_selectfile")
        self.t1_radioButton_major_left = QtGui.QRadioButton(self.tab_1)
        self.t1_radioButton_major_left.setGeometry(QtCore.QRect(660, 300, 61, 17))
        self.t1_radioButton_major_left.setChecked(True)
        self.t1_radioButton_major_left.setObjectName("t1_radioButton_major_left")
        self.t1_radioButton_major_right = QtGui.QRadioButton(self.tab_1)
        self.t1_radioButton_major_right.setGeometry(QtCore.QRect(660, 327, 61, 17))
        self.t1_radioButton_major_right.setChecked(False)
        self.t1_radioButton_major_right.setObjectName("t1_radioButton_major_right")
        self.t1_lineEdit_3 = QtGui.QLineEdit(self.tab_1)
        self.t1_lineEdit_3.setGeometry(QtCore.QRect(10, 297, 581, 20))
        self.t1_lineEdit_3.setObjectName("t1_lineEdit_3")
        self.t1_pushButton_merge_left = QtGui.QPushButton(self.tab_1)
        self.t1_pushButton_merge_left.setGeometry(QtCore.QRect(610, 297, 31, 23))
        self.t1_pushButton_merge_left.setObjectName("t1_pushButton_merge_left")
        self.t1_pushButton_merge_right = QtGui.QPushButton(self.tab_1)
        self.t1_pushButton_merge_right.setGeometry(QtCore.QRect(610, 330, 31, 23))
        self.t1_pushButton_merge_right.setObjectName("t1_pushButton_merge_right")
        self.t1_lineEdit_4 = QtGui.QLineEdit(self.tab_1)
        self.t1_lineEdit_4.setGeometry(QtCore.QRect(10, 327, 581, 20))
        self.t1_lineEdit_4.setObjectName("t1_lineEdit_4")
        self.t1_lineEdit_merge_on = QtGui.QLineEdit(self.tab_1)
        self.t1_lineEdit_merge_on.setGeometry(QtCore.QRect(960, 310, 71, 20))
        self.t1_lineEdit_merge_on.setObjectName("t1_lineEdit_merge_on")
        self.t1_label_4 = QtGui.QLabel(self.tab_1)
        self.t1_label_4.setGeometry(QtCore.QRect(930, 310, 21, 20))
        self.t1_label_4.setObjectName("t1_label_4")
        self.t1_pushButton_delete_left = QtGui.QPushButton(self.tab_1)
        self.t1_pushButton_delete_left.setGeometry(QtCore.QRect(130, 90, 101, 23))
        self.t1_pushButton_delete_left.setObjectName("t1_pushButton_delete_left")
        self.t1_pushButton_delete_right = QtGui.QPushButton(self.tab_1)
        self.t1_pushButton_delete_right.setGeometry(QtCore.QRect(710, 90, 101, 23))
        self.t1_pushButton_delete_right.setObjectName("t1_pushButton_delete_right")
        self.t1_lineEdit_transdic = QtGui.QLineEdit(self.tab_1)
        self.t1_lineEdit_transdic.setGeometry(QtCore.QRect(220, 460, 611, 20))
        self.t1_lineEdit_transdic.setObjectName("t1_lineEdit_transdic")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.t2_label_1 = QtGui.QLabel(self.tab_2)
        self.t2_label_1.setGeometry(QtCore.QRect(10, 10, 121, 20))
        self.t2_label_1.setObjectName("t2_label_1")
        self.t2_toolButton_load_csv = QtGui.QToolButton(self.tab_2)
        self.t2_toolButton_load_csv.setGeometry(QtCore.QRect(130, 10, 25, 21))
        self.t2_toolButton_load_csv.setObjectName("t2_toolButton_load_csv")
        self.t2_pushButton_em = QtGui.QPushButton(self.tab_2)
        self.t2_pushButton_em.setGeometry(QtCore.QRect(270, 855, 51, 23))
        self.t2_pushButton_em.setObjectName("t2_pushButton_em")
        self.t2_widget_1 = QtGui.QWidget(self.tab_2)
        self.t2_widget_1.setGeometry(QtCore.QRect(20, 71, 871, 221))
        self.t2_widget_1.setAutoFillBackground(True)
        self.t2_widget_1.setObjectName("t2_widget_1")
        self.t2_line_1 = QtGui.QFrame(self.tab_2)
        self.t2_line_1.setGeometry(QtCore.QRect(8, 50, 1241, 20))
        self.t2_line_1.setFrameShape(QtGui.QFrame.HLine)
        self.t2_line_1.setFrameShadow(QtGui.QFrame.Sunken)
        self.t2_line_1.setObjectName("t2_line_1")
        self.t2_label_3 = QtGui.QLabel(self.tab_2)
        self.t2_label_3.setGeometry(QtCore.QRect(10, 32, 131, 20))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.t2_label_3.setFont(font)
        self.t2_label_3.setObjectName("t2_label_3")
        self.t2_pushButton_prev_col = QtGui.QPushButton(self.tab_2)
        self.t2_pushButton_prev_col.setGeometry(QtCore.QRect(1100, 10, 75, 23))
        self.t2_pushButton_prev_col.setObjectName("t2_pushButton_prev_col")
        self.t2_pushButton_next_col = QtGui.QPushButton(self.tab_2)
        self.t2_pushButton_next_col.setGeometry(QtCore.QRect(1179, 10, 75, 23))
        self.t2_pushButton_next_col.setObjectName("t2_pushButton_next_col")
        self.t2_comboBox_header_data = QtGui.QComboBox(self.tab_2)
        self.t2_comboBox_header_data.setGeometry(QtCore.QRect(900, 10, 191, 22))
        self.t2_comboBox_header_data.setObjectName("t2_comboBox_header_data")
        self.t2_comboBox_header_data.addItem("")
        self.t2_widget_2 = QtGui.QWidget(self.tab_2)
        self.t2_widget_2.setGeometry(QtCore.QRect(20, 311, 871, 241))
        self.t2_widget_2.setAutoFillBackground(True)
        self.t2_widget_2.setObjectName("t2_widget_2")
        self.t2_widget_3 = QtGui.QWidget(self.tab_2)
        self.t2_widget_3.setGeometry(QtCore.QRect(20, 570, 871, 271))
        self.t2_widget_3.setAutoFillBackground(True)
        self.t2_widget_3.setObjectName("t2_widget_3")
        self.t2_label_5 = QtGui.QLabel(self.tab_2)
        self.t2_label_5.setGeometry(QtCore.QRect(20, 550, 131, 20))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.t2_label_5.setFont(font)
        self.t2_label_5.setObjectName("t2_label_5")
        self.t2_lineEdit_rem_rows = QtGui.QLineEdit(self.tab_2)
        self.t2_lineEdit_rem_rows.setGeometry(QtCore.QRect(20, 855, 41, 20))
        self.t2_lineEdit_rem_rows.setObjectName("t2_lineEdit_rem_rows")
        self.t2_label_6 = QtGui.QLabel(self.tab_2)
        self.t2_label_6.setGeometry(QtCore.QRect(70, 855, 91, 16))
        self.t2_label_6.setObjectName("t2_label_6")
        self.t2_pushButton_save_cpage = QtGui.QPushButton(self.tab_2)
        self.t2_pushButton_save_cpage.setGeometry(QtCore.QRect(160, 855, 101, 23))
        self.t2_pushButton_save_cpage.setObjectName("t2_pushButton_save_cpage")
        self.t2_pushButton_save_dic = QtGui.QPushButton(self.tab_2)
        self.t2_pushButton_save_dic.setGeometry(QtCore.QRect(620, 855, 131, 23))
        self.t2_pushButton_save_dic.setObjectName("t2_pushButton_save_dic")
        self.t2_pushButton_save_df = QtGui.QPushButton(self.tab_2)
        self.t2_pushButton_save_df.setGeometry(QtCore.QRect(760, 855, 131, 23))
        self.t2_pushButton_save_df.setObjectName("t2_pushButton_save_df")
        self.t2_line_2 = QtGui.QFrame(self.tab_2)
        self.t2_line_2.setGeometry(QtCore.QRect(10, 837, 1231, 20))
        self.t2_line_2.setFrameShape(QtGui.QFrame.HLine)
        self.t2_line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.t2_line_2.setObjectName("t2_line_2")
        self.t2_pushButton_reset = QtGui.QPushButton(self.tab_2)
        self.t2_pushButton_reset.setGeometry(QtCore.QRect(920, 815, 131, 23))
        self.t2_pushButton_reset.setObjectName("t2_pushButton_reset")
        self.t2_lineEdit_missing_percent = QtGui.QLineEdit(self.tab_2)
        self.t2_lineEdit_missing_percent.setGeometry(QtCore.QRect(920, 790, 131, 20))
        self.t2_lineEdit_missing_percent.setObjectName("t2_lineEdit_missing_percent")
        self.t2_label_19 = QtGui.QLabel(self.tab_2)
        self.t2_label_19.setGeometry(QtCore.QRect(920, 770, 121, 16))
        self.t2_label_19.setObjectName("t2_label_19")
        self.t2_comboBox_repl_outliers = QtGui.QComboBox(self.tab_2)
        self.t2_comboBox_repl_outliers.setGeometry(QtCore.QRect(920, 730, 131, 22))
        self.t2_comboBox_repl_outliers.setObjectName("t2_comboBox_repl_outliers")
        self.t2_comboBox_repl_outliers.addItem("")
        self.t2_comboBox_repl_outliers.addItem("")
        self.t2_comboBox_repl_outliers.addItem("")
        self.t2_comboBox_repl_outliers.addItem("")
        self.t2_comboBox_repl_outliers.addItem("")
        self.t2_label_18 = QtGui.QLabel(self.tab_2)
        self.t2_label_18.setGeometry(QtCore.QRect(920, 710, 111, 20))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.t2_label_18.setFont(font)
        self.t2_label_18.setObjectName("t2_label_18")
        self.t2_lineEdit_lpercentile = QtGui.QLineEdit(self.tab_2)
        self.t2_lineEdit_lpercentile.setGeometry(QtCore.QRect(920, 680, 61, 20))
        self.t2_lineEdit_lpercentile.setObjectName("t2_lineEdit_lpercentile")
        self.t2_lineEdit_upercentile = QtGui.QLineEdit(self.tab_2)
        self.t2_lineEdit_upercentile.setGeometry(QtCore.QRect(990, 680, 61, 20))
        self.t2_lineEdit_upercentile.setObjectName("t2_lineEdit_upercentile")
        self.t2_radioButton_histo = QtGui.QRadioButton(self.tab_2)
        self.t2_radioButton_histo.setGeometry(QtCore.QRect(920, 590, 82, 17))
        self.t2_radioButton_histo.setObjectName("t2_radioButton_histo")
        self.t2_label_15 = QtGui.QLabel(self.tab_2)
        self.t2_label_15.setGeometry(QtCore.QRect(918, 618, 101, 20))
        self.t2_label_15.setObjectName("t2_label_15")
        self.t2_radioButton_cumcurve = QtGui.QRadioButton(self.tab_2)
        self.t2_radioButton_cumcurve.setGeometry(QtCore.QRect(1020, 590, 82, 17))
        self.t2_radioButton_cumcurve.setObjectName("t2_radioButton_cumcurve")
        self.t2_label_16 = QtGui.QLabel(self.tab_2)
        self.t2_label_16.setGeometry(QtCore.QRect(918, 659, 61, 20))
        self.t2_label_16.setObjectName("t2_label_16")
        self.t2_label_17 = QtGui.QLabel(self.tab_2)
        self.t2_label_17.setGeometry(QtCore.QRect(988, 658, 61, 20))
        self.t2_label_17.setObjectName("t2_label_17")
        self.t2_label_14 = QtGui.QLabel(self.tab_2)
        self.t2_label_14.setGeometry(QtCore.QRect(1100, 630, 121, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.t2_label_14.setFont(font)
        self.t2_label_14.setObjectName("t2_label_14")
        self.t2_checkBox_target = QtGui.QCheckBox(self.tab_2)
        self.t2_checkBox_target.setGeometry(QtCore.QRect(780, 0, 101, 20))
        self.t2_checkBox_target.setObjectName("t2_checkBox_target")
        self.t2_comboBox_outliertest = QtGui.QComboBox(self.tab_2)
        self.t2_comboBox_outliertest.setGeometry(QtCore.QRect(1100, 650, 131, 22))
        self.t2_comboBox_outliertest.setObjectName("t2_comboBox_outliertest")
        self.t2_comboBox_outliertest.addItem("")
        self.t2_comboBox_outliertest.addItem("")
        self.t2_comboBox_outliertest.addItem("")
        self.t2_comboBox_outliertest.addItem("")
        self.t2_label_2 = QtGui.QLabel(self.tab_2)
        self.t2_label_2.setGeometry(QtCore.QRect(540, 13, 121, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.t2_label_2.setFont(font)
        self.t2_label_2.setObjectName("t2_label_2")
        self.t2_checkBox_delete = QtGui.QCheckBox(self.tab_2)
        self.t2_checkBox_delete.setGeometry(QtCore.QRect(780, 20, 121, 17))
        self.t2_checkBox_delete.setObjectName("t2_checkBox_delete")
        self.t2_comboBox_diagram_selection = QtGui.QComboBox(self.tab_2)
        self.t2_comboBox_diagram_selection.setGeometry(QtCore.QRect(640, 10, 101, 22))
        self.t2_comboBox_diagram_selection.setObjectName("t2_comboBox_diagram_selection")
        self.t2_comboBox_diagram_selection.addItem("")
        self.t2_comboBox_diagram_selection.addItem("")
        self.t2_lineEdit_bins = QtGui.QLineEdit(self.tab_2)
        self.t2_lineEdit_bins.setGeometry(QtCore.QRect(918, 638, 61, 21))
        self.t2_lineEdit_bins.setObjectName("t2_lineEdit_bins")
        self.t2_label_4 = QtGui.QLabel(self.tab_2)
        self.t2_label_4.setGeometry(QtCore.QRect(21, 292, 121, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.t2_label_4.setFont(font)
        self.t2_label_4.setObjectName("t2_label_4")
        self.t2_pushButton_exit = QtGui.QPushButton(self.tab_2)
        self.t2_pushButton_exit.setGeometry(QtCore.QRect(1170, 850, 71, 23))
        self.t2_pushButton_exit.setObjectName("t2_pushButton_exit")
        self.t2_groupBox_1 = QtGui.QGroupBox(self.tab_2)
        self.t2_groupBox_1.setGeometry(QtCore.QRect(910, 70, 341, 231))
        self.t2_groupBox_1.setObjectName("t2_groupBox_1")
        self.t2_toolButton_meanNCG = QtGui.QToolButton(self.t2_groupBox_1)
        self.t2_toolButton_meanNCG.setGeometry(QtCore.QRect(10, 160, 51, 19))
        self.t2_toolButton_meanNCG.setCheckable(True)
        self.t2_toolButton_meanNCG.setAutoRaise(False)
        self.t2_toolButton_meanNCG.setObjectName("t2_toolButton_meanNCG")
        self.t2_toolButton_sumNCG = QtGui.QToolButton(self.t2_groupBox_1)
        self.t2_toolButton_sumNCG.setGeometry(QtCore.QRect(70, 160, 51, 19))
        self.t2_toolButton_sumNCG.setCheckable(True)
        self.t2_toolButton_sumNCG.setObjectName("t2_toolButton_sumNCG")
        self.t2_pushButton_applyNCG = QtGui.QPushButton(self.t2_groupBox_1)
        self.t2_pushButton_applyNCG.setGeometry(QtCore.QRect(270, 200, 61, 23))
        self.t2_pushButton_applyNCG.setObjectName("t2_pushButton_applyNCG")
        self.t2_lineEdit_resultnameNCG = QtGui.QLineEdit(self.t2_groupBox_1)
        self.t2_lineEdit_resultnameNCG.setGeometry(QtCore.QRect(160, 200, 101, 20))
        self.t2_lineEdit_resultnameNCG.setObjectName("t2_lineEdit_resultnameNCG")
        self.t2_label_8 = QtGui.QLabel(self.t2_groupBox_1)
        self.t2_label_8.setGeometry(QtCore.QRect(20, 200, 111, 16))
        self.t2_label_8.setObjectName("t2_label_8")
        self.t2_pushButton_insert = QtGui.QPushButton(self.t2_groupBox_1)
        self.t2_pushButton_insert.setGeometry(QtCore.QRect(10, 50, 151, 23))
        self.t2_pushButton_insert.setObjectName("t2_pushButton_insert")
        self.t2_comboBox_selColNCG = QtGui.QComboBox(self.t2_groupBox_1)
        self.t2_comboBox_selColNCG.setGeometry(QtCore.QRect(10, 20, 151, 22))
        self.t2_comboBox_selColNCG.setObjectName("t2_comboBox_selColNCG")
        self.t2_lineEdit_NCG = QtGui.QLineEdit(self.t2_groupBox_1)
        self.t2_lineEdit_NCG.setGeometry(QtCore.QRect(170, 20, 161, 20))
        self.t2_lineEdit_NCG.setObjectName("t2_lineEdit_NCG")
        self.t2_pushButton_6NCG = QtGui.QPushButton(self.t2_groupBox_1)
        self.t2_pushButton_6NCG.setGeometry(QtCore.QRect(250, 80, 31, 31))
        self.t2_pushButton_6NCG.setObjectName("t2_pushButton_6NCG")
        self.t2_pushButton_0NCG = QtGui.QPushButton(self.t2_groupBox_1)
        self.t2_pushButton_0NCG.setGeometry(QtCore.QRect(210, 150, 31, 31))
        self.t2_pushButton_0NCG.setObjectName("t2_pushButton_0NCG")
        self.t2_pushButton_4NCG = QtGui.QPushButton(self.t2_groupBox_1)
        self.t2_pushButton_4NCG.setGeometry(QtCore.QRect(170, 80, 31, 31))
        self.t2_pushButton_4NCG.setObjectName("t2_pushButton_4NCG")
        self.t2_pushButton_1NCG = QtGui.QPushButton(self.t2_groupBox_1)
        self.t2_pushButton_1NCG.setGeometry(QtCore.QRect(170, 45, 31, 31))
        self.t2_pushButton_1NCG.setObjectName("t2_pushButton_1NCG")
        self.t2_pushButton_minusNCG = QtGui.QPushButton(self.t2_groupBox_1)
        self.t2_pushButton_minusNCG.setGeometry(QtCore.QRect(300, 80, 31, 31))
        self.t2_pushButton_minusNCG.setObjectName("t2_pushButton_minusNCG")
        self.t2_pushButton_7NCG = QtGui.QPushButton(self.t2_groupBox_1)
        self.t2_pushButton_7NCG.setGeometry(QtCore.QRect(170, 115, 31, 31))
        self.t2_pushButton_7NCG.setObjectName("t2_pushButton_7NCG")
        self.t2_pushButton_9NCG = QtGui.QPushButton(self.t2_groupBox_1)
        self.t2_pushButton_9NCG.setGeometry(QtCore.QRect(250, 115, 31, 31))
        self.t2_pushButton_9NCG.setObjectName("t2_pushButton_9NCG")
        self.t2_pushButton_multNCG = QtGui.QPushButton(self.t2_groupBox_1)
        self.t2_pushButton_multNCG.setGeometry(QtCore.QRect(300, 150, 31, 31))
        self.t2_pushButton_multNCG.setObjectName("t2_pushButton_multNCG")
        self.t2_pushButton_divNCG = QtGui.QPushButton(self.t2_groupBox_1)
        self.t2_pushButton_divNCG.setGeometry(QtCore.QRect(300, 115, 31, 31))
        self.t2_pushButton_divNCG.setObjectName("t2_pushButton_divNCG")
        self.t2_pushButton_plusNCG = QtGui.QPushButton(self.t2_groupBox_1)
        self.t2_pushButton_plusNCG.setGeometry(QtCore.QRect(300, 45, 31, 31))
        self.t2_pushButton_plusNCG.setObjectName("t2_pushButton_plusNCG")
        self.t2_pushButton_8NCG = QtGui.QPushButton(self.t2_groupBox_1)
        self.t2_pushButton_8NCG.setGeometry(QtCore.QRect(210, 115, 31, 31))
        self.t2_pushButton_8NCG.setObjectName("t2_pushButton_8NCG")
        self.t2_pushButton_2NCG = QtGui.QPushButton(self.t2_groupBox_1)
        self.t2_pushButton_2NCG.setGeometry(QtCore.QRect(210, 45, 31, 31))
        self.t2_pushButton_2NCG.setObjectName("t2_pushButton_2NCG")
        self.t2_pushButton_3NCG = QtGui.QPushButton(self.t2_groupBox_1)
        self.t2_pushButton_3NCG.setGeometry(QtCore.QRect(250, 45, 31, 31))
        self.t2_pushButton_3NCG.setObjectName("t2_pushButton_3NCG")
        self.t2_pushButton_clrNCG = QtGui.QPushButton(self.t2_groupBox_1)
        self.t2_pushButton_clrNCG.setGeometry(QtCore.QRect(250, 150, 31, 31))
        self.t2_pushButton_clrNCG.setObjectName("t2_pushButton_clrNCG")
        self.t2_pushButton_5NCG = QtGui.QPushButton(self.t2_groupBox_1)
        self.t2_pushButton_5NCG.setGeometry(QtCore.QRect(210, 80, 31, 31))
        self.t2_pushButton_5NCG.setObjectName("t2_pushButton_5NCG")
        self.t2_listWidget_NCG = QtGui.QListWidget(self.t2_groupBox_1)
        self.t2_listWidget_NCG.setGeometry(QtCore.QRect(10, 80, 151, 71))
        self.t2_listWidget_NCG.setObjectName("t2_listWidget_NCG")
        self.t2_groupBox_3 = QtGui.QGroupBox(self.tab_2)
        self.t2_groupBox_3.setGeometry(QtCore.QRect(910, 450, 341, 111))
        self.t2_groupBox_3.setObjectName("t2_groupBox_3")
        self.t2_pushButton_offsec = QtGui.QPushButton(self.t2_groupBox_3)
        self.t2_pushButton_offsec.setGeometry(QtCore.QRect(10, 20, 121, 23))
        self.t2_pushButton_offsec.setObjectName("t2_pushButton_offsec")
        self.t2_label_12 = QtGui.QLabel(self.t2_groupBox_3)
        self.t2_label_12.setGeometry(QtCore.QRect(190, 10, 51, 16))
        self.t2_label_12.setObjectName("t2_label_12")
        self.t2_label_13 = QtGui.QLabel(self.t2_groupBox_3)
        self.t2_label_13.setGeometry(QtCore.QRect(260, 10, 51, 16))
        self.t2_label_13.setObjectName("t2_label_13")
        self.t2_listWidget_mosmin = QtGui.QListWidget(self.t2_groupBox_3)
        self.t2_listWidget_mosmin.setGeometry(QtCore.QRect(190, 30, 61, 71))
        self.t2_listWidget_mosmin.setObjectName("t2_listWidget_mosmin")
        self.t2_listWidget_mosmax = QtGui.QListWidget(self.t2_groupBox_3)
        self.t2_listWidget_mosmax.setGeometry(QtCore.QRect(260, 30, 61, 71))
        self.t2_listWidget_mosmax.setObjectName("t2_listWidget_mosmax")
        self.t2_groupBox_2 = QtGui.QGroupBox(self.tab_2)
        self.t2_groupBox_2.setGeometry(QtCore.QRect(910, 310, 341, 141))
        self.t2_groupBox_2.setObjectName("t2_groupBox_2")
        self.t2_checkBox_norm_mean = QtGui.QCheckBox(self.t2_groupBox_2)
        self.t2_checkBox_norm_mean.setGeometry(QtCore.QRect(10, 18, 111, 17))
        self.t2_checkBox_norm_mean.setChecked(False)
        self.t2_checkBox_norm_mean.setObjectName("t2_checkBox_norm_mean")
        self.t2_checkBox_norm_minmax = QtGui.QCheckBox(self.t2_groupBox_2)
        self.t2_checkBox_norm_minmax.setGeometry(QtCore.QRect(140, 18, 111, 17))
        self.t2_checkBox_norm_minmax.setObjectName("t2_checkBox_norm_minmax")
        self.t2_label_10 = QtGui.QLabel(self.t2_groupBox_2)
        self.t2_label_10.setGeometry(QtCore.QRect(10, 80, 91, 16))
        self.t2_label_10.setObjectName("t2_label_10")
        self.t2_label_9 = QtGui.QLabel(self.t2_groupBox_2)
        self.t2_label_9.setGeometry(QtCore.QRect(10, 40, 121, 16))
        self.t2_label_9.setObjectName("t2_label_9")
        self.t2_label_11 = QtGui.QLabel(self.t2_groupBox_2)
        self.t2_label_11.setGeometry(QtCore.QRect(190, 78, 51, 16))
        self.t2_label_11.setObjectName("t2_label_11")
        self.t2_lineEdit_mcriterion = QtGui.QLineEdit(self.t2_groupBox_2)
        self.t2_lineEdit_mcriterion.setGeometry(QtCore.QRect(140, 76, 41, 20))
        self.t2_lineEdit_mcriterion.setObjectName("t2_lineEdit_mcriterion")
        self.t2_comboBox_interpolation = QtGui.QComboBox(self.t2_groupBox_2)
        self.t2_comboBox_interpolation.setGeometry(QtCore.QRect(140, 40, 111, 22))
        self.t2_comboBox_interpolation.setObjectName("t2_comboBox_interpolation")
        self.t2_comboBox_interpolation.addItem("")
        self.t2_comboBox_interpolation.addItem("")
        self.t2_comboBox_interpolation.addItem("")
        self.t2_comboBox_interpolation.addItem("")
        self.t2_comboBox_interpolation.addItem("")
        self.t2_comboBox_interpolation.addItem("")
        self.t2_comboBox_interpolation.addItem("")
        self.t2_comboBox_interpolation.addItem("")
        self.t2_comboBox_interpolation.addItem("")
        self.t2_comboBox_interpolation.addItem("")
        self.t2_comboBox_interpolation.addItem("")
        self.t2_comboBox_interpolation.addItem("")
        self.t2_comboBox_interpolation.addItem("")
        self.t2_comboBox_interpolation.addItem("")
        self.t2_comboBox_interpolation.addItem("")
        self.t2_lineEdit_textlod = QtGui.QLineEdit(self.t2_groupBox_2)
        self.t2_lineEdit_textlod.setGeometry(QtCore.QRect(140, 108, 41, 20))
        self.t2_lineEdit_textlod.setObjectName("t2_lineEdit_textlod")
        self.t2_checkBox_setlod = QtGui.QCheckBox(self.t2_groupBox_2)
        self.t2_checkBox_setlod.setGeometry(QtCore.QRect(190, 110, 70, 17))
        self.t2_checkBox_setlod.setObjectName("t2_checkBox_setlod")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.t3_pushButton_exit = QtGui.QPushButton(self.tab_3)
        self.t3_pushButton_exit.setGeometry(QtCore.QRect(1170, 850, 71, 23))
        self.t3_pushButton_exit.setObjectName("t3_pushButton_exit")
        self.t3_label_3 = QtGui.QLabel(self.tab_3)
        self.t3_label_3.setGeometry(QtCore.QRect(20, 90, 61, 16))
        self.t3_label_3.setObjectName("t3_label_3")
        self.t3_label_13 = QtGui.QLabel(self.tab_3)
        self.t3_label_13.setGeometry(QtCore.QRect(20, 120, 61, 16))
        self.t3_label_13.setObjectName("t3_label_13")
        self.t3_widget_1 = QtGui.QWidget(self.tab_3)
        self.t3_widget_1.setGeometry(QtCore.QRect(20, 240, 561, 241))
        self.t3_widget_1.setAutoFillBackground(True)
        self.t3_widget_1.setObjectName("t3_widget_1")
        self.t3_widget_3 = QtGui.QWidget(self.tab_3)
        self.t3_widget_3.setGeometry(QtCore.QRect(20, 570, 561, 241))
        self.t3_widget_3.setAutoFillBackground(True)
        self.t3_widget_3.setObjectName("t3_widget_3")
        self.t3_comboBox_1 = QtGui.QComboBox(self.tab_3)
        self.t3_comboBox_1.setGeometry(QtCore.QRect(20, 210, 131, 22))
        self.t3_comboBox_1.setObjectName("t3_comboBox_1")
        self.t3_comboBox_3 = QtGui.QComboBox(self.tab_3)
        self.t3_comboBox_3.setGeometry(QtCore.QRect(20, 540, 131, 22))
        self.t3_comboBox_3.setObjectName("t3_comboBox_3")
        self.t3_checkBox_TAN = QtGui.QCheckBox(self.tab_3)
        self.t3_checkBox_TAN.setGeometry(QtCore.QRect(390, 110, 81, 17))
        self.t3_checkBox_TAN.setObjectName("t3_checkBox_TAN")
        self.t3_checkBox_NB = QtGui.QCheckBox(self.tab_3)
        self.t3_checkBox_NB.setGeometry(QtCore.QRect(390, 130, 81, 17))
        self.t3_checkBox_NB.setObjectName("t3_checkBox_NB")
        self.t3_checkBox_ANN = QtGui.QCheckBox(self.tab_3)
        self.t3_checkBox_ANN.setGeometry(QtCore.QRect(500, 110, 61, 17))
        self.t3_checkBox_ANN.setObjectName("t3_checkBox_ANN")
        self.t3_checkBox_SMO = QtGui.QCheckBox(self.tab_3)
        self.t3_checkBox_SMO.setGeometry(QtCore.QRect(500, 130, 61, 17))
        self.t3_checkBox_SMO.setObjectName("t3_checkBox_SMO")
        self.t3_checkBox_J48 = QtGui.QCheckBox(self.tab_3)
        self.t3_checkBox_J48.setGeometry(QtCore.QRect(630, 150, 61, 17))
        self.t3_checkBox_J48.setObjectName("t3_checkBox_J48")
        self.t3_checkBox_RF = QtGui.QCheckBox(self.tab_3)
        self.t3_checkBox_RF.setGeometry(QtCore.QRect(630, 130, 91, 17))
        self.t3_checkBox_RF.setObjectName("t3_checkBox_RF")
        self.t3_checkBox_RT = QtGui.QCheckBox(self.tab_3)
        self.t3_checkBox_RT.setGeometry(QtCore.QRect(630, 110, 91, 17))
        self.t3_checkBox_RT.setObjectName("t3_checkBox_RT")
        self.t3_label_4 = QtGui.QLabel(self.tab_3)
        self.t3_label_4.setGeometry(QtCore.QRect(390, 90, 46, 13))
        self.t3_label_4.setObjectName("t3_label_4")
        self.t3_label_5 = QtGui.QLabel(self.tab_3)
        self.t3_label_5.setGeometry(QtCore.QRect(500, 90, 46, 13))
        self.t3_label_5.setObjectName("t3_label_5")
        self.t3_label_6 = QtGui.QLabel(self.tab_3)
        self.t3_label_6.setGeometry(QtCore.QRect(630, 90, 46, 13))
        self.t3_label_6.setObjectName("t3_label_6")
        self.t3_lineEdit_bins = QtGui.QLineEdit(self.tab_3)
        self.t3_lineEdit_bins.setGeometry(QtCore.QRect(160, 30, 41, 20))
        self.t3_lineEdit_bins.setObjectName("t3_lineEdit_bins")
        self.t3_comboBox_discMethod = QtGui.QComboBox(self.tab_3)
        self.t3_comboBox_discMethod.setGeometry(QtCore.QRect(50, 30, 101, 22))
        self.t3_comboBox_discMethod.setObjectName("t3_comboBox_discMethod")
        self.t3_comboBox_discMethod.addItem("")
        self.t3_comboBox_discMethod.addItem("")
        self.t3_label_2 = QtGui.QLabel(self.tab_3)
        self.t3_label_2.setEnabled(True)
        self.t3_label_2.setGeometry(QtCore.QRect(210, 30, 31, 21))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.t3_label_2.setFont(font)
        self.t3_label_2.setScaledContents(False)
        self.t3_label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.t3_label_2.setObjectName("t3_label_2")
        self.t3_pushButton_discApply = QtGui.QPushButton(self.tab_3)
        self.t3_pushButton_discApply.setGeometry(QtCore.QRect(260, 30, 75, 23))
        self.t3_pushButton_discApply.setObjectName("t3_pushButton_discApply")
        self.t3_toolButton_load_csv_disc = QtGui.QToolButton(self.tab_3)
        self.t3_toolButton_load_csv_disc.setGeometry(QtCore.QRect(10, 30, 25, 21))
        self.t3_toolButton_load_csv_disc.setObjectName("t3_toolButton_load_csv_disc")
        self.t3_label_1 = QtGui.QLabel(self.tab_3)
        self.t3_label_1.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.t3_label_1.setObjectName("t3_label_1")
        self.t3_line_1 = QtGui.QFrame(self.tab_3)
        self.t3_line_1.setGeometry(QtCore.QRect(10, 70, 1241, 20))
        self.t3_line_1.setFrameShape(QtGui.QFrame.HLine)
        self.t3_line_1.setFrameShadow(QtGui.QFrame.Sunken)
        self.t3_line_1.setObjectName("t3_line_1")
        self.t3_comboBox_2 = QtGui.QComboBox(self.tab_3)
        self.t3_comboBox_2.setGeometry(QtCore.QRect(670, 210, 131, 22))
        self.t3_comboBox_2.setObjectName("t3_comboBox_2")
        self.t3_widget_4 = QtGui.QWidget(self.tab_3)
        self.t3_widget_4.setGeometry(QtCore.QRect(670, 570, 561, 241))
        self.t3_widget_4.setAutoFillBackground(True)
        self.t3_widget_4.setObjectName("t3_widget_4")
        self.t3_widget_2 = QtGui.QWidget(self.tab_3)
        self.t3_widget_2.setGeometry(QtCore.QRect(670, 240, 561, 241))
        self.t3_widget_2.setAutoFillBackground(True)
        self.t3_widget_2.setObjectName("t3_widget_2")
        self.t3_comboBox_4 = QtGui.QComboBox(self.tab_3)
        self.t3_comboBox_4.setGeometry(QtCore.QRect(670, 540, 131, 22))
        self.t3_comboBox_4.setObjectName("t3_comboBox_4")
        self.t3_lineEdit_result = QtGui.QLineEdit(self.tab_3)
        self.t3_lineEdit_result.setGeometry(QtCore.QRect(20, 140, 131, 20))
        self.t3_lineEdit_result.setObjectName("t3_lineEdit_result")
        self.t3_toolButton_result = QtGui.QToolButton(self.tab_3)
        self.t3_toolButton_result.setGeometry(QtCore.QRect(160, 140, 25, 21))
        self.t3_toolButton_result.setObjectName("t3_toolButton_result")
        self.t3_pushButton_bnXML = QtGui.QPushButton(self.tab_3)
        self.t3_pushButton_bnXML.setGeometry(QtCore.QRect(1180, 30, 75, 23))
        self.t3_pushButton_bnXML.setObjectName("t3_pushButton_bnXML")
        self.t3_label_14 = QtGui.QLabel(self.tab_3)
        self.t3_label_14.setGeometry(QtCore.QRect(1140, 10, 111, 16))
        self.t3_label_14.setObjectName("t3_label_14")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.t4_pushButton_exit = QtGui.QPushButton(self.tab_4)
        self.t4_pushButton_exit.setGeometry(QtCore.QRect(1170, 850, 71, 23))
        self.t4_pushButton_exit.setObjectName("t4_pushButton_exit")
        self.t4_comboBox_2 = QtGui.QComboBox(self.tab_4)
        self.t4_comboBox_2.setGeometry(QtCore.QRect(10, 330, 171, 22))
        self.t4_comboBox_2.setObjectName("t4_comboBox_2")
        self.t4_comboBox_2.addItem("")
        self.t4_comboBox_2.addItem("")
        self.t4_comboBox_2.addItem("")
        self.t4_comboBox_2.addItem("")
        self.t4_comboBox_2.addItem("")
        self.t4_label_1 = QtGui.QLabel(self.tab_4)
        self.t4_label_1.setGeometry(QtCore.QRect(20, 10, 91, 16))
        self.t4_label_1.setObjectName("t4_label_1")
        self.t4_pushButton_startsimulation = QtGui.QPushButton(self.tab_4)
        self.t4_pushButton_startsimulation.setGeometry(QtCore.QRect(1160, 20, 91, 23))
        self.t4_pushButton_startsimulation.setObjectName("t4_pushButton_startsimulation")
        self.t4_widget_1 = QtGui.QWidget(self.tab_4)
        self.t4_widget_1.setGeometry(QtCore.QRect(10, 110, 581, 211))
        self.t4_widget_1.setAutoFillBackground(True)
        self.t4_widget_1.setObjectName("t4_widget_1")
        self.t4_pushButton_loadTargets = QtGui.QPushButton(self.tab_4)
        self.t4_pushButton_loadTargets.setGeometry(QtCore.QRect(10, 30, 91, 23))
        self.t4_pushButton_loadTargets.setObjectName("t4_pushButton_loadTargets")
        self.t4_comboBox_1 = QtGui.QComboBox(self.tab_4)
        self.t4_comboBox_1.setGeometry(QtCore.QRect(10, 80, 171, 22))
        self.t4_comboBox_1.setObjectName("t4_comboBox_1")
        self.t4_comboBox_1.addItem("")
        self.t4_comboBox_1.addItem("")
        self.t4_comboBox_1.addItem("")
        self.t4_comboBox_1.addItem("")
        self.t4_comboBox_1.addItem("")
        self.t4_comboBox_3 = QtGui.QComboBox(self.tab_4)
        self.t4_comboBox_3.setGeometry(QtCore.QRect(10, 400, 171, 22))
        self.t4_comboBox_3.setObjectName("t4_comboBox_3")
        self.t4_comboBox_3.addItem("")
        self.t4_comboBox_3.addItem("")
        self.t4_comboBox_3.addItem("")
        self.t4_comboBox_3.addItem("")
        self.t4_comboBox_3.addItem("")
        self.t4_widget_2 = QtGui.QWidget(self.tab_4)
        self.t4_widget_2.setGeometry(QtCore.QRect(10, 430, 581, 211))
        self.t4_widget_2.setAutoFillBackground(True)
        self.t4_widget_2.setObjectName("t4_widget_2")
        self.t4_comboBox_4 = QtGui.QComboBox(self.tab_4)
        self.t4_comboBox_4.setGeometry(QtCore.QRect(10, 650, 171, 22))
        self.t4_comboBox_4.setObjectName("t4_comboBox_4")
        self.t4_comboBox_4.addItem("")
        self.t4_comboBox_4.addItem("")
        self.t4_comboBox_4.addItem("")
        self.t4_comboBox_4.addItem("")
        self.t4_comboBox_4.addItem("")
        self.tabWidget.addTab(self.tab_4, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.objectfunctions(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Data Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_pushButton_exit.setText(QtGui.QApplication.translate("Form", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_label_1.setText(QtGui.QApplication.translate("Form", "1. Step upload raw data", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_pushButton_merge_combi.setText(QtGui.QApplication.translate("Form", ">> merge", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_pushButton_1.setText(QtGui.QApplication.translate("Form", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_pushButton_selectfile.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_comboBox_1.setItemText(0, QtGui.QApplication.translate("Form", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_comboBox_1.setItemText(1, QtGui.QApplication.translate("Form", "Type: Online 15min", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_comboBox_1.setItemText(2, QtGui.QApplication.translate("Form", "Type: Online 2h", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_comboBox_1.setItemText(3, QtGui.QApplication.translate("Form", "Type: Standard Sampling", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_pushButton_6.setText(QtGui.QApplication.translate("Form", "Common Header", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_pushButton_apply_trans.setText(QtGui.QApplication.translate("Form", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_pushButton_7.setText(QtGui.QApplication.translate("Form", "Apply threshold to missing row %", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_pushButton_submergeleft.setText(QtGui.QApplication.translate("Form", "sub_merge", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_pushButton_submergeright.setText(QtGui.QApplication.translate("Form", "sub_merge", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_comboBox_2.setItemText(0, QtGui.QApplication.translate("Form", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_comboBox_2.setItemText(1, QtGui.QApplication.translate("Form", "Type: Online 15min", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_comboBox_2.setItemText(2, QtGui.QApplication.translate("Form", "Type: Online 2h", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_comboBox_2.setItemText(3, QtGui.QApplication.translate("Form", "Type: Standard Sampling", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_pushButton_2.setText(QtGui.QApplication.translate("Form", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_label_2.setText(QtGui.QApplication.translate("Form", "2. Step: Merge data to one raw dataset", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_lineEdit_merge_combi.setText(QtGui.QApplication.translate("Form", "result", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_label_3.setText(QtGui.QApplication.translate("Form", "3. Step: Header translation", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_pushButton_selecttransdic.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_label_5.setText(QtGui.QApplication.translate("Form", "4. Step: Header adjustment", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_label_6.setText(QtGui.QApplication.translate("Form", "Select file", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_label_13.setText(QtGui.QApplication.translate("Form", "Select translation dictionary", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_label_14.setText(QtGui.QApplication.translate("Form", "Target file name", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_radioButton_major_left.setText(QtGui.QApplication.translate("Form", "Major", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_radioButton_major_right.setText(QtGui.QApplication.translate("Form", "Major", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_pushButton_merge_left.setText(QtGui.QApplication.translate("Form", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_pushButton_merge_right.setText(QtGui.QApplication.translate("Form", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_lineEdit_merge_on.setText(QtGui.QApplication.translate("Form", "UNIX", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_label_4.setText(QtGui.QApplication.translate("Form", "on", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_pushButton_delete_left.setText(QtGui.QApplication.translate("Form", "Remove selection", None, QtGui.QApplication.UnicodeUTF8))
        self.t1_pushButton_delete_right.setText(QtGui.QApplication.translate("Form", "Remove selection", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QtGui.QApplication.translate("Form", "Data Collector", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_label_1.setText(QtGui.QApplication.translate("Form", "Load .csv source path", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_toolButton_load_csv.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_pushButton_em.setText(QtGui.QApplication.translate("Form", "EM", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_label_3.setText(QtGui.QApplication.translate("Form", "Raw Data", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_pushButton_prev_col.setText(QtGui.QApplication.translate("Form", "Back", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_pushButton_next_col.setText(QtGui.QApplication.translate("Form", "Next", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_comboBox_header_data.setItemText(0, QtGui.QApplication.translate("Form", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_label_5.setText(QtGui.QApplication.translate("Form", "Outlier Detection", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_label_6.setText(QtGui.QApplication.translate("Form", "% rows remaining", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_pushButton_save_cpage.setText(QtGui.QApplication.translate("Form", "Save page as CSV", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_pushButton_save_dic.setText(QtGui.QApplication.translate("Form", "Save Dictionary as CSV", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_pushButton_save_df.setText(QtGui.QApplication.translate("Form", "Save dataframe as CSV", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_pushButton_reset.setText(QtGui.QApplication.translate("Form", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_label_19.setText(QtGui.QApplication.translate("Form", "Missing data percentage", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_comboBox_repl_outliers.setItemText(0, QtGui.QApplication.translate("Form", "No action", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_comboBox_repl_outliers.setItemText(1, QtGui.QApplication.translate("Form", "Delete outliers", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_comboBox_repl_outliers.setItemText(2, QtGui.QApplication.translate("Form", "Winsorizing", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_comboBox_repl_outliers.setItemText(3, QtGui.QApplication.translate("Form", "Replace by mean", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_comboBox_repl_outliers.setItemText(4, QtGui.QApplication.translate("Form", "Replace by missing", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_label_18.setText(QtGui.QApplication.translate("Form", "Missing percentiles", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_radioButton_histo.setText(QtGui.QApplication.translate("Form", "Histogram", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_label_15.setText(QtGui.QApplication.translate("Form", "Bins", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_radioButton_cumcurve.setText(QtGui.QApplication.translate("Form", "Cum Curve", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_label_16.setText(QtGui.QApplication.translate("Form", "L. Percentile", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_label_17.setText(QtGui.QApplication.translate("Form", "U. Percentile", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_label_14.setText(QtGui.QApplication.translate("Form", "Outlier Test", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_checkBox_target.setText(QtGui.QApplication.translate("Form", "Target Parameter", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_comboBox_outliertest.setItemText(0, QtGui.QApplication.translate("Form", "No action", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_comboBox_outliertest.setItemText(1, QtGui.QApplication.translate("Form", "Dfree z", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_comboBox_outliertest.setItemText(2, QtGui.QApplication.translate("Form", "Mod. z-score", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_comboBox_outliertest.setItemText(3, QtGui.QApplication.translate("Form", "z-score", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_label_2.setText(QtGui.QApplication.translate("Form", "Diagram Design", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_checkBox_delete.setText(QtGui.QApplication.translate("Form", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_comboBox_diagram_selection.setItemText(0, QtGui.QApplication.translate("Form", "Line plot", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_comboBox_diagram_selection.setItemText(1, QtGui.QApplication.translate("Form", "Scatter plot", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_label_4.setText(QtGui.QApplication.translate("Form", "Data preprozessing", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_pushButton_exit.setText(QtGui.QApplication.translate("Form", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_groupBox_1.setTitle(QtGui.QApplication.translate("Form", "New Column Generator", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_toolButton_meanNCG.setText(QtGui.QApplication.translate("Form", "Mean", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_toolButton_sumNCG.setText(QtGui.QApplication.translate("Form", "Sum", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_pushButton_applyNCG.setText(QtGui.QApplication.translate("Form", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_label_8.setText(QtGui.QApplication.translate("Form", "Result Column Name", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_pushButton_insert.setText(QtGui.QApplication.translate("Form", "Insert", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_pushButton_6NCG.setText(QtGui.QApplication.translate("Form", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_pushButton_0NCG.setText(QtGui.QApplication.translate("Form", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_pushButton_4NCG.setText(QtGui.QApplication.translate("Form", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_pushButton_1NCG.setText(QtGui.QApplication.translate("Form", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_pushButton_minusNCG.setText(QtGui.QApplication.translate("Form", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_pushButton_7NCG.setText(QtGui.QApplication.translate("Form", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_pushButton_9NCG.setText(QtGui.QApplication.translate("Form", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_pushButton_multNCG.setText(QtGui.QApplication.translate("Form", "*", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_pushButton_divNCG.setText(QtGui.QApplication.translate("Form", "/", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_pushButton_plusNCG.setText(QtGui.QApplication.translate("Form", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_pushButton_8NCG.setText(QtGui.QApplication.translate("Form", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_pushButton_2NCG.setText(QtGui.QApplication.translate("Form", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_pushButton_3NCG.setText(QtGui.QApplication.translate("Form", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_pushButton_clrNCG.setText(QtGui.QApplication.translate("Form", "Clr", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_pushButton_5NCG.setText(QtGui.QApplication.translate("Form", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_groupBox_3.setTitle(QtGui.QApplication.translate("Form", "Special System Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_pushButton_offsec.setText(QtGui.QApplication.translate("Form", "Mark offline section", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_label_12.setText(QtGui.QApplication.translate("Form", "Min", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_label_13.setText(QtGui.QApplication.translate("Form", "Max", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_groupBox_2.setTitle(QtGui.QApplication.translate("Form", "Data filter", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_checkBox_norm_mean.setText(QtGui.QApplication.translate("Form", "Normalize by mean", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_checkBox_norm_minmax.setText(QtGui.QApplication.translate("Form", "Normalize max/min", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_label_10.setText(QtGui.QApplication.translate("Form", "Gab threshold", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_label_9.setText(QtGui.QApplication.translate("Form", "Inter-/ extrapolation", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_label_11.setText(QtGui.QApplication.translate("Form", "Intances", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_comboBox_interpolation.setItemText(0, QtGui.QApplication.translate("Form", "none", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_comboBox_interpolation.setItemText(1, QtGui.QApplication.translate("Form", "forward", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_comboBox_interpolation.setItemText(2, QtGui.QApplication.translate("Form", "backward", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_comboBox_interpolation.setItemText(3, QtGui.QApplication.translate("Form", "both_fill", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_comboBox_interpolation.setItemText(4, QtGui.QApplication.translate("Form", "linear", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_comboBox_interpolation.setItemText(5, QtGui.QApplication.translate("Form", "index", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_comboBox_interpolation.setItemText(6, QtGui.QApplication.translate("Form", "values", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_comboBox_interpolation.setItemText(7, QtGui.QApplication.translate("Form", "nearest", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_comboBox_interpolation.setItemText(8, QtGui.QApplication.translate("Form", "zero", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_comboBox_interpolation.setItemText(9, QtGui.QApplication.translate("Form", "slinear", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_comboBox_interpolation.setItemText(10, QtGui.QApplication.translate("Form", "quadratic", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_comboBox_interpolation.setItemText(11, QtGui.QApplication.translate("Form", "cubic", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_comboBox_interpolation.setItemText(12, QtGui.QApplication.translate("Form", "p_polynomial", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_comboBox_interpolation.setItemText(13, QtGui.QApplication.translate("Form", "from_derivates", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_comboBox_interpolation.setItemText(14, QtGui.QApplication.translate("Form", "akima", None, QtGui.QApplication.UnicodeUTF8))
        self.t2_checkBox_setlod.setText(QtGui.QApplication.translate("Form", "Set LOD", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Form", "Pre-Processing", None, QtGui.QApplication.UnicodeUTF8))
        self.t3_pushButton_exit.setText(QtGui.QApplication.translate("Form", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.t3_label_3.setText(QtGui.QApplication.translate("Form", "Experiment", None, QtGui.QApplication.UnicodeUTF8))
        self.t3_label_13.setText(QtGui.QApplication.translate("Form", "Result_Path", None, QtGui.QApplication.UnicodeUTF8))
        self.t3_checkBox_TAN.setText(QtGui.QApplication.translate("Form", "TAN", None, QtGui.QApplication.UnicodeUTF8))
        self.t3_checkBox_NB.setText(QtGui.QApplication.translate("Form", "Naive Bayes", None, QtGui.QApplication.UnicodeUTF8))
        self.t3_checkBox_ANN.setText(QtGui.QApplication.translate("Form", "ANN", None, QtGui.QApplication.UnicodeUTF8))
        self.t3_checkBox_SMO.setText(QtGui.QApplication.translate("Form", "SMO", None, QtGui.QApplication.UnicodeUTF8))
        self.t3_checkBox_J48.setText(QtGui.QApplication.translate("Form", "J48", None, QtGui.QApplication.UnicodeUTF8))
        self.t3_checkBox_RF.setText(QtGui.QApplication.translate("Form", "Random Forest", None, QtGui.QApplication.UnicodeUTF8))
        self.t3_checkBox_RT.setText(QtGui.QApplication.translate("Form", "Random Tree", None, QtGui.QApplication.UnicodeUTF8))
        self.t3_label_4.setText(QtGui.QApplication.translate("Form", "Bayes", None, QtGui.QApplication.UnicodeUTF8))
        self.t3_label_5.setText(QtGui.QApplication.translate("Form", "Functions", None, QtGui.QApplication.UnicodeUTF8))
        self.t3_label_6.setText(QtGui.QApplication.translate("Form", "Tree", None, QtGui.QApplication.UnicodeUTF8))
        self.t3_comboBox_discMethod.setItemText(0, QtGui.QApplication.translate("Form", "Equal Distance", None, QtGui.QApplication.UnicodeUTF8))
        self.t3_comboBox_discMethod.setItemText(1, QtGui.QApplication.translate("Form", "Equal Frequency", None, QtGui.QApplication.UnicodeUTF8))
        self.t3_label_2.setText(QtGui.QApplication.translate("Form", "Bins", None, QtGui.QApplication.UnicodeUTF8))
        self.t3_pushButton_discApply.setText(QtGui.QApplication.translate("Form", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.t3_toolButton_load_csv_disc.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.t3_label_1.setText(QtGui.QApplication.translate("Form", "Discretization", None, QtGui.QApplication.UnicodeUTF8))
        self.t3_toolButton_result.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.t3_pushButton_bnXML.setText(QtGui.QApplication.translate("Form", "BN_XML", None, QtGui.QApplication.UnicodeUTF8))
        self.t3_label_14.setText(QtGui.QApplication.translate("Form", "Generate BN graph file", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("Form", "KI-Learning", None, QtGui.QApplication.UnicodeUTF8))
        self.t4_pushButton_exit.setText(QtGui.QApplication.translate("Form", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.t4_comboBox_2.setItemText(0, QtGui.QApplication.translate("Form", "Nitrate", None, QtGui.QApplication.UnicodeUTF8))
        self.t4_comboBox_2.setItemText(1, QtGui.QApplication.translate("Form", "Nitrite", None, QtGui.QApplication.UnicodeUTF8))
        self.t4_comboBox_2.setItemText(2, QtGui.QApplication.translate("Form", "TOC", None, QtGui.QApplication.UnicodeUTF8))
        self.t4_comboBox_2.setItemText(3, QtGui.QApplication.translate("Form", "pH", None, QtGui.QApplication.UnicodeUTF8))
        self.t4_comboBox_2.setItemText(4, QtGui.QApplication.translate("Form", "KS43", None, QtGui.QApplication.UnicodeUTF8))
        self.t4_label_1.setText(QtGui.QApplication.translate("Form", "Target Parameter", None, QtGui.QApplication.UnicodeUTF8))
        self.t4_pushButton_startsimulation.setText(QtGui.QApplication.translate("Form", "Start Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.t4_pushButton_loadTargets.setText(QtGui.QApplication.translate("Form", "Load Targets", None, QtGui.QApplication.UnicodeUTF8))
        self.t4_comboBox_1.setItemText(0, QtGui.QApplication.translate("Form", "TAN", None, QtGui.QApplication.UnicodeUTF8))
        self.t4_comboBox_1.setItemText(1, QtGui.QApplication.translate("Form", "J48", None, QtGui.QApplication.UnicodeUTF8))
        self.t4_comboBox_1.setItemText(2, QtGui.QApplication.translate("Form", "ANN", None, QtGui.QApplication.UnicodeUTF8))
        self.t4_comboBox_1.setItemText(3, QtGui.QApplication.translate("Form", "SMO", None, QtGui.QApplication.UnicodeUTF8))
        self.t4_comboBox_1.setItemText(4, QtGui.QApplication.translate("Form", "Random Forest", None, QtGui.QApplication.UnicodeUTF8))
        self.t4_comboBox_3.setItemText(0, QtGui.QApplication.translate("Form", "TAN", None, QtGui.QApplication.UnicodeUTF8))
        self.t4_comboBox_3.setItemText(1, QtGui.QApplication.translate("Form", "J48", None, QtGui.QApplication.UnicodeUTF8))
        self.t4_comboBox_3.setItemText(2, QtGui.QApplication.translate("Form", "ANN", None, QtGui.QApplication.UnicodeUTF8))
        self.t4_comboBox_3.setItemText(3, QtGui.QApplication.translate("Form", "SMO", None, QtGui.QApplication.UnicodeUTF8))
        self.t4_comboBox_3.setItemText(4, QtGui.QApplication.translate("Form", "Random Forest", None, QtGui.QApplication.UnicodeUTF8))
        self.t4_comboBox_4.setItemText(0, QtGui.QApplication.translate("Form", "Nitrate", None, QtGui.QApplication.UnicodeUTF8))
        self.t4_comboBox_4.setItemText(1, QtGui.QApplication.translate("Form", "Nitrite", None, QtGui.QApplication.UnicodeUTF8))
        self.t4_comboBox_4.setItemText(2, QtGui.QApplication.translate("Form", "TOC", None, QtGui.QApplication.UnicodeUTF8))
        self.t4_comboBox_4.setItemText(3, QtGui.QApplication.translate("Form", "pH", None, QtGui.QApplication.UnicodeUTF8))
        self.t4_comboBox_4.setItemText(4, QtGui.QApplication.translate("Form", "KS43", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("Form", "Prediction", None, QtGui.QApplication.UnicodeUTF8))


    def objectfunctions(self, Form):
       
        #Widget configurations
        #First Widget
        # a figure instance to plot on
        self.figure1 = plt.figure()
        self.canvas1 = FigureCanvas(self.figure1)
        self.navi_toolbar = NavigationToolbar(self.canvas1, self)
     
        # set the layout
        layout1 = QtGui.QVBoxLayout(self.t2_widget_1)
        layout1.addWidget(self.canvas1)
        layout1.addWidget(self.navi_toolbar)

        #Second Widget
        # a figure instance to plot on
        self.figure2 = plt.figure()
        self.canvas2 = FigureCanvas(self.figure2)
        self.navi_toolbar = NavigationToolbar(self.canvas2, self)
        # set the layout

        layout2 = QtGui.QVBoxLayout(self.t2_widget_2)
        layout2.addWidget(self.canvas2)
        layout2.addWidget(self.navi_toolbar)

        #Third Widget
        # a figure instance to plot on
        self.figure3 = plt.figure()
        self.canvas3 = FigureCanvas(self.figure3)
        # set the layout
        layout3 = QtGui.QVBoxLayout(self.t2_widget_3)
        layout3.addWidget(self.canvas3)


        #Direct item functions
  
        self.t2_toolButton_load_csv.clicked.connect(self.first_load)
        self.t2_pushButton_reset.clicked.connect(self.reset)
        self.t2_pushButton_save_dic.clicked.connect(self.save_dict)
        self.t2_pushButton_next_col.clicked.connect(self.next_col)
        self.t2_pushButton_prev_col.clicked.connect(self.prev_col)
        self.t2_pushButton_save_cpage.clicked.connect(self.save_page_csv)
        self.t2_comboBox_header_data.activated.connect(self.change_col_update_routine)
        self.t2_pushButton_em.clicked.connect(self.em_imputation)
        self.t2_pushButton_insert.clicked.connect(self.insert_ncg_column)
        self.t3_toolButton_load_csv_disc.clicked.connect(self.discretize)
        self.t3_pushButton_bnXML.clicked.connect(self.xml_generator)
        #self.t2_pushButton_exit.clicked.connect(self.exit)
        self.t1_pushButton_1.clicked.connect(self.load_left)
        self.t1_pushButton_2.clicked.connect(self.load_right)
        self.t1_pushButton_submergeleft.clicked.connect(self.sub_merge_left)
        self.t1_pushButton_submergeright.clicked.connect(self.sub_merge_right)
        self.t1_pushButton_merge_left.clicked.connect(self.load_merge_left)
        self.t1_pushButton_merge_right.clicked.connect(self.load_merge_right)

        self.t1_pushButton_merge_combi.clicked.connect(self.merge_combi)

        self.t1_pushButton_delete_left.clicked.connect(self.t1_listWidget_1.clear)
        self.t1_pushButton_delete_right.clicked.connect(self.t1_listWidget_2.clear)

        self.t1_pushButton_selectfile.clicked.connect(self.load_trans_file)
        self.t1_pushButton_selecttransdic.clicked.connect(self.load_transdic_file)
        self.t1_pushButton_apply_trans.clicked.connect(self.apply_translator)
        self.t1_pushButton_6.clicked.connect(self.common_header)

        


        
        # Method functions
        self.t2_comboBox_header_data.activated.connect(self.update_routine)
        self.t2_comboBox_diagram_selection.activated.connect(self.update_routine)
        self.t2_comboBox_interpolation.activated.connect(self.update_routine)
        self.t2_comboBox_outliertest.activated.connect(self.update_routine)
        self.t2_radioButton_histo.clicked.connect(self.update_routine)
        self.t2_radioButton_cumcurve.clicked.connect(self.update_routine)        
        self.t2_lineEdit_mcriterion.returnPressed.connect(self.update_routine)
        self.t2_lineEdit_bins.returnPressed.connect(self.update_routine)
        self.t2_lineEdit_lpercentile.returnPressed.connect(self.update_routine)
        self.t2_lineEdit_upercentile.returnPressed.connect(self.update_routine)
        self.t2_lineEdit_textlod.returnPressed.connect(self.update_routine)
        self.t2_checkBox_norm_mean.clicked.connect(self.update_routine)
        self.t2_checkBox_norm_minmax.clicked.connect(self.update_routine)
        self.t2_checkBox_target.clicked.connect(self.update_routine)
        self.t2_checkBox_delete.clicked.connect(self.update_routine)
        self.t2_checkBox_setlod.clicked.connect(self.update_routine)




####################################################################################################################
#Tab1###############################################################################################################

    def load_left(self):

         #0=None
         #1=Type: Online 15min
         #2=Type: Online 2h
         #3=Type: Standard Sampling

        if self.t1_comboBox_1.currentIndex()==0:
            xsyst=1
            
        elif self.t1_comboBox_1.currentIndex()==1:
            self.file_list_left = QtGui.QFileDialog.getOpenFileNames(self, 'Open file','.\\',"*xls")
            self.dir_left= os.path.dirname(self.file_list_left[0])
            for item in self.file_list_left:
                self.t1_listWidget_1.addItem(os.path.basename(item))     
                
        elif self.t1_comboBox_1.currentIndex()==2:
            self.file_list_left = QtGui.QFileDialog.getOpenFileNames(self, 'Open file','.\\',"*xls")
            self.dir_left= os.path.dirname(self.file_list_left[0])
            for item in self.file_list_left:
                self.t1_listWidget_1.addItem(os.path.basename(item))
                
        elif self.t1_comboBox_1.currentIndex()==3:           
            self.file_list_left = QtGui.QFileDialog.getOpenFileNames(self, 'Open file','.\\',"*xlsx")
            self.dir_left= os.path.dirname(self.file_list_left[0])
            for item in self.file_list_left:
                self.t1_listWidget_1.addItem(os.path.basename(item))

        self.lst_left = [os.path.dirname(self.file_list_left[0])+"\\"+i.text() for i in self.t1_listWidget_1.findItems("", QtCore.Qt.MatchContains)]
        print(self.lst_left)

          

        
    def load_right(self):

        if self.t1_comboBox_2.currentIndex()==0:
            xsyst=1
            
        elif self.t1_comboBox_2.currentIndex()==1:
            self.file_list_right = QtGui.QFileDialog.getOpenFileNames(self, 'Open file','.\\',"*xls")
            self.dir_right= os.path.dirname(self.file_list_right[0])

            for item in self.file_list_right:
                self.t1_listWidget_2.addItem(os.path.basename(item))
                
        elif self.t1_comboBox_2.currentIndex()==2:
            self.file_list_right = QtGui.QFileDialog.getOpenFileNames(self, 'Open file','.\\',"*xls")
            self.dir_left= os.path.dirname(self.file_list_right[0])

            for item in self.file_list_right:
                self.t1_listWidget_2.addItem(os.path.basename(item))
                
        elif self.t1_comboBox_2.currentIndex()==3:           
            self.file_list_right = QtGui.QFileDialog.getOpenFileNames(self, 'Open file','.\\',"*xlsx")
            self.dir_right= os.path.dirname(self.file_list_right[0])

            for item in self.file_list_right:
                self.t1_listWidget_2.addItem(os.path.basename(item))

        self.lst_right = [os.path.dirname(self.file_list_right[0])+"\\"+i.text() for i in self.t1_listWidget_2.findItems("", QtCore.Qt.MatchContains)]
        #print(self.lst_right)

    def sub_merge_left(self):
        self.target_file_left= str(self.t1_lineEdit_1.text())
        self.target_path_left = os.getcwd()+"\\"+self.target_file_left
        #print(self.target_path_left)
        #print(self.t1_comboBox_1.currentIndex())

        if self.t1_comboBox_1.currentIndex()==1:
            self.lst_input=self.lst_left
            self.out_path = self.target_path_left
            self.collector_online15()
        elif self.t1_comboBox_1.currentIndex()==2:
            self.lst_input=self.lst_left
            self.out_path = self.target_path_left
            self.collector_online2()
        elif self.t1_comboBox_1.currentIndex()==3:
            self.lst_input=self.lst_left
            self.out_path = self.target_path_left
            self.collector_sample()


    def sub_merge_right(self):
        self.target_file_right= str(self.t1_lineEdit_2.text())
        self.target_path_right = os.getcwd()+"\\"+self.target_file_right
        #print(self.target_path_right)
        #print(self.t1_comboBox_2.currentIndex())
        
        if self.t1_comboBox_2.currentIndex()==1:
            self.lst_input=self.lst_right
            self.out_path = self.target_path_right
            self.collector_online15()
            
            
        elif self.t1_comboBox_2.currentIndex()==2:
            self.lst_input=self.lst_right
            self.out_path = self.target_path_right
            self.collector_online2()
            
        elif self.t1_comboBox_2.currentIndex()==3:
            self.lst_input=self.lst_right
            self.out_path = self.target_path_right
            self.collector_sample()

    def collector_online15(self):
        print("online15")
        print("input_list")
        print(self.out_path)
        print(self.lst_input)
        import pandas as pd
        import glob
        import numpy as np
        import xlrd
        import ntpath
        import time
        from datetime import datetime

        data = [] # pd.concat takes a list of dataframes as an agrument

        counter=0
        for xls in self.lst_input:

            name = ntpath.basename(xls)
            name= name.split('.')[0]

            print(name)
            df1 = pd.read_excel(xls, 'Tabelle1',header=22, index_col=None)
            df1 = df1[['Messung am/um','Gültigkeitsmarke','Wert']]

            df2 = pd.read_excel(xls, 'Tabelle2', header=22, index_col=None)
            df2 = df2[['Messung am/um','Gültigkeitsmarke','Wert']]

            df3 = pd.read_excel(xls, 'Tabelle3', header=22, index_col=None)
            df3 = df3[['Messung am/um','Gültigkeitsmarke','Wert']]

            #print(df1.head())
            #print(df2.head())
            #print(df3.head())
            frames = [df1, df2, df3]
            rst = pd.concat(frames)
            rst.reset_index()


            #Filter G
            rst['mask'] = rst['Gültigkeitsmarke'].isin(['G'])
            rst[name] = np.where(rst['Gültigkeitsmarke']=='G', rst['Wert'], '?')


            #Round Wert and Value to 4 decimals
            decimals = pd.Series([4, 4], index=[name, 'Wert'])
            rst.round(decimals)


            #Take only relvant Columns before UNIX and merge
            rst = rst.drop('Wert', 1)
            rst = rst.drop('mask', 1)
            rst = rst.drop('Gültigkeitsmarke', 1)

            #print(rst.head())

            #Insert UNIX
            list_dates = rst['Messung am/um']
            index = pd.DatetimeIndex(list_dates)
            index.astype(np.int64)
            unix_list=index.astype(np.int64) // 10**9
            rst['UNIX'] = unix_list

            #print(rst)

            rst = rst.drop('Messung am/um', 1)
            rst= rst[['UNIX',name]]
            rst=rst.drop_duplicates(subset=["UNIX"])

            if counter==0:
                df = rst
                #print(df)                

            else:
                left = df
                right = rst 
                df = pd.merge(left, right,how='left', on='UNIX')
            #print(len(df.index))

            counter=counter+1
            

        df = df.fillna('?')
        
        
        df = df.replace("?", np.nan)
        col_num=int(len(list(left)))
        treshold10=(col_num/100)*10
        df = df.dropna(thresh=treshold10)
        
        #df.sort_index(axis=1, inplace=True)
        #print("FINALE")
        #print(df)
        #output CSV file
        filename= self.out_path + '.csv'
        df.to_csv(filename,  index = False)
        print("End")





        
        
    def collector_online2(self):
        print("online2")
        print("input_list")
        print(self.out_path)
        print(self.lst_input)
        import pandas as pd
        import glob
        import numpy as np
        from datetime import datetime

        #globbed_files = glob.glob(".\\Small_Dataset_2014_2015\\small_online_montoring\\*.xls") #creates a list of all csv files

        real_frame = pd.DataFrame()

        data= pd.read_excel(self.lst_input[0],sheetname=1,header=22)
        col_name1 = "Messung am/um"
        data1 = data[col_name1]
        col_name1 = "Datum"
        real_frame[col_name1]= data1

        list_dates = real_frame[col_name1]
        index = pd.DatetimeIndex(list_dates)
        index.astype(np.int64)
        unix_list=index.astype(np.int64) // 10**9

        real_frame["UNIX"] = unix_list


        for xls in self.lst_input:
            xls = pd.ExcelFile(xls)
            sheets = xls.sheet_names
            #print(sheets)
            for sheet in sheets:
                try:
                    data= pd.read_excel(xls,sheetname=sheet,header=22)
                    name= pd.read_excel(xls,sheetname=sheet)
                    name_str = str(name.iloc[0,1])
                    name_str = name_str.split("  -  ")[0]
                    name_str = name_str.replace("+","_")
                    name_str = name_str.replace("-","_")
                    print(name_str)


                    #print(name_str)

                    #col_name1 = "Messung am/um"
                    col_name2 = "Wert"
                    #col_name3 = "Gültigkeitsmarke"
                    #data1 = data[col_name1]
                    data2 = data[col_name2]
                    #data3 = data[col_name3]
                    #col_name1 = name_str + "_%_Date"
                    #col_name2 = name_str + "_%_Value"


                    col_name2 = name_str
                    #col_name3 = name_str + "_%_Filter"

                    #real_frame[col_name1]= data1
                    real_frame[col_name2]= data2
                    #real_frame[col_name3]= data3
                except IndexError: pass
                     

        #bigframe = pd.concat(real_frame, ignore_index=True) #dont want pandas to try an align row indexes
        real_frame.sort_index(axis=1, inplace=True)

        real_frame=real_frame.reindex(columns=['UNIX']+real_frame.columns[:-1].tolist())

        if 'Datum' in real_frame.columns:
            real_frame.drop('Datum', axis=1, inplace=True)
        
        real_frame = real_frame.fillna('?')
        #real_frame = real_frame.replace("?", np.nan)
        #col_num=int(len(list(left)))
        #treshold10=(col_num/100)*10
        #real_frame = real_frame.dropna(thresh=treshold10)

        
        filename= self.out_path + '.csv'
        real_frame.to_csv(filename,  index = False)


        
        #print(real_frame)
        print("End")
        

    def collector_sample(self):
        print("sample")
        print("input_list")
        #print(self.out_path)        
        #print(self.lst_input)

        import pandas as pd
        from pandas import read_csv
        import numpy as np
        import glob
        import csv
        import os
        import argparse
        import operator
        from datetime import datetime
        from os import listdir, rmdir, remove
        #####################################################################################################################################
        # Get xls all Paths in an Folder
        print("First Step")

        if os.path.isdir(os.path.dirname(self.file_list_left[0])+"\\"+self.target_file_left+"_csv")==True:
            for i in listdir(os.path.dirname(self.file_list_left[0])+"\\"+self.target_file_left+"_csv"):
                os.remove(os.path.join(os.path.dirname(self.file_list_left[0])+"\\"+self.target_file_left+"_csv", i))

            rmdir(os.path.dirname(self.file_list_left[0])+"\\"+self.target_file_left+"_csv\\") # Now the directory is empty of files
        
        folder_xls = os.path.dirname(self.file_list_left[0])
        os.makedirs(os.path.dirname(self.file_list_left[0])+"\\"+self.target_file_left+"_csv\\")
        folder_csv = os.path.dirname(self.file_list_left[0])+"\\"+self.target_file_left+"_csv\\"

        file_list = self.lst_input

        dic_sheets = {"Zu. VKB" : [2,0],
                      "Zu. Bio I":[2,0],
                      "Zu. Bio II":[2,0],
                      "Zu. SFI":[2,0],
                      "Ablauf 24h":[2,0],
                      "Ablauf 2h":[2,0],
                      "Dekantat":[2,0],
                      "SWP":[2,1],
                      "Bio I":[3,0],
                      "Bio II":[3,0],
                      "Schlammdat 1":[2,0],
                      "Schlammdat 2":[3,0]
                      }
        dic_header = {"Zu. VKB" : [],
                      "Zu. Bio I":[],
                      "Zu. Bio II":[],
                      "Zu. SFI":[],
                      "Ablauf 24h":[],
                      "Ablauf 2h":[],
                      "Dekantat":[],
                      "SWP":[],
                      "Bio I":[],
                      "Bio II":[],
                      "Schlammdat 1":[],
                      "Schlammdat 2":[]
                      }

        frame_dict={}
        length_header=0
        new_header=['Datum']

        for path in file_list:
            year= path.split("_")[-1]
            year=year.split(".")[0]
            xl = pd.ExcelFile(path)
            sheet_list= xl.sheet_names
            length= len(sheet_list)
            dfs = {sheet: xl.parse(sheet) for sheet in dic_sheets}
            #print(dfs)
            left=[]    
            for key in dic_sheets:
                #print(key)

                column=dic_sheets[key][1]
                
                row=dic_sheets[key][0]
                dfs[key].columns = dfs[key].iloc[row-1]
                dfs[key]= dfs[key].ix[row:,column:]
                dfs[key]=dfs[key].dropna(axis=1,how='all')

                df= pd.DataFrame.from_dict(dfs[key])
                new_col_names=['Datum']
                header=[]

                for i in df.columns[1:]:
                    name = key+"_"+i
                    name=name.split("\n")[0]
                    print(name)
                    name=name.replace(",", "")
                    new_col_names.append(name)

                df.rename(columns=dict(zip(df.columns, new_col_names)), inplace=True)
                if len(dic_header[key])< len(df.columns):
                    dic_header[key]= df.columns

                ##X## Not a normal Part only necessary to generate a header list once
                '''
                #df=df.columns
                #header= pd.DataFrame(df)
                filename= folder+"header_dict.csv"
                with open(filename, 'a') as f:
                    header.to_csv(f,header=False,index=False)
                    

                #remove duplicates in csv
                df_temp = pd.read_csv(filename, enc
                oding = "ISO-8859-1")
                df_temp.drop_duplicates(subset=None, inplace=True)
                df_temp.to_csv(filename,index=False)
                '''
                #print(df)
                        
                filename= str(folder_csv)+key+".csv"
                print(filename)
                with open(filename, 'a') as f:
                    if os.stat(filename).st_size == 0:
                        df.to_csv(f, header=True, index=None)               
                    else:                    
                        df.to_csv(f, header=False, index=None)

    
                l = dic_header[key]

                with open(filename, 'r') as data_file:
                    lines = data_file.readlines()
                    lines[0]= ",".join(l)+"\n" # replace first line, the "header" with list contents
                    with open(filename, 'w') as out_data:
                        for line in lines: # write updated lines
                            out_data.write(line)

                        

        ###################################################################################################################

        print("Second Part")

        file_list = glob.glob(str(folder_csv)+"\\*.csv")
        print("File list of CSV")

        print(file_list)
        result=pd.DataFrame()


        for path in file_list:
            if result.empty:
                result = pd.read_csv(path,encoding = "ISO-8859-1")
                
            else:
                left = result
                right = pd.read_csv(path,encoding = "ISO-8859-1")
                result= pd.merge(left, right, how='left', on=['Datum'])

        #print(result.columns.tolist())
        result = result[result.columns.drop(list(result.filter(regex='Wochentag')))]
        result = result[result.columns.drop(list(result.filter(regex='Uhrzeit')))]
        '''
        with open(".\\sub_files\\dict_online_en.csv") as f:
            d = dict(filter(None, csv.reader(f)))

        print(d)

        result=result.rename(columns = d)
        '''



        list_dates = result['Datum']
        index = pd.DatetimeIndex(list_dates)
        index.astype(np.int64)
        unix_list=index.astype(np.int64) // 10**9

        result['UNIX'] = unix_list

        result=result.reindex(columns=['UNIX']+result.columns[:-1].tolist())
        result=result.sort_values(by='UNIX')

        if 'Ablauf 24h_N-gesamt mg/l.1' in result.columns:
            result.drop('Ablauf 24h_N-gesamt mg/l.1', axis=1, inplace=True)
        if 'Ablauf 2h_N-gesamt mg/l.1' in result.columns:
            result.drop('Ablauf 2h_N-gesamt mg/l.1', axis=1, inplace=True)
        if 'Schlammdat 2_GV .1' in result.columns:
            result.drop('Schlammdat 2_GV .1', axis=1, inplace=True)
        if 'Datum' in result.columns:
            result.drop('Datum', axis=1, inplace=True)
            
        result.fillna('?', inplace =True)

        print(result.head())

        filename= self.out_path + '.csv'
        result[1:].to_csv(filename, header=True, index=None)

        print("End")



    def load_merge_left(self):
        self.file_left = QtGui.QFileDialog.getOpenFileName(self, 'Open file','.\\',"*csv")
        self.t1_lineEdit_3.setText(self.file_left)
        


    def load_merge_right(self):
        self.file_right = QtGui.QFileDialog.getOpenFileName(self, 'Open file','.\\',"*csv")
        self.t1_lineEdit_4.setText(self.file_right)


    def merge_combi(self):

        import pandas as pd
        from pandas import read_csv
        import numpy as np
        import glob
        import csv
        import os
        import argparse
        import operator
        from datetime import datetime
        import header_trans



        #file_list = all_file_string_module.get_value(x,"csv")
        #print(file_list)

        data_str_left=self.t1_lineEdit_3.text()
        data_str_right=self.t1_lineEdit_4.text()

        left = pd.DataFrame()
        right = pd.DataFrame()
        #load dataframe and remove empty rows
        left=pd.read_csv(data_str_left,encoding = "ISO-8859-1",low_memory=False)
        left = left.replace("?", np.nan)
        print("Left Dataset")
        print(left.head)

        #load dataframe right and remove empty rows
        right=pd.read_csv(data_str_right,encoding = "ISO-8859-1",low_memory=False)
        right = right.replace("?", np.nan)
        print("Right Dataset")
        print(right.head)
        print(self.t1_lineEdit_merge_on.text())


        if self.t1_radioButton_major_left.isChecked():
            result = pd.merge(left, right, how='left', on=[self.t1_lineEdit_merge_on.text()])
        else:
            result = pd.merge(left, right, how='right', on=[self.t1_lineEdit_merge_on.text()])
                
        if 'Datum' in result.columns:
            result.drop('Datum', axis=1, inplace=True)
            
        #result = result.dropna(thresh=200)
        #new_unix=right["UNIX"]
        #result = result.drop("UNIX", 1)
        #result= result.insert(0, "UNIX", new_unix)

        result = result.loc[:,~result.columns.duplicated()]

        #col_num=int(len(list(result)))
        #treshold10=(col_num/100)*10
        #result = result.dropna(thresh=treshold10)
        result=result.sort_values(by='UNIX')

        print("Result Dataset")
        print(result.head)
        '''
        with open(".\\sub_files\\dict_online_en.csv") as f:
            d = dict(filter(None, csv.reader(f)))
        #print(d)
        result=result.rename(columns = d)
        '''
        filename= ".\\"+"final_"+self.t1_lineEdit_merge_combi.text()+".csv"
        with open(filename, 'w') as f:
            result.to_csv(f, header=True, index=None)

    def apply_translator(self):
     
        #self.target_file_path = self.t1_lineEdit_transdic.setText(self.transdic_file_path)
        self.target_file=pd.read_csv(self.trans_file_path,encoding = "ISO-8859-1",low_memory=False)
        dirpath= os.path.dirname(self.trans_file_path)
        target_file_name= dirpath+"\\"+self.t1_lineEdit_targetpath.text()+".csv"

        with open(self.transdic_file_path ) as f:
            d = dict(filter(None, csv.reader(f)))
        self.target_file=self.target_file.rename(columns = d)

        with open(target_file_name, 'w') as f:
            self.target_file.to_csv(f, header=True, index=None)

        print("Finished translation")

        
    def load_trans_file(self):        
        self.trans_file_path = QtGui.QFileDialog.getOpenFileName(self, 'Open file','.\\',"*csv")
        self.t1_lineEdit_selectfile.setText(self.trans_file_path)

    def load_transdic_file(self):
        self.transdic_file_path = QtGui.QFileDialog.getOpenFileName(self, 'Open file','.\\',"*csv")
        self.t1_lineEdit_transdic.setText(self.transdic_file_path)

    def common_header(self):

        self.common_header_list = QtGui.QFileDialog.getOpenFileNames(self, 'Open file','.\\',"*csv")
        
        new_header = pd.read_csv(self.common_header_list[0],low_memory=False).columns.values
        print("before loop")

        for item in self.common_header_list[1:]:
            header = pd.read_csv(item,low_memory=False).columns.values
            new_header = sorted(set(new_header).intersection(header),key=lambda x:new_header.tolist().index(x))


        for item in self.common_header_list:
            data=None
            header_path=None
            data= pd.read_csv(item,low_memory=False)
            data_new=data[new_header]
            data_new = data_new.loc[:,~data_new.columns.duplicated()]
            ##In der nächsten Zeile ist ein Fehler...
            header_path= os.path.dirname(self.common_header_list[item])+os.path.basename(self.common_header_list[item]).split(".")[0]+"_ch.csv" 

            with open(header_path, 'w') as f:
                data_new.to_csv(f, header=True, index=None)



      

####################################################################################################################
#Tab2###############################################################################################################

   
    def first_load(self):
        self.fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file','.\\',"*csv")
        self.header = pd.read_csv(self.fname,low_memory=False,nrows=1).columns
        self.header=self.header[1:]
        self.t2_comboBox_header_data.clear()
        self.t2_comboBox_header_data.addItems(self.header)
        self.initial_routine()
        
    def initial_routine(self):
        self.current_title=self.t2_comboBox_header_data.currentText()
        #self.current_col = str(self.comboBox_header_data.currentText())
        self.load_data()
        self.initialize_dict()
        self.initialize_items()
        self.load_selcolncg()
        #Generate Data
        self.transform_data()
        #generate Plots
        self.call_plots()
        missing_col=self.new_df
        self.missing(missing_col)

    def update_routine(self):
        self.current_title=self.t2_comboBox_header_data.currentText()
        self.change_dict()
        self.load_data()
        self.initialize_items()
        #Generate Data
        self.transform_data()
        #generate Plots
        self.call_plots()
        missing_col=self.new_df
        self.missing(missing_col)

    def change_col_update_routine(self):
        self.current_title=self.t2_comboBox_header_data.currentText()
        self.load_data()
        self.initialize_items()
        #Generate Data
        self.transform_data()
        #generate Plots
        self.call_plots()
        missing_col=self.new_df
        self.missing(missing_col)


    def transform_data(self):

        #interpolate missing
        self.set_lod()
        self.interpol()
        #normalize
        self.normalize()        
        #outlier removal
        self.outlier_removal()
        self.interpol()

    def set_lod(self):
        if self.my_dict[self.current_title]["setlod"]==True:
            lod=float(self.my_dict[self.current_title]["textlod"])
            self.new_df[self.current_title] = self.new_df[self.current_title].apply(lambda x: lod if x < lod else x)
            print(lod)
        else:
            print("LOD not set")

    def load_selcolncg(self):   
        self.t2_comboBox_selColNCG.addItems(self.header)

    def ncg(self):
        xysades=1    

    def insert_ncg_column(self):        
        self.current_title_ncg_col=self.t2_comboBox_selColNCG.currentText()
        self.t2_listWidget_NCG.addItem(self.current_title_ncg_col)

    def outlier_removal(self):
        self.minval = round(float(self.my_dict[self.current_title]["lpercentile"]),2)
        self.maxval = round(float(self.my_dict[self.current_title]["upercentile"]),2)        
        self.minval= np.nanpercentile(self.new_df[self.current_title], self.minval)
        self.maxval= np.nanpercentile(self.new_df[self.current_title], self.maxval)

        if self.my_dict[self.current_title]["outliertest"]==0:
            #Replace by Outliers/Row
            if self.my_dict[self.current_title]["missing_percentiles"]==1:
                self.new_df = (self.new_df[self.new_df[self.current_title] < self.maxval])
                self.new_df = (self.new_df[self.new_df[self.current_title] > self.minval])
            # Replace by Winsorizing
            elif self.my_dict[self.current_title]["missing_percentiles"]==2:
                self.new_df[self.current_title] = self.new_df[self.current_title].apply(lambda x: self.minval if x < self.minval else x)
                self.new_df[self.current_title] = self.new_df[self.current_title].apply(lambda x: self.maxval if x > self.maxval else x)
            #Replace by mean
            elif self.my_dict[self.current_title]["missing_percentiles"]==3:
                print("Mike"+str(round(float(self.new_df[self.current_title].mean()),2)))
                self.new_df[self.current_title] = self.new_df[self.current_title].apply(lambda x: round(float(self.new_df[self.current_title].mean()),2) if x < self.minval else x)
                self.new_df[self.current_title] = self.new_df[self.current_title].apply(lambda x: round(float(self.new_df[self.current_title].mean()),2) if x > self.maxval else x)
            #Replace by missing
            elif self.my_dict[self.current_title]["missing_percentiles"]==4:
                self.new_df[self.current_title] = self.new_df[self.current_title].apply(lambda x: np.NaN if x < self.minval else x)
                self.new_df[self.current_title] = self.new_df[self.current_title].apply(lambda x: np.NaN if x > self.maxval else x)


        elif self.my_dict[self.current_title]["outliertest"]==1:
            #distribution-free test (Mathematical Statistics With Applications>>"K.M. Ramachandran, Chris P. Tsokos")
            MAD=self.new_df[self.current_title].mad()
            col_median_val=np.nanmedian(self.new_df[self.current_title])
            col_avg_val=np.nanmean(self.new_df[self.current_title])
            #print("mean_MAD: "+str(MAD))
            #print("Median: "+str(col_median_val))
            #print("Mean: "+str(col_avg_val))
            xyz=np.nanmedian(MAD)
            #print("Test: "+str(xyz))
            med = np.nanmedian(self.new_df[self.current_title], keepdims=True)
            #print("med: "+str(med))
            MAD = np.nanmedian(np.absolute(self.new_df[self.current_title] - med))
            #print("median MAD: "+str(MAD))
            
            if self.my_dict[self.current_title]["missing_percentiles"]==1:
                self.new_df = (self.new_df[self.new_df[self.current_title] < self.maxval])
                self.new_df = (self.new_df[self.new_df[self.current_title] > self.minval])
            # Replace by Winsorizing
            elif self.my_dict[self.current_title]["missing_percentiles"]==2:
                self.new_df[self.current_title] = self.new_df[self.current_title].apply(lambda x: self.minval if (((abs(x-col_median_val))/(MAD))) > 5 else x)
                self.new_df[self.current_title] = self.new_df[self.current_title].apply(lambda x: self.maxval if (((abs(x-col_median_val))/(MAD))) > 5 else x)
            #Replace by mean
            elif self.my_dict[self.current_title]["missing_percentiles"]==3:
                print("Mike"+str(round(float(self.new_df[self.current_title].mean()),2)))
                self.new_df[self.current_title] = self.new_df[self.current_title].apply(lambda x: round(float(self.new_df[self.current_title].mean()),2) if (((abs(x-col_median_val))/(MAD))) > 5 else x)
                self.new_df[self.current_title] = self.new_df[self.current_title].apply(lambda x: round(float(self.new_df[self.current_title].mean()),2) if (((abs(x-col_median_val))/(MAD))) > 5 else x)
            #Replace by missing
            elif self.my_dict[self.current_title]["missing_percentiles"]==4:
                self.new_df[self.current_title] = self.new_df[self.current_title].apply(lambda x: np.NaN if (((abs(x-col_median_val))/(MAD))) > 5 else x)
                self.new_df[self.current_title] = self.new_df[self.current_title].apply(lambda x: np.NaN if (((abs(x-col_median_val))/(MAD))) > 5 else x)

            
        elif self.my_dict[self.current_title]["outliertest"]==2:
            #distribution-free test (Mathematical Statistics With Applications>>"K.M. Ramachandran, Chris P. Tsokos")
            MAD=self.new_df[self.current_title].mad()
            col_median_val=np.nanmedian(self.new_df[self.current_title])
            col_avg_val=np.nanmean(self.new_df[self.current_title])
            #print("mean_MAD: "+str(MAD))
            #print("Median: "+str(col_median_val))
            #print("Mean: "+str(col_avg_val))
            #xyz=np.nanmedian(MAD)
            #print("Test: "+str(xyz))
            med = np.nanmedian(self.new_df[self.current_title], keepdims=True)
            #print("med: "+str(med))
            MAD = np.nanmedian(np.absolute(self.new_df[self.current_title] - med))
            #print("median MAD: "+str(MAD))
            
            if self.my_dict[self.current_title]["missing_percentiles"]==1:
                self.new_df = (self.new_df[self.new_df[self.current_title] < self.maxval])
                self.new_df = (self.new_df[self.new_df[self.current_title] > self.minval])
            # Replace by Winsorizing
            elif self.my_dict[self.current_title]["missing_percentiles"]==2:
                self.new_df[self.current_title] = self.new_df[self.current_title].apply(lambda x: self.minval if ((x-col_avg_val)/(MAD)) > 3.5 else x)
                self.new_df[self.current_title] = self.new_df[self.current_title].apply(lambda x: self.maxval if ((x-col_avg_val)/(MAD)) > 3.5 else x)
            #Replace by mean
            elif self.my_dict[self.current_title]["missing_percentiles"]==3:
                print("Mike"+str(round(float(self.new_df[self.current_title].mean()),2)))
                self.new_df[self.current_title] = self.new_df[self.current_title].apply(lambda x: round(float(self.new_df[self.current_title].mean()),2) if ((x-col_avg_val)/(MAD)) > 3.5 else x)
                self.new_df[self.current_title] = self.new_df[self.current_title].apply(lambda x: round(float(self.new_df[self.current_title].mean()),2) if ((x-col_avg_val)/(MAD)) > 3.5 else x)
            #Replace by missing
            elif self.my_dict[self.current_title]["missing_percentiles"]==4:
                self.new_df[self.current_title] = self.new_df[self.current_title].apply(lambda x: np.NaN if ((x-col_avg_val)/(MAD)) > 3.5 else x)
                self.new_df[self.current_title] = self.new_df[self.current_title].apply(lambda x: np.NaN if ((x-col_avg_val)/(MAD)) > 3.5 else x)

        elif self.my_dict[self.current_title]["outliertest"]==3:
            #distribution-free test (Mathematical Statistics With Applications>>"K.M. Ramachandran, Chris P. Tsokos")
            #col_median_val=np.nanmedian(self.new_df[self.current_title])
            col_avg_val=np.nanmean(self.new_df[self.current_title])

            std_col=np.std(self.new_df[self.current_title])


            
            if self.my_dict[self.current_title]["missing_percentiles"]==1:
                self.new_df = (self.new_df[self.new_df[self.current_title] < self.maxval])
                self.new_df = (self.new_df[self.new_df[self.current_title] > self.minval])
            # Replace by Winsorizing
            elif self.my_dict[self.current_title]["missing_percentiles"]==2:
                self.new_df[self.current_title] = self.new_df[self.current_title].apply(lambda x: self.minval if ((x-col_avg_val)/std_col) > 3  else x)
                self.new_df[self.current_title] = self.new_df[self.current_title].apply(lambda x: self.minval if ((x-col_avg_val)/std_col) < -3 else x)
                #self.new_df[self.current_title] = self.new_df[self.current_title].apply(lambda x: self.maxval if ((x-col_avg_val)/(MAD)) < -3 else x)
            #Replace by mean
            elif self.my_dict[self.current_title]["missing_percentiles"]==3:
                #print("Mike"+str(round(float(self.new_df[self.current_title].mean()),2)))
                self.new_df[self.current_title] = self.new_df[self.current_title].apply(lambda x: self.minval if ((x-col_avg_val)/std_col) > 3 else x)
                self.new_df[self.current_title] = self.new_df[self.current_title].apply(lambda x: self.minval if ((x-col_avg_val)/std_col) < -3 else x)
                #self.new_df[self.current_title] = self.new_df[self.current_title].apply(lambda x: round(float(self.new_df[self.current_title].mean()),2) if ((x-col_avg_val)/(MAD)) > 3.5 else x)
            #Replace by missing
            elif self.my_dict[self.current_title]["missing_percentiles"]==4:
                self.new_df[self.current_title] = self.new_df[self.current_title].apply(lambda x: self.minval if ((x-col_avg_val)/std_col) > 3 else x)
                self.new_df[self.current_title] = self.new_df[self.current_title].apply(lambda x: self.minval if ((x-col_avg_val)/std_col) < -3 else x)
                #self.new_df[self.current_title] = self.new_df[self.current_title].apply(lambda x: np.NaN if ((x-col_avg_val)/(MAD)) > 3.5 else x)

      
        
    def interpol(self):
        #if self.comboBox_interpolation.currentIndex()==1:

        self.interpol_dict = {'linear':'linear',
                              'index':'index',
                              'values':'values',
                              'nearest':'nearest',
                              'zero':'zero',
                              'slinear':'slinear',
                              'quadratic':'quadratic',
                              'cubic':'cubic',
                              'p_polynomial':'piecewise_polynomial',
                              'from_derivates':'from_derivatives',
                              'akima':'akima'
                              }

        if self.my_dict[self.current_title]["interpolation"]==0:
            
            missing_col=pd.DataFrame()
            missing_col=self.new_df
            self.missing(missing_col)
            
        elif self.my_dict[self.current_title]["interpolation"]==1:
            mask = self.new_df.copy()
            grp = ((mask.notnull() != mask.shift().notnull()).cumsum())
            grp['ones'] = 1
            gap= int(self.t2_lineEdit_mcriterion.text())
            for i in self.new_df:
                mask[self.current_title] = (grp.groupby(self.current_title)['ones'].transform('count') < gap) | self.new_df[self.current_title].notnull()

            #self.new_df[self.current_title] = self.new_df.interpolate('from_derivatives')[mask]
            self.new_df[self.current_title] = self.new_df.ffill()[mask]
            missing_col=pd.DataFrame()
            missing_col=self.new_df
            self.missing(missing_col)

        elif self.my_dict[self.current_title]["interpolation"]==2:
            #Linear Interpolation
            mask = self.new_df.copy()
            grp = ((mask.notnull() != mask.shift().notnull()).cumsum())
            grp['ones'] = 1
            gap= int(self.t2_lineEdit_mcriterion.text())
            for i in self.new_df:
                mask[self.current_title] = (grp.groupby(self.current_title)['ones'].transform('count') < gap) | self.new_df[self.current_title].notnull()

            self.new_df[self.current_title] = self.new_df.bfill()[mask]
            missing_col=pd.DataFrame()
            missing_col=self.new_df
            self.missing(missing_col)
            
        elif self.my_dict[self.current_title]["interpolation"]==3:
            #Forward Fill
            mask = self.new_df.copy()
            grp = ((mask.notnull() != mask.shift().notnull()).cumsum())
            grp['ones'] = 1
            gap= int(self.t2_lineEdit_mcriterion.text())
            for i in self.new_df:
                mask[self.current_title] = (grp.groupby(self.current_title)['ones'].transform('count') < gap) | self.new_df[self.current_title].notnull()

            self.new_df[self.current_title] = self.new_df.ffill().bfill()[mask]
            missing_col=pd.DataFrame()
            missing_col=self.new_df
            self.missing(missing_col)
            
        else:
            #remaining dictionary
            mask = self.new_df.copy()
            grp = ((mask.notnull() != mask.shift().notnull()).cumsum())
            grp['ones'] = 1
            gap= int(self.t2_lineEdit_mcriterion.text())
            for i in self.new_df:
                mask[self.current_title] = (grp.groupby(self.current_title)['ones'].transform('count') < gap) | self.new_df[self.current_title].notnull()

            self.new_df[self.current_title] = self.new_df.interpolate(self.interpol_dict[self.t2_comboBox_interpolation.currentText()])[mask]
            missing_col=pd.DataFrame()
            missing_col=self.new_df
            self.missing(missing_col)

    def normalize(self):

        if self.t2_checkBox_norm_mean.isChecked():
            self.new_df[self.current_title]= (self.new_df[self.current_title]-self.new_df[self.current_title].mean())/self.new_df[self.current_title].std()

        elif self.t2_checkBox_norm_minmax.isChecked():
            self.new_df[self.current_title]=(self.new_df[self.current_title]-self.new_df[self.current_title].min())/(self.new_df[self.current_title].max()-self.new_df[self.current_title].min())
            


    def missing(self,missing_col):
            length_data=len(missing_col)
            missing=(np.count_nonzero(missing_col.isnull()))
            self.percent_missing = (missing/length_data)*100
            self.t2_lineEdit_missing_percent.setText(str(round(self.percent_missing, 1)) + "% missing")

    def call_plots(self):
        self.plot_1()
        self.plot_2()
        self.plot_3()
        

    def plot_1(self):
        a=self.raw_df
        a=pd.to_numeric(a,errors='coerce')
        data_1=a
        # create an axis
        self.ax1 = self.figure1.add_subplot(1,1,1)
        # discards the old graph
        self.ax1.clear()
        self.ax1.set_xlim(0,len(data_1))
        # plot data
        if self.t2_comboBox_diagram_selection.currentIndex()==0:
            self.ax1.plot(data_1,color='C0',alpha=0.5)
        elif self.t2_comboBox_diagram_selection.currentIndex()==1:
            self.ax1.plot(data_1,'ro',markersize=1,color='C0',alpha=0.5, linewidth=1.0)

        # refresh canvas
        self.figure1.tight_layout()
        self.canvas1.draw()
        

    def plot_2(self):
        data_2=self.new_df
        # create an axis
        self.ax2 = self.figure2.add_subplot(1,1,1)
        # discards the old graph
        self.ax2.clear()
        self.ax2.set_xlim(0,len(data_2)) 
        # plot data
        if self.t2_comboBox_diagram_selection.currentIndex()==0:
            self.ax2.plot(data_2,color='C0',alpha=0.5)
        elif self.t2_comboBox_diagram_selection.currentIndex()==1:
            self.ax2.plot(data_2,'ro',markersize=1,color='C0',alpha=0.5, linewidth=1.0)          
        # refresh canvas
        self.figure2.tight_layout()
        self.canvas2.draw()  
        
    def plot_3(self):
        f=int(self.t2_lineEdit_bins.text())
        b=self.new_df[self.current_title]


        b=pd.to_numeric(b,errors='coerce')
        b=b.dropna()
        self.ax3= self.figure3.add_subplot(1,1,1)
        self.ax3.clear()
        if self.t2_radioButton_histo.isChecked():
            #n, self.bins, patches = self.ax3.hist(b,bins=f)
            n, self.bins, patches = self.ax3.hist(b,bins=f)
            
        elif self.t2_radioButton_cumcurve.isChecked():
            n, self.bins, patches = self.ax3.hist(b,bins=f, histtype='step',cumulative=True,label='Empirical')
        
        self.ax3.clear()
        self.binlist=[]

        q= np.var(self.bins)
        #print("variance"+str(q))
        if q>1:
            dec='%.1f'
        elif q>0.1:
            dec='%.2f'
        else:
            dec='%.4f'

        

        self.bins= [ dec % elem for elem in self.bins ]

        for i in range(len(self.bins)-1):
            a=str(self.bins[i])
            b=str(self.bins[i+1])
            stringbin = a + " -< " + b
            self.binlist.append(stringbin)

        x=self.binlist
        y=n
        y_pos = np.arange(1,f+1)
        performance = y
        plt.bar(y_pos, performance, align='edge', alpha=0.5)
               
        self.ax3.set_xlim(0, f)
        start, end = self.ax3.get_xlim()
        stepsize= (end-start)/f
        self.ax3.xaxis.set_ticks(np.arange(start, end, stepsize))
        self.ax3.set_xticklabels(self.binlist,rotation=70,fontsize=9)
        self.span=SpanSelector(self.ax3,self.onselect, 'horizontal', useblit=True,rectprops=dict(alpha=0.5, facecolor='red'))
        self.figure3.tight_layout()
        self.canvas3.draw()

    def onselect(self,xmin, xmax):
        #print(xmin,xmax)
    
        binmax=float(len(self.binlist))
        print(binmax)
        l=round(float(xmin),0)
        u=round(float(xmax),0)

        #print(l)
        #print(u)

        l=int(l)
        
        u=int(u)
        
        if l < 0:
            l=0

        if u > binmax:
            
            u=binmax

        #print(self.bins)
        self.l=self.bins[l]
        self.u=self.bins[u]

        #print(self.l,self.u)

        ar=pd.DataFrame()

        if self.t2_checkBox_norm_mean.isChecked():
            ar=self.raw_df.dropna()
            ar= (ar-ar.mean())/ar.std()

        elif self.t2_checkBox_norm_minmax.isChecked():
            ar=self.raw_df.dropna()
            ar=(ar-ar.min())/(ar.max()-ar.min())
        else:
            ar=self.raw_df.dropna()
               
        ar=ar.dropna()
        #ar=np.array(self.raw_df.dropna())

        self.lp=round(stats.percentileofscore(ar, float(self.l)),2)
        self.up=round(stats.percentileofscore(ar, float(self.u)),2)
        self.lpercentile=str(self.lp)
        self.upercentile=str(self.up)
        #print(self.lpercentile,self.upercentile)
        self.t2_lineEdit_lpercentile.setText(self.lpercentile)
        self.t2_lineEdit_upercentile.setText(self.upercentile)
        self.change_dict()

        self.update_routine()     

    def load_data(self):
        self.raw_df = pd.read_csv(self.fname, usecols=[self.current_title],low_memory=False)
        self.raw_df = pd.to_numeric(self.raw_df[self.current_title], errors='coerce')
        self.raw_df = self.raw_df.replace(' ', '?')
        
        self.raw_df = self.raw_df.replace('?', np.NaN)
        self.new_df = pd.DataFrame()
        self.new_df[self.current_title] = self.raw_df

    def initialize_dict(self):

        path= os.path.dirname(self.fname)
        file=os.path.basename(self.fname)
        self.my_dict={}
        file=file.split('.')[0]
        #new_dict_path=path+"/dict_small"+file+'.pkl'
        new_dict_path=".\\dict_small.pkl"

        self.initial={"line_plot":int(1),
                      "interpolation":int(4),
                      "norm_mean":False,
                      "norm_minmax":False,
                      "gap_size":"500",
                      "histogram":True,
                      "cumcurve":False,
                      "num_bins":"50",
                      "lpercentile":"0",
                      "upercentile":"100",
                      "missing_percentiles":int(2),
                      "target_parameter":False,
                      "delete_parameter":False,
                      "outliertest":int(0),
                      "setlod":True,
                      "textlod":float(0)
                      }
        if not os.path.exists(new_dict_path):
            self.my_dict={}
            '''
            self.initial={"line_plot":int(1),
                          "interpolation":int(4),
                          "norm_mean":False,
                          "norm_minmax":False,
                          "gap_size":"500",
                          "histogram":True,
                          "cumcurve":False,
                          "num_bins":"50",
                          "lpercentile":"0",
                          "upercentile":"100",
                          "missing_percentiles":int(2),
                          "target_parameter":False,
                          "delete_parameter":False,
                          "outliertest":int(0),
                          "setlod":True,
                          "textlod":float(0)
                          }
            '''
            for value in self.header:
                self.my_dict[value] =self.initial
        else:
            with open(new_dict_path, 'rb') as handle:
                self.initial={"line_plot":int(1),
                              "interpolation":int(4),
                              "norm_mean":False,
                              "norm_minmax":False,
                              "gap_size":"500",
                              "histogram":True,
                              "cumcurve":False,
                              "num_bins":"50",
                              "lpercentile":"0",
                              "upercentile":"100",
                              "missing_percentiles":int(2),
                              "target_parameter":False,
                              "delete_parameter":False,
                              "outliertest":int(0),
                              "setLlod":True,
                              "textlod":float(0)
                              }
                
                self.my_inter_dict= pickle.load(handle)

                for value in self.header:
                    if value in self.my_inter_dict:
                        self.my_dict[value]=self.my_inter_dict[value]
                    else:
                        self.my_dict[value] =self.initial



    def initialize_items(self):

        line_plot = self.my_dict[self.current_title]["line_plot"]
        interpolation = self.my_dict[self.current_title]["interpolation"]
        histogram = self.my_dict[self.current_title]["histogram"]
        cumcurve = self.my_dict[self.current_title]["cumcurve"]
        norm_mean=self.my_dict[self.current_title]["norm_mean"]
        norm_minmax=self.my_dict[self.current_title]["norm_minmax"]
        gap_size = self.my_dict[self.current_title]["gap_size"]
        histogram = self.my_dict[self.current_title]["histogram"]
        num_bins = self.my_dict[self.current_title]["num_bins"]
        lpercentile = self.my_dict[self.current_title]["lpercentile"]
        upercentile = self.my_dict[self.current_title]["upercentile"]
        missing_percentiles = self.my_dict[self.current_title]["missing_percentiles"]
        target_parameter = self.my_dict[self.current_title]["target_parameter"]
        delete_parameter = self.my_dict[self.current_title]["delete_parameter"]
        outliertest = self.my_dict[self.current_title]["outliertest"]
        setlod = self.my_dict[self.current_title]["setlod"]
        textlod = self.my_dict[self.current_title]["textlod"]

        self.t2_comboBox_diagram_selection.setCurrentIndex(line_plot)
        self.t2_comboBox_interpolation.setCurrentIndex(interpolation)
        self.t2_checkBox_norm_mean.setChecked(norm_mean)
        self.t2_checkBox_norm_minmax.setChecked(norm_minmax)
        self.t2_checkBox_target.setChecked(target_parameter)
        self.t2_checkBox_delete.setChecked(delete_parameter)
        self.t2_lineEdit_mcriterion.setText(gap_size)
        self.t2_radioButton_histo.setChecked(histogram)
        self.t2_radioButton_cumcurve.setChecked(cumcurve)
        self.t2_lineEdit_bins.setText(num_bins)
        self.t2_lineEdit_lpercentile.setText(lpercentile)
        self.t2_lineEdit_upercentile.setText(upercentile)
        self.t2_comboBox_repl_outliers.setCurrentIndex(missing_percentiles)
        self.t2_comboBox_outliertest.setCurrentIndex(outliertest)
        self.t2_checkBox_setlod.setChecked(setlod)
        self.t2_lineEdit_textlod.setText(str(textlod))

    def change_dict(self):
        interpolation = self.t2_comboBox_interpolation.currentIndex()
        line_plot= self.t2_comboBox_diagram_selection.currentIndex()
        norm_mean=self.t2_checkBox_norm_mean.isChecked()
        norm_minmax=self.t2_checkBox_norm_minmax.isChecked()
        target_parameter=self.t2_checkBox_target.isChecked()
        delete_parameter=self.t2_checkBox_target.isChecked()
        delete_parameter=self.t2_checkBox_delete.isChecked()
        gap_size=self.t2_lineEdit_mcriterion.text()
        histogram=self.t2_radioButton_histo.isChecked()
        cumcurve=self.t2_radioButton_cumcurve.isChecked()
        num_bins= self.t2_lineEdit_bins.text()
        lpercentile= self.t2_lineEdit_lpercentile.text()
        upercentile= self.t2_lineEdit_upercentile.text()
        missing_percentiles= self.t2_comboBox_repl_outliers.currentIndex()
        outliertest= self.t2_comboBox_outliertest.currentIndex()
        setlod = self.t2_checkBox_setlod.isChecked()
        textlod = self.t2_lineEdit_textlod.text()

        self.new_input={}        
        self.new_input={"line_plot":line_plot,
                        "norm_mean":norm_mean,
                        "norm_minmax":norm_minmax,
                        "interpolation":interpolation,
                        "gap_size":gap_size,
                        "histogram":histogram,
                        "cumcurve":cumcurve,
                        "num_bins":num_bins,
                        "lpercentile":lpercentile,
                        "upercentile":upercentile,
                        "missing_percentiles":missing_percentiles,
                        "target_parameter":target_parameter,
                        "delete_parameter":delete_parameter,
                        "outliertest":outliertest,
                        "setlod":setlod,
                        "textlod":textlod
                        }                
        self.my_dict[self.current_title]=self.new_input

    def item_change(self):
        #save changes first to dictionary key
        self.change_dict()
        #call universal loader

    def prev_col(self):
        current_index= self.t2_comboBox_header_data.currentIndex()
        
        self.t2_comboBox_header_data.setCurrentIndex(current_index-1)
        self.change_col_update_routine()


    def next_col(self):
        current_index= self.t2_comboBox_header_data.currentIndex()
        self.t2_comboBox_header_data.setCurrentIndex(current_index+1)
        self.change_col_update_routine()

    def column_selection(self):
        self.load_data()

    def reset(self):
        self.my_dict[self.current_title]=self.initial
        self.initialize_items()
        self.change_dict()
        self.update_routine()
        

    def save_dict(self):
        path= os.path.dirname(self.fname)
        file=os.path.basename(self.fname)
        #print(path)
        file=file.split('.')[0]

        #print(file)
        #self.new_dict_path=path+"/dict_"+file+'.pkl'
        self.new_dict_path=path+".\\dict_small.pkl"

        #print(new_dict_path)
        
        with open(self.new_dict_path, 'wb') as f:
            pickle.dump(self.my_dict,f, pickle.HIGHEST_PROTOCOL)

        print("Dictionary Saved")

    def generate_dataframe(self):
        self.result = pd.read_csv(self.fname, usecols=['UNIX'],low_memory=False)
        

        for i in range(len(self.header)):
            self.t2_comboBox_header_data.setCurrentIndex(i)
            self.change_col_update_routine()
            
            if self.my_dict[self.current_title]["delete_parameter"]==False:
                print(self.current_title)
                left = self.result
                right = self.new_df
                self.result= left.join(right)


        #print(self.result)
        self.result.dropna(axis=1, how='all')
        s1=self.result.shape[0]
        s2=self.result.dropna(axis=0).shape[0]
        rows_missing=round(float((s2/s1)*100),2)
        self.t2_lineEdit_rem_rows.setText(str(rows_missing))

        if self.t2_checkBox_delete_missing.isChecked():
            self.result=self.result.dropna(axis=0)


    def save_page_csv(self):
        self.generate_dataframe()

        path= os.path.dirname(self.fname)
        file=os.path.basename(self.fname)
        file=file.split('.')[0]
        filename=path+"/prepro_"+file+'.csv'
        
        with open(filename, 'w') as f:
            self.result.to_csv(f, header=True, index=None)

    def generate_em_dataframe(self):
        self.result_em = pd.read_csv(self.fname, usecols=['UNIX'],low_memory=False)
        self.result_target = pd.read_csv(self.fname, usecols=['UNIX'],low_memory=False)        
        self.result_left = pd.read_csv(self.fname, usecols=['UNIX'],low_memory=False)
        self.result_em_total = pd.read_csv(self.fname, usecols=['UNIX'],low_memory=False)

        for i in range(len(self.header)):
            self.t2_comboBox_header_data.setCurrentIndex(i)
            self.change_col_update_routine()
            print(self.current_title)



            if self.my_dict[self.current_title]["delete_parameter"]==False and self.my_dict[self.current_title]["target_parameter"]==False:
                #print(self.my_dict[self.current_title]["delete_parameter"])
                left = self.result_em
                right = self.new_df
                self.result_em= left.join(right)                
           
            if self.my_dict[self.current_title]["target_parameter"]==True:
                #print(self.my_dict[self.current_title]["delete_parameter"])
                left = self.result_target
                right = self.new_df
                self.result_target= left.join(right)

            if self.my_dict[self.current_title]["delete_parameter"]==False:
                left = self.result_em_total
                right = self.new_df
                self.result_em_total= left.join(right)

        

        self.result_em_total.dropna(axis=1,how='all', inplace=True)
        self.result_em.dropna(axis=1,how='all', inplace=True)

 

    def save_result_em(self):

        path= os.path.dirname(self.fname)
        file=os.path.basename(self.fname)
        file=file.split('.')[0]
        base_file_str = path+"/em_total_"+file+'.csv'

        if not os.path.exists(base_file_str):           
            self.generate_em_dataframe()
            self.filename_em=path+"/em_support_"+file+'.csv'
            with open(self.filename_em, 'w') as f:
                self.result_em.to_csv(f, header=True, index=None)

            self.filename_target=path+"/targets_"+file+'.csv'
            with open(self.filename_target, 'w') as f:
                self.result_target.to_csv(f, header=True, index=None)

            self.filename_em_total=path+"/em_total_"+file+'.csv'
            with open(self.filename_em_total, 'w') as f:
                self.result_em.to_csv(f, header=True, index=None)

        else:
            self.result_left = pd.read_csv(path+"/em_total_"+file+'.csv', usecols=['UNIX'],low_memory=False)
            self.filename_em=path+"/em_support_"+file+'.csv'           
            self.filename_target=path+"/targets_"+file+'.csv'
            self.filename_em_total=path+"/em_total_"+file+'.csv'

            


    def em_imputation(self):
        #Generate Folder for Output
        self.save_dict()
        self.save_result_em()
        result_left = self.result_left
        file = os.path.basename(self.fname)
        file = file.split('.')[0]

        path_folder= os.path.dirname(self.filename_em)
        path_folder=path_folder+"/output_folder_"+file        
        pathlib.Path(path_folder).mkdir(parents=True, exist_ok=True)

        globbed_filesx = glob.glob(path_folder+"/"+"*.csv")
        current_num = len(globbed_filesx)
        if current_num > 1:
            k=current_num+1
        else:
            k=2

        self.result_left_string= path_folder+"/"+file+"_result_1"+'.csv'
        with open(self.result_left_string, 'w') as f:
            result_left.to_csv(f, header=True, index=None)
      
        
        print("Fourth_step: Load Data for Weka")
        #import weka.core.jvm as jvm
        #jvm.start(packages=True,max_heap_size="6144m")
        from weka.classifiers import Classifier
        from weka.core.converters import Loader, Saver
        from weka.filters import Filter
        from weka.attribute_selection import ASSearch, ASEvaluation, AttributeSelection
        import weka.core.converters as converters
        import weka.core.classes as cl  
        #print("Load operation")

        data = converters.load_any_file(self.filename_em)
        #Filter function
        print("Fifth_step: Filter operation")
        remove = Filter(classname="weka.filters.unsupervised.attribute.RemoveUseless", options=["-M", "99.0"])        
        remove.inputformat(data)
        filtered = remove.filter(data)

        path= os.path.dirname(self.fname)
        em_sup_path=path+"/em_support_"+file+"2"+'.csv'  
        saver = Saver(classname="weka.core.converters.CSVSaver")
        saver.save_file(filtered, em_sup_path)

        
        
        col_counts = len((list(pd.read_csv(em_sup_path,nrows=0))))
        print(col_counts)

        #For small Dataset:
        for i in range(k, col_counts, 1):       

            process_data=filtered
            print("Iteration : "+str(i))
            #set class on i
            classassign = Filter(classname="weka.filters.unsupervised.attribute.ClassAssigner", options=["-C", str(i)])
            classassign.inputformat(process_data)
            process_data = classassign.filter(process_data)
            search = ASSearch(classname="weka.attributeSelection.BestFirst", options=["-D", "1", "-N", "5"])
            evaluator = ASEvaluation(classname="weka.attributeSelection.CfsSubsetEval", options=["-P", "6", "-E", "6"])
            attsel = AttributeSelection()
            attsel.search(search)
            attsel.evaluator(evaluator)
            attsel.select_attributes(process_data)
            result_string = attsel.results_string        
            start = 'Selected attributes: '
            end = ' :'
            result = str(re.search('%s(.*)%s' % (start, end), result_string).group(1))+","+str(i)
            #print(result)

            remove = Filter(classname="weka.filters.unsupervised.attribute.Remove", options=["-V","-R",result])
            remove.inputformat(process_data)
            process_data = remove.filter(process_data)
            em = Filter(classname="weka.filters.unsupervised.attribute.EMImputation", options=["-N", "-1", "-E", "1.0E-4", "-Q", "1.0E-8"])
            em.inputformat(process_data)
            process_data = em.filter(process_data)
            #print(em_imputed)

            last = attsel.number_attributes_selected+1
            remove = Filter(classname="weka.filters.unsupervised.attribute.Remove", options=["-V","-R",str(last)])
            remove.inputformat(process_data)
            process_data = remove.filter(process_data)

            #Saver arff to csv
            path= os.path.dirname(self.fname)
            file=os.path.basename(self.fname)
            file=file.split('.')[0]
            
            filename_em_imputed_csv = path_folder+"/"+file+"_result_"+str(i)+'.csv'
            saver = Saver(classname="weka.core.converters.CSVSaver")
            saver.save_file(process_data, filename_em_imputed_csv)         

            del process_data


        #print("i is: "+str(i))
        i=1000
        if col_counts <= int(i):
            globbed_files = glob.glob(path_folder+"/"+"*.csv")
            result_left= pd.read_csv(globbed_files[0], header=0)
            print(globbed_files)
            for i in globbed_files[1:]:
                new_right=pd.read_csv(i, header=0)
                result_left= result_left.join(new_right)       
            path= os.path.dirname(self.fname)
            file=os.path.basename(self.fname)
            file=file.split('.')[0]

            filename=path_folder+"/result_EM_"+file+'.csv'

            with open(filename, 'w') as f:
                result_left.to_csv(f, header=True, index=None)


            ## Merging attributes and Target

            left = pd.read_csv(filename,low_memory=False)
            right = pd.read_csv(self.filename_target,low_memory=False)

            for i in right:
                if i != "UNIX":
                    new=right[['UNIX',i]]
                    print(new)
                    result_final = pd.merge(left, new, how='left', on=['UNIX'])
                    filename=path_folder+"/result_final_"+file+"_"+i+'.csv'
                    with open(filename, 'w') as f:
                        result_final.to_csv(f, header=True, index=None)        

                    del result_final
                    result_final = converters.load_any_file(filename)
                    filename_em_imputed_arff = path_folder+"/result_final_"+file+"_"+i+'.arff'
                    saver = Saver(classname="weka.core.converters.ArffSaver")
                    saver.save_file(result_final, filename_em_imputed_arff)
        
            print("Seventh_step: Save Files")
            #jvm.stop()
            print("EM-Impuation finished")

        jvm.stop()


####################################################################################################################
#Tab3###############################################################################################################
        
    def discretize(self):
        from weka.core.converters import Loader, Saver
        from weka.filters import Filter
        import weka.core.converters as converters

        #disc_num = self.lineEdit_discnum.text()
        self.disc_fname_list = QtGui.QFileDialog.getOpenFileNames(self, 'Open file','.\\',"*csv")
        file_d= os.path.dirname(self.disc_fname_list[0])
        bin_list = list((self.t3_lineEdit_bins.text().split(',')))
        
        sort=1

        print(bin_list)

        for disc_num in bin_list:

            if sort == "s":

                if not os.path.exists(file_d+"/output_dicretized"+"_sorted"):
                    path_folder=file_d+"/output_dicretize"+"_sorted"
                    pathlib.Path(path_folder).mkdir(parents=True, exist_ok=True)
                
                    for self.disc_fname in self.disc_fname_list:
                        print(self.disc_fname)
                        file=os.path.basename(self.disc_fname)
                        file=file.split('.')[0]    
                        df = pd.read_csv(self.disc_fname,low_memory=False)
                        print(df)
                        print(df.columns[-1])
                        df.sort_values(df.columns[-1], axis=0, ascending=True,na_position='last', inplace=True)
                        print(df)
                        filename_disc= path_folder+"/"+file+'_sorted.csv'

                        with open(filename_disc, 'w') as f:
                            df.to_csv(f, header=True, index=None)

                    globbed_files = glob.glob(path_folder+"/"+"*.csv")

            else:
                path_folder=file_d+"/output_dicretized_non_sorted"
                pathlib.Path(path_folder).mkdir(parents=True, exist_ok=True)                
                globbed_files = self.disc_fname_list
            
            #for self.disc_fname in self.disc_fname_list:
            for self.disc_fname in globbed_files:
                saver_arff = Saver(classname="weka.core.converters.ArffSaver")
                saver_csv = Saver(classname="weka.core.converters.CSVSaver")


                file=os.path.basename(self.disc_fname)
                file=file.split('.')[0]      
                pathlib.Path(path_folder).mkdir(parents=True, exist_ok=True)
                print("Discretize")
                data_final = converters.load_any_file(self.disc_fname)
                #disc_num = self.lineEdit_discnum.text()

                #Remove UNIX timestamp
                remove = Filter(classname="weka.filters.unsupervised.attribute.Remove", options=["-R", "first"])
                remove.inputformat(data_final)
                data_final = remove.filter(data_final)
                
                disc = Filter(classname="weka.filters.unsupervised.attribute.Discretize", options=["-B", str(disc_num), "-M", "-1.0", "-R", "first-last", "-unset-class-temporarily"])
                disc.inputformat(data_final)
                disc_data = disc.filter(data_final)

                filename_disc_eqdist = path_folder+"/files_disc_"+str(disc_num)+"/"+file+"_dis_eqdis_"+str(disc_num)+'.csv'
                filename_disc_eqdist_arff = path_folder+"/files_disc_"+str(disc_num)+"/"+file+"_dis_eqdis_"+str(disc_num)+'.arff'

                
                saver_csv.save_file(disc_data, filename_disc_eqdist)
                saver_arff.save_file(disc_data, filename_disc_eqdist_arff)
                del disc_data

                

                disc2 = Filter(classname="weka.filters.unsupervised.attribute.Discretize", options=["-F","-B", str(disc_num), "-M", "-1.0", "-R", "first-last", "-unset-class-temporarily"])
                disc2.inputformat(data_final)
                disc_data2 = disc2.filter(data_final)
                filename_disc_eqfreq= path_folder+"/files_disc_"+str(disc_num)+"/"+file+"_dis_eqfreq_"+str(disc_num)+'.csv'
                filename_disc_eqfreq_arff= path_folder+"/files_disc_"+str(disc_num)+"/"+file+"_dis_eqfreq_"+str(disc_num)+'.arff'
                saver_csv.save_file(disc_data2, filename_disc_eqfreq)
                saver_arff.save_file(disc_data2, filename_disc_eqfreq_arff)
                del disc_data2

                '''
                disc3 = Filter(classname="weka.filters.unsupervised.attribute.Discretize", options=["-F","-B", str(disc_num), "-M", "-1.0", "-R", "last", "-unset-class-temporarily"])
                disc3.inputformat(data_final)
                disc_data3 = disc3.filter(data_final)

                filename_conti_eqfreq= path_folder+"/files_disc_"+str(disc_num)+"/"+file+"_dis_eqfreq_conti_"+str(disc_num)+'.csv'
                filename_conti_eqfreq_arff= path_folder+"/files_disc_"+str(disc_num)+"/"+file+"_dis_eqfreq_conti_"+str(disc_num)+'.arff'

                saver_csv.save_file(disc_data3, filename_conti_eqfreq)
                saver_arff.save_file(disc_data3, filename_conti_eqfreq_arff)
                del disc_data3

                disc4 = Filter(classname="weka.filters.unsupervised.attribute.Discretize", options=["-B", str(disc_num), "-M", "-1.0", "-R", "last", "-unset-class-temporarily"])
                disc4.inputformat(data_final)
                disc_data4 = disc4.filter(data_final)

                filename_conti_eqdist = path_folder+"/files_disc_"+str(disc_num)+"/"+file+"_dis_eqdis_conti_"+str(disc_num)+'.csv'
                filename_conti_eqdist_arff = path_folder+"/files_disc_"+str(disc_num)+"/"+file+"_dis_eqdis_conti_"+str(disc_num)+'.arff'
                
                saver_csv.save_file(disc_data4, filename_conti_eqdist)
                saver_arff.save_file(disc_data4, filename_conti_eqdist_arff)
                del disc_data4


                ####Conti Discretisation including normalization####

                disc31 = Filter(classname="weka.filters.unsupervised.attribute.Normalize", options=["-S","1.0","-T","0.0"])
                disc31.inputformat(data_final)
                disc_data31 = disc31.filter(data_final)
                
                disc31 = Filter(classname="weka.filters.unsupervised.attribute.Discretize", options=["-F","-B", str(disc_num), "-M", "-1.0", "-R", "last", "-unset-class-temporarily"])
                disc31.inputformat(disc_data31)
                disc_data31 = disc31.filter(disc_data31)

                filename_norm_conti_eqfreq= path_folder+"/files_disc_"+str(disc_num)+"/"+file+"_dis_eqfreq_conti_norm_"+str(disc_num)+'.csv'
                filename_norm_conti_eqfreq_arff= path_folder+"/files_disc_"+str(disc_num)+"/"+file+"_dis_eqfreq_conti_norm_"+str(disc_num)+'.arff'

                saver_csv.save_file(disc_data31, filename_norm_conti_eqfreq)
                saver_arff.save_file(disc_data31, filename_norm_conti_eqfreq_arff)
                del disc_data31

                disc41 = Filter(classname="weka.filters.unsupervised.attribute.Normalize", options=["-S","1.0","-T","0.0"])
                disc41.inputformat(data_final)
                disc_data41 = disc41.filter(data_final)              
                disc41 = Filter(classname="weka.filters.unsupervised.attribute.Discretize", options=["-B", str(disc_num), "-M", "-1.0", "-R", "last", "-unset-class-temporarily"])
                disc41.inputformat(disc_data41)
                disc_data41 = disc41.filter(disc_data41)
                filename_norm_conti_eqdist = path_folder+"/files_disc_"+str(disc_num)+"/"+file+"_dis_eqdis_conti_norm_"+str(disc_num)+'.csv'
                filename_norm_conti_eqdist_arff = path_folder+"/files_disc_"+str(disc_num)+"/"+file+"_dis_eqdis_conti_norm_"+str(disc_num)+'arff'
                saver_csv.save_file(disc_data41, filename_norm_conti_eqdist)
                saver_arff.save_file(disc_data41, filename_norm_conti_eqdist_arff)
                del disc_data41
                '''






        print("Discretizing finished")
        jvm.stop()


    def xml_generator(self):
        from weka.core.converters import Loader, Saver
        from weka.filters import Filter
        import weka.core.converters as converters
        import arff
        import fileinput
        import sys,re,glob,csv,pickle,os,time,pandas as pd,numpy as np,scipy.stats as stats,matplotlib.pyplot as plt,matplotlib.mlab as mlab,matplotlib.pylab as pylab
        import pandas as pd
        from pandas import read_csv
        import matplotlib.pyplot as plt
        from adjustText import adjust_text
        import numpy as np
        import tempfile
        import traceback
        import weka.core.converters as converters
        from weka.filters import Filter
        from weka.attribute_selection import ASEvaluation, ASSearch
        from weka.classifiers import Classifier, FilteredClassifier, NumericPrediction
        from weka.classifiers import Evaluation
        import weka.core.classes
        from weka.core.classes import split_options as split, join_options as join, Random

        #disc_num = self.lineEdit_discnum.text()
        globbed_files = QtGui.QFileDialog.getOpenFileNames(self, 'Open file','.\\',"*arff")
        #binnum = self.t3_lineEdit_discnum.text()
        binnum = 5        

        #for self.disc_fname in self.disc_fname_list:
        print("XML_Pre-Processing")        
        for arr_file_path in globbed_files:

            '''
            # Data preparation



            arr=[]
            arff_file = open(arr_file_path)

            for line in arff_file:
                    if (line.startswith("@")):
                            arr.append(line)
                            
            start = '{'
            end = '}'

            dict_att={}
            

            for parameter in arr[2:-2]:
                    print("Parameter_Input")
                    print(parameter)
                    class_state_string = re.search('%s(.*)%s' % (start, end), parameter).group(1)
                    d={}
                    d_new={}
                    class_list=class_state_string.split(",")
                    counter=-1
                    for i in class_list:
                            counter=counter+1
                            d[counter]=i
                            d_new[counter]=i
                    for key,item in d.items():
                            if '-inf-' in item:
                                    d[key]=float(-99999999999)
                            elif '-inf' in item:
                                    d[key]=float(9999999999)
                            else:
                                    state_level_string= item.replace("inf-","")
                                    state_level_string= state_level_string.replace("\\'","")
                                    state_level_string= state_level_string.replace("]","")
                                    state_level_string= state_level_string.replace("(","")
                                    state_level_string= state_level_string.replace(")","")
                                    state_level_string= state_level_string.replace("'","")
                                    d[key]=state_level_string


                                    if "-" in item:
                                            sls=state_level_string.split("-")[0]
                                            if sls.isdigit():
                                                    d[key]=float(state_level_string.split("-")[1])
                                            else:
                                                    if sls=="":
                                                            d[key]=float(float(state_level_string.split("-")[1])*-1)
                                                    else:
                                                            print("ELSE2 part"+str(sls))
                                                            d[key]=float(sls)
                    i=0
                    d_new2={}
                    result_list=[]
                    for i in range(len(d)):
                            x=d_new[sorted(d.items(), key=lambda x: x[1])[i][0]]
                            i=i+1
                            result_list.append(x)
                    print(result_list)
                    result_list=str(result_list).replace('\"','')
                    
                    result_list=str(result_list).replace('\'\\\\\'','\'\\\'')
                    result_list=str(result_list).replace('\\\\\'\'','\\\'\'')
                    result_list=str(result_list).replace('[','')
                    result_list=str(result_list).replace(')\\\'\']',')\\\'\'')
                    print(result_list)
                    return_str = parameter.replace(re.search('%s(.*)%s' % (start, end), parameter).group(1),result_list)
                    if len(parameter.split(","))!= 5:
                            dict_att[parameter]=parameter
                    else:
                            dict_att[parameter]=return_str
                    print(return_str)
            with open(arr_file_path, 'r') as f:
                lines = f.readlines()
            with open(arr_file_path, 'w') as f:
                for line in lines:
                    if (line.startswith("@")):
                            if line in dict_att:
                                    line = line.replace(line,dict_att[line])
                                    print("Corrected_Data")
                                    sys.stdout.write(line)
                    f.write(line)
            f.close()

            '''

            print("XML_Generator")
            #XML Generator
            
            data = converters.load_any_file(arr_file_path)
            data.class_is_last()

            #tan = Classifier(classname="weka.classifiers.bayes.BayesNet", options=[])
            tan = Classifier(classname="weka.classifiers.bayes.BayesNet", options=["-D","-Q","weka.classifiers.bayes.net.search.local.TAN","--","-S","BAYES","-E","weka.classifiers.bayes.net.estimate.SimpleEstimator","--","-A","0.5"])
            #tan = Classifier(classname="weka.classifiers.trees.J48", options=[])

            #### Section to define Meta Classifier ####    
            as_eval = ASEvaluation(classname="weka.attributeSelection.CfsSubsetEval", options=["P","4","E","4"])
            as_search = ASSearch(classname="weka.attributeSelection.BestFirst", options=[])
            as_filter = Filter(classname="weka.filters.supervised.attribute.AttributeSelection",options=["-E", as_eval.to_commandline(), "-S", as_search.to_commandline()])
            #as_filter.inputformat(data)
            fc = FilteredClassifier()
            fc.filter = as_filter
            fc.classifier = tan
            print(fc.to_commandline())
            fc.build_classifier(data)
            result=fc.graph

            file_name_xml= os.path.dirname(arr_file_path)+"\\"+ os.path.basename(arr_file_path).split(".")[0] + ".xml"
            with open(file_name_xml,'w') as f:
                f.write(result)

            with open(file_name_xml, 'r') as f:
                lines = f.readlines()

            with open(file_name_xml, 'w') as f:
                for line in lines:
                    line = line.replace('\&apos;&apos;', '')
                    line = line.replace('&apos;\&apos;', '')

                    f.write(line)


            #evaluation = Evaluation(data)
            #evaluation.crossvalidate_model(fc,data,10,Random(1))
            #print("pctCorrect:"+ str(evaluation.percent_correct))
            #print(evaluation.class_details())            




        print("XML_finished")
        
####################################################################################################################
#Tab4###############################################################################################################

        

####################################################################################################################
#End################################################################################################################
if __name__ == "__main__":
    #import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = ApplicationWindow()
    ui.setupUi(Form)
    #ui.__init__(Form)
    Form.show()
    sys.exit(app.exec_())
    jvm.stop()



