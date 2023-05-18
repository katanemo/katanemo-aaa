
log() {
  echo `date "+%Y-%m-%dT%H:%M:%S%z"` " - " "${@}"
}

EHR_ADMIN_PASSWORD=7TOfroc9aab3$
SUBSCRIBER_PASSWORD=7TOfroc9aab3$
DOCTOR_PASSWORD=7TOfroc9aab3$

# source https://gist.github.com/thomasdarimont/46358bc8167fce059d83a1ebdb92b0e7

decode_base64_url() {
  local len=$((${#1} % 4))
  local result="$1"
  if [ $len -eq 2 ]; then result="$1"'=='
  elif [ $len -eq 3 ]; then result="$1"'='
  fi
  echo "$result" | tr '_-' '/+' | openssl enc -d -base64
}

decode_jwt(){
   decode_base64_url $(echo -n $2 | cut -d "." -f $1) | jq .
}

# Decode JWT header
alias jwth="decode_jwt 1"

# Decode JWT Payload
alias jwtp="decode_jwt 2"
