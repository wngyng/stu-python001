#!/bin/bash
#label:wang
#date:22-5-17


function tiger(){
h=$1	
l=0
while [ "$h" -gt 0 ];do
	RAN=$(echo "$RANDOM" | cut -c 1-3)
	read -rp "请输入3位数，或q退出:" m
	[ "$m" == "q" ] && return "$h"
	(( h-- ))
	((l++))
	if [[ "$m" =~ [^0-9] ]] ;then
	         echo "输入不是纯数字重新输入"
		((h++))
		((l--))
	elif [ "${#m}" -ne 3 ]; then
		 echo "输入非三位数重新输入"
		(( h++ ))
		((l--))
	elif [ $l -ge 10 ];then
		echo "winner"
                l=0
                (( h++ ))
	elif [ "$RAN" -gt "$m" ]; then
		 echo "小了"
	elif [ "$RAN" -lt "$m" ]; then
		 echo "大了"
	elif [ "$RAN" -eq "$m" ]; then
		echo "正确"
		echo "winner"
		(( h++ ))
	fi	
	echo "还有 $h 次机会"
done
return 0
} 

