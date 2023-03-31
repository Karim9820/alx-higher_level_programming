#!/bin/bash
# Bash scripts that sends a POST request to a given URL.
# email must be sent with the value test@gmail.com
# variable subject must be sent with the value I will always be here for PLD
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
