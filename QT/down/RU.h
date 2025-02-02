#ifndef RU_H
#define RU_H

#include <QWidget>
#include <QPushButton>
#include <QLabel>
#include <QHBoxLayout>
#include <QVBoxLayout>
#include <QSpacerItem>



class ru : public QWidget
{
    Q_OBJECT

public:
    ru(QWidget * parent = nullptr);
    ~ru();
    //
    QString user;
    QPushButton * h_btn;
    QPushButton * e_btn;
    QPushButton * c_btn;
    QPushButton * t_btn;
    QPushButton * ls_btn;
    QHBoxLayout *mainlayout;
    QVBoxLayout *u_lo;
    QVBoxLayout *d_lo;
    QPushButton *u_btn;
    QString buttonStyle;
    QString roundButtonStyle;

    //
    void ori();
    void works();
    void t();
    void ls();
    void getuser(QString name);
    //

signals:
    void tocp();
    void topp();
    void tocgtk();
    void tohis();


};





#endif // RU_H
