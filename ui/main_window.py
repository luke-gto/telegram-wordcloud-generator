# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(859, 772)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(859, 772))
        MainWindow.setMaximumSize(QtCore.QSize(859, 772))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_json = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_json.setGeometry(QtCore.QRect(20, 20, 331, 32))
        self.pushButton_json.setObjectName("pushButton_json")
        self.label_json = QtWidgets.QLabel(self.centralwidget)
        self.label_json.setGeometry(QtCore.QRect(20, 60, 501, 21))
        self.label_json.setText("")
        self.label_json.setObjectName("label_json")
        self.pushButton_stopwords = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stopwords.setGeometry(QtCore.QRect(20, 100, 331, 32))
        self.pushButton_stopwords.setObjectName("pushButton_stopwords")
        self.label_stopwords = QtWidgets.QLabel(self.centralwidget)
        self.label_stopwords.setGeometry(QtCore.QRect(20, 140, 511, 21))
        self.label_stopwords.setText("")
        self.label_stopwords.setObjectName("label_stopwords")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 200, 821, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_font = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_font.setGeometry(QtCore.QRect(600, 250, 131, 32))
        self.pushButton_font.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.pushButton_font.setToolTip("")
        self.pushButton_font.setWhatsThis("")
        self.pushButton_font.setAccessibleDescription("")
        self.pushButton_font.setObjectName("pushButton_font")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 240, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 270, 51, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 270, 51, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.spinBox_height = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_height.setGeometry(QtCore.QRect(20, 290, 91, 30))
        self.spinBox_height.setMaximum(10000)
        self.spinBox_height.setSingleStep(100)
        self.spinBox_height.setProperty("value", 200)
        self.spinBox_height.setObjectName("spinBox_height")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(590, 430, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.doubleSpinBox_horizontal = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_horizontal.setGeometry(QtCore.QRect(630, 460, 70, 30))
        self.doubleSpinBox_horizontal.setSingleStep(0.25)
        self.doubleSpinBox_horizontal.setObjectName("doubleSpinBox_horizontal")
        self.spinBox_contour = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_contour.setGeometry(QtCore.QRect(700, 580, 70, 30))
        self.spinBox_contour.setObjectName("spinBox_contour")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(660, 560, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(520, 560, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.lineEdit_cont_color = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cont_color.setGeometry(QtCore.QRect(540, 580, 113, 30))
        self.lineEdit_cont_color.setText("")
        self.lineEdit_cont_color.setObjectName("lineEdit_cont_color")
        self.doubleSpinBox_scale = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_scale.setGeometry(QtCore.QRect(160, 460, 70, 30))
        self.doubleSpinBox_scale.setSingleStep(0.25)
        self.doubleSpinBox_scale.setObjectName("doubleSpinBox_scale")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(120, 430, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(250, 340, 91, 20))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.spinBox_font_step = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_font_step.setGeometry(QtCore.QRect(270, 370, 52, 30))
        self.spinBox_font_step.setProperty("value", 1)
        self.spinBox_font_step.setObjectName("spinBox_font_step")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(140, 340, 81, 20))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.spinBox_min_font = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_min_font.setGeometry(QtCore.QRect(150, 370, 52, 30))
        self.spinBox_min_font.setProperty("value", 4)
        self.spinBox_min_font.setObjectName("spinBox_min_font")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(370, 340, 81, 20))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.spinBox_max_font = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_max_font.setGeometry(QtCore.QRect(380, 370, 52, 30))
        self.spinBox_max_font.setObjectName("spinBox_max_font")
        self.spinBox_max_words = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_max_words.setGeometry(QtCore.QRect(510, 370, 52, 30))
        self.spinBox_max_words.setSingleStep(10)
        self.spinBox_max_words.setObjectName("spinBox_max_words")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(470, 340, 131, 20))
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(260, 430, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.lineEdit_back_color = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_back_color.setGeometry(QtCore.QRect(260, 460, 121, 30))
        self.lineEdit_back_color.setText("")
        self.lineEdit_back_color.setObjectName("lineEdit_back_color")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(440, 430, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.lineEdit_color_mode = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_color_mode.setGeometry(QtCore.QRect(440, 460, 121, 30))
        self.lineEdit_color_mode.setObjectName("lineEdit_color_mode")
        self.doubleSpinBox_relative_scale = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_relative_scale.setGeometry(QtCore.QRect(240, 590, 70, 30))
        self.doubleSpinBox_relative_scale.setSingleStep(0.25)
        self.doubleSpinBox_relative_scale.setProperty("value", 0.5)
        self.doubleSpinBox_relative_scale.setObjectName("doubleSpinBox_relative_scale")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(200, 560, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(230, 240, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.checkBox_repeat = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_repeat.setGeometry(QtCore.QRect(270, 270, 21, 20))
        self.checkBox_repeat.setText("")
        self.checkBox_repeat.setObjectName("checkBox_repeat")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(380, 240, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.checkBox_num = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_num.setGeometry(QtCore.QRect(450, 270, 21, 20))
        self.checkBox_num.setText("")
        self.checkBox_num.setObjectName("checkBox_num")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(620, 340, 131, 20))
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.spinBox_min_word_length = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_min_word_length.setGeometry(QtCore.QRect(660, 370, 52, 30))
        self.spinBox_min_word_length.setObjectName("spinBox_min_word_length")
        self.spinBox_collocation = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_collocation.setGeometry(QtCore.QRect(80, 590, 52, 30))
        self.spinBox_collocation.setProperty("value", 30)
        self.spinBox_collocation.setObjectName("spinBox_collocation")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(40, 560, 131, 20))
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(10, 530, 351, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_20.setAutoFillBackground(False)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(480, 530, 351, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_21.setAutoFillBackground(False)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(320, 650, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(580, 0, 251, 201))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_map = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_map.setCheckable(True)
        self.pushButton_map.setAutoExclusive(False)
        self.pushButton_map.setObjectName("pushButton_map")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.pushButton_map)
        self.verticalLayout.addWidget(self.pushButton_map)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.buttonGroup.addButton(self.pushButton_2)
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_textonly = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_textonly.setCheckable(True)
        self.pushButton_textonly.setObjectName("pushButton_textonly")
        self.buttonGroup.addButton(self.pushButton_textonly)
        self.verticalLayout.addWidget(self.pushButton_textonly)
        self.spinBox_width = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_width.setGeometry(QtCore.QRect(120, 290, 91, 30))
        self.spinBox_width.setMaximum(10000)
        self.spinBox_width.setSingleStep(100)
        self.spinBox_width.setProperty("value", 400)
        self.spinBox_width.setObjectName("spinBox_width")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 859, 28))
        self.menubar.setObjectName("menubar")
        self.menuGuide = QtWidgets.QMenu(self.menubar)
        self.menuGuide.setObjectName("menuGuide")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuGuide.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton_textonly.toggled['bool'].connect(self.lineEdit_cont_color.setDisabled) # type: ignore
        self.pushButton_textonly.toggled['bool'].connect(self.spinBox_contour.setDisabled) # type: ignore
        self.pushButton_map.toggled['bool'].connect(self.spinBox_height.setDisabled) # type: ignore
        self.pushButton_map.toggled['bool'].connect(self.spinBox_width.setDisabled) # type: ignore
        self.pushButton_map.toggled['bool'].connect(self.checkBox_repeat.setDisabled) # type: ignore
        self.pushButton_map.toggled['bool'].connect(self.checkBox_num.setDisabled) # type: ignore
        self.pushButton_map.toggled['bool'].connect(self.pushButton_font.setDisabled) # type: ignore
        self.pushButton_map.toggled['bool'].connect(self.spinBox_min_font.setDisabled) # type: ignore
        self.pushButton_map.toggled['bool'].connect(self.spinBox_font_step.setDisabled) # type: ignore
        self.pushButton_map.toggled['bool'].connect(self.spinBox_max_font.setDisabled) # type: ignore
        self.pushButton_map.toggled['bool'].connect(self.spinBox_max_words.setDisabled) # type: ignore
        self.pushButton_map.toggled['bool'].connect(self.spinBox_min_word_length.setDisabled) # type: ignore
        self.pushButton_map.toggled['bool'].connect(self.doubleSpinBox_scale.setDisabled) # type: ignore
        self.pushButton_map.toggled['bool'].connect(self.lineEdit_back_color.setDisabled) # type: ignore
        self.pushButton_map.toggled['bool'].connect(self.lineEdit_color_mode.setDisabled) # type: ignore
        self.pushButton_map.toggled['bool'].connect(self.doubleSpinBox_horizontal.setDisabled) # type: ignore
        self.pushButton_map.toggled['bool'].connect(self.spinBox_collocation.setDisabled) # type: ignore
        self.pushButton_map.toggled['bool'].connect(self.doubleSpinBox_relative_scale.setDisabled) # type: ignore
        self.pushButton_map.toggled['bool'].connect(self.lineEdit_cont_color.setDisabled) # type: ignore
        self.pushButton_map.toggled['bool'].connect(self.spinBox_contour.setDisabled) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Telegram chat word cloud generator"))
        self.pushButton_json.setText(_translate("MainWindow", "Select a Telegram chat JSON file backup"))
        self.pushButton_stopwords.setText(_translate("MainWindow", "Select the stopwords list file"))
        self.label.setText(_translate("MainWindow", "Wordcloud options"))
        self.pushButton_font.setStatusTip(_translate("MainWindow", "Choose a custom font (OTF or TTF files only)."))
        self.pushButton_font.setText(_translate("MainWindow", "Custom font path"))
        self.label_2.setText(_translate("MainWindow", "Canvas dimensions"))
        self.label_3.setText(_translate("MainWindow", "Height"))
        self.label_4.setText(_translate("MainWindow", "Width"))
        self.spinBox_height.setSuffix(_translate("MainWindow", "px"))
        self.label_5.setText(_translate("MainWindow", "Prefer horizontal"))
        self.doubleSpinBox_horizontal.setToolTip(_translate("MainWindow", "The ratio of times to try horizontal fitting as opposed to vertical."))
        self.doubleSpinBox_horizontal.setStatusTip(_translate("MainWindow", "The ratio of times to try horizontal fitting as opposed to vertical."))
        self.spinBox_contour.setToolTip(_translate("MainWindow", "The ratio of times to try horizontal fitting as opposed to vertical."))
        self.spinBox_contour.setStatusTip(_translate("MainWindow", "The ratio of times to try horizontal fitting as opposed to vertical."))
        self.label_6.setText(_translate("MainWindow", "Contour width"))
        self.label_7.setText(_translate("MainWindow", "Mask contour color"))
        self.lineEdit_cont_color.setStatusTip(_translate("MainWindow", "Mask contour color"))
        self.doubleSpinBox_scale.setToolTip(_translate("MainWindow", "The ratio of times to try horizontal fitting as opposed to vertical."))
        self.doubleSpinBox_scale.setStatusTip(_translate("MainWindow", "Scaling between computation and drawing."))
        self.label_8.setText(_translate("MainWindow", "Scale"))
        self.label_10.setText(_translate("MainWindow", "Font step"))
        self.spinBox_font_step.setStatusTip(_translate("MainWindow", "Step size for the font."))
        self.label_12.setText(_translate("MainWindow", "Min font size"))
        self.spinBox_min_font.setStatusTip(_translate("MainWindow", "Smallest font size to use."))
        self.label_11.setText(_translate("MainWindow", "Max font size"))
        self.spinBox_max_font.setStatusTip(_translate("MainWindow", "Maximum font size for the largest word."))
        self.spinBox_max_words.setStatusTip(_translate("MainWindow", "The maximum number of words"))
        self.label_13.setText(_translate("MainWindow", "Max words number"))
        self.label_9.setText(_translate("MainWindow", "Background color"))
        self.lineEdit_back_color.setStatusTip(_translate("MainWindow", "Background color for the word cloud image."))
        self.label_14.setStatusTip(_translate("MainWindow", "Transparent background will be generated when mode is \"RGBA\" and background_color is None."))
        self.label_14.setText(_translate("MainWindow", "Color mode"))
        self.lineEdit_color_mode.setStatusTip(_translate("MainWindow", "Transparent background will be generated when mode is \"RGBA\" and background_color is None."))
        self.lineEdit_color_mode.setText(_translate("MainWindow", "RGB"))
        self.doubleSpinBox_relative_scale.setToolTip(_translate("MainWindow", "The ratio of times to try horizontal fitting as opposed to vertical."))
        self.doubleSpinBox_relative_scale.setStatusTip(_translate("MainWindow", "Scaling between computation and drawing."))
        self.label_15.setText(_translate("MainWindow", "Relative scaling"))
        self.label_16.setText(_translate("MainWindow", "Repeat words"))
        self.checkBox_repeat.setStatusTip(_translate("MainWindow", "Whether to repeat words and phrases until max words or min font size is reached."))
        self.label_17.setText(_translate("MainWindow", "Include numbers"))
        self.checkBox_num.setStatusTip(_translate("MainWindow", "Whether to repeat words and phrases until max words or min font size is reached."))
        self.label_18.setText(_translate("MainWindow", "Min word length"))
        self.spinBox_min_word_length.setStatusTip(_translate("MainWindow", "Minimum number of letters a word must have to be included."))
        self.spinBox_collocation.setStatusTip(_translate("MainWindow", "Bigrams must have a Dunning likelihood collocation score greater than this parameter to be counted as bigrams."))
        self.label_19.setText(_translate("MainWindow", "Collocation threshold"))
        self.label_20.setText(_translate("MainWindow", "Read the docs before messing with this stuff"))
        self.label_21.setText(_translate("MainWindow", "Only for word clouds with masks:"))
        self.pushButton_start.setText(_translate("MainWindow", "START"))
        self.pushButton_map.setText(_translate("MainWindow", "Text processing only"))
        self.pushButton_2.setText(_translate("MainWindow", "Word cloud with map"))
        self.pushButton_textonly.setText(_translate("MainWindow", "Standard word cloud"))
        self.spinBox_width.setSuffix(_translate("MainWindow", "px"))
        self.menuGuide.setTitle(_translate("MainWindow", "Guide"))
        self.menuExit.setTitle(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())