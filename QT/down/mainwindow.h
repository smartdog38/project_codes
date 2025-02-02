#ifndef MAINWINDOW_H
#define MAINWINDOW_H


#include "CP.h"
#include "LI.h"
#include "UU.h"
#include "CT.h"
#include "BT.h"
#include "RU.h"
#include "PP.h"
#include "ui_mainwindow.h"
#include "CGTK.h"
#include <QMainWindow>
#include <QStackedWidget>
#include <QDebug>
#include <QVariant>
#include <QVector>
#include <QTimer>
#include <QDate>
#include <QTime>
#include <QDateTime>
#include "tp.h"


QT_BEGIN_NAMESPACE
namespace Ui {
class MainWindow;
}
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    QString user;
    QDateTime currentTime = QDateTime::currentDateTime();
    QDate currentDate = QDate::currentDate();
    //
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();
    //
    QStackedWidget * SW;
    QAxObject* sheets;
    QAxObject* workbook;
    QAxObject* excel;
    QString filePath;

    void performScheduledTask();
    QTimer *timer; // 定时器
    void setupTimer(); // 设置定时器
    uu* uu1;
    cp* cp1;
    pp* pp1;
    li* li1;
    ru* ru1;
    bt* bt1;
    ct* ct1;
    cgtk* cgtk1;
    TicketWindow* tp1;

    void allori();
    void switchs();
    void sheetwork();
    void otherslot();
    void openexcel();
    void checksign(QString name,QString pwd);
    void checklog(QString name,QString pwd,int state);
    int getmaxrow(int i);
    int getmaxcol(int i);
    void setvalue(int i,int row ,int col, QVariant value);//第一个表的位置，第二个为行，第三个为列，第四个为设置的值
    QVariant getvalue(int i, int row ,int  col);//第一个表的位置，第二个为行，第三个为列，返回值
    int getrow(int i,int col,QVariant value);
    int getcol(int i,int row,QVariant value);

    void set_pian(int daytime,int time,int house ,int film);
    void check_and_set(int daytime,int time,int house ,int film);
    void time_torenew();
    void renew_ticket();

    void getfilm(int house,int daytime);
    void getticket(int houuse ,int daytime,int time);
    void buy_ticket(QList<int> rows,QList<int>  cols);
signals:
    void signback(int i);
    void logback(int i);
    void touu(QString name);
    void toru(QString name);
    void topai(int i);
    void backfilm(QString first,QString second,QString third);
    void backticket(int  tickets[4][5]);
    void back_buy(int i);
private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
