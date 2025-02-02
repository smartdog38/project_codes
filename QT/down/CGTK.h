#ifndef CGTK_H
#define CGTK_H


#include <QWidget>
#include <QVector>
#include <QPushButton>
#include <QLineEdit>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QSpacerItem>
#include <QLabel>
#include <QDebug>
#include <QMessageBox>

class cgtk : public QWidget
{
    Q_OBJECT
public:
    cgtk();
    ~cgtk();


    //
    int film = 0;
    QLabel * price_lb;
    QVBoxLayout * mainlayout;
    QVBoxLayout * uplayout;
    QVBoxLayout * filmlayoutv;
    QHBoxLayout * filmlayouth;
    QVBoxLayout * setlayout;
    QPushButton * back_btn;
    QVector<QPushButton *> filmarray;
    QPushButton * set_btn;
    QLineEdit * price_text;
    //
    void ori();
    void works();
    void send_price();


signals:
    void toru();
    void set_price(int i,double price);

};

#endif // CGTK_H
