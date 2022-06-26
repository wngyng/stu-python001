#!/bin/bash
#label:wangy
#date:22-5-17
#this is gmblacklist

. ./gmregister.sh #传入邮箱验证函数用
logpath="./Accountfile.log"
. ./picture.sh

changebl() {
	#---修改黑名单状态---
	# $1传入更改的账户名;
	# 修改bldate=后的值为$2

	row=$(grep -wn $1 $logpath | awk -F ":" '{print $1}')
	$(sed -i ''"$row"'s/bldate=[0-9]*/bldate='"$2"'/g' $logpath)
}

gmblacklist() {
	#----邮箱申诉函数--------

	clear
	picture4

	while :; do
		echo "
---------------------已进入黑名单申诉程序----------------------"

		read -p "请输入账户名：
(按q,返回上一级)" name
		[ $name == "q" ] && break
		#验证账户是否存在
		[ -z $(awk -F "[ =]+" '$2~/^'"$name"'$/{print $2}' $logpath) ] && echo "账户名不存在！" && continue
		mailname=$(awk -F "[ =]+" '$2~/^'"$name"'$/{print $10}' $logpath)
		echo "验证已发送邮箱：$mailname"
		mailVerif $mailname
		[ $? -eq 0 ] && changebl $name "0" && echo "申诉成功" && break || echo "验证邮箱失败"
	done
}

reClear() {
	#----定时清理黑名单---- ;$1为账户名
	name=$1
	today=$(date +%Y%m%d)
	bldate=$(awk -F "[ =]+" '$2~/^'"$name"'$/{print $6}' $logpath)

	if [ $bldate -eq 0 ]; then
		echo "不在黑名单"
	elif [ $bldate -le $today ]; then
		changebl $name 0
		echo "超过10天,已移除黑名单！"
	fi
}
