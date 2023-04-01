## 0x19. Postmortem
### A Postmortem Incident Report on GAS (Genero Application Server) Disconnection
#### Issue Summary
A financial institution in Ethiopia currently I am working on has got frequent failurity by gas (genero application server) between Monday Jan 09, 2023 10:20 AM and Wend Jan 11, 2023 11:00 AM EAT. When GAS disconnected, users will get an error site unrechable massage as they try to access the web system. At a down time, The web system totally unreachable and customers can’t work. The main root cause was, the number of process and size of open file on the server for gas user was not able to handle all users.
#### Timeline
##### Monday Jan 09
8:40 AM: More than 1500 users start working.
10:20 AM: GAS outage starts
10:25 AM: Users starts to calling and complain by the system down. At this time first level support   team notified
10 :25 AM: Support teams escalates the issue tho system administrators 
10:30 AM: GAS service starts and system starts fully working.
11:10 AM: GAS outage began
11:20 AM The system vendors are got notified about the issues
12:00 AM: More CPU and RAM was add to the server. This was the wrong assumption
2:00 PM: GAS started and system available for work
3:40 PM GAS stopped
##### Tuesday Jan 10
3:00 AM additional user licenses are purchased and deployed
5:30 AM GAS stopped
##### Wednesday Jan 11
4:30 AM: Number of process and open file size for gas user is increased
5:00 AM: 100% the outage is solved and system is available for work fully
#### Root cause and resolution
During peace instability in Ethiopia, some customers (users) were not at work at this  time. A the same time the company introduced new web based application for its financial work. At first there was a maximum of 1000 users can work and the server was able to handle all the connections. After peace instability overs all the users (more than 1500 users) start working. Now Server specifically the GAS server start to unable handle and outages. The root causes was the number of process and open file size for gas user was default configuration. So When number of process or open file size reached maximum default configuration, GAS stopped. After investigation we increased them on the server in /etcl security/limits.conf. Then After restarting the system the issues solved permanently.
#### Corrective and preventative measures
After issue is resolved, We start all the default and customized configurations of different services. Some configurations are changed based on analysis. To fix the we did different things:
* Increase the CPU and RAM size for the server.
* We change the other web service configuration in order to not face such kind of  outage by the other services also.
* We increase the maximum number licensed users.
* We configure resources for different users on system level.
* we increases specifically number maximum processes and open file size for gas user on.
* We do a documenting the incident for feature use with the same issue.
