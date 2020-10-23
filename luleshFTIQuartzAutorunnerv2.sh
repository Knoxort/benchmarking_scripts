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

eprList="5 10 15 20 25";	#Elements per Rank List	

rankList="1 8 64 216 512 1000"; # 1331 1728";	#Number of Ranks	
gsList="2" 	#Group Size List (Total Number of Nodes?); max size is 32

#rankList="27 729"; # 1331 1728";	#Number of Ranks	
#gsList="3" 	#Group Size List (Total Number of Nodes?); max size is 32

#rankList="125"; # 1331 1728";	#Number of Ranks	
#gsList="5" 	#Group Size List (Total Number of Nodes?); max size is 32

#rankList="343"; # 1331 1728";	#Number of Ranks	
#gsList="7" 	#Group Size List (Total Number of Nodes?); max size is 32

nsList="1" 		#Node Size List (Ranks per Node)
qCpN="1"	#Quartz cores per node
chkptLevelList="1";			#When I start doing different checkpointing frequencies, I need to find a way that this only runs when prem is activated.

l1="luleshMPI.o";
perm="luleshMPI-perm";
exe="lulesh2.0"
root=`pwd`

make

for groupSize in $gsList
do
	#for elmsPerCore in $probSizeList
	for nodeSize in $nsList
	do
		for ElmPerRank in $eprList
		do

		for ranks in $rankList
		do

		
                cd $root
		numNodes=$ranks
                #numRanks=$(( ${groupSize}*${nodeSize} ))
                numRanks=$ranks
		#tasksPerNode=${nodeSize}
		tasksPerNode=1
		baseword="luleshFTI_${ElmPerRank}EPR_${ranks}R_${nodeSize}NS_${groupSize}GS"

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
	        echo "#SBATCH -t 02:00:00" >> $outputJobFile
	        #echo "##SBATCH --mem-per-cpu=1G" >> $outputJobFile
	        #echo "##SBATCH --ntasks=${numRanks}" >> $outputJobFile
	        #echo "##SBATCH --ntasks-per-node=${tasksPerNode}" >> $outputJobFile
        	echo "#SBATCH -V" >> $outputJobFile
	        echo "#SBATCH -J ${baseword}" >> $outputJobFile
	        echo "#SBATCH -o log_${baseword}.txt" >> $outputJobFile
                echo "srun -n ${numRanks} ${exe} -s ${ElmPerRank}" >> $outputJobFile
        	sbatch $outputJobFile
		done
		done
	done
done
