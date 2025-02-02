#include "mainwindow.h"



MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    allori();
    switchs();
    otherslot();
    sheetwork();
    openexcel();
    time_torenew();
}



void MainWindow::checksign(QString name,QString pwd)
{
    int i = 0;
    int rows = getmaxrow(1);
    // qDebug()<<rows;
    for (i =1; i<=rows;++i)
    {
        if (name == getvalue(1,i,1).toString())
        {
            emit signback(0);
            break;
        }
    }
    if ( i == rows+1)
    {
        emit signback(1);
        setvalue(1,i,1,name);
        setvalue(1,i,2,pwd);
        setvalue(1,i,3,5);
        setvalue(1,i,4,0);
        setvalue(1,i,5,200.0);
    }

}
void MainWindow::checklog(QString name,QString pwd,int state)
{
    int i;
    int rows = getmaxcol(1);
    qDebug()<<rows;
    for (i=1;i<=rows;++i)
    {
        if (name == getvalue(1,i,1).toString())
        {
            if (pwd == getvalue(1,i,2).toString())
            {
                if (state==0&&getvalue(1,i,3)==0){
                    emit toru(name);
                    user =name;
                }
                if (state==0&&getvalue(1,i,3)!=0){
                    emit logback(1);
                }
                if (state==1) {
                    emit touu(name);
                    user=name;
                }
                break;
            }
            else {
                emit logback(0);
                break;
            }
        }
    }
    if (i>rows){
        emit logback(1);
    }
    else {
        emit logback(2);
    }
}



//接受转换动作
void MainWindow::switchs()
{
    //cp界面
    connect(cp1,&cp::toli,this,[&](){
        SW->setCurrentIndex(1);});
    connect(cp1,&cp::toli,li1,&li::ch_state);
    //li界面
    connect(li1,&li::tocp,this ,[&](){
        SW->setCurrentIndex(0);});
    connect(this,&MainWindow::toru,this,[&](){
        SW->setCurrentIndex(3);});
    connect(this,&MainWindow::touu,this,[&](){
        SW->setCurrentIndex(2);});
    //ru界面
    connect(ru1,&ru::tocp,this,[&](){
        SW->setCurrentIndex(0);});
    connect(ru1,&ru::topp,this,[&](){
        SW->setCurrentIndex(6);});
    connect(ru1,&ru::tocgtk,this,[&](){
        SW->setCurrentIndex(7);
    });
    //bt
    connect(bt1,&bt::toct,this,[&](){
    SW->setCurrentIndex(5);});

    //uu界面
    connect(uu1,&uu::tocp,this,[&](){
        SW->setCurrentIndex(0);});
    connect(uu1,&uu::toct,this,[&](){
        SW->setCurrentIndex(5);});
    connect(uu1,&uu::totp,this,[&](){
        SW->setCurrentIndex(8);});
    //ct界面
    connect(ct1,&ct::tobt,this,[&](){
        SW->setCurrentIndex(4);});
    connect(ct1,&ct::touu,this,[&](){
        SW->setCurrentIndex(2);});
    connect(bt1,&bt::toct,this,[&](){
        SW->setCurrentIndex(5);});
    //pp界面
    connect(pp1,&pp::toru,this,[&](){
        SW->setCurrentIndex(3);});
    connect(ru1,&ru::tocgtk,this,[&](){
        SW->setCurrentIndex(7);
    });
    //cgtk界面
    connect(cgtk1,&cgtk::toru,this,[&](){
        SW->setCurrentIndex(3);    
    });
    connect(tp1,&TicketWindow::touu,this,[&](){
        SW->setCurrentIndex(2);});
}
void MainWindow::otherslot()
{
    connect(this,&MainWindow::signback,li1,&li::signback);
    connect(this ,&MainWindow::logback,li1,&li::logback);
    connect(this,&MainWindow::topai,pp1,&pp::data_back);
    connect(this,&MainWindow::backfilm,ct1,&ct::setfilm);
    // connect(this,&MainWindow::backticket,bt1,&bt::);
    connect(this,&MainWindow::toru,ru1,&ru::getuser);
    connect(this,&MainWindow::touu,uu1,&uu::getuser);
}
void MainWindow::sheetwork()
{
    connect(li1,&li::sign,this,[&](QString name,QString pwd){
        checksign(name,pwd);
    });
    connect(li1,&li::log,this,[&](QString name ,QString pwd ,int state){
        checklog(name,pwd,state);
    });
    connect(cgtk1,&cgtk::set_price,this,[&](int film,double price){
        int row = getrow(5,1,film);
        setvalue(5,row,3,price);
    });
    connect(pp1,&pp::send_data,this ,&MainWindow::set_pian);
    connect(ct1,&ct::getfilm,this,&MainWindow::getfilm);
    connect(ct1,&ct::tobt,this,&MainWindow::getticket);
    connect(this,&MainWindow::backticket,bt1,&bt::recv_set);
    connect(bt1,&bt::buy_ticket,this ,&MainWindow::buy_ticket);

}
MainWindow::~MainWindow()
{
    delete timer; // 清理定时器
    workbook->dynamicCall("Save()");
    workbook->dynamicCall("Close()");
    excel->dynamicCall("Quit()");
    delete workbook;
    delete excel;
    delete SW;
    delete ui;

}
void MainWindow::allori()
{
    resize(1200,800);
    //主界面,创建所有的界面对象，放到这里保存，并接受跳转
    //创建切换堆栈
    SW = new QStackedWidget(this);
    //创建窗口
    cp1 = new cp();
    pp1 = new pp();
    li1 = new li();
    ru1 = new ru();
    uu1 = new uu();
    bt1 = new bt();
    ct1 = new ct();
    cgtk1 = new cgtk();
    tp1 = new TicketWindow();

    //将窗口放入堆栈
    SW->addWidget(cp1);//0
    SW->addWidget(li1);//1
    SW->addWidget(uu1);//2
    SW->addWidget(ru1);//3
    SW->addWidget(bt1);//4
    SW->addWidget(ct1);//5
    SW->addWidget(pp1);//6
    SW->addWidget(cgtk1);//7
    SW->addWidget(tp1);//8
    setCentralWidget(SW);
    SW->setCurrentIndex(0);
}
void MainWindow::openexcel()
{
    filePath = "D:\\Desktop\\test.xlsx";
    excel = new QAxObject("Excel.Application");
    excel->setProperty("Visible", true);
    workbook = excel->querySubObject("Workbooks")->querySubObject("Open(const QString&)", filePath);
    sheets = workbook->querySubObject("Sheets");
}
void MainWindow::setvalue(int i,int row ,int col, QVariant value)
{
    sheets->querySubObject("Item(int)", i)->querySubObject("Cells(int,int)", row, col)->setProperty("Value", value);
}
QVariant MainWindow::getvalue(int i,int row ,int col)
{
    return sheets->querySubObject("Item(int)", i)->querySubObject("Cells(int,int)", row, col)->dynamicCall("Value");
}
int MainWindow::getmaxcol(int i)
{
    QAxObject* sheet = sheets->querySubObject("Item(int)", i);
    QAxObject* usedRange = sheet->querySubObject("UsedRange");
    QAxObject* columns = usedRange->querySubObject("Columns");
    QVariant countVariant = columns->property("Count");
    int rowCount = countVariant.toInt();
    return rowCount;
}
int MainWindow::getmaxrow(int i)
{
    QAxObject* sheet = sheets->querySubObject("Item(int)", i);
    QAxObject* usedRange = sheet->querySubObject("UsedRange");
    QAxObject* rows = usedRange->querySubObject("Rows");
    QVariant countVariant = rows->property("Count");
    int rowCount = countVariant.toInt();
    return rowCount;
}
int MainWindow::getrow(int i,int col,QVariant value)
{

    int max = getmaxrow(i);
    for (int row=1;row<=max;row++)
    {
        if (getvalue(i,row,col)==value)
        {
            return row;
        }
    }
    return 0;
}
int MainWindow::getcol(int i,int row,QVariant value)
{
    int max = getmaxcol(i);
    for (int col=1;col<=max;col++)
    {
        if (getvalue(i,row,col)==value)
        {
            return col;
        }
    }
    return 0;
}

void MainWindow::set_pian(int daytime,int time,int house ,int film)
{

    if (daytime==1)//需要进行时间判断
    {
        QTime time1(10, 0); // 10:00
        QTime time2(6, 0);  // 06:00
        QTime time3(14, 0); // 14:00
        QDateTime specifiedTime1(currentDate, time1);
        QDateTime specifiedTime2(currentDate, time2);
        QDateTime specifiedTime3(currentDate, time3);

        if (time==1)
        {
            if (currentTime>=specifiedTime1)
            {
                emit topai(1);
            }
            else {
                check_and_set(daytime,time,house ,film);
            }
        }
        if (time==2)
        {
            if (currentTime>=specifiedTime2)
            {
                emit topai(1);
            }
            else {
                check_and_set(daytime,time,house ,film);
            }
        }

        if (time==3)
        {
            if (currentTime>=specifiedTime3)
            {
                emit topai(1);
            }
            else {
                check_and_set(daytime,time,house ,film);
            }
        }

    }
    else {   //直接判断就行
        check_and_set(daytime,time,house ,film);
    }
}
void MainWindow::check_and_set(int daytime,int time,int house ,int film)
{
    int minrow = (daytime-1)*12+(time-1)*4 + 1;
    int mincol = (house-1)*5 + 1;
    int state = 1;
    for (int row = minrow;row<minrow+4;++row)
    {
        for (int col =mincol;col<mincol+5;++col)
        {
            if (getvalue(4,row,col).toInt()<0)
            {
                state = 0;
                break;
            }
        }
        if (state==0)
        {
            emit topai(2);
            break;
        }
    }
    if (state==1){
        for (int row = minrow;row<minrow+4;++row)
        {
            for (int col =mincol;col<mincol+5;++col)
            {
                setvalue(4,row,col,film);
            }
        }
        emit topai(0);
    }
}
void MainWindow::time_torenew()
{
    QTime scheduledTime(23, 0, 0); // 每天晚上11点

    // 获取当前时间
    QDateTime currentDateTime = QDateTime::currentDateTime();
    QDate dateToday = currentDateTime.date();

    // 构造下一个执行时间
    QDateTime nextScheduledTime(dateToday, scheduledTime);
    if (nextScheduledTime <= currentDateTime) {  // 如果当前时间已超过今天的11点，则设为明天的11点
        nextScheduledTime = nextScheduledTime.addDays(1);
    }

    // 计算距离下一个执行时间的毫秒数
    qint64 interval = currentDateTime.msecsTo(nextScheduledTime);

    // 创建定时器
    timer = new QTimer(this);
    connect(timer, &QTimer::timeout, this, &MainWindow::renew_ticket);

    // 启动定时器并设置间隔
    timer->start(interval);

    // 如果希望后续也能进行定时操作，可以重新设置间隔
    connect(timer, &QTimer::timeout, [this]() {
        timer->start(24 * 60 * 60 * 1000); // 每24小时执行一次
    });
}
void MainWindow::renew_ticket()
{
    //第二天放到第一天
    for (int row =1 ;row<=12;++row)
    {
        for(int col =1;col<=25;++col)
        {
            int value = getvalue(4,row+12,col+12).toInt();
            setvalue(4,row,col,value);
        }
    }
    //第三天放到第二天
    for (int row =13 ;row<=24;++row)
    {
        for(int col =1;col<=25;++col)
        {
            int value = getvalue(4,row+12,col+12).toInt();
            setvalue(4,row,col,value);

        }
    }
    //第三天清零

    for (int row = 25 ; row <= 36; ++row)
    {
        for (int col =1 ; col <= 25 ; ++col)
        {
            setvalue(4,row,col,0);
        }
    }
}

void MainWindow::getfilm(int house ,int daytime)
{
    QString first = "";
    QString second = "";
    QString third = "";
    int ints[3];
    ints[0] = qAbs(getvalue(4,12*(daytime-1)+4,5*house).toInt());
    ints[1] = qAbs(getvalue(4,12*(daytime-1)+8,5*house).toInt());
    ints[2] = qAbs(getvalue(4,12*(daytime-1)+12,5*house).toInt());
    if (ints[0]!=0)
    {
        first = getvalue(5,ints[0],2).toString();
    }
    if (ints[1]!=0)
    {
        second = getvalue(5,ints[1],2).toString();
    }
    if (ints[2]!=0)
    {
        third = getvalue(5,ints[2],2).toString();
    }
    emit backfilm(first,second,third);
}
void MainWindow::getticket(int house ,int daytime,int time)
{
    qDebug()<<house<<daytime<<time;
    int  tickets[4][5];
    int minrow = (daytime-1)*12 + 1 + (time-1)*4;
    int mincol = 5*(house-1)+1;
    int x=0;
    int y=0;
    for (int row=minrow;row<minrow+4;row++)
    {
        y=0;
        for (int col=mincol;col<mincol+5;col++)
        {

            tickets[x][y] = getvalue(4,row,col).toInt();
            y++;
        }
        x++;
    }
    emit backticket(tickets);
}
void MainWindow::buy_ticket(QList<int> rows,QList<int>  cols)
{

}
