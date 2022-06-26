#!/bin/bash
#labal:wangy
#date:22-5-12
#this is gmmenu
. ./picture.sh
. ./tiger.sh
#文件路径
logpath="./Accountfile.log"

changeAm(){  
#更改金额：此函数用于更改文档中的金额。$1为账户名，$2为更改成为的金额
name=$1   #把账户名传给变量name
total=$2
row=`grep -wn $name $logpath | awk -F ":" '{print $1}'`
`sed -i ''"$row"'s/money=[0-9]*/money='"$total"'/g' $logpath`
}

#游戏充值函数,把输入的金额与原有金额相加后存入记录金额位置
recharge(){
while :  #判断输入是否是数字
do
    read -p "输入充值金额：" am
    #验证数字是否符合要求
    [ -z `echo $am | grep [^0-9]` ]&& break ||echo "输入非纯数字！";continue
done
#更改金额
name=$1   #把登录成功的账户名传给变量name
echo "账号名$name"
balance=`awk -F "[ =]+" '$2~/^'"$1"'$/{print $8}' $logpath`
((total=$am + $balance))
changeAm $name $total
#打印充值后余额
echo "账户余额：`awk -F "[ =]+" '$2~/^'"$1"'$/{print $8}' $logpath`"
}


#菜单主程序
while :
do
#clear
picture3
echo "
-------------------------------    欢迎玩家：$1     ---------------------------------
-------------------------------    已进入游戏菜单     ------------------------------- "
balance=`awk -F "[ =]+" '$2~/^'"$1"'$/{print $8}' $logpath`
echo "当前账户余额:$balance"

read -p "1、进入贪吃蛇游戏
2、进入老虎机游戏
3、进入俄罗斯方块游戏
4、游戏充值
5、或任意键退出登录
请选择：" m
case $m in
        1)
	if [ $balance -ge 1 ] ;then
        	((total=$balance -1))
		changeAm $1 $total
		./snake.sh
		continue
	else
		echo "账户余额不足"
		sleep 4
	fi
        ;;
        2)
	if [ $balance -ge 1 ] ;then
		tiger $balance
		changeAm $1 $?
		continue
        else
              echo "账户余额不足"
		sleep 4
	fi	
        ;;
        3)
	if [ $balance -ge 1 ] ;then
               ((total=$balance -1))
               changeAm $1 $total
               ./elsfk.sh
               continue
        else
              echo "账户余额不足"
		sleep 4
        fi
        ;;
        4)
       recharge $1  #充值
        ;;
        *)
        echo "已退出登录！！！"
	sleep 4
        break
esac
done

