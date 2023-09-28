#!/bin/bash
#this bash script prints the size of the body of the response
curl -s $1 | wc -c 
