#!/bin/bash
echo "---"
echo "classes:"
if [ "$1" = "$(hostname)" ]
then
         echo "   - role::config_master"
else
         echo "   role::lightweight_component:"
         echo "       id: 1"
fi
exit 0