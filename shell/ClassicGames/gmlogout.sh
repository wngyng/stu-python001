#!/bin/bash
#label:wangy
#date:22-5-18

logpath=./Accountfile.log
. ./picture.sh


gmlogout(){
#账号注销   $1为账号名
while :
do
clear
picture2

	read -p "请输入账户名
(按q或空,返回上一级):" name
        [ -z $name ] && break
	[ $name == "q" ] && break
	#验证账户是否存在
        [ -z `awk -F "[ =]+" '$2~/^'"$name"'$/{print $2}' $logpath` ] && echo "账户名不存在！" && continue
        mailname=`awk -F "[ =]+" '$2~/^'"$name"'$/{print $10}' $logpath`
        echo "验证已发送邮箱：$mailname"
       mailVerif $mailname
       [ $? -eq 1 ] && echo "验证邮箱失败" && break
	echo "邮箱验证成功" 
	while :
	do
		read -p "二次确认，是否删除?
（删除,按y,取消按n)" x
		if [ $x == "y" ];then
			row=`awk -F "[ =]+" '$2~/'"$name"'/{print NR}' $logpath`
			`sed -i ''"$row"'d' $logpath`     # 删除指定行
			echo "删除成功"
			sleep 4
			break 2
		elif [ $x == "n" ];then 
			echo "取消删除"
			sleep 4
			break 
		else 
			echo "输入错误，重新输入"
			sleep 4
		fi
	done
done
}
