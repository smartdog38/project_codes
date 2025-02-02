#ifndef BT_H
#define BT_H

#include <QSpacerItem>
#include <QVector>
#include <QWidget>
#include <QGridLayout>
#include <QPushButton>
#include <QMessageBox>
#include <QLabel>
#include <QList>
#include <QDebug>



class bt : public QWidget
{
    Q_OBJECT

public:
    bt(QWidget * parent = nullptr);
    ~bt();
    QString clickedStyle = "background-color: blue; color: white;";
    QString normalStyle = "background-color: lightgray; ";
    QList<int> rows;
    QList<int> cols;
    QPushButton *backButton;         // 返回按钮
    QPushButton *buyTicketButton;    // 购票按钮
    QPushButton *seatButtons[4][5];  // 座位按钮组
    QLabel *statusLabel;             // 状态标签
    QLabel *styleGuideLabel;         // 样式指南标签
    //

    void recv_set(int tickets[4][5]);
    void ori();
    void works();
    void click_seat();
    void recv_judge();
signals:
    void toct();
    void buy_ticket(QList<int> row,QList<int> col);
};


#endif // BT_H
