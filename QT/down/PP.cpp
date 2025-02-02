#include <PP.h>

pp::pp(QWidget *parent) : QWidget(parent)
{
    ori();
    works();

}

pp::~pp()
{

}


void pp::ori()
{
    mainlayout = new QVBoxLayout(this);
    mainlayout->setSpacing(10); // 布局元素之间的间距
    mainlayout->setContentsMargins(15, 15, 15, 15); // 主布局的边距

    // 设置窗口背景颜色为白色
    this->setStyleSheet("background-color: white;");

    // 创建返回按钮和timer
    back_btn = new QPushButton("返回", this);
    timer = new QComboBox(this);

    // 为timer添加选项
    timer->addItems({"空","今天", "明天", "后天"});

    // 设置返回按钮样式
    back_btn->setStyleSheet("QPushButton { "
                            "background-color: #4CAF50; "
                            "color: white; "
                            "border-radius: 10px; "
                            "padding: 10px; "
                            "font-size: 16px; "
                            "font-weight: bold; }"
                            "QPushButton:hover { background-color: #45a049; }");

    // 设置下拉框样式
    timer->setStyleSheet("QComboBox { "
                         "border: 1px solid #ccc; "
                         "border-radius: 5px; "
                         "padding: 8px; "
                         "height: 35px; "
                         "font-size: 14px; }");

    // 创建顶部布局，包含返回按钮和 timer
    QHBoxLayout *toplayout = new QHBoxLayout();
    toplayout->addWidget(back_btn);
    toplayout->addWidget(timer);

    // 添加伸缩项以使返回按钮靠左
    toplayout->addStretch();

    // 将toplayout添加到主布局
    mainlayout->addLayout(toplayout);

    // 创建5个组合框和标签的布局
    QStringList colors = { "#FF5733", "#33FF57", "#3357FF", "#F1C40F", "#9B59B6" }; // 颜色列表
    QStringList movieOptions = {"空","王者归来", "the king of the world", "加勒比海盗", "复仇者联盟", "情迷西雅图"}; // 电影选项
    QStringList timeOptions = {"空","8:00-10:00", "12:00-14:00", "16:00-18:00"}; // 时间选项

    for (int i = 0; i < 5; ++i) {
        QHBoxLayout *horizontalLayout = new QHBoxLayout();

        // 创建控件
        QComboBox* com = new QComboBox(this);
        QLabel* house = new QLabel(QString("%1号厅").arg(i + 1), this); // 从1开始编号
        QComboBox* time = new QComboBox(this);

        // 添加电影选项到com
        com->addItems(movieOptions);

        // 添加时间选项到time
        time->addItems(timeOptions);

        // 设置标签样式
        house->setStyleSheet(QString("QLabel { font-size: 16px; margin-right: 10px; background-color: %1; padding: 5px; border-radius: 5px; color: white; }").arg(colors[i]));

        // 设置下拉框样式
        com->setStyleSheet("QComboBox { "
                           "border: 1px solid #ccc; "
                           "border-radius: 5px; "
                           "padding: 8px; "
                           "height: 35px; "
                           "font-size: 14px; }");
        time->setStyleSheet("QComboBox { "
                            "border: 1px solid #ccc; "
                            "border-radius: 5px; "
                            "padding: 8px; "
                            "height: 35px; "
                            "font-size: 14px; }");

        // 添加控件到数组
        comarray.append(com);
        timearray.append(time);
        housearray.append(house);

        // 设置控件的最小尺寸
        com->setMinimumSize(100, 35);
        time->setMinimumSize(100, 35);

        // 将控件添加到水平布局
        horizontalLayout->addWidget(house);
        horizontalLayout->addWidget(time);
        horizontalLayout->addWidget(com);

        // 将水平布局添加到主布局
        mainlayout->addLayout(horizontalLayout);
    }

    // 设置窗口的主布局
    setLayout(mainlayout);
}
void pp::works()
{
    for (int i = 0;i<5;++i)
    {
        comarray[i]->setVisible(false);
        timearray[i]->setVisible(false);
        connect(comarray[i],&QComboBox::currentIndexChanged,this,[=](){
            filmchange(i);
        });
        connect(timearray[i],&QComboBox::currentIndexChanged,this,[=](){
            timechange(i);
        });
    }
    connect(back_btn,&QPushButton::clicked,this,[&](){
        emit toru();
        timer->setCurrentIndex(0);
        for (int i=0;i<5;++i)
        {
            comarray[i]->setCurrentIndex(0);
            timearray[i]->setCurrentIndex(0);
        }
    });
    connect(timer,&QComboBox::currentIndexChanged,this,&pp::timerchange);


}

void pp::timerchange()
{
    // timer 为 0，隐藏所有下拉框
    if (timer->currentIndex() == 0) {
        for (int i = 0; i < 5; ++i) {
            comarray[i]->setVisible(false);
            timearray[i]->setVisible(false);
        }
    }
    else {

        for (int i = 0; i < 5; ++i) {
            timearray[i]->setVisible(true); // 显示所有 timearray
            // 根据 timearray 的当前索引控制 comarray 的可见性
            if (timearray[i]->currentIndex() == 0) {
                comarray[i]->setVisible(false);
            } else {
                comarray[i]->setVisible(true);
            }
        }
    }

    daytime = timer->currentIndex();
}
void pp::timechange(int i)
{
    // 更新 comarray 的可见性
    if (timearray[i]->currentIndex() == 0) {
        comarray[i]->setVisible(false);
    } else {
        comarray[i]->setVisible(true);
    }

    time = timearray[i]->currentIndex();
}
void pp::filmchange(int i)
{
    film = comarray[i]->currentIndex();
    int house = i+1;
    emit send_data(daytime,time,house,film);
}
void pp::data_back(int i)
{
    if (i==0)
    {
        QMessageBox::information(this, "排片", "排片成功！");
    }
    if (i==1)
    {
        QMessageBox::information(this, "排片", "排片失败！<br>排片时间已过");
    }
    if (i==2)
    {
        QMessageBox::information(this, "排片", "排片失败！<br>当前时间已有顾客买票");
    }
}
