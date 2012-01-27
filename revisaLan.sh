#/bin/sh

ip=$1

valorPing=` ping -s $ip 500 1 | grep packets`
fecha=`date`

echo "$fecha //// $valorPing " >> /tmp/conectividad.log
