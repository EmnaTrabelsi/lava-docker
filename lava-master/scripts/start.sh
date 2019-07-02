#!/bin/bash

#/setup.sh || exit $?

cp /setup.sh /root/entrypoint.d/

/root/entrypoint.sh
exit 0

