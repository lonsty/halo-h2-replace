printf "$(date)\nRsyncing remote .halo to local ...\n"
rsync -av ubuntu@124.156.119.138:/home/ubuntu/.halo ~/

printf "\nReplacing domain name ... "
docker stop halo-blog
python3 /home/ubuntu/workspace/halo-h2-replace/h2_replace.py \
	-o http://lonsty.me \
	-n http://blog.lonsty.me \
	--url /home/ubuntu/.halo/db/halo \
	--h2jar /home/ubuntu/workspace/halo-h2-replace/h2.jar
python3 /home/ubuntu/workspace/halo-h2-replace/h2_replace.py \
	-o http://hk.lonsty.me \
	-n http://blog.lonsty.me \
	--url /home/ubuntu/.halo/db/halo \
	--h2jar /home/ubuntu/workspace/halo-h2-replace/h2.jar

docker start halo-blog
printf "Restarted.\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n"
