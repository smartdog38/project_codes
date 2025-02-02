#ifndef TP_H
#define TP_H

#include <QWidget>
#include <QPushButton>
#include <QVBoxLayout>
#include <QGridLayout>

class TicketWindow : public QWidget {
    Q_OBJECT

public:
    TicketWindow(QWidget *parent = nullptr);
    QVBoxLayout *mainLayout;
    QPushButton *backButton;

private slots:
    void onButtonClicked();
private:
    void setupUI(); // 设置用户界面


signals:
    void touu();
};
#endif // TP_H
