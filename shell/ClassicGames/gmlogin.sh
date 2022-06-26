#!/usr/bin/bash
#label:wangy
#date:22-5-15
#this is gmlogin
#shellcheck source=/dev/null

logpath="./Accountfile.log"
. ./gmblacklist.sh
. ./picture.sh

gmlogin() {
  #  ----登录函数-----------
  #clear
  picture6

  while :; do

    count=3
    echo "已进入账号登录状态"
    #验证账户是否存在
    read -rp "请输入用户名
(或按q返回上一级):" name
    [ "$name" == "q" ] && break
    [ -z "$(awk -F "[ =]+" '$2~/^'"$name"'$/{print $2}' $logpath)" ] && echo "账户名不存在！" && continue

    reClear "$name" #超过10天取消黑名单

    #验证是否在黑名单中
    [ "$(awk -F "[ =]+" '$2~/^'"$name"'$/{print $6}'$logpath)" -ne 0 ] && echo "账号为黑名单状态，请申诉后登录" && continue

    #验证密码
    while :; do
      read -rp "请输入密码：" pswd
      if [ "$(awk -F "[ =]+" '$2~/^'"$name"'$/{print $4}' $logpath)" != "$pswd" ]; then
        ((count--))
        if [ $count -eq 0 ]; then
          echo "错误次数过多，已加入黑名单"
          bldate=$(date +%Y%m%d --date="+10 day")
          changebl "$name" "$bldate"
          echo "锁定时间至：$bldate"
          sleep 4
          continue 2
        else
          echo "密码错误！,还有$count次机会"
        fi
      else
        break
      fi
    done
    echo "登录成功"
    ./gmmenu.sh "$name" #运行主菜单
    break
  done
}
