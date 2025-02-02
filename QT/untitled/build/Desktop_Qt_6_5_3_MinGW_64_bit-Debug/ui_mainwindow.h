/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 6.5.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QPushButton *scaleButton;
    QPushButton *startButton;
    QPushButton *startButton_2;
    QPushButton *startButton_3;
    QMenuBar *menuBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName("MainWindow");
        MainWindow->resize(836, 504);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName("centralWidget");
        scaleButton = new QPushButton(centralWidget);
        scaleButton->setObjectName("scaleButton");
        scaleButton->setGeometry(QRect(260, 390, 0, 0));
        QFont font;
        font.setPointSize(12);
        scaleButton->setFont(font);
        scaleButton->setStyleSheet(QString::fromUtf8("background-color: rgb(146, 110, 255);\n"
"border:none;"));
        startButton = new QPushButton(centralWidget);
        startButton->setObjectName("startButton");
        startButton->setGeometry(QRect(260, 70, 80, 40));
        QFont font1;
        font1.setFamilies({QString::fromUtf8("\351\273\221\344\275\223")});
        font1.setPointSize(20);
        startButton->setFont(font1);
        startButton->setStyleSheet(QString::fromUtf8(""));
        startButton_2 = new QPushButton(centralWidget);
        startButton_2->setObjectName("startButton_2");
        startButton_2->setGeometry(QRect(500, 70, 80, 40));
        startButton_2->setFont(font1);
        startButton_2->setStyleSheet(QString::fromUtf8(""));
        startButton_3 = new QPushButton(centralWidget);
        startButton_3->setObjectName("startButton_3");
        startButton_3->setGeometry(QRect(370, 70, 100, 40));
        QFont font2;
        font2.setFamilies({QString::fromUtf8("\351\273\221\344\275\223")});
        font2.setPointSize(20);
        font2.setStyleStrategy(QFont::PreferDefault);
        startButton_3->setFont(font2);
        startButton_3->setStyleSheet(QString::fromUtf8(""));
        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName("menuBar");
        menuBar->setGeometry(QRect(0, 0, 836, 18));
        MainWindow->setMenuBar(menuBar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        scaleButton->setText(QCoreApplication::translate("MainWindow", "scale", nullptr));
        startButton->setText(QCoreApplication::translate("MainWindow", "start", nullptr));
        startButton_2->setText(QCoreApplication::translate("MainWindow", "loop", nullptr));
        startButton_3->setText(QCoreApplication::translate("MainWindow", "back", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
