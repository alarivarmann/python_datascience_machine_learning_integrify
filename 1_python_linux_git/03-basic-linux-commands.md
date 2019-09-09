---
title: 03 - Basic Linux commands
root: '/modules/module-0'
tree: '00 - Prerequisites'
module: module-0
---

# 03. Basic Linux-commands

One thing anyone at the IT-industry should know about is how to "survive" on a Linux environment as it's the most commonly used. Below we'll discover a decent set of commands and their descriptions to get us started.


## Absolute basics

* TAB-key can be used to fill up in terminal. For example, we just need to type `cd /hom` and then TAB-key and the terminal fills the rest up and makes it “cd /home”.
* Up and Down keys will show last used commands, so no need to write that 120 letter command all over again if something failed
* `clear` command will clear up the bloated terminal screen and gives us a blank canvas
* Ctrl+C can be used to stop any command in terminal safely. If it doesn't stop with that, then Ctrl+Z can be used to force stop it.
* We can exit from the terminal by using the `exit` command.
* We can power off or reboot the computer by using the command `sudo halt` and `sudo reboot`.
* `$PATH` is a special environmental-variable which Linux uses to find executables. More about `$PATH` [here](http://www.linfo.org/path_env_var.html)
* Our home directory is located at `/home/[OURUSERNAME]`, and we can refer to that by using `$HOME`-variable, tilde character (´~´)
* Our terminal uses special configuration-files (dotfiles) which usually include `.profile`, `.bashrc` or `.zshrc` depending our shell and many more. One can use these configuration files to customize pretty much anything in the shell.
* Pretty much every command uses some sort of switches. Switches are defined after the command with `--like-this` or for short `-L`. We can get the full list of switches per command by typing `man [COMMANDNAME]`
* Aliases are command shortcuts which live inside dotfiles, e.g. `ls -l` is usually aliased as  `ll`.
* Linux Distros (Distributions) ship with couple of editors: `Nano` and `Vi` and we'll use the former as Vi & Vim will need a couple of years of training to exit...
* We can combine commands with `&&`, e.g. `cd && echo "Wazzup?"` which gets us to the home folder and echoes "Wazzup?".

## Moving around in the filesystem

### 01. `cd`

`cd` (short for Change Directory) is used to navigate to a specific folder. Shortcut for going back to home is `cd`.

Examples:

```bash
$ cd /var # will get us the /var-folder. Note the preceding slash which starts from the root so it doesn't matter where we are => we move from root-down.
$ cd log # Now we're inside var-folder and we're moving to log-folder inside our current directory so no preceding slash required.
$ cd .. # go up one step in the directory-tree
```

### 02. `ls`

`ls` (short list) is used to list the files and folders in the directory we specify. By default it lists our currect directory.

Examples:

```bash
$ ls # basic list
$ ls -l # Detailed list. Note the -l switch which stands for long
$ ls -la # Detailed list with hidden files included
$ ls -lah # Detailed list with hidden files included and with a human-friendly file sizes
```

## Getting info about folders and files

### 03. `pwd`

`pwd` (short for Print Working Directory) simply shows the current directory we're in.

Examples:

```bash
$ pwd
/usr/bin
```

### 04. `whoami`

`whoami` (short for Who am I...) shows the current user name

Examples:

```bash
$ whoami
ubuntu
```

### 06. `uname`

`uname` shows information about the computer.

Examples:

```bash
$ uname # just the distro
Darwin
$ uname -a # everything
Darwin willemb.local 18.6.0 Darwin Kernel Version 18.6.0: Thu Apr 25 23:16:27 PDT 2019; root:xnu-4903.261.4~2/RELEASE_X86_64 x86_64
$ uname -s # kernel name
Darwin
$ uname -r # kernel release
18.6.0
$ uname -v # kernel version
Darwin Kernel Version 18.6.0: Thu Apr 25 23:16:27 PDT 2019; root:xnu-4903.261.4~2/RELEASE_X86_64
```

### 07. `hostname`

`hostname` shows computer’s hostname and domain name (DNS) (Domain Name Service), and to display or set a computer’s hostname or domain name.

Examples:

```bash
$ hostname
willemb.local
$ hostname newhostname.com
```

### 08. `top`

`top` shows a real-time display of the data relating to our Linux machine. The top of the screen is a status summary. Top is exited by typing `Ctrl+c`

Examples:

```bash
Processes: 433 total, 2 running, 431 sleeping, 2478 threads                                                                                                                                            11:31:08
Load Avg: 1.31, 1.57, 1.74  CPU usage: 3.53% user, 3.65% sys, 92.80% idle  SharedLibs: 263M resident, 61M data, 51M linkedit. MemRegions: 188738 total, 5985M resident, 111M private, 3488M shared.
PhysMem: 16G used (4069M wired), 254M unused. VM: 5138G vsize, 1373M framework vsize, 38259328(0) swapins, 40681995(0) swapouts. Networks: packets: 43329127/50G in, 28841720/29G out.
Disks: 28243956/476G read, 20621372/402G written.

PID    COMMAND      %CPU TIME     #TH   #WQ  #PORT MEM    PURG   CMPRS  PGRP  PPID  STATE    BOOSTS           %CPU_ME %CPU_OTHRS UID       FAULTS     COW     MSGSENT    MSGRECV    SYSBSD     SYSMACH
98381  MTLCompilerS 0.0  00:00.31 2     2    26    12M    0B     12M    98381 1     sleeping  0[9]            0.00000 0.00000    501       9770       458     175        49         1472       391
98380  VTDecoderXPC 0.0  00:00.86 2     1    69    11M    0B     10M    98380 1     sleeping  0[199]          0.00000 0.00000    501       20094      240     18546      14784      25583      21239
92682  MTLCompilerS 0.0  00:00.07 2     2    24    5800K  0B     5784K  92682 1     sleeping  0[2]            0.00000 0.00000    501       5439       455     125        39         723        314
87332  com.apple.hi 0.0  00:00.74 2     2    43    1532K  0B     512K   87332 1     sleeping  0[1870]         0.00000 0.00000    501       9154       128     15534      3321       14775      14356
```

### 09. `man`

`man` (short for manual) is our besst friend. It shows all the options and switches to a particular command. Man is exited by typing `Q`

Examples:

```bash
$ man ls
LS(1)                     BSD General Commands Manual                    LS(1)

NAME
     ls -- list directory contents

SYNOPSIS
     ls [-ABCFGHLOPRSTUW@abcdefghiklmnopqrstuwx1] [file ...]

DESCRIPTION
     For each operand that names a file of a type other than directory, ls displays its name as well as any requested, associated information.  For each operand that names a file of type
     directory, ls displays the names of files contained within that directory, as well as any requested, associated information.

     If no operands are given, the contents of the current directory are displayed.  If more than one operand is given, non-directory operands are displayed first; directory and non-
     directory operands are sorted separately and in lexicographical order.

     The following options are available:

     -@      Display extended attribute keys and sizes in long (-l) output.

     -1      (The numeric digit ``one''.)  Force output to be one entry per line.  This is the default when output is not to a terminal.

     -A      List all entries except for . and ...  Always set for the super-user.
...
```

### 10. `df`

`df` shows the free disk space in our system.

Examples:

```bash
$ df -h # human-readable file-sizes
Filesystem           Size   Used  Avail Capacity iused               ifree %iused  Mounted on
/dev/disk1s1        465Gi  441Gi   19Gi    96% 6783627 9223372036847992180    0%   /
devfs               228Ki  228Ki    0Bi   100%     788                   0  100%   /dev
/dev/disk1s4        465Gi  4.0Gi   19Gi    18%       4 9223372036854775803    0%   /private/var/vm
map -hosts            0Bi    0Bi    0Bi   100%       0                   0  100%   /net
map auto_home         0Bi    0Bi    0Bi   100%       0                   0  100%   /home
map -fstab            0Bi    0Bi    0Bi   100%       0                   0  100%   /Network/Servers
keybase-redirector    0Bi    0Bi    0Bi   100%       0                   0  100%   /keybase
```

### 11. `du`

`du` (short for Disk Usage) shows the disk usage of a directory tree and each of its subdirectories. Default (if no directory submitted) is from root so beware not to loop each and every directory inside of our filesystem unless that's the intention.

Examples:

```bash
$ du -h /var/log # human-readable output of /var/log
4.0K	/var/log/dist-upgrade
236K	/var/log/apt
14M	/var/log/installer/cdebconf
15M	/var/log/installer
41M	/var/log/journal/987674e53c4d4e0181f663b7339526e1
41M	/var/log/journal
6.6M	/var/log/nginx
4.0K	/var/log/unattended-upgrades
4.0K	/var/log/redis
4.0K	/var/log/ntpstats
4.0K	/var/log/mysql
65M	/var/log
$ du -hs /var/log # human-readable total usage of /var/log
65M	/var/log
```

### 12. `free`

`free` (short for, uhm, nothing) shows the summary of memory usage.

Examples:

```bash
$ free -h # human-readable output of memory usage
              total        used        free      shared  buff/cache   available
Mem:           985M        341M        354M         57M        289M        453M
Swap:          2.0G          0B        2.0G
```

## Creating and modifying directories & files

### 13. `touch`

`touch` is used to create empty file(s). By default it creates file(s) to our current directory.

Examples:

```bash
$ touch newfile # creates a newfile within the current working directory
$ touch newfile secondnewfile # creates a newfile and a secondnewfile within the current working directory
$ touch /some/folder/newfile /some/other/folder/secondnewfile # creates a newfile and secondnewfile to different locations
```

### 14. `mkdir`

`mkdir` (short for make directory) creates new directories.

Examples:

```bash
$ mkdir foo # creates a folder named "foo" to current working directory
$ mkdir foo/bar # creates a folder named "bar" to recently created "foo" dorectory
$ mkdir -p new/directory/path/which/doesnt/exist # creates a full directory. -p switch instructs to create parents also if they don't exist.
```

### 15. `mv`

`mv` (short for move) allows us to move files and directories from directory to directory. It also allows us to rename files.

Examples:

```bash
$ mv /var/log/nginx/error.log . # move error.log file from one directory to current (dot represents current) directory
$ mv /var/log/nginx/error.log renamed_error.log # move and rename log-file to current dir
$ mv /var/log/nginx/error.log /var/log/nginx/renamed_error.log # Rename log-file inplace
```

### 16. `cp`

`cp` (short for copy) the same thing as `mv` but instead of moving it copies files and folders.

Examples:

```bash
$ cp /var/log/nginx/error.log . # copy error.log to current working directory
$ cp -r /var/log . # copy the whole log-directory recuresively (-r switch) to current working dir.
```

### 17. `rm`

`rm` (short for remove) removes files and folders specified.

Examples:

```bash
$ rm .bash_logout # remove .bash_logout file from current working dir
$ rm /some/file/in/filesystem.log # remove filesystem.log by it's absolute path
$ rm -rf /home/ubuntu/.cache # remove .cache folder using recursive (-r) force (-f)
```

### 18. `rmdir`

`rmdir` (short for remove directory) removes directories specified. If any of the specified directories is not empty, `rmdir` will not remove it, and will proceed to try and remove any other directories you specified.

Examples:

```bash
$ rmdir mydir # remove mydir IF it's empty
$ rmdir dir1 dir2 dir3 # remove specified directories IF they are empty
$ rmdir -p dir/subdir # attempt to remove first subdir and then dir. -p switch instructs to use each directory argument to be treated as pathname of which all components will be removed, if they are empty
```

### 19. `chmod`

`chmod` (short for change mode) sets the file permissions flags on a file or folder. The flags define who can read, write to or execute the file. Read a comprehensive description [here](https://www.howtogeek.com/67987/htg-explains-how-do-linux-file-permissions-work/).

### 20. `chown`

`chown` (short for change owner) allows us to change the owner and group owner of a file. Read a comprehensive description [here](https://www.geeksforgeeks.org/chown-command-in-linux-with-examples/).

### 21. `tar`

`tar` is used to create and extract a compressed archive-file, a "tarball", which can contain multiple files.

Examples:

```bash
$ tar -cvf logs.tar /var/log/nginx # create (-c) a file named (-f) logs.tar by giving a visual (verbose) (-v) feedback
$ tar -czvf logs.tar.gz /var/log/nginx # create (-c) a file named (-f) logs.tar.gz using gzip-utility (-z) and with a visual (verbose) (-v) feedback
$ tar -xvzf logs.tar.gz extracted_folder # Extract (-x) compressed file named logs.tar.gz (-f) by using gzip-utility (-z) and with a visual (verbose) feedback (-v) to extracted_folder
```

### 22. `unzip`

`unzip` is used to unzip (decompress) zipped files.

Examples:

```bash
$ unzip filename.zip # Unzip filename.zip -archive
$ unzip filename.zip -vd extracted_folder # Unzip filename.zip with visual (verbose) feedback to destination (-d) extracted_folder
$ unzip filename.zip -q # Unzip filename.zip and suppress (-q, quiet) all messagesn during
```

## Displaying content of file(s)

### 23. `cat`

`cat` (short for concatenate) lists the contents of files to the terminal window.

Examples:

```bash
$ cat /var/log/nginx/error.log # output file contents to terminal
```

### 24. `head`

`head` outputs a listing of the first 10 lines of a file.

```bash
$ head /var/log/syslog # output first ten lines of a file
May 20 06:25:01 localhost rsyslogd:  [origin software="rsyslogd" swVersion="8.32.0" x-pid="502" x-info="http://www.rsyslog.com"] rsyslogd was HUPed
May 20 06:39:01 localhost CRON[15538]: (root) CMD (  [ -x /usr/lib/php/sessionclean ] && if [ ! -d /run/systemd/system ]; then /usr/lib/php/sessionclean; fi)
May 20 06:39:05 localhost systemd[1]: Starting Clean php session files...
May 20 06:39:05 localhost systemd[1]: Started Clean php session files.
May 20 07:09:01 localhost CRON[15698]: (root) CMD (  [ -x /usr/lib/php/sessionclean ] && if [ ! -d /run/systemd/system ]; then /usr/lib/php/sessionclean; fi)
May 20 07:09:05 localhost systemd[1]: Starting Clean php session files...
May 20 07:09:05 localhost systemd[1]: Started Clean php session files.
May 20 07:17:01 localhost CRON[15788]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
May 20 07:39:01 localhost CRON[15858]: (root) CMD (  [ -x /usr/lib/php/sessionclean ] && if [ ! -d /run/systemd/system ]; then /usr/lib/php/sessionclean; fi)
May 20 07:39:05 localhost systemd[1]: Starting Clean php session files...
$ head /var/log/syslog -n 2 # output first 2 (-n, number) lines of a file
May 20 06:25:01 localhost rsyslogd:  [origin software="rsyslogd" swVersion="8.32.0" x-pid="502" x-info="http://www.rsyslog.com"] rsyslogd was HUPed
May 20 06:39:01 localhost CRON[15538]: (root) CMD (  [ -x /usr/lib/php/sessionclean ] && if [ ! -d /run/systemd/system ]; then /usr/lib/php/sessionclean; fi)
```

### 26. `tail`

`tail` is similar to `head` but it outputs last 10 lines of a file.

Examples:

```bash
$ tail /var/log/syslog # output last ten lines of a file
May 20 06:25:01 localhost rsyslogd:  [origin software="rsyslogd" swVersion="8.32.0" x-pid="502" x-info="http://www.rsyslog.com"] rsyslogd was HUPed
May 20 06:39:01 localhost CRON[15538]: (root) CMD (  [ -x /usr/lib/php/sessionclean ] && if [ ! -d /run/systemd/system ]; then /usr/lib/php/sessionclean; fi)
May 20 06:39:05 localhost systemd[1]: Starting Clean php session files...
May 20 06:39:05 localhost systemd[1]: Started Clean php session files.
May 20 07:09:01 localhost CRON[15698]: (root) CMD (  [ -x /usr/lib/php/sessionclean ] && if [ ! -d /run/systemd/system ]; then /usr/lib/php/sessionclean; fi)
May 20 07:09:05 localhost systemd[1]: Starting Clean php session files...
May 20 07:09:05 localhost systemd[1]: Started Clean php session files.
May 20 07:17:01 localhost CRON[15788]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
May 20 07:39:01 localhost CRON[15858]: (root) CMD (  [ -x /usr/lib/php/sessionclean ] && if [ ! -d /run/systemd/system ]; then /usr/lib/php/sessionclean; fi)
May 20 07:39:05 localhost systemd[1]: Starting Clean php session files...
vagrant@wordpress-vagrant:/var/log$ sudo head /var/log/syslog -n 2
May 20 06:25:01 localhost rsyslogd:  [origin software="rsyslogd" swVersion="8.32.0" x-pid="502" x-info="http://www.rsyslog.com"] rsyslogd was HUPed
May 20 06:39:01 localhost CRON[15538]: (root) CMD (  [ -x /usr/lib/php/sessionclean ] && if [ ! -d /run/systemd/system ]; then /usr/lib/php/sessionclean; fi)
vagrant@wordpress-vagrant:/var/log$ sudo tail syslog
May 31 10:09:00 localhost systemd[1]: Started Clean php session files.
May 31 10:09:01 localhost CRON[20767]: (root) CMD (  [ -x /usr/lib/php/sessionclean ] && if [ ! -d /run/systemd/system ]; then /usr/lib/php/sessionclean; fi)
May 31 10:17:01 localhost CRON[20834]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
May 31 10:39:01 localhost systemd[1]: Starting Clean php session files...
May 31 10:39:01 localhost systemd[1]: Started Clean php session files.
May 31 10:39:01 localhost CRON[21272]: (root) CMD (  [ -x /usr/lib/php/sessionclean ] && if [ ! -d /run/systemd/system ]; then /usr/lib/php/sessionclean; fi)
May 31 11:09:01 localhost CRON[21961]: (root) CMD (  [ -x /usr/lib/php/sessionclean ] && if [ ! -d /run/systemd/system ]; then /usr/lib/php/sessionclean; fi)
May 31 11:09:02 localhost systemd[1]: Starting Clean php session files...
May 31 11:09:02 localhost systemd[1]: Started Clean php session files.
May 31 11:17:01 localhost CRON[22256]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
$ tail /var/log/syslog -n 2 # output last 2 (-n, number) lines of a file
May 31 11:09:02 localhost systemd[1]: Started Clean php session files.
May 31 11:17:01 localhost CRON[22256]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
```

### 27. `less`

`less` allows us to quicklook files which is much faster than opening them in editor. Less is exited by typing `Q`

Examples:

```bash
$ less somefilename.txt
```

### 28. `diff`

`diff` (short for difference) compares two files and shows the differences between them.

Examples:

```bash
$ diff first.txt second.txt
```

## Networking

### 33. `wget`

`wget` fetches content from remote server. Type `man wget` to get full list of options and configuration parameters

Examples:

```bash
$ wget https://www.google.com/robots.txt # fetch google's robots.txt file to local filesystem
```

### 34. `curl`

`curl` (short for client url) is used - unlike `wget` - for two way data-transfer on remote servers. It also supports a wide range of protocols, such as:
* DICT
* FILE
* FTP
* FTPS
* HTTP
* HTTPS
* IMAP
* IMAPS
* LDAP
* LDAPS
* POP3
* POP3S
* RTMP
* RTSP
* SCP
* SFTP
* SMTP
* SMTPS
* Telnet
* TFTP

To see the overwhelming list of options and configurable things type `man curl`.

Examples:

```bash
$ curl google.com # fetch google.com and display it directly without saving
... a huge amount of html here ...

$ curl -O https://www.google.com/robots.txt # fetch robots.txt from google and save it to current folder (-O, keep the filename as is)
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   230  100   230    0     0   1423      0 --:--:-- --:--:-- --:--:--  1428

$ curl https://www.google.com/robots.txt -o google_robots.txt # fetch robots.txt from google and save it as (-o, output) google_robots.txt to current folder

$ curl -I https://google.com #fetch header-information (-I) about google.com but do not follow redirections
HTTP/2 301
location: https://www.google.com/
content-type: text/html; charset=UTF-8
date: Sat, 01 Jun 2019 10:43:05 GMT
expires: Mon, 01 Jul 2019 10:43:05 GMT
cache-control: public, max-age=2592000
server: gws
content-length: 220
x-xss-protection: 0
x-frame-options: SAMEORIGIN
alt-svc: quic=":443"; ma=2592000; v="46,44,43,39"

$ curl -IL https://google.com #fetch header-information (-I) about google.com but AND follow redirections (-L)
HTTP/2 301
location: https://www.google.com/
content-type: text/html; charset=UTF-8
date: Sat, 01 Jun 2019 10:44:02 GMT
expires: Mon, 01 Jul 2019 10:44:02 GMT
cache-control: public, max-age=2592000
server: gws
content-length: 220
x-xss-protection: 0
x-frame-options: SAMEORIGIN
alt-svc: quic=":443"; ma=2592000; v="46,44,43,39"

HTTP/2 200
date: Sat, 01 Jun 2019 10:44:02 GMT
expires: -1
cache-control: private, max-age=0
content-type: text/html; charset=ISO-8859-1
p3p: CP="This is not a P3P policy! See g.co/p3phelp for more info."
server: gws
x-xss-protection: 0
x-frame-options: SAMEORIGIN
set-cookie: 1P_JAR=2019-06-01-10; expires=Mon, 01-Jul-2019 10:44:02 GMT; path=/; domain=.google.com
set-cookie: NID=184=O_k6HxFx0tNAOUY57UEECv-vPQ6jZejMyW_uuxRqo8g_E4utJA5pKCgqarZy25f9zzpt7arMSsxZsCR8lr8-OLhzq680H86NTUANWozk4SECng8TFdUDFGevGOoZ-LrGHSx0u04NZGiDV3pJx_3ksEPXnH_AEWpKQhr1Ue-tdRw; expires=Sun, 01-Dec-2019 10:44:02 GMT; path=/; domain=.google.com; HttpOnly
alt-svc: quic=":443"; ma=2592000; v="46,44,43,39"
accept-ranges: none
vary: Accept-Encoding

$ curl -d "parameter_1=value_1&parameter_2=value_2" -X POST https://httpbin.org/post # send a POST (-X) request to httpbin with application/x-www-form-urlencoded -header (default) and with data (-d) parameter_1=value_1&parameter_2=value_2
{
  "args": {},
  "data": "",
  "files": {},
  "form": {
    "parameter_1": "value_1",
    "parameter_2": "value_2"
  },
  "headers": {
    "Accept": "*/*",
    "Content-Length": "39",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "httpbin.org",
    "User-Agent": "curl/7.58.0"
  },
  "json": null,
  "origin": "82.203.188.134, 82.203.188.134",
  "url": "https://httpbin.org/post"
}

$ curl -d '{"key1":"value1", "key2":"value2"}' -H "Content-Type: application/json" -X POST https://httpbin.org/post # create a POST (-X) request to httpbin with application/json-header (default) and with json-encoded data (-d) '{"key1":"value1", "key2":"value2"}'
{
  "args": {},
  "data": "{\"key1\":\"value1\", \"key2\":\"value2\"}",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Content-Length": "34",
    "Content-Type": "application/json",
    "Host": "httpbin.org",
    "User-Agent": "curl/7.58.0"
  },
  "json": {
    "key1": "value1",
    "key2": "value2"
  },
  "origin": "82.203.188.134, 82.203.188.134",
  "url": "https://httpbin.org/post"
}
```

### 35. `nslookup`

`nslookup` (short for name server lookup) is used to find (name-service) information of a domain.

Examples:

```bash
$ nslookup google.com # fetch ns-information of google.com
Server:		127.0.0.53 # our system own nameserver
Address:	127.0.0.53#53 # our system operates ns-queries on port 53 (default)

Non-authoritative answer:
Name:	google.com
Address: 172.217.20.46 # google.com IPv4-address
Name:	google.com
Address: 2a00:1450:400f:80c::200e # google.com IPv6-address
```

### 37. `ping`

`ping` (short for Packet InterNet Groper) is used to check the connectivity status between a source and a destination computer/device. We need to

Examples:

```bash
$ ping google.com # ping google.com to see if any packets are lost. By default it pings indefinitely
PING google.com (172.217.21.174) 56(84) bytes of data.
64 bytes from fra07s64-in-f174.1e100.net (172.217.21.174): icmp_seq=1 ttl=63 time=21.8 ms
64 bytes from fra07s64-in-f174.1e100.net (172.217.21.174): icmp_seq=2 ttl=63 time=25.3 ms
64 bytes from fra07s64-in-f174.1e100.net (172.217.21.174): icmp_seq=3 ttl=63 time=31.3 ms
64 bytes from fra07s64-in-f174.1e100.net (172.217.21.174): icmp_seq=4 ttl=63 time=27.6 ms
^C
--- google.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3005ms
rtt min/avg/max/mdev = 21.869/26.539/31.314/3.442 ms

$ ping -c 3 google.com # ping google.com three (-c, count) times to see if any packets are lost.
PING google.com (172.217.21.174) 56(84) bytes of data.
64 bytes from arn11s03-in-f14.1e100.net (172.217.21.174): icmp_seq=1 ttl=63 time=33.4 ms
64 bytes from arn11s03-in-f14.1e100.net (172.217.21.174): icmp_seq=2 ttl=63 time=26.1 ms
64 bytes from arn11s03-in-f14.1e100.net (172.217.21.174): icmp_seq=3 ttl=63 time=23.9 ms

--- google.com ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2005ms
rtt min/avg/max/mdev = 23.958/27.852/33.498/4.091 ms
```

## Seeking files and executables

### 40. `find`

`find` seeks fiels and folder within our filesystem. It's really powerful tools so let's make sure to always check every option with `man find`.

Examples:

```bash
$ find /var/log -type d -name ngi # search from var/log directory for a folder (-type d, directory) named (-name) which starts with ngi
/var/log/nginx

$ find /var/log -type f -name error* # search from /var/log folder for a file (-type f, file) which starts with error
/var/log/nginx/error.log.1
/var/log/nginx/error.log
```

### 41. `which`

`which` is used to locate the executable file associated with the given command by searching it in the $PATH environment variable. It's also a great utility-tool to see if a certain program is installed and working.

Examples:

```bash
$ which python # lookup python executable
/usr/bin/python

$ which java # java isn't installed by default so this returns nothing
```

## Root User

### 29. `sudo`

`sudo` (short for super user do) is a special command which instructs Linux to run command with super-user (root, admin) rights. Some commands / programs require a root-user rights and without `sudo` they won't work.

Examples:

```bash
$ cat /var/log/syslog # even for viewing, syslog requires admin-rights and thus returns error...
cat: /var/log/syslog: Permission denied
$ sudo cat /var/log/syslog # ...but with preceeding the command with sudo it works
May 20 06:25:01 localhost rsyslogd:  [origin software="rsyslogd" swVersion="8.32.0" x-pid="502" x-info="http://www.rsyslog.com"] rsyslogd was HUPed
May 20 06:39:01 localhost CRON[15538]: (root) CMD (  [ -x /usr/lib/php/sessionclean ] && if [ ! -d /run/systemd/system ]; then /usr/lib/php/sessionclean; fi)
May 20 06:39:05 localhost systemd[1]: Starting Clean php session files...
May 20 06:39:05 localhost systemd[1]: Started Clean php session files.
May 20 07:09:01 localhost CRON[15698]: (root) CMD (  [ -x /usr/lib/php/sessionclean ] && if [ ! -d /run/systemd/system ]; then /usr/lib/php/sessionclean; fi)
May 20 07:09:05 localhost systemd[1]: Starting Clean php session files...
May 20 07:09:05 localhost systemd[1]: Started Clean php session files.
May 20 07:17:01 localhost CRON[15788]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
May 20 07:39:01 localhost CRON[15858]: (root) CMD (  [ -x /usr/lib/php/sessionclean ] && if [ ! -d /run/systemd/system ]; then /usr/lib/php/sessionclean; fi)
May 20 07:39:05 localhost systemd[1]: Starting Clean php session files...
...
```

### 30. `su`

`su` (short for switch user) switches our current user to the one typed. If no username given, switches to `root`.

Examples:

```bash
$ su # prompts for root user's password and makes the switch
$ su ubuntu # prompts for ubuntu's password and makes the switch
```

## Installing software

### 42. `apt`

`apt` (short for Advanced Package Tool) is the command line tool to interact with Debian (Ubuntu, etc.) packaging system. Apt has two main tools: `apt-get` for installing, upgrading and cleaning packages and `apt-cache` for finding new packages.

Examples:

```bash
$ sudo apt-get update # apt-get basically works on a database of available packages and updating the package database requires super user privileges so we’ll need to use sudo. This updates only the local registry of packages and doesn't touch the packages at all

$ sudo apt-get upgrade # upgrade actually updates the packages. We can also introduce the -y switch to answer all questions "yes"

$ sudo apt-get upgrade <package_name> # we want to update only specific package

$ sudo apt-get install <package_name> # install a specific package

$ sudo apt-get remove <package_name> # uninstall a specific package (if installed)

$ sudo apt-get purge <package_name> # uninstall a specific package (if installed) and all it's configuration files

$ sudo apt-get clean # clean clears out the local repository of retrieved package files. It removes everything but the lock file from /var/cache/apt/archives/ and /var/cache/apt/archives/partial/.

$ sudo apt-get autoclean # Like clean, autoclean clears out the local repository of retrieved package files. The difference is that it only removes package files that can no longer be downloaded, and are largely useless.

$ sudo apt-get autoremove # Is used to remove packages that were automatically installed to satisfy dependencies for other packages and are now no longer needed.

$ sudo apt-cache search <package_name> # Search package_name from package-cache.
```

### 43. `dpkg`

`dpkg` is used to install, remove, and provide information about `.deb` packages. Sometimes a (Debian-based) package isn't available through package system but needs to be downloaded from elsewhere and be installed with `dpkg`.

Examples:

```bash
$ dpkg -i <package_name>.deb # install package_name.deb which is located in out current working dir.
$dpkg -l # list installed packages
$dpkg -r <package_name></p # Remove package_name
```

## Processes

### 31. `ps`

`ps` (short for process status) is used to display a list of processes currently running.

Examples:

```bash
$ ps # ps without arguments doesn't give that much information...
PID TTY          TIME CMD
2163 pts/0    00:00:00 bash
3551 pts/0    00:00:00 ps

$ ps -e # display information about other users' processes, including those without controlling terminals.
PID TTY          TIME CMD
  1 ?        00:00:01 systemd
  2 ?        00:00:00 kthreadd
  4 ?        00:00:00 kworker/0:0H
  6 ?        00:00:00 mm_percpu_wq
  7 ?        00:00:00 ksoftirqd/0
...

$ ps aux # display processes owned by all users in a user-friendly format
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.8 159536  8720 ?        Ss   14:21   0:01 /sbin/init
root         2  0.0  0.0      0     0 ?        S    14:21   0:00 [kthreadd]
root         4  0.0  0.0      0     0 ?        I<   14:21   0:00 [kworker/0:0H]
root         6  0.0  0.0      0     0 ?        I<   14:21   0:00 [mm_percpu_wq]
root         7  0.0  0.0      0     0 ?        S    14:21   0:00 [ksoftirqd/0]
root         8  0.0  0.0      0     0 ?        I    14:21   0:03 [rcu_sched]
root         9  0.0  0.0      0     0 ?        I    14:21   0:00 [rcu_bh]
root        10  0.0  0.0      0     0 ?        S    14:21   0:00 [migration/0]
root        11  0.0  0.0      0     0 ?        S    14:21   0:00 [watchdog/0]
...
```

### 32. `kill`

`kill` is used to send a signal to a process. It requires a `pid` which can be obtained e.g. with `ps`.

Examples:

```bash
$ kill -L # get a list of numerical signals kill can use
 1) SIGHUP	 2) SIGINT	 3) SIGQUIT	 4) SIGILL	 5) SIGTRAP
 6) SIGABRT	 7) SIGBUS	 8) SIGFPE	 9) SIGKILL	10) SIGUSR1
11) SIGSEGV	12) SIGUSR2	13) SIGPIPE	14) SIGALRM	15) SIGTERM
16) SIGSTKFLT	17) SIGCHLD	18) SIGCONT	19) SIGSTOP	20) SIGTSTP
21) SIGTTIN	22) SIGTTOU	23) SIGURG	24) SIGXCPU	25) SIGXFSZ
26) SIGVTALRM	27) SIGPROF	28) SIGWINCH	29) SIGIO	30) SIGPWR
31) SIGSYS	34) SIGRTMIN	35) SIGRTMIN+1	36) SIGRTMIN+2	37) SIGRTMIN+3
38) SIGRTMIN+4	39) SIGRTMIN+5	40) SIGRTMIN+6	41) SIGRTMIN+7	42) SIGRTMIN+8
43) SIGRTMIN+9	44) SIGRTMIN+10	45) SIGRTMIN+11	46) SIGRTMIN+12	47) SIGRTMIN+13
48) SIGRTMIN+14	49) SIGRTMIN+15	50) SIGRTMAX-14	51) SIGRTMAX-13	52) SIGRTMAX-12
53) SIGRTMAX-11	54) SIGRTMAX-10	55) SIGRTMAX-9	56) SIGRTMAX-8	57) SIGRTMAX-7
58) SIGRTMAX-6	59) SIGRTMAX-5	60) SIGRTMAX-4	61) SIGRTMAX-3	62) SIGRTMAX-2
63) SIGRTMAX-1	64) SIGRTMAX

$ kill -9 610 # send SIGKILL (destroy) signal to process which Process ID (pid) is 610
```

### 38. `grep`

`grep` is used to searc for lines which contain a search pattern. Among many other commands, `grep` offers a huge amount of options so let's always check the `man grep` if we're unsure about anything.

Examples:

```bash
$ grep root /etc/passwd # search for "root" -string in /etc/password-file
root:x:0:0:root:/root:/bin/bash

$ grep -i ROOT /etc/passwd # search case insensitive (-i) ROOT string
root:x:0:0:root:/root:/bin/bash

$ grep -i ROOT /etc/passwd # search case insensitive (-i) ROOT string and display the line-number (-n)
1:root:x:0:0:root:/root:/bin/bash
```

### 39. `xargs`

`xargs` takes its standard input and turns it into command line args. Doesn't do anything by itself so needs to be combined with other programs. More coming in [Pipe](#pipe) section

Examples:

```bash
$ ls / | xargs -I {} echo "Output is: {}" # pipe output of ls to xargs and set a placeholder (-I) which is then used in echo
```

## Working on remote machines

### 44. `ssh`

`ssh` (short for secure shell) is used to operate on remote machines. After a successfull connection our current shell operates in the remote machine. The ssh command reads its configuration from the SSH client configuration file `~/.ssh/config`.

Examples:

```bash
$ ssh ubuntu@192.168.1.1 # open up a secure shell with username ubuntu to IP 192.168.1.1

$ ssh -p 2233 ubuntu@192.168.1.1 # open up a secure shell on port (-p, port) 2233 with username ubuntu to IP 192.168.1.1

$ ssh -p 2233 -i ~/.ssh/somekey.pem ubuntu@192.168.1.1 # open up a secure shell on port (-p, port) 2233 with identity-file (-i) located in ~/.ssh/somekey.pem and with username ubuntu to IP 192.168.1.1
```


## Piping, combining and building up combined commands

The real power of command line relies on _piping_, _combining_ and outputting commands for later use.

### pipe (`|`)

Piping means sending output of a program to another program and it's done by separating the commands with the pipe (`|`) character.

Examples:

```bash
$ ls -l /etc | head -n 5 # list contents of /etc folder and pipe the result to head
total 804
-rw-r--r-- 1 root root    3028 Jul 25  2018 adduser.conf
-rw-r--r-- 1 root root      51 Apr 25 12:03 aliases
-rw-r--r-- 1 root root   12288 Apr 25 12:03 aliases.db
drwxr-xr-x 2 root root    4096 Apr 25 12:06 alternatives

$ ps -e | grep redis # lists processes and pipe the output to grep which finds for word "redis"
552 ?        00:00:25 redis-server

$ find /var/log -type f | xargs grep -il 'error' # find all files inside /var/log and pipe results via xargs to grep and search for 'error'.
/var/log/kern.log
/var/log/syslog
/var/log/apt/term.log
/var/log/apt/history.log
...

$ find /var/log -type f -exec grep -il 'error' {} \; # Same as above but with find-commands -exec. {} is a placeholder which gets filled with result from find.

$ find / -name "*.png" -type f -print0 | xargs -0 tar -cvzf all_imgs.tar.gz # Find every png-file within the filesystem (-print0 instructs to print the full path), pipe the results to xargs (-0 removes spaces in arguments) and finally create a tarball from the images

```

### use output of a command as a variable `$(commandname)`

Command subsitution means running a shell command and store its output to a variable or display it back using echo command.

Examples:

```bash
$ sudo chown -r $(whoami) . # chown current folder recursively (-r) using output of whoami

$ echo "It's $(date +%D) now!" # Echo out a sentence where current date is included formatted
It's 06/01/19 now!
```

### output result (`>` & `>>`)

We can also redirect outputs (STDOUT) of commands to and from files.

Examples:

```bash
$ echo -e "Foo\nBar\nBaz" > somefile.txt # Add lines to somefile.txt. > overrides everything
$ echo -e "\nAnother" >> somefile.txt # Append a line to the file. >> adds to the end
$ xargs -I {} < somefile.txt echo "Line in file: {}" # Read contents (redirect) of a file with xargs and use placeholder {} to echo a sentence per line.
Line in file: Foo
Line in file: Bar
Line in file: Baz
Line in file: Another
```

### Combine commands (`&&`)

Combining separate commands is done by adding double ampersands `&&` between them.

Examples:

```bash
$ ls -l && cd / && ls -l # List contents of current directory, after that cd to root and finally list contents of that directory
```
