#include "widget.h"
#include <QMessageBox>
#include <QPainter>

Widget::Widget(QWidget *parent) : QWidget(parent)
{
    QVBoxLayout *mainLayout = new QVBoxLayout(this);

    // 返回按钮
    QPushButton *backButton = new QPushButton("返回", this);
    connect(backButton, &QPushButton::clicked, this, [this]() {
        qDebug() << "返回按钮被点击";
        close(); // 关闭当前窗口
    });
    backButton->setFixedSize(80, 30);
    mainLayout->addWidget(backButton, 0, Qt::AlignLeft | Qt::AlignTop);

    // 按钮组
    QGridLayout *buttonGroupLayout = new QGridLayout();

    // 创建按钮并设置名称
    QString buttonNames[6] = { "加勒比海盗", "加勒比海盗", "加勒比海盗", "加勒比海盗", "复仇者联盟", "复仇者联盟" };

    for (int i = 0; i < 2; ++i) { // 两行
        for (int j = 0; j < 3; ++j) { // 三列
            QPushButton *button = new QPushButton(buttonNames[i * 3 + j], this);
            button->setFixedSize(100, 40);
            connect(button, &QPushButton::clicked, this, &Widget::onButtonClicked);
            buttonGroupLayout->addWidget(button, i, j);
        }
    }

    mainLayout->addLayout(buttonGroupLayout);
    setLayout(mainLayout);
}

void Widget::onButtonClicked() {
    QPushButton *button = qobject_cast<QPushButton*>(sender());
    if (button) {
        button->hide(); // 隐藏被点击的按钮
        qDebug() << button->text() << "被点击并已隐藏";
    }
}




Widget::~Widget()
{

}




