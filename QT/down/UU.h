#ifndef UU_H
#define UU_H


#include <QWidget>
#include <QPushButton>
#include <QLabel>
#include <QHBoxLayout>
#include <QVBoxLayout>
#include <QSpacerItem>


class uu : public QWidget
{
    Q_OBJECT

public:
    uu(QWidget * parent = nullptr);
    ~uu();
    //

    QString user;
    QPushButton * h_btn;
    QPushButton * e_btn;
    QPushButton * t_btn;
    QPushButton * c_btn;
    QPushButton * ls_btn;
    QHBoxLayout *mainlayout;
    QVBoxLayout *u_lo;
    QVBoxLayout *d_lo;
    QPushButton * u_btn;
    QString buttonStyle;
    QString roundButtonStyle;

    //
    void ori();
    void works();
    void getuser(QString name);

    void t();
    void c();
    void ls();
signals:
    void tocp();
    void toct();
    void totp();

};


#endif // UU_H
