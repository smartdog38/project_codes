#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QPropertyAnimation>
#include <QParallelAnimationGroup>
#include <QSequentialAnimationGroup>
#include <QGraphicsOpacityEffect>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    //scale
    QPropertyAnimation *pScaleAnimation1 = new QPropertyAnimation(ui->scaleButton, "geometry");
    pScaleAnimation1->setDuration(1000);
    pScaleAnimation1->setStartValue(QRect(190, 500, 0, 0));//(起始横坐标，起始纵坐标，起始窗口长度，起始窗口宽度)
    pScaleAnimation1->setEndValue(QRect(120, 160, 140, 140));//(末尾横坐标，末尾纵坐标，末尾窗口长度，末尾窗口宽度)
    pScaleAnimation1->setEasingCurve(QEasingCurve::InOutQuad);

    QPropertyAnimation *pScaleAnimation2 = new QPropertyAnimation(ui->scaleButton, "geometry");
    pScaleAnimation2->setDuration(1000);
    pScaleAnimation2->setStartValue(QRect(120, 160, 140, 140));//(起始横坐标，起始纵坐标，起始窗口长度，起始窗口宽度)
    pScaleAnimation2->setEndValue(QRect(190, 230, 0, 0));//(末尾横坐标，末尾纵坐标，末尾窗口长度，末尾窗口宽度)
    pScaleAnimation2->setEasingCurve(QEasingCurve::InOutQuad);

    QSequentialAnimationGroup *pScaleGroup = new QSequentialAnimationGroup(this);
    pScaleGroup->addAnimation(pScaleAnimation1);
    pScaleGroup->addAnimation(pScaleAnimation2);
    ui->scaleButton->setText("这是一个提示");
    ui->startButton->setText("提示");
    m_group = new QParallelAnimationGroup(this);
    m_group->addAnimation(pScaleGroup);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_startButton_clicked()
{
    m_group->setDirection(QAbstractAnimation::Forward);
    m_group->setLoopCount(1);
    m_group->start();
}

void MainWindow::on_startButton_3_clicked()
{
    m_group->setDirection(QAbstractAnimation::Backward);
    m_group->setLoopCount(1);
    m_group->start();
}

void MainWindow::on_startButton_2_clicked()
{
    m_group->setDirection(QAbstractAnimation::Forward);
    m_group->setLoopCount(-1);
    m_group->start();
}


