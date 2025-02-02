#ifndef PP_H
#define PP_H

#include <QWidget>
#include <QPushButton>
#include <QComboBox>
#include <QLabel>
#include <QIcon>
#include <QPixmap>
#include <QVector>
#include <QHBoxLayout>
#include <QVBoxLayout>
#include <QScrollArea>
#include <QScrollBar>
#include <QMessageBox>


class pp : public QWidget
{
    Q_OBJECT

public:
    pp(QWidget * parent = nullptr);
    ~pp();
    //
    int daytime;
    int time;
    int film;
    QVBoxLayout * mainlayout;
    QVBoxLayout * toplayout;
    QVBoxLayout * firstlayoutv;
    QVBoxLayout * secondlayoutv;
    QVBoxLayout * thirdlayoutv;
    QVBoxLayout * fourthlayoutv;
    QVBoxLayout * fifthlayoutv;
    QHBoxLayout * firstlayouth;
    QHBoxLayout * secondlayouth;
    QHBoxLayout * thirdlayouth;
    QHBoxLayout * fourthlayouth;
    QHBoxLayout * fifthlayouth;
    QVector<QComboBox *> comarray;
    QVector<QLabel*> housearray;
    QVector<QComboBox *> timearray;
    QPushButton *back_btn;
    QComboBox * timer;
    //
    void ori();
    void works();
    void timerchange();
    void timechange(int i);
    void filmchange(int i);
    void data_back(int i);
    //
signals:
    void toru();
    void send_data(int daytime,int time,int house ,int film);

};



#endif // PP_H
