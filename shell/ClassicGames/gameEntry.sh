#!/bin/bash
#label:wangy
#date:22-5-14
. ./gmlogin.sh
. ./gmregister.sh
. ./gmblacklist.sh
. ./gmlogout.sh
. ./picture.sh

while :; do
	clear
	picture1
	read -p "1、账号登录
2、账号注册
3、账号注销
4、黑名单申诉
5、或任意键退出
请选择：" m
	case $m in
	1)
		gmlogin
		;;
	2)
		gmregister
		;;
	3)
		gmlogout
		;;
	4)
		gmblacklist
		;;
	*)
		echo "已退出！！！"
		exit 1
		;;
	esac
done
