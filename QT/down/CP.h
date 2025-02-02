#ifndef CP_H
#define CP_H

#include <QWidget>
#include <QPushButton>
#include <QLabel>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QSpacerItem>



class cp : public QWidget
{
    Q_OBJECT

public:
    cp(QWidget * parent = nullptr);
    ~cp();
    //
    QPushButton * us_btn;
    QPushButton * gm_btn;
    QLabel * lb;
    QVBoxLayout * mainlayout;
    QHBoxLayout *lb_ly;
    QHBoxLayout *btn_ly;
    //
    void ori();
    //
    void signalsworks();
//一个信号 - 1 用户  0 管理员 跳转到li 同时打开对应的excel表

signals:
    void toli(int i);


};



#endif // CP_H
