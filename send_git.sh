

#!/bin/sh

#usage(op1,op2){
#    echo $0 op1 op2;
#    return 0
#}
usage() {
    echo $0 'target'
    echo '***** usage finish *****'
}
#while getopts "hn:p:" OPT #n: p: はoptionに引数必須/hは引数を取れない/先頭に:でエラー処理必須
#do
#    case $OPT in
#    h)usage;;
#    n)next=$OPTARG;;
#    p)preview=$OPTARG;;
#    esac
#done

#usage op1 op2
#echo $next

#sh $0 -n sample

git add .
git commit -m $1
git status
git push origin master
