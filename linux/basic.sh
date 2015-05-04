# Run backgrouind task
nohup /path/script.sh > /dev/null 2>&1 &

# Compresion de archivos
tar -zcvf file.tar.gz file1 file2 ... dir1 dir2 ...
tar -zxvf file.tar.gz
tar -zxvf file.tar.gz -C /tmp/extractHere/

# add shared library
vi /etc/ld.so.conf
vi /etc/ld.so.conf.d/libc.conf
sudo ldconfig

