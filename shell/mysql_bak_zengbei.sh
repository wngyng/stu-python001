#!/bin/bash
# MySQL数据库增量备份脚本
#设置登录变量
MY_USER="root"
MY_PASS="123123"
MY_HOST="192.168.200.136"
MY_CONN="-u$MY_USER-p$MY_PASS-h$MY_HOST"
#定义备份路径、工具、二进制日志前缀、二进制日志存放路径
BF_TIME="$(date +%Y%m%d)"
BF_DIR="/mysql_bak/zengbei/$BF_TIME"
CMD="/usr/bin/mysqladmin"
QZ="mysql-bin"
LOG_DIR="/var/lib/mysql"
#拷贝二进制日志
[ -d "$BF_DIR" ] || mkdir-p $BF_DIR
$CMD $MY_CONN flush-logs
/bin/cp -p $(ls $LOG_DIR/$QZ.* |awk-v RS="" '{print $(NF-2)}') "$BF_DIR"
