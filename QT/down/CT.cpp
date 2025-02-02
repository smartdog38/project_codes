#include "CT.h"

ct::ct(QWidget *parent) : QWidget(parent)
{
    ori();
    works();


}



void ct::works()
{
    connect(backButton,&QPushButton::clicked,this,[&](){
        emit touu();
    });
    for (int i=0;i<5;++i)
    {
        connect(movieButtons[i],&QPushButton::clicked,this,[=](){
            house = i+1;
        });
    }
    for (int i=0;i<3;++i)
    {
        connect(extraButtons[i],&QPushButton::clicked,this,[=](){
            time = i+1;
            if (extraButtons[i]->text()!="")
                {
                emit tobt(house,daytime,time);
            }
        });
        connect(timeButtons[i],&QPushButton::clicked,this,[=](){
            daytime = i+1;
            if (house!=0&&daytime!=0)
                {
                for (int i=0;i<3;i++)
                {
                    extraButtons[i]->setText("");
                }
                emit getfilm(house,daytime);
            }
        });
    }

}

void ct::ori()
{
    mainLayout = new QVBoxLayout(this);
    mainLayout->setSpacing(20); // 设置控件之间的垂直间距
    mainLayout->setContentsMargins(30, 30, 30, 30); // 设置主布局的边距
    // 创建返回按钮并添加到布局
    backButton = new QPushButton("返回", this);
    backButton->setStyleSheet("background-color: #4CAF50; color: white; font-size: 16px; padding: 15px; border-radius: 10px;");
    mainLayout->addWidget(backButton, 0, Qt::AlignLeft);
    // 创建电影按钮组（5个按钮）
    moviesLayout = new QGridLayout();
    moviesLayout->setSpacing(20); // 设置电影按钮之间的间距
    for (int i = 0; i < 5; ++i) {
        movieButtons[i] = new QPushButton(QString("影厅 %1").arg(i + 1), this);
        movieButtons[i]->setFixedSize(200, 300); // 设置按钮大小为 200x300 像素
        movieButtons[i]->setStyleSheet("background-color: #2196F3; color: white; font-size: 18px; padding: 25px; border-radius: 10px;");
        moviesLayout->addWidget(movieButtons[i], 0, i);
    }
    // 将电影按钮组添加到主布局
    mainLayout->addLayout(moviesLayout);
    // 创建时间按钮组（3个按钮），并使用水平布局
    timeButtonsLayout = new QHBoxLayout();
    timeButtonsLayout->setSpacing(20); // 设置时间按钮之间的间距
    for (int i = 0; i < 3; ++i) {
        timeButtons[i] = new QPushButton(this);
        timeButtons[i]->setStyleSheet("background-color: #FF5722; color: white; font-size: 18px; padding: 15px; border-radius: 10px;");
        timeButtonsLayout->addWidget(timeButtons[i]); // 添加时间按钮到水平布局
    }
    timeButtons[0]->setText("今天");
    timeButtons[1]->setText("明天");
    timeButtons[2]->setText("后天");
    // 将时间按钮组添加到主布局
    mainLayout->addLayout(timeButtonsLayout);
    // 创建额外的按钮组（3个按钮），更改为垂直布局
    extraButtonsLayout = new QVBoxLayout(); // 使用垂直布局
    extraButtonsLayout->setSpacing(20); // 设置额外按钮之间的间距
    for (int i = 0; i < 3; ++i) {
        extraButtons[i] = new QPushButton(QString(""), this);
        extraButtons[i]->setStyleSheet("background-color: #FFC107; color: black; font-size: 18px; padding: 20px; border-radius: 10px;");
        extraButtonsLayout->addWidget(extraButtons[i]); // 添加到垂直布局
    }
    // 将额外按钮组添加到主布局
    mainLayout->addLayout(extraButtonsLayout);
    // 设置背景色
    setStyleSheet("background-color: #f0f0f0;"); // 设置主窗口背景颜色
}
ct::~ct()
{
}
void ct::setfilm(QString first,QString second,QString third)
{
    qDebug()<<first<<second<<third;
    if (first!="")
    {
        extraButtons[0]->setText(first);
    }
    if (second!="")
    {
        extraButtons[1]->setText(second);
    }
    if (third!="")
    {
        extraButtons[2]->setText(third);
    }
}

