#!/bin/bash

REDIRECTED_URL=$(curl -w "%{url_effective}\n" -I -L -s -S $1 -o /dev/null)
CLEAN_URL=https://clearthis.page/?u=${REDIRECTED_URL}
echo $CLEAN_URL
