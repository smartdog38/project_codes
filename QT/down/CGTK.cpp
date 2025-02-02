#include <CGTK.h>

cgtk::cgtk()
{
    ori();
    works();

}

cgtk::~cgtk()
{

}


void cgtk::works()
{
    connect(back_btn,&QPushButton::clicked,this,[&](){
        emit toru();
    });
    connect(set_btn,&QPushButton::clicked,this,&cgtk::send_price);
    for (int i=0;i<5;i++)
    {
        connect(filmarray[i],&QPushButton::clicked,this,[=](){
            film = i+1;
        });
    }
}

void cgtk::send_price()
{
    QString price = price_text->text();
    if (price!="")
    {
        emit set_price(film,price.toDouble());

    }
    else {
        QMessageBox::information(nullptr,"错误","不能为空值！",QMessageBox::Ok);
    }
}
void cgtk::ori()
{
    // 设置窗口背景颜色为柔和的颜色
    QPalette palette = this->palette();
    palette.setColor(QPalette::Window, QColor(173, 216, 230)); // 浅蓝色
    this->setPalette(palette);
    this->setAutoFillBackground(true); // 确保背景填充

    // 初始化布局
    mainlayout = new QVBoxLayout(this);

    // 用户布局，放置返回按钮
    uplayout = new QVBoxLayout();
    back_btn = new QPushButton("返回");
    back_btn->setFixedSize(80, 40); // 调整返回按钮大小
    uplayout->addWidget(back_btn);

    // 添加用户布局到主布局
    mainlayout->addLayout(uplayout);

    // 电影按钮布局
    filmlayoutv = new QVBoxLayout();
    filmlayouth = new QHBoxLayout();

    // 调整电影按钮的大小
    for (int i = 0; i < 5; ++i) {
        QPushButton *btn = new QPushButton(QString::number(i + 1)); // 按钮文本从 "1" 改为 "1", "2" 等
        btn->setFixedSize(200, 300); // 增大电影按钮的大小，以便更好地显示海报
        filmarray.append(btn);
        filmlayouth->addWidget(btn);
        if (i < 4) { // 只在前四个按钮之间添加水平间隔
            filmlayouth->addSpacerItem(new QSpacerItem(10, 0, QSizePolicy::Fixed, QSizePolicy::Minimum));
        }
    }

    // 将电影按钮布局添加到垂直电影布局
    filmlayoutv->addLayout(filmlayouth);
    mainlayout->addLayout(filmlayoutv); // 添加电影布局到主布局

    // 输入框及标签设置
    price_lb = new QLabel("定价");
    price_text = new QLineEdit();
    price_text->setPlaceholderText("请输入价格"); // 添加占位文字
    price_text->setFixedHeight(50); // 增加文本框的高度

    // 设置按钮并添加到电影布局下方
    set_btn = new QPushButton("设置");
    set_btn->setFixedSize(200, 80);

    // 创建一个新的布局来集中排列文本框和设置按钮
    QVBoxLayout *centerLayout = new QVBoxLayout();
    centerLayout->addWidget(price_lb);
    centerLayout->addWidget(price_text);
    centerLayout->addWidget(set_btn, 0, Qt::AlignHCenter); // 确保设置按钮在中心位置

    // 将中心布局添加到主布局
    mainlayout->addLayout(centerLayout);

    // 在距离电影区域的顶部增加一些空间以偏移位置
    mainlayout->addStretch(); // 添加伸缩量，推动内容向上
    mainlayout->addStretch(); // 在海报区域和输入框之间添加更多空间

    // 美化布局（设置间距）
    mainlayout->setSpacing(10);
    mainlayout->setContentsMargins(10, 10, 10, 10);  // 边距

    // 设置主布局
    setLayout(mainlayout);
}


