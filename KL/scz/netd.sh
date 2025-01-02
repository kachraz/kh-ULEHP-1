#!/usr/bin/bash
# Runnin netdiscover
clear

# Colors
export RED='\033[0;31m'
export GREEN='\033[0;32m'
export YELLOW='\033[0;33m'
export BLUE='\033[0;34m'
export PURPLE='\033[0;35m'
export CYAN='\033[0;36m'
export WHITE='\033[0;37m'
export NC='\033[0m' # No Color

# Commands
b1() {
    echo -e "${CYAN} ======================"
    echo -e "Running Netdiscoery on internal network"
    echo -e " ======================${NC}"
}

c1() {
    TAR="10.10.245.122"
    COM1="netdiscover -r ${TAR}/24"
    echo -e "${GREEN} ${COM1} ${NC}"
    ${COM1}
}

# Execution
b1
c1
