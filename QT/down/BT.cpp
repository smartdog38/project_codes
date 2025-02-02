#include "BT.h"


bt::bt(QWidget *parent) : QWidget(parent)
{
    ori();
    works();




}


void bt::works()
{
    connect(backButton, &QPushButton::clicked, this, [&]() {
        emit toct();
        // for (int i=0;i<4;++i)
        // {
        //     for(int j=0;j<5;++j)
        //     {
        //        seatButtons[i][j]->setVisible(true);
        //     }
        // }

    });
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 5; j++) {
            int row = i;
            int col = j;

            connect(seatButtons[row][col], &QPushButton::clicked, this, [this, row, col]() {
                // qDebug() << "Button clicked at:" << row << col;  // 添加此行以调试点击事件

                if (seatButtons[row][col]->text() == "空位") {
                    seatButtons[row][col]->setStyleSheet(clickedStyle);
                    seatButtons[row][col]->setText("选中");
                    rows << row;
                    cols << col;
                } else {
                    seatButtons[row][col]->setStyleSheet(
                        "QPushButton {"
                        "   background-color: lightgray;"
                        "   color: black;"
                        "   border: 2px solid #888;"
                        "   border-radius: 10px;"
                        "   padding: 10px;"
                        "   font-size: 16px;"
                        "   transition: background-color 0.3s, color 0.3s;"
                        "}"
                        "QPushButton:hover {"
                        "   background-color: #007BFF;"
                        "   color: white;"
                        "   border: 2px solid #0056b3;"
                        "}"
                        "QPushButton:pressed {"
                        "   background-color: #0056b3;"
                        "   color: white;"
                        "   border: 2px solid #004085;"
                        "}");
                    seatButtons[row][col]->setText("空位");
                    rows.removeOne(row);
                    cols.removeOne(col);
                }
            });
        }
    }
    connect(buyTicketButton, &QPushButton::clicked, this, [&]() {
        emit buy_ticket(rows,cols);
        for(int i =0;i<rows.size();i++)
        {
            seatButtons[rows[i]][cols[i]]->setVisible(false);
            QMessageBox::information(this,"购票","购票成功！");
        }
    });

}

void bt::recv_set(int tickets[4][5])
{
    for (int i=0;i<4;++i)
    {
        for(int j=0;j<5;++j)
        {
            if(tickets[i][j]<0)
            {
                seatButtons[i][j]->setVisible(false);
            }
        }
    }
}
bt::~bt()
{

}
void bt::ori()
{
    setWindowTitle("购票系统");
    // 创建主要布局
    QVBoxLayout *mainLayout = new QVBoxLayout(this);
    mainLayout->setSpacing(20);
    mainLayout->setContentsMargins(30, 30, 30, 30); // 设置边距
    // 设置背景颜色
    this->setStyleSheet("background-color: #F9F9F9;"); // 淡灰色背景
    // 创建返回按钮并添加到布局
    backButton = new QPushButton("返回", this);
    backButton->setStyleSheet("QPushButton { background-color: #4CAF50; color: white; padding: 10px; border-radius: 5px; font-size: 16px; }"
                              "QPushButton:hover { background-color: #45a049; }");
    mainLayout->addWidget(backButton, 0, Qt::AlignLeft);
    // 创建购票按钮并添加到布局
    buyTicketButton = new QPushButton("购票", this);
    buyTicketButton->setStyleSheet("QPushButton { background-color: #008CBA; color: white; padding: 10px; border-radius: 5px; font-size: 16px; }"
                                   "QPushButton:hover { background-color: #007B9E; }");
    mainLayout->addWidget(buyTicketButton, 0, Qt::AlignCenter);
    // 创建座位按钮组
    QGridLayout *seatsLayout = new QGridLayout();
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 5; ++j) {
            seatButtons[i][j] = new QPushButton("空位", this);
            seatButtons[i][j]->setStyleSheet(
                      "QPushButton {"
                      "   background-color: lightgray;"
                      "   color: black;"
                      "   border: 2px solid #888; "
                      "   border-radius: 10px;"
                      "   padding: 10px;"
                      "   font-size: 16px;"
                      "   transition: background-color 0.3s, color 0.3s;"
                      "}"
                      "QPushButton:hover {"
                      "   background-color: #007BFF;"
                      "   color: white;"
                      "   border: 2px solid #0056b3;"
                      "}"
                      "QPushButton:pressed {"
                      "   background-color: #0056b3;"
                      "   color: white;"
                      "   border: 2px solid #004085;"
                "}");
            seatsLayout->addWidget(seatButtons[i][j], i, j);

            // connect(seatButtons[i][j], &QPushButton::clicked, this, &bt::onSeatButtonClicked);
        }
    }

    // 将座位按钮组添加到主布局
    mainLayout->addLayout(seatsLayout);
    statusLabel = new QLabel("售票状态: 未售票", this);
    statusLabel->setStyleSheet("font-size: 18px; font-weight: bold; color: #333;");
    mainLayout->addWidget(statusLabel, 0, Qt::AlignCenter);
    styleGuideLabel = new QLabel("样式说明: <br> "
                                 "<span style='color: green;'>未售</span> - 座位按钮正常状态 <br> "
                                 "<span style='color: red;'>已售</span> - 座位消失", this);
    styleGuideLabel->setWordWrap(true);
    styleGuideLabel->setStyleSheet("font-size: 14px; color: #555555; text-align: center;");
    mainLayout->addWidget(styleGuideLabel, 0, Qt::AlignCenter);
}
