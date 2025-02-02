#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include <QStackedWidget>
#include <QPushButton>
#include <QVBoxLayout>
#include <QPropertyAnimation>
#include <QLabel>
#include <QLineEdit>
#include <QVideoWidget>
#include <QMediaPlayer>
#include <QMouseEvent>
#include <QSpacerItem>
#include <QSlider>
#include <QScrollArea>
#include <QScrollBar>
#include <QComboBox>
#include <QDebug>
#include <QDate>
#include <QDateTime>
#include <QTime>




class Widget : public QWidget
{
    Q_OBJECT

public:
    Widget(QWidget *parent = nullptr);
    ~Widget();



private slots:
    void onButtonClicked();
};

















#endif // WIDGET_H
