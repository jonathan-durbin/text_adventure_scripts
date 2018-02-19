#!/bin/bash

echo "adding everything"

git add .

echo "describe your comittment: "

read comittment

git commit -m "$comittment"

echo "do you want to push? (y/n) "

read push

if [ "$push" == "y" ]; then
	echo "pushing"
	git push
else
	echo "will not push"
fi
