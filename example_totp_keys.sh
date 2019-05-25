#!/usr/bin/env bash
# This is sourced by the 2fa utility in order to create an array of secret keys
# in the shell.
#
# To add an account, replace "Account_Name" with a description of the account.
# Replace "username" with the identity. Replace "secretKey" with the secret
# string for that account.
#
declare -A totp
totp[Account_Name/username]=secretKey
totp[Account_Name/username]=secretKey
totp[Account_Name/username]=secretKey
export totp
