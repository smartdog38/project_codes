#include <CP.h>
#include <QVideoWidget>
#include <QMediaPlayer>


cp::cp(QWidget *parent) : QWidget(parent)
{
    // 创建标签和按钮
    ori();
    signalsworks();

}



cp::~cp()
{}
void cp::ori()
{
    lb = new QLabel("欢迎来到我们的电影院！！！");
    lb->setAlignment(Qt::AlignCenter);
    lb->setFixedHeight(300);
    lb->setStyleSheet("font-size: 64px; font-weight: bold; color: #2E7D32;");

    gm_btn = new QPushButton("管理员", this);
    gm_btn->setFixedSize(400, 300);
    gm_btn->setStyleSheet("background-color: #4CAF50; color: white; font-size: 20px; border: none; border-radius: 10px;");

    us_btn = new QPushButton("用户", this);
    us_btn->setFixedSize(400, 300);
    us_btn->setStyleSheet("background-color: #2196F3; color: white; font-size: 20px; border: none; border-radius: 10px;");

    // 主布局
    mainlayout = new QVBoxLayout(this);
    lb_ly = new QHBoxLayout();
    btn_ly = new QHBoxLayout();

    mainlayout->addLayout(lb_ly);
    mainlayout->addLayout(btn_ly);

    lb_ly->addWidget(lb);
    // 按钮布局
    btn_ly->addSpacerItem(new QSpacerItem(20, 20, QSizePolicy::Expanding, QSizePolicy::Fixed));
    btn_ly->addWidget(gm_btn);
    btn_ly->addSpacerItem(new QSpacerItem(100, 20, QSizePolicy::Fixed, QSizePolicy::Fixed));
    btn_ly->addWidget(us_btn);
    btn_ly->addSpacerItem(new QSpacerItem(20, 20, QSizePolicy::Expanding, QSizePolicy::Fixed));
    setStyleSheet("background-image: url(:/nnn.jpg);"
                  "background-repeat: no-repeat;"
                  "background-position: center;");
}
void cp::signalsworks()
{
    connect(gm_btn,&QPushButton::clicked,this,[&](){
        emit toli(0);
    });
    connect(us_btn,&QPushButton::clicked,this,[&](){
        emit toli(1);
    });
}
