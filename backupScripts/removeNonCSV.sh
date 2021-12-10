for file in *.log;
do
	sed '/\,/!d' $file > "formatted${file}"
done
