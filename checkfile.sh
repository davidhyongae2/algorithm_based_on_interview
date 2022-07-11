#!/bin/bash
echo "checkfilelog.sh [pathname]" 
echo "[pathname] = /Users/dgae/coding"

file=.
function1() {
echo "checked today"
find $file -name "*.py" -type f -mtime -1
find $file -name "*.h" -type f -mtime 1
find $file -name "*.py" -type f -mtime 1
find $file -name "*.js" -type f -mtime 1
find $file -name "*.tcl" -type f -mtime 1 
find $file -name "*.mov" -type f -mtime 1
find $file -name "*.pptx" -type f -mtime 1
find $file -name "*.docx" -type f -mtime 1
find $file -name "*.xlsx" -type f -mtime 1
find $file -name "*.conf" -type f -mtime 1
find $file -name "*.ai" -type f -mtime 1

echo "checked 20 days ago"
find $file -name "*.c" -type f -mtime -20
find $file -name "*.h" -type f -mtime -20
find $file -name "*.py" -type f -mtime -20
find $file -name "*.js" -type f -mtime -20
find $file -name "*.tcl" -type f -mtime -20
find $file -name "*.mov" -type f -mtime -20
find $file -name "*.pptx" -type f -mtime -20
find $file -name "*.docx" -type f -mtime -20
find $file -name "*.xlsx" -type f -mtime -20
find $file -name "*.conf" -type f -mtime -20
find $file -name "*.ai" -type f -mtime -20
}
function1
exit 0
