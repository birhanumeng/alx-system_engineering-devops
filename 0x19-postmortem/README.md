## 0x19. Postmortem
### A Postmortem Incident Report on GAS (Genero Application Server) Disconnection
##### Issue Summary
A financial institution in Ethiopia currently I am working on has got frequent failurity by gas (genero application server) between Monday Jan 09, 2023 10:20 AM and Wend Jan 11, 2023 11:00 AM EAT. When GAS disconnected, users will get an error site unrechable massage as they try to access the web system. At a down time, The web system totally unreachable and customers can’t work. The main root cause was, the number of process and size of open file on the server for gas user was not able to handle all users.
