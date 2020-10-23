#!/bin/bash

#Parameters
	#number of processors
		#must be a cube number?
	#Problem Size

#From Output of LuleshTo run other sizes, use -s <integer>.
	#To run a fixed number of iterations, use -i <integer>.
	#To run a more or less balanced region set, use -b <integer>.
	#To change the relative costs of regions, use -c <integer>.
	#To print out progress, use -p
	#To write an output file for VisIt, use -v
	#See help (-h) for more options

qCpN="1"	#Quartz cores per node
numCoresList="1 8 27 64 125 216 343 512 729 1000"; # 216 343 512 1000 1728 2197 4913 32768";
probSizeList="256 512 1024";	
chkptFreqList="1";			#When I start doing different checkpointing frequencies, I need to find a way that this only runs when prem is activated.

l1="luleshMPI.o";
perm="luleshMPI-perm";
root=`pwd`

#if [ "$1" = "lulesh1" ]; then
#  executable=$l1;
#elif [ "$1" = "perm" ]; then
#  executable=$perm;
#else
#  echo "Command line argument does not match library. Exiting"
#  exit 1
#fi
	
for numCores in $numCoresList
do
	#for elmsPerCore in $probSizeList
	for probSize in $probSizeList
	do
		for chkptFreq in $chkptFreqList
		do
		
                cd $root
		#numNodes=$(( ${numCores}/${qCpN} + 1 ))
		numNodes=$numCores
		#probSize=$(( ${numCores}*${elmsPerCore} ))
		#probSize="20"
		tasksPerNode=$(( ${numCores}/${numNodes} ))

		baseword="lulesh_${chkptFreq}CPF_${probSize}Size_${numCores}Cores"

	        if [ $chkptFreq = "-1" ]; then
                #if [ "$1" = "lulesh1" ]; then
                  executable=$l1;
                else
                  executable=$perm;
                fi
		
                outputJobFile="batch_${baseword}.sh"
		workDir="dir_${baseword}"
		mkdir $workDir
		cd $workDir

	        if [ $chkptFreq = "-1" ]; then
		  cp ../l1Makefile ../luleshMPI.cc . 
		  mv l1Makefile makefile
		  sed -i "s/size = .*;/size = $probSize;/" luleshMPI.cc
                else
                #elif [ "$1" = "perm" ]; then
                  cp ../permMakefile ../luleshMPI-perm.cc . 
		  mv permMakefile makefile
		  sed -i "s/size = .*;/size = $probSize;/" luleshMPI-perm.cc
		fi

		#make clean 								#Since we're doing different directories, no need to clean
		make #remake the file with the actual right size

		#Start actual job file
	        echo "#!/bin/bash" > $outputJobFile
	        echo "#SBATCH -N $numNodes" >> $outputJobFile                          	      
		echo "#SBATCH -p pbatch" >> $outputJobFile                  #For TST18, only 1 node/16 cores for quartz
	        echo "#SBATCH -t 01:30:00" >> $outputJobFile
	        #echo "##SBATCH --mem-per-cpu=1G" >> $outputJobFile
	        #echo "##SBATCH --ntasks=${numCores}" >> $outputJobFile
	        #echo "##SBATCH --ntasks-per-node=${tasksPerNode}" >> $outputJobFile
        	echo "#SBATCH -V" >> $outputJobFile
	        echo "#SBATCH -J ${baseword}" >> $outputJobFile
	        echo "#SBATCH -o log_${baseword}.txt" >> $outputJobFile
	        if [ $chkptFreq = "-1" ]; then
                  echo "srun -n ${numCores} ${executable}" >> $outputJobFile
		else
                  echo "export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/workspace/trokon/myLibs/installDir/perm/lib/" >> $outputJobFile
                  echo "srun -n ${numCores} ${executable} -c${chkptFreq}" >> $outputJobFile
                fi
        	  sbatch $outputJobFile
		done
	done
done
