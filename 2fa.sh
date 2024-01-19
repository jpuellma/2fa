#!/usr/bin/env bash
daemon=false
source ~/.totp_keys.sh
IFS=$'\n' sorted=($(sort <<<"${!totp[*]}"))
unset IFS
function do_get_keys() {
  for i in ${sorted[@]}; do
    k=$(oathtool --base32 --totp ${totp[${i}]})
    echo "${k}" "${i}"
  done
}

c=$(tput clear)
if [[ _${1} == "_-d" ]]; then
  while :; do
    printf "%s" ${c}
    do_get_keys
    sleep 5
  done
elif [[ _${1} == "_-r" ]]; then
  printf "${tput_set_bold}Press Enter for new keys.${tput_reset}\n"
  while read; do
    printf "%s" ${c}
    do_get_keys
    printf "${tput_set_bold}Press Enter for new keys.${tput_reset}"
  done
elif [[ _${1} != "_" ]]; then
  do_get_keys | grep -i "${1}"
else
  do_get_keys
fi

if [[ $1 -gt 0 ]]; then
  echo Sleeping $1 seconds...
  sleep $1
fi

