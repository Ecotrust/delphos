# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'credits_dialog.ui'
#
# Created: Tue Jun 17 10:39:26 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_CreditsDialog(object):
    def setupUi(self, CreditsDialog):
        CreditsDialog.setObjectName("CreditsDialog")
        CreditsDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        CreditsDialog.resize(591,522)
        self.vboxlayout = QtGui.QVBoxLayout(CreditsDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.groupBox = QtGui.QGroupBox(CreditsDialog)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setObjectName("groupBox")
        self.vboxlayout1 = QtGui.QVBoxLayout(self.groupBox)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setMinimumSize(QtCore.QSize(138,83))
        self.label_6.setMaximumSize(QtCore.QSize(138,83))
        self.label_6.setPixmap(QtGui.QPixmap(":/images/cobi_logo.jpg"))
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.vboxlayout2.addWidget(self.label_6)
        spacerItem = QtGui.QSpacerItem(20,0,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout2.addItem(spacerItem)
        self.hboxlayout.addLayout(self.vboxlayout2)
        self.cobi_label = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.cobi_label.setFont(font)
        self.cobi_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.cobi_label.setWordWrap(True)
        self.cobi_label.setObjectName("cobi_label")
        self.hboxlayout.addWidget(self.cobi_label)
        self.vboxlayout1.addLayout(self.hboxlayout)
        spacerItem1 = QtGui.QSpacerItem(20,10,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout1.addItem(spacerItem1)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setObjectName("hboxlayout2")
        self.wwf_label = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.wwf_label.setFont(font)
        self.wwf_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.wwf_label.setWordWrap(True)
        self.wwf_label.setObjectName("wwf_label")
        self.hboxlayout2.addWidget(self.wwf_label)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setMaximumSize(QtCore.QSize(16777215,73))
        self.label_3.setPixmap(QtGui.QPixmap(":/images/wwf_logo.gif"))
        self.label_3.setObjectName("label_3")
        self.hboxlayout2.addWidget(self.label_3)
        self.hboxlayout1.addLayout(self.hboxlayout2)
        self.vboxlayout1.addLayout(self.hboxlayout1)
        spacerItem2 = QtGui.QSpacerItem(20,10,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout1.addItem(spacerItem2)
        self.hboxlayout3 = QtGui.QHBoxLayout()
        self.hboxlayout3.setObjectName("hboxlayout3")
        self.vboxlayout3 = QtGui.QVBoxLayout()
        self.vboxlayout3.setObjectName("vboxlayout3")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setMaximumSize(QtCore.QSize(16777215,51))
        self.label_2.setPixmap(QtGui.QPixmap(":/images/ecotrust_logo.gif"))
        self.label_2.setObjectName("label_2")
        self.vboxlayout3.addWidget(self.label_2)
        spacerItem3 = QtGui.QSpacerItem(20,0,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout3.addItem(spacerItem3)
        self.hboxlayout3.addLayout(self.vboxlayout3)
        self.ecotrust_label = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.ecotrust_label.setFont(font)
        self.ecotrust_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ecotrust_label.setWordWrap(True)
        self.ecotrust_label.setObjectName("ecotrust_label")
        self.hboxlayout3.addWidget(self.ecotrust_label)
        self.vboxlayout1.addLayout(self.hboxlayout3)
        self.vboxlayout.addWidget(self.groupBox)
        self.hboxlayout4 = QtGui.QHBoxLayout()
        self.hboxlayout4.setObjectName("hboxlayout4")
        spacerItem4 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout4.addItem(spacerItem4)
        self.pushButton = QtGui.QPushButton(CreditsDialog)
        self.pushButton.setObjectName("pushButton")
        self.hboxlayout4.addWidget(self.pushButton)
        self.vboxlayout.addLayout(self.hboxlayout4)

        self.retranslateUi(CreditsDialog)
        QtCore.QObject.connect(self.pushButton,QtCore.SIGNAL("clicked()"),CreditsDialog.close)
        QtCore.QObject.connect(self.pushButton,QtCore.SIGNAL("clicked()"),CreditsDialog.deleteLater)
        QtCore.QMetaObject.connectSlotsByName(CreditsDialog)

    def retranslateUi(self, CreditsDialog):
        CreditsDialog.setWindowTitle(QtGui.QApplication.translate("CreditsDialog", "Delphos Credits", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setStyleSheet(QtGui.QApplication.translate("CreditsDialog", "background-color: white", None, QtGui.QApplication.UnicodeUTF8))
        self.cobi_label.setText(QtGui.QApplication.translate("CreditsDialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><a href=\"http://www.cobi.org.mx/\"><span style=\" font-size:10pt; font-weight:600; text-decoration: underline; color:#0000ff;\">Comunidad Y Biodiversidad</span></a><span style=\" font-size:10pt; font-weight:600;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600;\"><span style=\" font-size:9pt; font-weight:400;\">COBI promotes the conservation of marine</span><span style=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; font-weight:400;\">biodiversity through community involvement schemes.  </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\">COBI designed Delphos for Marine Protected Areas including the documentation and design.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.wwf_label.setText(QtGui.QApplication.translate("CreditsDialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><a href=\"http://www.wwf.org/\"><span style=\" font-size:10pt; font-weight:600; text-decoration: underline; color:#0000ff;\">World Wildlife Fund</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600;\"><span style=\" font-size:9pt; font-weight:400;\">Known in the United States as World Wildlife Fund and recognized worldwide by its panda logo, WWF leads international efforts to protect endangered species and their habitats and to conserve the diversity of life on Earth. Now in its fifth decade, WWF, the global conservation organization, works in more than 100 countries around the world.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.ecotrust_label.setText(QtGui.QApplication.translate("CreditsDialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><a href=\"http://www.ecotrust.org\"><span style=\" font-size:10pt; font-weight:600; text-decoration: underline; color:#0000ff;\">Ecotrust</span></a><span style=\" font-size:10pt; font-weight:600;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600;\"><span style=\" font-size:9pt; font-weight:400;\">Ecotrust believes in a place where economic, ecological, and socialconditions are improving, where a \"conservation economy\" is emerging.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\">Ecotrust Knowledge Systems designed and developed this software, makingit available free and open source.  The source code is available underthe GPL2 license and can be found on the Delphos development site.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("CreditsDialog", "Close Window", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
