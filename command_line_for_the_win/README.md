## STEPS TO ESTABLISH AN SFTP CONNECTION

***We can establish an SFTP session by issuing the following command***

- *$ sftp username@hostname*

***You will be requested to input your password. Make sure you enter the correct password***

***Navigate to the root directory and create***

- *sftp cd /root*

***Create the alx-system_engineering-devops/command_line_for_the_win/ directory using the mkdir command***

- *sftp mkdir alx-system_engineering*
- *sftp mkdir command_line_for_the_win*

***Navigate to the local directory where the file you want to upload is stored using lcd command***

- *sftp lcd directoryName*

***Use the put command to upload the file from the local machine to the remote machine***

- *stfp put -P filename destination*
