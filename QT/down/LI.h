#ifndef LI_H
#define LI_H


#include <QWidget>
#include <QPushButton>
#include <QSpacerItem>
#include <QLabel>
#include <QHBoxLayout>
#include <QHBoxLayout>
#include <QLineEdit>
#include <QAxObject>
#include <QFile>
#include <QDir>
#include <QMessageBox>
#include <QString>
#include <QFileDialog>
#include <QVariant>
#include <QVariantList>
#include <QStringList>

class li :public QWidget
{
    Q_OBJECT

public:
    int state;//0 ru 1 uu
    //构造函数
    li(QWidget * parent =nullptr);
    ~li();




    //控件的定义
    QPushButton *backButton;
    QPushButton *signInButton;
    QPushButton *loginButton;
    QLabel *usernameLabel;
    QLineEdit *usernameLineEdit;
    QLabel *passwordLabel;
    QLineEdit *passwordLineEdit;
    QAxObject *sheet;
    QAxObject *sheets;
    QAxObject * workbooks;
    QAxObject * workbook;
    QLabel *titleLabel;
    QAxObject *excel;
    QVBoxLayout *mainLayout;
    QHBoxLayout *headerLayout;
    QHBoxLayout *usernameLayout;
    QHBoxLayout *passwordLayout;
    QVBoxLayout *buttonLayout;
    //
    void ts(QString text);
    void ori();
    void login();
    void signin();

    void works();
    void signback(int i);
    void logback(int i);
    void ch_state(int i);
    //
signals:
    void tocp();
    void sign(QString name,QString pwd);
    void log(QString name,QString pwd,int i);

};





#endif // LI_H
