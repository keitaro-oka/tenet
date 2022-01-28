#statement_file="statement/oka_own/model_file/conv_edsr_1.s"
statement_file="statement/oka_own/model_file/conv_vrn_1.s"
hw_file="pe_array/oka_own/oka_own_systolic.p"
mapping_file="mapping/oka_own/map_data/map_file"
num_dir=30
maps_per_exp=500

id=1
for dir_id in $(seq 1 $num_dir) ; do
  ##################
  end=`expr ${dir_id} \* ${maps_per_exp}`
  echo "end"${end}
  dir_name="./oka_own"${dir_id}"/experiment"
  if [ ! -e ${dir_name} ] ; then
      mkdir -p ${dir_name}
  fi

  start=`expr ${end} - ${maps_per_exp} + 1`
  echo "start" ${start} "end" ${end}
  for i in $(seq ${start} $end); do
      bin_file="experiment_"${i}
      echo ${mapping_file}${i} >> ${dir_name}/$bin_file
      echo ${hw_file} >> ${dir_name}/$bin_file
      echo ${statement_file} >> ${dir_name}/$bin_file
  done
  id=${dir_id}+1
  ##################
done
