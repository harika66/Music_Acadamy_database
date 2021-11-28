#!/bin/bash

declare -i retry_count=0
while [ $retry_count -lt 10 ]; do
  nmap $1 -p $2 | grep -i open > /dev/null 2>&1
  if [ $? -eq 0 ]; then
    break
  fi
  sleep 5
  ((retry_count = retry_count + 1))
  echo "Tried connecting to $1:$2. $retry_count times "
done
