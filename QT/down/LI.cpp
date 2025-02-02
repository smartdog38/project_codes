#include "LI.h"
#include<QDebug>


li::li(QWidget *parent) : QWidget(parent)
{
    ori();
    works();






}


li::~li()
{}


void li::login()
{
    QString name = usernameLineEdit->text();
    QString pwd = passwordLineEdit->text();
    emit log(name,pwd,state);//state代表是用户还是管理员
}

void li::works()
{
    connect(loginButton,&QPushButton::clicked,this,[&](){
        login();
    });
    connect(backButton,&QPushButton::clicked,this,[&](){
        emit tocp();
        usernameLineEdit->clear();
        passwordLineEdit->clear();
        signInButton->setVisible(true);
    });
    connect(signInButton,&QPushButton::clicked,this,[&](){
        signin();
    });


}
void li::signin()
{
    QString name = usernameLineEdit->text();
    QString pwd = passwordLineEdit->text();
    emit sign(name,pwd);
}
void li::ori()
{
    resize(400, 500);  // 设置窗口大小
    mainLayout = new QVBoxLayout(this);
    mainLayout->setSpacing(10);
    mainLayout->setContentsMargins(20, 20, 20, 20);

    // 标签和返回按钮的布局
    headerLayout = new QHBoxLayout();

    // 返回按钮
    backButton = new QPushButton("返回", this);
    backButton->setFixedSize(40,30);
    backButton->setStyleSheet(
        "background-color: #f44336; color: white; border: none; border-radius: 5px;"
        "padding: 5px;"
        "font-size: 14px;"
        "}"
        "QPushButton:hover { background-color: #d32f2f; }" // 鼠标悬停背景色
        );
    // 标签
    titleLabel = new QLabel("登录/注册", this);
    titleLabel->setFixedHeight(60);
    titleLabel->setStyleSheet("font-size: 24px; font-weight: bold; color: #333;");

    // 添加返回按钮和标题到headerLayout
    headerLayout->addWidget(backButton);
    headerLayout->addSpacerItem(new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Fixed)); // 添加弹性空间
    headerLayout->addWidget(titleLabel);

    mainLayout->addLayout(headerLayout); // 将headerLayout添加到主布局

    // 用户名标签和输入框
    usernameLabel = new QLabel("Username", this);
    usernameLabel->setFixedHeight(30);
    usernameLabel->setStyleSheet("font-size: 16px; color: #555;");

    usernameLineEdit = new QLineEdit();
    usernameLineEdit->setPlaceholderText("请输入账号名");
    usernameLineEdit->setFixedHeight(40);
    usernameLineEdit->setMaxLength(50);
    usernameLineEdit->setStyleSheet("padding: 5px; border: 1px solid #aaa; border-radius: 5px;");

    // 密码标签和输入框
    passwordLabel = new QLabel("Password", this);
    passwordLabel->setFixedHeight(30);
    passwordLabel->setStyleSheet("font-size: 16px; color: #555;");

    passwordLineEdit = new QLineEdit();
    passwordLineEdit->setPlaceholderText("请输入密码");
    passwordLineEdit->setFixedHeight(40);
    passwordLineEdit->setMaxLength(50);
    passwordLineEdit->setEchoMode(QLineEdit::Password);
    passwordLineEdit->setStyleSheet("padding: 5px; border: 1px solid #aaa; border-radius: 5px;");

    // 按钮
    signInButton = new QPushButton("Sign In", this);
    signInButton->setFixedHeight(40);
    signInButton->setStyleSheet("background-color: #4CAF50; color: white; border: none; border-radius: 5px;");

    loginButton = new QPushButton("Log In", this);
    loginButton->setFixedHeight(40);
    loginButton->setStyleSheet("background-color: #2196F3; color: white; border: none; border-radius: 5px;");

    // 用户名布局
    usernameLayout = new QHBoxLayout();
    usernameLayout->addWidget(usernameLabel);
    usernameLayout->addWidget(usernameLineEdit);
    mainLayout->addLayout(usernameLayout);

    // 密码布局
    passwordLayout = new QHBoxLayout();
    passwordLayout->addWidget(passwordLabel);
    passwordLayout->addWidget(passwordLineEdit);
    mainLayout->addLayout(passwordLayout);

    // 按钮布局
    buttonLayout = new QVBoxLayout();
    buttonLayout->addWidget(signInButton);
    buttonLayout->addWidget(loginButton);
    mainLayout->addLayout(buttonLayout);

    // 设置主窗口的样式
    setLayout(mainLayout);
    setWindowTitle("Login Form");
    setStyleSheet("background-color: #f9f9f9;");
}
void li::signback(int i)
{
    if (i==1)
    {
        QMessageBox::information(this,"注册","您已成功注册！");
        usernameLineEdit->clear();
        passwordLineEdit->clear();
    }
    else{
        QMessageBox::information(this,"注册","该用户已存在！");
        usernameLineEdit->clear();
        passwordLineEdit->clear();

    }
}
void li::logback(int i)
{
    if (i==0)
    {
        QMessageBox::warning(this,"登录","密码错误");
    }
    if (i == 1) {
        QMessageBox::warning(this,"登录","用户名错误");
    }
    else {
        usernameLineEdit->clear();
        passwordLineEdit->clear();
    }
}
void li::ch_state(int i)
{
    if (i==0)
    {
        state = 0;
        signInButton->setVisible(false);
    }
    else{
        state = 1;
        signInButton->setVisible(true);
    }
}
