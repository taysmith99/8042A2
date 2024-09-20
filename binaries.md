./buf
gcc -fno-stack-protector -z execstack -no-pie buf.c -o buf

./pie (Protection: removed -no-pie)
gcc -fno-stack-protector -z execstack buf.c -o pie

