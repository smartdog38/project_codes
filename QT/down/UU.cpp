#include <UU.h>
#include <QMessageBox>

uu::uu(QWidget *parent) : QWidget(parent)
{
    ori();
    works();



}


void uu::works()
{
    connect(h_btn,&QPushButton::clicked,this,[&](){
        QMessageBox::information(nullptr, "帮助", "想充值吗？<br>点点头像看看，嘿嘿嘿");
    });//帮助(done)
    connect(e_btn,&QPushButton::clicked,this,[&](){
        emit tocp();
    });//退出(done)

    connect(c_btn,&QPushButton::clicked,this,[&](){
        emit toct();
    });//选票

    connect(ls_btn,&QPushButton::clicked,this,&uu::ls);//历史纪录
    connect(t_btn,&QPushButton::clicked,this,[&](){
        emit totp();
    });//退票
}


void uu::t(){

}

void uu::getuser(QString name)
{
    u_btn->setText(name);
    user=name;
}
void uu::ls(){
    QMessageBox::information(nullptr, "历史购票记录", "2011.11.21：购买了加勒比海盗4*1<br>2011.11.22：申请退票（加勒比海盗*1）成功<br>2023.11.12：购买了海贼王*3");
}



void uu::ori()
{
    resize(800, 600);
    mainlayout = new QHBoxLayout(this);
    u_lo = new QVBoxLayout();
    d_lo = new QVBoxLayout();

    // 定义按钮
    h_btn = new QPushButton("帮助");
    e_btn = new QPushButton("退出");
    c_btn = new QPushButton("浏览排片信息");
    t_btn = new QPushButton("退票");
    ls_btn = new QPushButton("浏览历史购票记录");

    // 用户标签
    u_btn = new QPushButton("用户", this);
    u_btn->setStyleSheet("font-size: 24px; font-weight: bold; color: #2E7D32;");
    u_btn->setFixedSize(120,100);

    // 设置左侧按钮样式（增加高度和内边距）
    buttonStyle = "background-color: #4CAF50; color: white; font-size: 20px; border: none; border-radius: 10px; height: 70px; padding: 10px;";
    h_btn->setStyleSheet(buttonStyle);
    e_btn->setStyleSheet(buttonStyle);

    // 设置右侧按钮为圆形
    roundButtonStyle = "background-color: #2196F3; color: white; font-size: 20px; border: none; border-radius: 35px; height: 70px; width: 70px;"; // 圆形按钮
    c_btn->setStyleSheet(roundButtonStyle);
    t_btn->setStyleSheet(roundButtonStyle);
    ls_btn->setStyleSheet(roundButtonStyle);
    // 添加布局
    mainlayout->addLayout(u_lo);
    mainlayout->addLayout(d_lo);

    // 用户布局
    u_lo->addWidget(u_btn);
    u_lo->addSpacerItem(new QSpacerItem(40, 350, QSizePolicy::Fixed, QSizePolicy::Expanding)); // 给用户标签和按钮之间留出一些空间
    u_lo->addWidget(h_btn);
    u_lo->addWidget(e_btn);
    u_lo->addSpacerItem(new QSpacerItem(40, 20, QSizePolicy::Fixed, QSizePolicy::Expanding)); // 留出空间

    // 功能布局
    d_lo->addSpacerItem(new QSpacerItem(1, 50, QSizePolicy::Expanding, QSizePolicy::Fixed)); // 在顶部留空间
    d_lo->addWidget(c_btn);
    d_lo->addWidget(t_btn);
    d_lo->addWidget(ls_btn);
    d_lo->addSpacerItem(new QSpacerItem(1, 50, QSizePolicy::Expanding, QSizePolicy::Fixed)); // 在底部留空间

    // 设置主布局
    setLayout(mainlayout);

}
uu::~uu()
{
}

