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

#Test parameters
numRankList="8 64 216 512 1000"
#numRankList=""
#eprList="2 4 6 8 10 12 14";	#Elements per Rank List	
eprList="20";	#Elements per Rank List	
groupSize="2"
nodeSize="1"

#groupSize="3"
#nodeSize="1"


l1="luleshMPI.o";
perm="luleshMPI-perm";
exe="lulesh2.0"
root=`pwd`

make

for numRanks in $numRankList
do
	for elmPerRank in $eprList
	do
                cd $root
		numNodes=$numRanks
                #numRanks=$(( ${groupSize}*${nodeSize} ))
		tasksPerNode=${nodeSize}
		baseword="luleshFTI_${elmPerRank}EPR_${groupSize}GS_${nodeSize}NS_${numRanks}R"

                outputJobFile="batch_${baseword}.sh"
		workDir="dir_${baseword}"
		mkdir $workDir
                cp Makefile  defaultConfig.fti lulesh* $workDir
		cd $workDir
		mv defaultConfig.fti config.fti

		#make #remake the file with the actual right size
			#For LULESH2.0, don't have to remake for size

		#Change the config file
		sed -i "s/tjl_rpgs/${groupSize}/" config.fti
		sed -i "s/tjl_rpns/${nodeSize}/" config.fti

		#If these directories haev to be created manually
		mkdir ckpt_files; 
		mkdir ckpt_files/global; mkdir ckpt_files/local; mkdir ckpt_files/meta;

		#Start actual job file
	        echo "#!/bin/bash" > $outputJobFile
	        echo "#SBATCH -N $numNodes" >> $outputJobFile                          	      
		echo "#SBATCH -p pbatch" >> $outputJobFile                  #For TST18, only 1 node/16 cores for quartz
	        echo "#SBATCH -t 00:10:00" >> $outputJobFile
	        #echo "##SBATCH --mem-per-cpu=1G" >> $outputJobFile
	        #echo "##SBATCH --ntasks=${numRanks}" >> $outputJobFile
	        #echo "##SBATCH --ntasks-per-node=${tasksPerNode}" >> $outputJobFile
        	echo "#SBATCH -V" >> $outputJobFile
	        echo "#SBATCH -J ${baseword}" >> $outputJobFile
	        echo "#SBATCH -o log_${baseword}.txt" >> $outputJobFile
                echo "srun -n ${numRanks} ${exe} -s ${elmPerRank}" >> $outputJobFile
        	sbatch $outputJobFile
	done
done
