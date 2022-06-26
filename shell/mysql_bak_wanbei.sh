#!/bin/bash
# MySQL数据库完全备份脚本
#设置登录变量
MY_USER="root"
MY_PASS="123123"
MY_HOST="192.168.200.136"
MY_CONN=" -u $MY_USER -p$MY_PASS -h $MY_HOST"
#设置备份的数据库(或表)
MY_DB="yun1"
#定义备份路径、工具、时间、文件名
BF_DIR="/home/pc/pyproject/shell/mysql_bak/wanbei"
BF_CMD="/usr/bin/mysqldump"
BF_TIME=$(date +%Y%m%d-%H%M)
NAME="$MY_DB-$BF_TIME"
#备份为.sql脚本，然后打包压缩(打包后删除原文件)
[ -d $BF_DIR ] || mkdir -p $BF_DIR
cd $BF_DIR || exit
$BF_CMD --column-statistics=0 $MY_CONN --databases $MY_DB >"$NAME".sql
usr/bin/tar zcf "$NAME".tar.gz "$NAME".sql --remove &>/dev/null
