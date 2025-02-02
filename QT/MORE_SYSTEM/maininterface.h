#ifndef MAININTERFACE_H
#define MAININTERFACE_H

#include <QWidget>
#include <QStackedWidget>
#include <QDebug>
#include <QVariant>
#include <QVector>
#include <QTimer>
#include <QDate>
#include <QTime>
#include <QDateTime>
#include <QAxObject>




QT_BEGIN_NAMESPACE
namespace Ui {
class MainInterface;
}
QT_END_NAMESPACE

class MainInterface : public QWidget
{
    Q_OBJECT

public:
    //构造与析构
    MainInterface(QWidget *parent = nullptr);
    ~MainInterface();
    //定义状态量
    QString user_name;
    QDateTime currentTime;
    QDate currentDate;
    QString filePath;
    //定义控件
    QStackedWidget * SW;
    QVector<QAxObject* > sheet[5];
    QAxObject* sheets;
    QAxObject* workbook;
    QAxObject* excel;
    //定义函数（包括槽函数）
    void ori();
    void sheet_work();
    void other_connect_work();
    void switch_work();



    //定义相关信号
signals:




private:
    Ui::MainInterface *ui;
};
#endif // MAININTERFACE_H
