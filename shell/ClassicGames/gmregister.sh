#!/bin/bash
#label:wangy
#date:22-5-15
#this is gmregister

logpath="./Accountfile.log"
. ./picture.sh

#先注释掉，需要在开启
mailVerif(){
#----邮箱验证函数--- 输入$1为发送验证码目的邮箱地址，return 0成功，1失败。

RAN=`echo "$RANDOM" | cut -c 1-6`
echo "邮箱验证码：$RAN" | mail -s "验证邮件" $1 &>/dev/null
read -p "请输入邮箱验证码：" mailcode
[ $mailcode == $RAN ] && return 0 || return 1
#return 0
}



gmregister(){
#----账号注册函数----

clear
picture2

echo "
已进入这是注册账号程序"
while :
do 
    read -p "
请输入注册的用户名：
(按q键返回上一级)" newname
    [ $newname == "q" ]&& break
    read -p "请输入6位注册的密码（需要数字加字母）：" newpswd
    #验证文件是否重名
    logname=`awk -F "[ =]+" '{print $2}' $logpath |grep $newname `
    [ ! -z $logname ]&& echo "账户已存在" && sleep 4 && continue 
    #验证密码是否符合要求
    if echo "$newpswd"|grep "[a-zA-Z]" >/dev/null &&echo "$newpswd"|grep "[0-9]" >/dev/null &&  [ "${#newpswd}" -eq 6 ] ;then

	#账号邮箱验证
	while :
	do
	    read -p "请输入注册邮箱：" usermail
	     str=`echo $usermail | egrep "[a-zA-Z0-9\_\-\.]+@[a-zA-Z0-9\_\-]+(\.[a-zA-Z0-9]+)"|grep -n ""`
	    [ ! -z ${str} ]&& echo "邮箱格式符合要求" && break || echo "邮箱格式不合要求" 
	done

	mailVerif $usermail 
	[ $? -eq 1 ] && echo "邮箱验证失败！" && break
	echo "账号$newname注册成功！！！"
	echo "name=$newname password=$newpswd bldate=0 money=0 email=$usermail">> $logpath 
	sleep 4
	break
    else
	echo "密码不符合要求"
    fi
    
done
}

