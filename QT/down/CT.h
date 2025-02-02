#ifndef CT_H
#define CT_H

#include <QWidget>
#include <QPushButton>
#include <QSlider>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QScrollArea>
#include <QScrollBar>
#include <QMessageBox>

class ct : public QWidget
{
    Q_OBJECT

public:

    ct(QWidget *parent =nullptr);
    ~ct();
    //
    int house = 0;
    int daytime = 0;
    int time = 0;
    QString first;
    QString second;
    QString third;

    QVBoxLayout *mainLayout;
    // 返回按钮
    QPushButton *backButton;
    // 电影按钮
    QPushButton *movieButtons[5];
    // 电影按钮布局
    QGridLayout *moviesLayout;
    // 时间按钮数组
    QPushButton *timeButtons[3]; // 新增：时间按钮数组
    // 时间按钮布局
    QHBoxLayout *timeButtonsLayout;
    // 额外按钮
    QPushButton *extraButtons[3];
    // 额外按钮布局
    QVBoxLayout *extraButtonsLayout;
    //
    void works();
    void ori();
    void setfilm(QString first,QString second,QString third);

signals:
    void touu();
    void tobt(int house,int daytime,int time);
    void getfilm(int house,int daytime);
};



#endif // CT_H
