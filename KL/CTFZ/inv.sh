#!/usr/bin/bash
# Investigation of htbctf -
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

# Machine
MACHINE_IP="10.129.147.243"

# Commands
b1() {
    echo -e "${CYAN} ======================"
    echo -e "Investigative worh for htb - ${MACHINE_IP}"
    echo -e " ======================${NC}"
}

c1() {
    COM2="nmap ${MACHINE_IP} -PR"
    echo -e "${PURPLE}[=]${COM2} ${NC} "
    ${COM2}
    echo -e "${GREEN}[+]${COM2} "
}

c2() {
    COM1="nmap -sV -O ${MACHINE_IP}"
    echo -e "${PURPLE}[=]${COM1} ${NC} "
    ${COM1}
    echo -e "${GREEN}[+]${COM1} "
}

# Execution
b1
c1
c2
