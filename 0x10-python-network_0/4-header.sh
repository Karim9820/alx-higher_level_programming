#!/bin/bash
# takes in a URL as an argument, sends a GET request to the URL
# displays the body of the response.
# header variable X-School-User-Id must be sent with the value 98
curl -sH "X-School-User-Id: 98" "$1"
