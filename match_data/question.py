content = """
QUESTION  1
以下⼯作于OSI  参考模型数据链路层的设备是______。（选择⼀项或多项） 
 
A.  ⼴域⽹交换机     
B.  路由器     
C.  中继器     
   
D.  集线器 
   
 
   
Correct  Answer:  A 
   
Explanation 
   
 
   
Explanation/Reference: 
A.⼴域⽹交换机  B.  路由器  C.  中继器  D.  集线器 
数据链路  ⽹络层  物理层  物理层 
 
QUESTION  2 
下列有关光纤的说法中哪些是错误的？ 
 
A.  多模光纤可传输不同波长不同⼊射⾓度的光 
B.  多模光纤的纤芯较细 
C.  采⽤多模光纤时，信号的最⼤传输距离⽐单模光纤长 
D.  多模光纤的成本⽐单模光纤低 
 
Correct  Answer:  BC 
Explanation 
 
Explanation/Reference: 
 
QUESTION  5
FTP  默认使⽤的控制协议端⼜是______。 
 
A.  20 
B.  21 
C.  23 
D.  22 
 
Correct  Answer:  B 
Explanation 
 
Explanation/Reference: 
A.  20  B.  21  C.  23  D.  22 
ftp数据连接  ftp控制连接  telnet  ssh 
 
QUESTION  6 
⽤______命令可指定下次启动使⽤的操作系统软件。 
 
A.  startup 
B.  boot-loader 
C.  bootfile 
D.  boot  startup 
 
Correct  Answer:  B 
Explanation 
 
Explanation/Reference: 
boot-loader-加载应⽤程序⽂件P192 
 
QUESTION  7 
通常情况下，路由器会对长度⼤于接⼜MTU  的报⽂分⽚。为了检测线路MTU，可以带______参数ping 
⽬的地址。 
 
A.  –a 
B.  –d 
C.  –f 
D.  –c 
 
Correct  Answer:  C 
Explanation 
 
Explanation/Reference: 
-a  ————带源 
-f  ————不允许对ICMP  Echo  Request报⽂进⾏分⽚ 
-tos————  type  of  service  tos域的值  默认0（0-255） 
-t  ————报⽂超时时间  ，默认2000毫秒 
-s  ————报⽂⼤⼩，默认56字节（20-8100） 
-c  ————报⽂数⽬，默认5 
-h  ————指定报⽂ttl值，默认255（0-255） 
-m————指定发送报⽂时间间隔，默认200毫秒  （1-65535） 
 
QUESTION  8 
如果以太⽹交换机中某个运⾏STP  的端⼜不接收或转发数据，接收并发送BPDU，不进⾏地址学习，那么该 
端⼜应该处于______状态。 
 
A.  Blocking 
B.  Listening 
C.  Learning 
D.  Forwarding 
E.  Waiting 
F.  Disable 
 
Correct  Answer:  B 
Explanation 
 
E  xplanation/Reference: 
  接收配置BPDU  发送配置BPDU  MAC地址学习  收发数据 
Disable         
Blocking  √       
Listening  √  √     
Learning  √  √  √   
Forwarding  √  √  √  √ 

 
QUESTION  10 
配置交换机SWA  的桥优先级为0  的命令为______。 
 
A.  [SWA]  stp  priority  0 
B.  [SWA-Ethernet1/0/1]  stp  priority  0 
C.  [SWA]  stp  root  priority  0 
D.  [SWA-Ethernet1/0/1]  stp  root  priority  0 
 
Correct  Answer:  A 
Explanation 
 
Explanation/Reference: 
 
 
QUESTION  11 
IP  地址10.0.10.32  和掩码255.255.255.224  代表的是⼀个______。 
 
A.  主机地址 
B.  ⽹络地址 
C.  ⼴播地址 
D.  以上都不对 
 
Correct  Answer:  B 
Explanation 
 
Explanation/Reference: 
10.  0.  10.  001  00000 
255.255.255.111  00000 
 
QUESTION  12 
IP  地址132.119.100.200  的⼦⽹掩码是255.255.255.240，哪么它所在⼦⽹的⼴播地址是______。 
 
A.  132.119.100.207 
B.  132.119.100.255 
C.  132.119.100.193 
D.  132.119.100.223 
 
Correct  Answer:  A 
Explanation 
 
Explanation/Reference: 
132.119.100.1100  1000 
132.119.100.1100  1111  ….  ⼴播地址 
 
QUESTION  13 
TFTP  采⽤的传输层知名端⼜号为______。 
 
A.  67 
B.  68 
C.  69 
D.  53 
 
Correct  Answer:  C 
Explanation 
 
Explanation/Reference: 
TCP（6）：ftp——20/21 
ssh——22 
telnet——23 
smtp——25  接收邮件 
pop3——110  发送邮件 
DNS——53 
http——  80 
https——443  http安全版，下加⼊ssl层 
UDP(17)  ：DNS——53 
Bootp——67服务器/68客户端（就是dhcp  ，dhcp基于bootp发展⽽来  ） 
Tftp——69 
Snmp——161/162  服务器监听的端⼜号161，客户端监听端⼜号 
 
QUESTION  14 
在Windows  操作系统中，哪⼀条命令能够显⽰ARP  表项信息？ 
 
A.  display  arp 
B.  arp  –a 
C.  arp  –d 
D.  show  arp 
 
Correct  Answer: 
Explanation 
 
Explanation/Reference: 
arp  –  d  删除arp表项 
arp  –s  IP  MAC  ——MAC静态绑定arp 
 
QUESTION  15 
客户的⽹络连接形如： 
HostA----GE0/0--MSR-1--S1/0-----WAN-----S1/0--MSR-2--GE0/0----HostB 
两台MSR  路由器通过⼴域⽹实现互连，⽬前物理连接已经正常。MSR-1  的接⼜S1/0  地址为3.3.3.1/30， 
MSR-2  的接⼜S1/0  地址为3.3.3.2/30，现在在MSR-1  上配置了如下三条静态路由： 
ip  route-static  192.168.1.0  255.255.255.0  3.3.3.2 
ip  route-static  192.168.2.0  255.255.255.0  3.3.3.2 
ip  route-static  192.168.0.0  255.255.255.0  3.3.3.2 
其中192.168.0.0/22  ⼦⽹是主机HostB  所在的局域⽹段。那么如下描述哪些是正确的？（选择⼀项或多项） 
 
A.  这三条路由都会被写⼊MSR-1  的路由表 
B.  只有第三条路由会被写⼊MSR-1  的路由表 
C.  这三条路由可以被⼀条路由ip  route-static  192.168.0.0  255.255.252.0  3.3.3.2  代替 
D.  只有第⼀条路由会被写⼊MSR-1  的路由表 
 
Correct  Answer:  AC 
Explanation 
 
Explanation/Reference: 
第三条注意掩码24位，不能代替前两条 
 
QUESTION  16 
如下哪种路由协议只关⼼到达⽬的⽹段的距离和⽅向？（选择⼀项或多项） 
 
A.  IGP 
B.  OSPF 
C.  RIPv1 
D.  RIPv2 
 
Correct  Answer:  CD 
Explanation 
 
Explanation/Reference: 
 

QUESTION  18 
在路由器的路由表中有⼀条默认路由，其⽬的⽹段和掩码都是0.0.0.0，⽽其下⼀跳是路由器的S0/0  接⼜， 
那么下列关于此路由的描述正确的是______。 
 
A.  当路由器收到去往⽬的地址120.1.1.1  的数据包时，如果路由器表中没有其他确切匹配项，那么该数据包 
将匹配此默认路由 
B.  该路由的掩码最短，因此只有在没有其它路由匹配数据包的情况下，数据包才会按照默认路由转发 
C.  这条路由的度量值有可能是3 
D.  这条路由的优先级有可能是100 
 
Correct  Answer:  ABCD 
Explanation 
 
Explanation/Reference: 
静态默认路由度量值为0，不可能 
协议默认路由的度量值可能是3  ， 
stub区域： 
 
 
 
 
 
 
 
 
 
设置为stub区域后，产⽣⼀条三类lsa默认路由，该默认路由度量值类似引⼊外部路由 
将RTD接⼜开销设置为2，则可达到题中效果 
 
 
QUESTION  19 
在运⾏了RIP  的MSR  路由器上看到如下路由信息： 
<MSR>display  ip  routing-table  6.6.6.6 
Routing  Table  :  Public 
Summary  Count  :  2 
Destination/Mask  Proto  Pre  Cost  NextHop  Interface 
6.6.0/24  RIP  100  1  100.1.1.1  GE0/0 
6.0.0.0/8  Static  60  0  100.1.1.1  GE0/0 
此时路由器收到⼀个⽬的地址为6.6.6.6  的数据包，那么______。 
 
A.  该数据包将优先匹配路由表中的RIP  路由，因为其掩码最长 
B.  该数据包将优先匹配路由表中RIP  路由，因为其优先级⾼ 
C.  该数据包将优先匹配路由表中的静态路由，因为其花费Cost  ⼩ 
D.  该数据包将优先匹配路由表中的静态路由，因为其掩码最短 
 
Correct  Answer:  A 
Explanation 
 
Explanation/Reference: 
只有优先级最⾼的会被加⼊路由表，掩码不同都会被加⼊路由表 
路由表查找规则1）最长匹配转发  2）⾮直连⽹段迭代查找  3）默认路由最后匹配 
 
QUESTION  20 
⼀台空配置MSR  路由器RTA  分别通过GE0/0、GE1/0  连接两台运⾏在OSPF  Area  0  的路由器RTB  和 
RTC。RTA  的接⼜GE0/0  和GE1/0  的IP  地址分别为192.168.3.2/24  和192.168.4.2/24。在RTA  上添加如下 
配置： 
[MSR-ospf-1]  area  0.0.0.0 
[MSR-ospf-1-area-0.0.0.0]network  192.168.0  0.0.3.255 
[MSR-GigabitEthernet0/0]ospf  cost  2 
[MSR-GigabitEthernet1/0]ospf  dr-priority  0 
那么关于上述配置描述正确的是_____。（选择⼀项或多项） 
 
A.  该配置在MSR  路由器的GE0/0、GE1/0  上都启动了OSPF 
B.  该配置只在MSR  路由器的GE0/0  接⼜上启动了OSPF 
C.  RTA  可能成为两个GE  接⼜所在⽹段的DR 
D.  RTA  只可能成为其中⼀个GE  接⼜所在⽹段的DR 
E.  修改接⼜GE0/0  的Cost  不影响OSPF  邻接关系的建⽴ 
 
Correct  Answer:  BDE 
Explanation 
 
Explanation/Reference: 
[MSR-ospf-1-area-0.0.0.0]network  192.168.0  0.0.3.255 
掩码22，说明在接⼜⽹段为0.0  、1.0、  2.0、  3.0  上启动ospf 
G1/0接⼜优先级改为0，优先级为0的接⼜不参与DR,BDR选举 
 
QUESTION  21 
客户路由器的接⼜GigabitEthernet0/0  下连接了局域⽹主机HostA，其IP  地址为192.168.0.2/24；接⼜ 
Serial6/0  接⼜连接远端，⽬前运⾏正常。现增加ACL  配置如下： 
firewall  enable 
firewall  default  permit 
acl  number  3003 
rule  0  permit  tcp 
rule  5  permit  icmp 
acl  number  2003 
rule  0  deny  source  192.168.0.0  0.0.0.255 
interface  GigabitEthernet0/0 
firewall  packet-filter  3003  inbound 
firewall  packet-filter  2003  outbound 
ip  address  192.168.0.1  255.255.255.0 
interface  Serial6/0 
link-protocol  ppp 
ip  address  6.6.6.2  255.255.255.0 
假设其他相关配置都正确，那么______。（选择⼀项或多项） 
 
A.  HostA  不能ping  通该路由器上的两个接⼜地址 
B.  HostA  不能ping  通6.6.6.2，但是可以ping  通192.168.0.1 
C.  HostA  不能ping  通192.168.0.1，但是可以ping  通6.6.6.2 
D.  HostA  可以Telnet  到该路由器上 
 
Correct  Answer:  CD 
Explanation 
 
Explanation/Reference: 
ACL实际上起限制作⽤的只有2003 
3003，允许  tcp  icmp，默认允许⽆意义 
注意：拒绝掉的是源地址192.168.0.0/24的所有报⽂，包括icmp的echo，echo-reply等 
⽤在的是G0/0接⼜的outbound⽅向，当A  ping⽹关时，⽹关返回的icmp  echo  reply报⽂被deny 
如果⽤在G0/0  inbound⽅向，A  ping⽹关时，发送的icmp  echo报⽂被deny 
Ping  6.6.6.2  同理 
 

QUESTION  24 
在配置ISDN  DCC  的时候，客户在⾃⼰的MSR  路由器上配置了如下的dialer-rule： 
[MSR]  dialer-rule  1  acl  3000那么关于此配置如下哪些说法正确？（选择⼀项或多项） 
A.  只有匹配ACL  3000  的数据包能触发拨号 
B.  只有匹配ACL  3000  的数据包会被路由器通过拨号链路发送 
C.  没有定义permit  或者deny，配置错误 
D.  正确的配置应为：[MSR]  dialer-rule  1  acl  3000  permit 
 
Correct  Answer:  A 
Explanation 
 
Explanation/Reference: 
 
 
QUESTION  25 
两台空配置的MSR  路由器RTA、RTB  通过各⾃的Serial1/0  接⼜背靠背互连。在两台路由器上做如下配置： 
RTA：跳过 
[RouterA-Serial1/0]  link-protocol  fr  ietf 
[RouterA-Serial1/0]  ip  address  10.1.1.1  30 
[RouterA-Seria11/0]  fr  map  ip  10.1.1.2  30 
RTB： 
[RouterB-Serial1/0]  link-protocol  fr  ietf 
[RouterB-Serial1/0]  interface  serial0/0.1 
[RouterB-Serial1/0.1]  ip  address  10.1.1.2  30 
[RouterB-Serial1/0.1]  fr  map  ip  10.1.1.1  30 
路由器之间的物理链路良好，那么下⾯说法正确的是______。（选择⼀项或多项） 
 
A.  两台路由器上都没有配置DLCI，在RTA  上不能ping  通RTB 
B.  在RTA  上不能ping  通10.1.1.2 
C.  在RTA  上可以ping  通10.1.1.2 
D.  在上述配置中，如果仅将RTB  上⼦接⼜serial0/0.1  的类型改为P2MP，那么在RTA  上不能ping  通 
10.1.1.2 
E.  在上述配置中，如果仅将RTB  上⼦接⼜serial0/0.1  的类型改为P2MP，那么在RTA  上可以ping  通 
10.1.1.2 
 
Correct  Answer:  BD 
Explanation 
 
Explanation/Reference: 
 
 
QUESTION  26 
以下关于星型⽹络拓扑结构的描述正确的是______。（选择⼀项或多项） 
 
A.  星型拓扑易于维护 
B.  在星型拓扑中，某条线路的故障不影响其它线路下的计算机通信 
C.  星型拓扑具有很⾼的健壮性，不存在单点故障的问题  中⼼结点故障 
D.  由于星型拓扑结构的⽹络是共享总线带宽，当⽹络负载过重时会导致性能下降 
 
Correct  Answer:  AB 
Explanation 
 
Explanation/Reference: 
Hub连接总线型⽹络共享总线带宽 
 
QUESTION  27 
以下关于星型⽹络拓扑结构的描述错误的是______。（选择⼀项或多项） 
 
A.  星型拓扑易于维护 
B.  在星型拓扑中，某条线路的故障不影响其它线路下的计算机通信 
C.  星型拓扑具有很⾼的健壮性，不存在单点故障的问题 
D.  由于星型拓扑结构的⽹络是共享总线带宽，当⽹络负载过重时会导致性能下降 
 
Correct  Answer:  CD 
Explanation 
 
Explanation/Reference: 
 
 
QUESTION  28 
以下关于电路交换和分组交换的描述正确的是______。（选择⼀项或多项） 
 
A.  电路交换延迟⼩，传输实时性强 
B.  电路交换⽹络资源利⽤率⾼ 
C.  分组交换延迟⼤，传输实时性差 
D.  分组交换⽹络资源利⽤率低 
 
Correct  Answer:  AC 
Explanation 
 
Explanation/Reference: 
电路交换:  优点  延迟⼩，透明传输 
缺点  固定带宽，⽹络资源利⽤率低 
分组交换：优点  多路复⽤，⽹络资源利⽤率⾼ 
缺点：延迟⼤，实时性差，设备功能复杂 
 
QUESTION  29 
以下关于电路交换和分组交换的描述正确的是______。（选择⼀项或多项） 
 
A.  分组交换⽹络资源利⽤率低 
B.  分组交换延迟⼤，传输实时性差 
C.  电路交换⽹络资源利⽤率⾼ 
D.  电路交换延迟⼩，传输实时性强 
 
Correct  Answer:  BD 
Explanation 
 
Explanation/Reference: 
 
 
QUESTION  30 
⽹络的延迟（delay）定义了⽹络把数据从⼀个⽹络节点传送到另⼀个⽹络节点所需要的时间。⽹络延迟包 
括______。 
 
A.  传播延迟（propagation  delay） 
B.  交换延迟（switching  delay） 
C.  介质访问延迟（access  delay） 
D.  队列延迟（queuing  delay） 
 
Correct  Answer:  AB 
Explanation 
 
Explanation/Reference: 
⽹络的延迟包括：传播延迟PD、交换延迟SD、介质访问延迟AD、队列延迟QD 
 
QUESTION  31 
集线器（Hub）⼯作在OSI  参考模型的______。 
 
A.  物理层 
B.  数据链路层 
C.  ⽹络层 
D.  传输层 
 
Correct  Answer:  A 
Explanation 
 
Explanation/Reference: 
 
 
QUESTION  32 
TCP/IP  协议栈包括以下哪些层次？ 
 
A.  ⽹络层 
B.  传输层 
C.  会话层 
D.  应⽤层 
E.  ⽹络接⼜层 
F.  表⽰层 
 
Correct  Answer:  ABDE 
Explanation 
 
Explanation/Reference: 
 
 
QUESTION  33 
在⽹络层上实现⽹络互连的设备是______。 
 
A.  路由器 
B.  交换机 
C.  集线器 
D.  中继器 
 
Correct  Answer:  A 
Explanation 
 
Explanation/Reference: 
路由器和三层交换机 
 
QUESTION  34 
在开放系统互连参考模型（OSI）中，______以帧的形式传输数据流。 
 
A.  ⽹路层 
B.  会话层 
C.  传输层 
D.  数据链路层 
 
Correct  Answer:  D 
Explanation 
 
Explanation/Reference:   
应⽤层  APDU 
表⽰层  PPDU 
会话层  SPDU 
传输层  段segment 
 
⽹络层  包packet 
 
数据链路层  帧frame 
物理层  ⽐特流bit   
 
QUESTION  35 
OSI  参考模型具有以下哪些优点？ 
 
A.  OSI  参考模型提供了设备间的兼容性和标准接⼜，促进了标准化⼯作。 
B.  OSI  参考模型是对发⽣在⽹络设备间的信息传输过程的⼀种理论化描述，并且定义了如何通过硬件和软 
件实现每⼀层功能。 
C.  OSI  参考模型的⼀个重要特性是其采⽤了分层体系结构。分层设计⽅法可以将庞⼤⽽复杂的问题转化为 
若⼲较⼩且易于处理的问题。 
D.  以上说法均不正确。 
 
Correct  Answer:  AC 
Explanation 
 
Explanation/Reference: 
 
 
QUESTION  36 
OSI  参考模型具有以下哪些优点？ 
 
A.  OSI  参考模型提供了设备间的兼容性和标准接⼜，促进了标准化⼯作。 
B.  OSI  参考模型的⼀个重要特性是其采⽤了分层体系结构。分层设计⽅法可以将庞⼤⽽复杂的问题转化为 
若⼲较⼩且易于处理的问题。 
C.  OSI  参考模型是对发⽣在⽹络设备间的信息传输过程的⼀种理论化描述，并且定义了如何通过硬件和软 
件实现每⼀层功能。 
D.  以上说法均不正确。 
 
Correct  Answer:  AB 
Explanation 
 
Explanation/Reference: 
 
 
QUESTION  37 
下⾯关于OSI  参考模型各层功能的说法正确的是______。（选择⼀项或多项） 
 
A.  物理层涉及在通信信道（Channel）上传输的原始⽐特流，它定义了传输数据所需要的机械、电⽓功能 
及规程等特性。 
B.  ⽹络层决定传输报⽂的最佳路由，其关键问题是确定数据包从源端到⽬的端如何选择路由。 
C.  传输层的基本功能是建⽴、维护虚电路，进⾏差错校验和流量控制。 
D.  会话层负责数据格式处理、数据加密等。 
E.  应⽤层负责为应⽤程序提供⽹络服务。 
 
Correct  Answer:  ABCE 
Explanation 
 
Explanation/Reference: 
 
 
QUESTION  38 
下⾯关于OSI  参考模型各层功能的说法错误的是______。（选择⼀项或多项） 
 
A.  物理层涉及在通信信道（Channel）上传输的原始⽐特流，它定义了传输数据所需要的机械、电⽓功能 
及规程等特性。 
B.  ⽹络层决定传输报⽂的最佳路由，其关键问题是确定数据包从源端到⽬的端如何选择路由。
C.  传输层的基本功能是建⽴、维护虚电路，进⾏差错校验和流量控制。 
D.  会话层负责数据格式处理、数据加密等。 
E.  应⽤层负责为应⽤程序提供⽹络服务。 
 
Correct  Answer:  D 
Explanation 
 
E  xplanation/Reference: 
应⽤层  为应⽤进程提供⽹络服务   
 
表⽰层  定义数据格式与结构、协商上层数据格式、数据加密压缩 
 
会话层  主机间通信，建⽴、维护、终结应⽤程序间会话，⽂字处理、邮件、表格 
 
传输层  分段上层数据，端到端连接，透明可靠传输，差错校验、重传，流量控制 
 
⽹络层  编址，路由，拥塞控制，异种⽹络互连   
数据链路层  编帧、链路建⽴/维持/释放，流量控制，差错校验，寻址，标识上层数据   
物理层  电压，接⼜，线缆，传输距离等物理参数。四⼤特性：机械、电器、功能、规   
程   
 
QUESTION  39 
下⾯关于OSI  参考模型各层功能的说法正确的是______。（选择⼀项或多项） 
 
A.  会话层负责数据格式处理、数据加密等。 
B.  传输层的基本功能是建⽴、维护虚电路，进⾏差错校验和流量控制。 
C.  ⽹络层决定传输报⽂的最佳路由，其关键问题是确定数据包从源端到⽬的端如何选择路由。 
D.  物理层涉及在通信信道（Channel）上传输的原始⽐特流，它定义了传输数据所需要的机械、电⽓功能 
及规程等特性。 
E.  应⽤层负责为应⽤程序提供⽹络服务。 
 
Correct  Answer:  BCDE 
Explanation 
 
Explanation/Reference: 
 
 
QUESTION  40 
下⾯关于OSI  参考模型的说法正确的是______。（选择⼀项或多项） 
 
A.  传输层的数据称为帧（Frame） 
B.  ⽹络层的数据称为段（Segment） 
C.  数据链路层的数据称为数据包（Packet） 
D.  物理层的数据称为⽐特（Bit） 
 
Correct  Answer:  D 
Explanation 
 
Explanation/Reference: 
 
 
QUESTION  41 
OSI  参考模型物理层的主要功能是______。（选择⼀项或多项） 
 
A.  物理地址定义 
B.  建⽴端到端连接 
C.  在终端设备间传送⽐特流，定义了电压、接⼜、电缆标准和传输距离等 
D.  将数据从某⼀端主机传送到另⼀端主机 
 
Correct  Answer:  C 
Explanation 
Explanation/Reference: 
 
 
QUESTION  42 
IP  协议对应于OSI  参考模型的第______层。 
 
A.  5 
B.  3 
C.  2 
D.  1 
 
Correct  Answer:  B 
Explanation 
 
Explanation/Reference: 
应⽤层协议：见T13 
传输层协议：TCP(6)  UDP(17) 
⽹络层协议：IP,ICMP（ICMP消息可分为ICMP差错消息和ICMP查询消息）,IGMP（互联⽹组管理协议，负 
责管理组播组） 
⽹络接⼜层协议：以太⽹、令牌环，HDLC,PPP,X.25,帧中继,PSTN,ISDN等 
 
QUESTION  43 
在OSI  参考模型中，⽹络层的功能主要是______。（选择⼀项或多项） 
 
A.  在信道上传输原始的⽐特流 
B.  确保到达对⽅的各段信息正确⽆误 
C.  确定数据包从源端到⽬的端如何选择路由 
D.  加强物理层数据传输原始⽐特流的功能，并且进⾏流量调控 
 
Correct  Answer:  C 
Explanation 
 
Explanation/Reference: 
 
 
QUESTION  44 
数据分段是在OSI  参考模型中的______完成的。（选择⼀项或多项） 
 
A.  物理层 
B.  ⽹络层 
C.  传输层 
D.  接⼊层 
 
Correct  Answer:  C 
Explanation 
 
Explanation/Reference: 
 
 
QUESTION  45 
提供端到端可靠数据传输和流量控制的是OSI  参考模型的______。 
 
A.  表⽰层 
B.  ⽹络层 
C.  传输层 
D.  会话层 
Correct  Answer:  C 
Explanation 
 
Explanation/Reference: 
 
 
QUESTION  46 
在OSI  参考模型中，加密是______的功能。 
 
A.  物理层 
B.  传输层 
C.  会话层 
D.  表⽰层 
 
Correct  Answer:  D 
Explanation 
 
Explanation/Reference: 
 
 
QUESTION  47 
TCP  属于OSI  参考模型的______。 
 
A.  ⽹络层 
B.  传输层 
C.  会话层 
D.  表⽰层 
 
Correct  Answer:  B 
Explanation 
 
Explanation/Reference: 
 
 
QUESTION  48 
UDP  属于OSI  参考模型的______。 
 
A.  ⽹络层 
B.  传输层 
C.  会话层 
D.  表⽰层 
 
Correct  Answer:  B 
Explanation 
 
Explanation/Reference: 
 
 
QUESTION  49 
SPX  属于OSI  参考模型的______。 
 
A.  ⽹络层 
B.  传输层 
C.  会话层 
D.  表⽰层 
 
Correct  Answer:  B 
Explanation 
 
Explanation/Reference: 
传输层协议有TCP/IP协议族的TCP/UDP  ,以及IPX/SPX协议族的SPX等 
 
QUESTION  50 
DNS  ⼯作于OSI  参考模型的______。 
 
A.  ⽹络层 
B.  传输层 
C.  会话层 
D.  应⽤层 
 
Correct  Answer:  D 
Explanation 
 
Explanation/Reference: 
 
 
QUESTION  51 
⽤以太⽹线连接两台交换机，互连端⼜的MDI  类型都配置为across，则此以太⽹线应该为________。 
 
A.  只能使⽤交叉⽹线 
B.  只能使⽤直连⽹线 
C.  平⾏⽹线和交叉⽹线都可以 
D.  平⾏⽹线和交叉⽹线都不可以 
 
Correct  Answer:  A 
Explanation 
 
Explanation/Reference: 
同层设备交叉线，不同层直连线 
以太⽹交换机接⼜类型MDI/MDIX⾃适应 
MDI直通线 
MDIX交叉线 
这⾥设置成MDI，只能⽤交叉线 
 
QUESTION  52 
下列关于以太⽹的说法正确的是________。（选择⼀项或多项） 
 
A.  以太⽹是基于共享介质的⽹络 
B.  以太⽹采⽤CSMA/CD  机制 
C.  以太⽹传输距离短，最长传输距离为500m 
D.  以上说法均不正确 
 
Correct  Answer:  AB 
Explanation 
 
Explanation/Reference: 
10BASE以太⽹传输距离跟传输介质有关 
10BASE5  粗同轴电缆  500m 
10BASE2  细同轴电缆  200m  （同轴电缆布设繁琐，不便使⽤） 
10BASE-T双绞线  三类UTP  100m  （逐渐成为以太⽹标准） 
五类  150m 
 
QUESTION  53 
100BASE-TX  的标准物理介质是______。 
 
A.  粗同轴电缆 
B.  细同轴电缆 
C.  3  类双绞线 
D.  5  类双绞线 
E.  光纤 
 
Correct  Answer:  D 
Explanation 
 
Explanation/Reference: 
100BASE-TX  2对五类双绞线 
100BASE-FX  多模光纤 
100BASE-T4  4对三类双绞线 
1000BASE-SX  多模光纤 
LX  单模 
 
QUESTION  54 
以下关于CSMA/CD  的说法中正确的是______。（选择⼀项或多项） 
 
A.  CSMA/CD  应⽤在总线型以太⽹中，主要解决在多个站点同时发送数据时如何检测冲突、确保数据有序 
传输的问题。 
B.  当连在以太⽹上的站点要传送⼀个帧时，它必须等到信道空闲，即载波消失。 
C.  信道空闲时站点才能开始传送它的帧。 
D.  如果两个站点同时开始传送，它们将侦听到信号的冲突，并暂停帧的发送。 
 
Correct  Answer:  ABCD 
Explanation 
 
Explanation/Reference: 
 
 
QUESTION  55 
下列有关MAC  地址的说法中哪些是正确的？ 
 
A.  以太⽹⽤MAC  地址标识主机 
B.  MAC  地址是⼀种便于更改的逻辑地址 
C.  MAC  地址固化在ROM  中，通常情况下⽆法改动 
D.  通常只有终端主机才需要MAC  地址，路由器等⽹络设备不需要 
 
Correct  Answer:  AB 
Explanation 
 
Explanation/Reference: 
FLASH存储器：存储应⽤程序⽂件，配置⽂件 
IP地址在操作系统的RAM（随机访问存储器，⽤于随机存储，如当前配置）中 
MAC地址固化在⽹卡ROM（只读存储器，存储BOOTROM程序，，⽤于在应⽤程序or配置⽂件故障时的回 
复⼿段）中， 
理论不可改，全球唯⼀ 
MAC  48位  :  24位OUI  （申请，标志⼚商）  +  24位EUI 
IP地址将物理地址对上层隐藏，使internet表现出统⼀地址格式，但实际通信ip地址不能被物理⽹络识别，物 
理⽹络使⽤依然物理地址，因此arp解析出MAC是必要的 
即设备之间数据通信既要知道ip地址也要解析MAC地址 
 
QUESTION  56 
下列有关MAC  地址的说法中哪些是错误的？ 
 
A.  以太⽹⽤MAC  地址标识主机 
B.  MAC  地址是⼀种便于更改的逻辑地址 
C.  MAC  地址固化在ROM  中，通常情况下⽆法改动 
D.  通常只有终端主机才需要MAC  地址，路由器等⽹络设备不需要 
Correct  Answer:  BD 
Explanation 
 
Explanation/Reference: 
 
 
QUESTION  57 
下列有关光纤的说法哪些是正确的？ 
 
A.  多模光纤可传输不同波长不同⼊射⾓度的光 
B.  多模光纤的成本⽐单模光纤低 
C.  采⽤多模光纤时，信号的最⼤传输距离⽐单模光纤长 
D.  多模光纤的纤芯较细 
 
Correct  Answer:  AB 
Explanation 
 
Explanation/Reference: 
 
 
QUESTION  58 
WLAN（Wireless  LAN）是计算机⽹络与⽆线通信技术相结合的产物。下列哪些属于WLAN  技术标准？ 
（选择⼀项或多项） 
 
A.  802.11a 
B.  802.11b 
C.  802.11c 
D.  802.11g 
 
Correct  Answer:  AB 
Explanation 
 
Explanation/Reference: 
最⾼传输速率  802.11  2Mbps 
802.11  a  54 
802.11  g  54 
802.11  b  11 
802.11  n  300 
b/g相互兼容，与a不兼容 
 
QUESTION  59 
802.11b  协议在2.4GHz  频段定义了14  个信道，相邻的信道之间在频谱上存在交叠。为了最⼤程度地利⽤频 
段资源，可以使⽤如下哪组信道来进⾏⽆线覆盖？（选择⼀项或多项） 
 
A.  1、5、9 
B.  1、6、11 
C.  2、6、10 
D.  3、6、9 
 
Correct  Answer:  B 
Explanation 
 
Explanation/Reference: 
两两之间相差要≥5 
 
QUESTION  60 
802.11b  协议在2.4GHz  频段定义了14  个信道，相邻的信道之间在频谱上存在交叠。为了最⼤程度地利⽤频 
段资源，可以使⽤如下哪组信道来进⾏⽆线覆盖？（选择⼀项或多项） 
A.  1、5、9 
B.  1、6、10 
C.  2、7、12 
D.  3、6、9 
 
Correct  Answer:  C 
Explanation 
 
Explanation/Reference: 
两两之间相差要≥5 
 
QUESTION  61 
⼴域⽹接⼜多种多样，下列对于⼴域⽹接⼜的描述错误的是______。（选择⼀项或多项） 
 
A.  V.24  规程接⼜可以⼯作在同异步两种⽅式下，在异步⽅式下，链路层使⽤PPP  封装。 
B.  V.35  规程接⼜可以⼯作在同异步两种⽅式下，在异步⽅式下，链路层使⽤PPP  封装。 
C.  BRI/PRI  接⼜⽤于ISDN  接⼊，默认的链路封装是PPP 
D.  G.703  接⼜提供⾼速数据同步通信服务。 
 
Correct  Answer:  B 
Explanation 
 
Explanation/Reference: 
V．24  ⽀持同、异步：异步最⾼速率115kps  同步最⾼速率64kbps 
V．35  只⽀持同步：  最⾼速率为2048000bps=  2Mbps 
ISDN两种接⼊⽅式：BRI接⼜  →2B+D  B信道64kbps  D信道16kbps 
PRI接⼜  →E1  30B+D 
T1  23B+D 
默认PPP封装 
 
QUESTION  62 
⼴域⽹接⼜多种多样，下列对于⼴域⽹接⼜的描述正确的是______。（选择⼀项或多项） 
 
A.  V.24  规程接⼜可以⼯作在同异步两种⽅式下，在异步⽅式下，链路层使⽤PPP  封装。 
B.  V.35  规程接⼜可以⼯作在同异步两种⽅式下，在异步⽅式下，链路层使⽤PPP  封装。 
C.  BRI/PRI  接⼜⽤于ISDN  接⼊，默认的链路封装是PPP 
D.  G.703  接⼜提供⾼速数据同步通信服务。 
 
Correct  Answer:  ACD 
Explanation 
 
Explanation/Reference: 
 
 
QUESTION  63 
对于分组交换⽅式的理解，下列说法中正确的是______。（选择⼀项或多项） 
 
A.  分组交换是⼀种基于存储转发（Store-and-Forward  switching）的交换⽅式 
B.  传输的信息被划分为⼀定长度的分组，以分组为单位进⾏转发 
C.  每个分组都载有接收⽅和发送⽅的地址标识，分组可以不需要任何操作⽽直接转发，从⽽提⾼了效率 
D.  分组交换包括基于帧的分组交换和基于信元的分组交换 
 
 
Correct  Answer:  ABD 
Explanation 
 
Explanation/Reference: 
对每个分组都要去查看源和⽬的，重新操作，逐⼀对分组进⾏转发，增加了延迟 
但资源利⽤率⾼，虽然某⼀时刻线路是被某⼀分组独占，但是线路带宽在多路复⽤后，总的利⽤率⾼ 
 
QUESTION  64 
对于分组交换⽅式的理解，下列说法中正确的是______。（选择⼀项或多项） 
 
A.  分组交换是⼀种基于直通转发（cut-through  switching  ）的交换⽅式 
B.  传输的信息被划分为⼀定长度的分组，以分组为单位进⾏转发 
C.  分组交换包括基于帧的分组交换和基于信元的分组交换 
D.  每个分组都载有接收⽅和发送⽅的地址标识，分组可以不需要任何操作⽽直接转发，从⽽提⾼了效率 
 
Correct  Answer:  BC 
Explanation 
 
Explanation/Reference: 
 
 
QUESTION  65 
某公司组建公司⽹络需要进⾏⼴域⽹连接，要求该连接的带宽⼤于1Mbps，则下⾯哪些接⼜和协议可⽤？ 
 
A.  V.35  规程接⼜及线缆，使⽤PPP  作为链路层协议 
B.  V.35  规程接⼜及线缆，使⽤Frame  Relay  作为链路层协议 
C.  PRI  接⼜及线缆，捆绑多个时隙，使⽤PPP  作为链路层协议 
D.  BRI  接⼜及线缆，捆绑多个时隙，使⽤PPP  作为链路层协议。 
 
 
Correct  Answer:  ABC 
Explanation 
 
Explanation/Reference: 
V．24  ⽀持同、异步：异步最⾼速率115kbps  同步最⾼速率64kbps 
V．35  只⽀持同步：  最⾼速率为2048000bps=  2Mbps 
ISDN两种接⼊⽅式：BRI接⼜  →2B+D  B信道64kbps  D信道16kbps  最⼤速率144kbps 
PRI接⼜  →E1  30B+D  最⼤速率2Mbps 
T1  23B+D  最⼤速率1.544Mbps 
 
QUESTION  66 
客户的两台路由器通过V.35  电缆背靠背连接在⼀起，其中⼀台路由器上有如下接⼜信息： 
[MSR-Serial0/0]display  interface  Serial  0/0 
Serial0/0  current  state:  UP 
Line  protocol  current  state:  UP 
Description:  Serial6/0  Interface 
The  Maximum  Transmit  Unit  is  1500,  Hold  timer  is  10(sec) 
Internet  Address  is  6.6.6.1/30  Primary 
Link  layer  protocol  is  PPP 
LCP  opened,  IPCP  opened 
从上述信息可以得知______。 
 
A.  这台路由器已经和远端设备完成了PPP  协商，并成功建⽴了PPP  链路 
B.  这台路由器和远端设备之间成功完成了PPP  PAP  或者CHAP  的验证  验证可选项，题中⽆法看出是否设 
有验证、是否通过 
C.  在这台路由器上已经可以ping  通对端的地址6.6.6.2  了  ⽆法判断是否通过了验证，所以对端地址也不⼀ 
定可以ping通 
D.  该接⼜信息提⽰，在该接⼜下还可以配置第⼆个IP  地址  subordinate 
 
Correct  Answer:  AD 
Explanation 
 
Explanation/Reference: 
 
QUESTION  67 
客户的两台路由器通过V.35  电缆背靠背连接在⼀起，并在V.35  接⼜上运⾏了PPP  协议，在其中⼀台路 
由器上有如下接⼜信息： 
[MSR-Serial0/0]display  interface  Serial  0/0 
Serial6/0  current  state:  UP 
Line  protocol  current  state:  DOWN 
从如上信息可以推测______。 
 
A.  两路由器之间的物理连接正常，但PPP  协议协商没有成功 
B.  PPP  的LCP  协商有可能未通过 
C.  PPP  验证可能失败了 
D.  两路由器V.35  接⼜的IP  地址有可能不在同⼀⽹段 
 
Correct  Answer:  ABC 
Explanation 
 
Explanation/Reference: 
即使不在同⼀⽹段，只要两端配了地址，链路层协议就起来了 
 
QUESTION  68 
某公司的MSR  路由器的⼴域⽹主链路为同异步串⼜，通过⼀根V.35  电缆接⼊运营商⽹络；该路由器同时以 
⼀个ISDN  BRI  接⼜做备份链路。那么关于线路带宽，如下哪些说法是正确的？ 
 
A.  备份线路的带宽可能是64Kbps 
B.  备份线路的带宽可能是128Kbps 
C.  备份线路的带宽可能是144Kbps 
D.  主链路的带宽可能是1Mbps 
 
Correct  Answer:  ABD 
Explanation 
 
Explanation/Reference: 
ISDN两种接⼊⽅式：BRI接⼜  →2B+D  B信道64kbps  D信道16kbps  最⼤速率144kbps 
PRI接⼜  →E1  30B+D  最⼤速率2Mbps 
T1  23B+D  最⼤速率1.544Mbps 
B信道⽤来传输数据，D信道⽤来传输控制信令，因此BRI  最⾼提供128kbps带宽（单位时间可传输的数据 
量） 
V．24  ⽀持同、异步：异步最⾼速率115kbps  同步最⾼速率64kbps 
V．35  只⽀持同步：  最⾼速率为2048000bps=  2Mbps 
 
QUESTION  69 
ping  实际上是基于______协议开发的应⽤程序。 
 
A.  ICMP 
B.  IP 
C.  TCP 
D.  UDP 
 
Correct  Answer:  A 
Explanation 
 
Explanation/Reference: 
Ping  功能是基于ICMP  协议来实现的：源端向⽬的端发送ICMP  回显请求（ECHO-REQUEST）报⽂后，根 
据是否收到⽬的端的ICMP  回显应答（ECHO-REPLY）报⽂来判断⽬的端是否可达，对于可达的⽬的端， 
再根据发送报⽂个数、接收到响应报⽂个数来判断链路的质量，根据ping  报⽂的往返时间来判断源端与⽬ 
的端之间的“距离”。 
 
QUESTION  70 
IP  地址203.108.2.110  是______地址。 
 
A.  A  类 
B.  B  类 
C.  C  类 
D.  D  类 
 
Correct  Answer:  C 
Explanation 
 
Explanation/Reference: 
 
 
QUESTION  71 
IP  地址133.18.2.110  是______地址。 
 
A.  A  类 
B.  B  类 
C.  C  类 
D.  D  类 
 
Correct  Answer:  B 
Explanation 
 
Explanation/Reference: 
 
 
QUESTION  72 
源主机ping  ⽬的设备时，如果⽹络⼯作正常，则⽬的设备在接收到该报⽂后，将会向源主机回应 
ICMP______报⽂。 
 
A.  Echo  Request 
B.  Echo  Reply 
C.  TTL-Exceeded 
D.  Port-Unreachable 
 
Correct  Answer:  B 
Explanation 
 
Explanation/Reference: 
Echo  Request 
————————————————————————————> 
Echo  Reply（正常） 
<———————————————————————————— 
TTL-Exceeded/  Port-Unreachable（超时/⽬的地址不可达） 
 
QUESTION  76 
根据来源的不同，路由表中的路由通常可分为以下哪⼏类？ 
 
A.  接⼜路由 
B.  直连路由 
C.  静态路由 
D.  动态路由 
 
Correct  Answer:  BCD 
Explanation 
 
Explanation/Reference: 
 
 
QUESTION  77 
以下关于IP  地址的说法正确的是______。（选择⼀项或多项） 
 
A.  IP  地址可以固化在硬件中，是独⼀⽆⼆的  MAC 
B.  IP  地址分为A、B、C、D、E  五类 
C.  IP  地址通常⽤点分⼗六进制来表⽰，例如：10.110.192.111 
D.  IP  地址是由32  个⼆进制位组成的 
 
Correct  Answer:  BD 
Explanation 
 
Explanation/Reference: 
IP地址点分⼗进制：A  1.0.0.0~126.255.255.255  127⽤作环路测试  127.0.0.1表⽰本机 
B  128.0.0.0~191.255.255.255 
C  192.0.0.0~223.255.255.255 
D  224.0.0.0~239.255.255.255  组播地址 
E  240~  保留⽤于研究 
 

QUESTION  80 
下⾯关于IP  地址的说法正确的是______。（选择⼀项或多项） 
 
A.  IP  地址由两部分组成：⽹络号和主机号。 
B.  A  类IP  地址的⽹络号有8  位，实际的可变位数为7  位。 
C.  D  类IP  地址通常作为组播地址。 
D.  地址转换（NAT）技术通常⽤于解决A  类地址到C  类地址的转换。 
 
Correct  Answer:  ABC 
Explanation 
 
Explanation/Reference: 
C类地址第⼀个8位110起始 
NAT⽤于私⽹地址到公⽹地址转换，和地址类型⽆关 
 
QUESTION  81 
下⾯关于IP  地址的说法错误的是______。（选择⼀项或多项） 
 
A.  IP  地址由两部分组成：⽹络号和主机号。 
B.  A  类IP  地址的⽹络号有8  位，实际的可变位数为7  位。 
C.  C  类IP  地址的第⼀个⼋位段以100  起始。 
D.  地址转换（NAT）技术通常⽤于解决A  类地址到C  类地址的转换。 
 
Correct  Answer:  CD 
Explanation 
 
Explanation/Reference: 
C类地址第⼀个8位110起始 
NAT⽤于私⽹地址到公⽹地址转换，和地址类型⽆关 
 
QUESTION  82 
以下关于IP  地址的说法正确的是______。（选择⼀项或多项） 
 
A.  IP  地址由两部分构成：⽹络号和主机号 
B.  A  类地址的第⼀个字节为0～126（127  留作他⽤） 
C.  IP  地址通常表⽰为点分⼗进制形式，例如：10.110.168.121 
D.  主机号部分⼆进制全为1  的IP  地址称为⽹络地址，⽤来标识⼀个⽹络的所有主机 
 
Correct  Answer:  AC 
Explanation 
 
Explanation/Reference: 
A  类地址的第⼀个字节为1～126 
 
QUESTION  83 
以下关于IP  地址的说法正确的是______。（选择⼀项或多项） 
 
A.  A  类地址的第⼀个字节为0～126（127  留作他⽤） 
B.  主机号部分⼆进制全为0  的IP  地址称为⽹络地址，⽤来标识⼀个⽹络的所有主机。 
C.  IP  地址通常表⽰为点分⼗进制形式，例如：10.110.168.121 
D.  IP  地址由两部分构成：⽹络号和主机号 
 
Correct  Answer:  BCD 
Explanation 
Explanation/Reference: 
 
 
QUESTION  84 
以下哪个选项描述的参数可以唯⼀确定⼀条TCP  连接？ 
 
A.  源端⼜号，源IP  地址 
B.  ⽬的端⼜号，⽬的IP  地址 
C.  源端⼜号，⽬的端⼜号 
D.  源MAC  地址，⽬的MAC  地址 
E.  以上都不对 
 
Correct  Answer:  E 
Explanation 
 
Explanation/Reference: 
源IP地址、源端⼜、⽬的IP地址、⽬的端⼜  组成套接字socket  唯⼀确定⼀条TCP连接 
 
QUESTION  85 
TCP  协议通过______来区分不同的连接。 
 
A.  端⼜号 
B.  端⼜号和IP  地址 
C.  端⼜号和MAC  地址 
D.  IP  地址和MAC  地址 
 
Correct  Answer:  B 
Explanation 
 
Explanation/Reference: 
 
 
QUESTION  86 
UDP  协议和TCP  协议头部的共同字段有______。 
 
A.  源IP  地址 
B.  流量控制 
C.  校验和 
D.  序列号 
E.  ⽬的端⼜ 
F.  源端⼜ 
 
Correct  Answer:  CEF 
Explanation 
 
Explanation/Reference: 
UDP头部：由源端⼜，⽬的端⼜，长度，校验和组成 
TCP头部：源端⼜，⽬的端⼜，校验和，序列号，确认号，窗⼜，数据便宜等等许多，确保了可靠性 
UDP  协议和TCP  协议头部的共同字段：源端⼜、⽬的端⼜、校验和 
 
QUESTION  87 
UDP  协议和TCP  协议头部的共同字段有______。 
 
A.  源端⼜ 
B.  ⽬的端⼜ 
C.  流量控制 
D.  源IP  地址 
E.  校验和 
F.  序列号 
 
Correct  Answer:  ABE 
Explanation 
 
Explanation/Reference: 

QUESTION  92 
下列关于路由器特点的描述，正确的是______。 
 
A.  是⽹络层设备 
B.  根据链路层信息进⾏路由转发 
C.  提供丰富的接⼜类型 
D.  可以⽀持多种路由协议 
 
Correct  Answer:  ACD 
Explanation 
 
Explanation/Reference: 
⼯作在底三层 
根据⽹络层信息进⾏路由转发 
接⼜类型丰富，可⽤来连接不同介质的⽹络 
 
QUESTION  93 
下列关于Comware  特点的描述，正确的是______。 
 
A.  ⽀持IPv4  和IPv6  双协议 
B.  ⽀持多CPU 
C.  路由和交换功能融合 
D.  ⾼可靠性和弹性拓展 
E.  灵活的裁减和定制功能 
Correct  Answer:  ABCDE 
Explanation 
 
Explanation/Reference: 
 
 
QUESTION  94 
通过控制台（Console）端⼜配置刚出⼚未经配置的MSR  路由器，终端的串⼜波特率应设置为_____。 
 
A.  9600 
B.  2400 
C.  115200 
D.  38400 
 
Correct  Answer:  A 
Explanation 
 
Explanation/Reference: 
 
 
QUESTION  95 
下⾯关于H3C  设备中VTY  特点的描述，正确的是______。（选择⼀项或多项） 
 
A.  只⽤于对设备进⾏Telnet 
B.  每台设备可以⽀持多个VTY  ⽤户同时访问 
C.  每个VTY  ⽤户对应⼀个物理接⼜ 
D.  不⽀持⽆密码验证 
 
Correct  Answer:  B 
Explanation 
 
Explanation/Reference: 
Vty即虚拟登陆接⼜，⽀持多⽤户、⽀持认证 
Vty  0-4  5个接⼜，可以有5个⼈同时访问 
逻辑线路0-4  随机分配的，如果关闭1-4，只剩下0，但却未必随机到0，还是⽆法访问 
 
QUESTION  96 
SSH  默认使⽤TCP  端⼜号______。（选择⼀项或多项） 
 
A.  20 
B.  21 
C.  22 
D.  23 
 
Correct  Answer:  C 
Explanation 
 
Explanation/Reference: 
 
 
QUESTION  97 
如果需要在MSR  上配置以太⼜的IP  地址，应该在______下配置。 
 
A.  系统视图 
B.  ⽤户视图 
C.  接⼜视图 
D.  路由协议视图 
Correct  Answer:  C 
Explanation 
 
Explanation/Reference: 
 
 
QUESTION  98 
下⾯关于H3C  ⽹络设备升级的说法，正确的是______。（选择⼀项或多项） 
 
A.  使⽤Xmodem  升级可以达到与FTP  ⼀样的速度 
B.  当使⽤FTP  升级时，设备只能做FTP  客户端 
C.  在设备⽆法引导到命令⾏模式⽽需要对操作系统软件进⾏升级时，只能使⽤Xmodem  ⽅式 
D.  在客户端和服务器之间不便于复杂交互的环境下，可以使⽤TFTP  进⾏升级 
 
 
Correct  Answer:  D 
Explanation 
 
Explanation/Reference: 
设备可做客户端或服务器 
TFTP  69  简单⽂件传输协议 
⽆法进⼊设备时，可以通过bootrom菜单通过ftp/tftp/Xmodem升级： 
在设备⽆法引导到命令⾏模式⽽需要对操作系统软件进⾏升级时，在BOOTROM模式中利⽤BOOTROM菜 
单提供的操作功能，采⽤ftp/tftp使设备正常启动并引导到命令⾏模式。 
如果⽆法实现FTP、TFTP服务器与设备的⽹络连接，则只有在BOOTROM模式中通过console⼜采⽤ 
Xmodem完成升级，使设备正常引导到命令⾏模式 
 
QUESTION  99 
下⾯关于H3C  ⽹络设备升级的说法，正确的是______。（选择⼀项或多项） 
 
A.  使⽤Xmodem  升级可以达到与FTP  ⼀样的速度 
B.  当使⽤FTP  升级时，设备可以作为FTP  服务器端或客户端 
C.  在设备⽆法引导到命令⾏模式⽽需要对操作系统软件进⾏升级时，可以使⽤Xmodem  和TFTP  ⽅式 
D.  在客户端和服务器之间不便于复杂交互的环境下，可以使⽤TFTP  进⾏升级 
 
Correct  Answer:  BCD 
Explanation 
 
Explanation/Reference: 
Xmodem升级速度蜗⽜ 
 
QUESTION  100 
下列选项中对路由器系统的启动过程描述正确的是______。 
 
A.  内存检测------启动bootrom------应⽤程序解压-------应⽤程序加载 
B.  启动bootrom------内存检测------应⽤程序加载 
C.  应⽤程序解压------应⽤程序加载------启动bootrom------内存检测 
D.  内存检测------应⽤程序解压------应⽤程序加载 
 
 
Correct  Answer:  A 
Explanation 
 
Explanation/Reference: 
路由器系统的启动：内存检测＞启动bootrom＞应⽤程序解压＞应⽤程序加载 

QUESTION 101

"""
