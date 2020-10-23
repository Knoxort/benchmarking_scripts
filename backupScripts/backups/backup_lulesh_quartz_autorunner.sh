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

numCoresList="27";
probSizeList="10 150";	#Right now, only works for 2 digit sizes
chkptFreqList="-1 0 5";			#When I start doing different checkpointing frequencies, I need to find a way that this only runs when prem is activated.

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
	for probSize in $probSizeList
	do
		for chkptFreq in $chkptFreqList
		do

	        if [ $chkptFreq = "-1" ]; then
                #if [ "$1" = "lulesh1" ]; then
                  executable=$l1;
                else
                  executable=$perm;
                fi
		
		cd $root
		#mkdir "luleshDir${numCores}Cores${probSize}Size"
		#cp makefile luleshMPI.cc "luleshDir${numCores}Cores${probSize}Size"
		#cd "luleshDir${numCores}Cores${probSize}Size"

	        #if [ "$1" = "lulesh1" ]; then
	        if [ $chkptFreq = "-1" ]; then
                  outputJobFile="lulesh_${chkptFreq}CPF_${numCores}Cores_${probSize}Size.sh"
		  mkdir "luleshDir_${chkptFreq}CPF_${numCores}Cores${probSize}Size"
		  cp makefile luleshMPI.cc "luleshDir_${chkptFreq}CPF_${numCores}Cores${probSize}Size"
		  cd makefile luleshMPI.cc "luleshDir_${chkptFreq}CPF_${numCores}Cores${probSize}Size"
		  sed -i "s/mySize = .*;/mySize = $probSize;/" luleshMPI.cc
                else
                #elif [ "$1" = "perm" ]; then
                  outputJobFile="lulesh_${chkptFreq}CPF_${numCores}Cores_${probSize}Size.sh"
                  mkdir "luleshDir_${chkptFreq}CPF_${numCores}Cores_${probSize}Size.sh"
                  cp makefile luleshMPI-perm.cc "luleshDir_${chkptFreq}CPF_${numCores}Cores_${probSize}Size.sh"
                  cd "luleshDir_${chkptFreq}CPF_${numCores}Cores_${probSize}Size.sh"
		  sed -i "s/mySize = .*;/mySize = $probSize;/" luleshMPI-perm.cc
		fi
		
		#make clean 								#Since we're doing different directories, no need to clean
		make #remake the file with the actual right size

		#Start actual job file
	        echo "#!/bin/bash" > $outputJobFile
	        echo "#MSUB -l nodes=1" >> $outputJobFile                          	      
		echo "#MSUB -l partition=quartz" >> $outputJobFile                  #For TST18, only 1 node/16 cores for quartz
	        echo "#MSUB -l walltime=02:00:00" >> $outputJobFile
        	echo "#MSUB -q pbatch" >> $outputJobFile
	        echo "#MSUB -m abe" >> $outputJobFile
        	echo "#MSUB -V" >> $outputJobFile
	        echo "#MSUB -j oe" >> $outputJobFile
	        echo "#MSUB -N lulesh_${chkptFreq}CPF_${numCores}Cores_${probSize}Size" >> $outputJobFile
	        #if [ "$1" = "lulesh1" ]; then
	        if [ $chkptFreq = "-1" ]; then
	          echo "#SBATCH -o lulesh_${numCores}Cores_${probSize}Size.log" >> $outputJobFile
                  echo "srun -n ${numCores} ${executable} -s ${probSize}" >> $outputJobFile
                #elif [ "$1" = "perm" ]; then
		else
	          echo "#SBATCH -o lulesh_${chkptFreq}CPF_${numCores}Cores_${probSize}Size.log" >> $outputJobFile
                  echo "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/workspace/trokon/myLibs/installDir/perm/lib/" >> $outputJobFile
                  echo "srun -n ${numCores} ${executable} -c${chkptFreq}" >> $outputJobFile
                fi
        	sbatch $outputJobFile
		done
	done
done
