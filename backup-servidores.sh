#!/bin/bash

TIMESTAMP=$(date +"%F")
BACKUP_DIR="/backup/server_configs_$TIMESTAMP"
mkdir -p $BACKUP_DIR

cp /etc/nginx/nginx.conf $BACKUP_DIR/
cp /etc/ssh/sshd_config $BACKUP_DIR/
cp /etc/mysql/my.cnf $BACKUP_DIR/

tar -czvf $BACKUP_DIR.tar.gz $BACKUP_DIR
rm -rf $BACKUP_DIR

echo "Backup completed and saved as $BACKUP_DIR.tar.gz"
