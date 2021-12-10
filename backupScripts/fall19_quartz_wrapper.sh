#!/bin/bash

#10/10/19
#For this first test run, I just basically want to change the number of particles, kind of like
#we did by changing in the spg-overview file in UF Apps. That means, for now, nothing else needs to change.

#It looks like npart in size, but that doesn't seem right... Oh well, I guess I'll just give it a shot and see what happens. Or compare to the other node test.
	#yeah, that's weird. The par files matched exactly, except for the distribute box. So why?
#Oh, I never changed the number of particles, duh! I just changed the size of the distribute box. So, changing npart should do everything

#npart of 52742 seems arbitrary; not divisable by 16; or anything besides 2 and a prime number, according to calculator.net. So, we're gonna increase to a round 75000 and see if it runs in a reasonable time 

#Remember, Sai also said to increase the number of time steps

#Ok, we're getting fun "nek has been compiled for this lelt and lelg" again.

#Static Parameters
numCore="36"
alphapercore="1"		#Where does this affect? Does it need to be removed?

#Varying Parameters
#lx1List="2 3 4 5 6 7"			#Element Size?
lx1List="6 7"			#Element Size?
elmsPerCoreList="5 10 15 20 25"		#Elements per core?
#elmsPerCoreList="5"		#Elements per core?
partsPerCoreList="10 50 100 500 1000"		#Particles per Processor
root=`pwd`

#export PATH=/g/g19/trokon/workspace/cmt_Nek_BE_Instrumentation_repo/bin:$PATH
export PATH=/usr/workspace/trokon/Nek5000/bin:$PATH
for lx1 in $lx1List
do
  for elmsPerCore in $elmsPerCoreList
  do
    for partsPerCore in $partsPerCoreList
    do
	echo "Lx1: "$lx1
	echo "Elements per Core: "$elmsPerCore
	echo "Particles per Processor: "$partsPerCore
	let lxd=$lx1+2	
	#let globalElms=$numCore*$elmsPerCore
	let globalElms=3600
	let numParticles=$partsPerCore*$numCore

	#This cd makes no sense to me...
	cd $root
	mkdir 'quartz_'$numCore'C_'$lx1'LX1_'$elmsPerCore'EPC'_$partsPerCore'PPC'
	cp TORO makenek SIZE_template shktb.* riemann.inp  fall19_quartz_generator.sh myClean.sh 'quartz_'$numCore'C_'$lx1'LX1_'$elmsPerCore'EPC'_$partsPerCore'PPC'
	cd 'quartz_'$numCore'C_'$lx1'LX1_'$elmsPerCore'EPC'_$partsPerCore'PPC'
	cp SIZE_template SIZE
			
        #lxdval=($lx1+2)
        lxd=($lx1+2)
	sed -i "s/(lx1=?/(lx1=$lx1/" SIZE
	sed -i "s/(lxd=?/(lxd=$lxd/" SIZE
	sed -i "s/(lelg=?)/(lelg=$globalElms)/" SIZE

	sed -i "s/npart = ?/npart = $numParticles/" shktb.par

	#Is this still necessary
	#if [ $nelx -gt 900 ]
	#then
	#	nlx=$(expr "$nelx" / 16)
	#	sed -i "s/-4  -4  -4/-$nlx  -32  -32/" uniform.box
	#else
	#	sed -i "s/-4  -4  -4/-$nelx  -8  -8/" uniform.box
	#fi
	echo "shktb.box" > gbox.in
	echo "Updates Complete!!!"
	#Modules used to be loaded here; to keep consistency, for repeatability,
		#perhaps need to load that again?
	genbox < gbox.in
	mv box.re2 shktb.re2
	echo "shktb" > gmap.in
	echo "0.2" >> gmap.in
	genmap < gmap.in
	#Shouldn't need to convert .rea to .re2 anymore
	chmod 777 fall19_quartz_generator.sh
	chmod 777 myClean.sh
	echo "Running the job script"
	./fall19_quartz_generator.sh 
    done
  done
done

#echo "Wrapper test script to modify the SIZE and cmtparticles.usrp file completed. Check the changes"

