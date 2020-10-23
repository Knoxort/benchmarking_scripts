#!/bin/bash

#uniform vs part_swept

#This really needs to be a case by case variable name

#Shouldn't need this anymore, as
#export PATH=/g/g19/trokon/workspace/cmt_Nek_BE_Instrumentation_repo/bin:$PATH

echo shktb > SESSION.NAME
echo `pwd`'/' >> SESSION.NAME

#./makenek clean #I couldn't find out how to make the yes command automatically accept, so,
#for now, it's just not accepted
./makenek shktb

FILE="nek5000"
DIR="${PWD##*/}"

if [ -f "$FILE" ];
then


	#Start actual job file 
	echo "#!/bin/bash" > fdt_gen.sh
	echo "######These are Moab commands" >> fdt_gen.sh		
	echo "#MSUB -l nodes=1" >> fdt_gen.sh			#For TST18, only 1 node/16 cores for quartz
	echo "#MSUB -l partition=quartz" >> fdt_gen.sh			#For TST18, only 1 node/16 cores for quartz
	echo "#MSUB -l walltime=01:30:00" >> fdt_gen.sh		
	echo "#MSUB -q pbatch" >> fdt_gen.sh		
	echo "#MSUB -m abe" >> fdt_gen.sh			
	echo "#MSUB -V" >> fdt_gen.sh			
	echo "#MSUB -j oe" >> fdt_gen.sh			
	echo "#MSUB -o "$DIR"_fdt_gen.log" >> fdt_gen.sh	
	echo "#MSUB -N shktb2D_gen" >> fdt_gen.sh		

	echo "" >> fdt_gen.sh		
	echo "######These are shell commands" >> fdt_gen.sh		
	echo "arch=`uname -p`" >> fdt_gen.sh		
	echo "echo Architecture = \$arch" >> fdt_gen.sh		

	echo "" >> fdt_gen.sh		
	echo "CASE=shktb" >> fdt_gen.sh		
	echo "EXEC=./nek5000" >> fdt_gen.sh		

	echo "" >> fdt_gen.sh		
	echo "echo \"Executable 	=\" \$EXEC" >> fdt_gen.sh		
	echo "echo \"Current Directory 	=\" \`pwd\`" >> fdt_gen.sh		


	echo "" >> fdt_gen.sh
	#echo "echo \$CASE > SESSION.NAME" >> fdt_gen.sh		
	#echo "echo \`pwd\`'/' >> SESSION.NAME" >> fdt_gen.sh		
	echo "rm -f logfile" >> fdt_gen.sh		
	echo "rm -f iofile" >> fdt_gen.sh		
	echo " \$CASE.log \$CASE.log1 2>\/dev\/null " >> fdt_gen.sh		
	

	echo "" >> fdt_gen.sh		
	echo "srun -n 36 \$EXEC" >> fdt_gen.sh	

	msub fdt_gen.sh	
else
	echo " $PWD : Compilation error!! Most probably due to lack of memory!! Try with a smaller problem size"
fi
