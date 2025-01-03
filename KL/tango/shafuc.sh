#!/usr/bin/bash
# bash for sha workz
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
    echo -e "${CYAN} ===================================="
    echo -e "Sha/adi.com workz"
    echo -e "====================================${CYAN}"
}

c1() {
    # Running a standard nmap scan
    echo ""
    CO1="nmap -sV -O shaadi.com"
    echo -e "${GREEN}[+] ${CO1} ${NC}"
    ${CO1}
    echo "~~~DONE~~~"
}

# Execution
b1
c1
