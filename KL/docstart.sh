#!/usr/bin/bash
# List and start the docker contatiner
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
    echo -e "${BLUE} ======================"
    echo -e "1. List docker container "
    echo -e "2. Start Container"
    echo -e "3. Get inside container"
    echo -e " ======================${NC}"
}

c1() {
    C1A="docker container ls -a"
    C1B="docker start pussy"
    C1C="docker exec -it pussy bash"
    echo -e "${GREEN} ${C1A} "
    echo -e "${GREEN} ${C1B} "
    echo -e "${GREEN} ${C1C} ${NC}"
    ${C1A} && ${C1B} && ${C1C}
}

# Execution
b1
c1
