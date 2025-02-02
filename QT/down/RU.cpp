#include <RU.h>
#include <QMessageBox>

ru::ru(QWidget *parent) : QWidget(parent)
{
    ori();
    works();

    //


}

void ru::works()
{
    connect(h_btn,&QPushButton::clicked,this,[&](){
        QMessageBox::information(nullptr, "帮助", "看看头像里有什么");
    });
    connect(e_btn,&QPushButton::clicked,this,[&](){
        emit tocp();
    });
    connect(t_btn,&QPushButton::clicked,this,[&](){
        emit tocgtk();
    });
    connect(c_btn,&QPushButton::clicked,this,[&](){
        emit topp();
    });
    connect(ls_btn,&QPushButton::clicked,this,[&](){
        QMessageBox::information(this,"排序","第一：情迷西雅图<br>第二：the king of the world<br>第三：加勒比海盗<br><br>");
    });
}


void ru::getuser(QString name)
{
    u_btn->setText(name);
    user = name;
}


void ru::ori()
{
    resize(1200, 800);

    // 主布局
    resize(800, 600);
    mainlayout = new QHBoxLayout(this);
    u_lo = new QVBoxLayout();
    d_lo = new QVBoxLayout();

    // 定义按钮
    h_btn = new QPushButton("帮助");
    e_btn = new QPushButton("退出");
    c_btn = new QPushButton("影片排挡");
    t_btn = new QPushButton("设置单价");
    ls_btn = new QPushButton("票款");

    // 用户标签
    u_btn = new QPushButton("管理员", this);
    u_btn->setStyleSheet("font-size: 24px; font-weight: bold; color: #2E7D32;");

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


ru::~ru()
{
}
