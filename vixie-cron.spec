#
# Conditional build:
%bcond_without	selinux		# without SELinux support
#
Summary:	The Vixie cron daemon for executing specified programs at set times
Summary(cs):	Démon pro periodické spou¹tìní zadaných programù v nastaveném èase
Summary(da):	Vixie cron-dæmon for kørsel af specificerede programmer ved bestemte tider
Summary(de):	Der Vixie-cron-Dämon zum Ausführen von Programmen zu bestimmten Zeiten
Summary(es):	Demonio Vixie cron para ejecutar programas a horas específicas
Summary(fr):	Démon vixie cron pour l'exécution de programmes spécifiés à des moments déterminés
Summary(id):	Vixie cron daemon untuk menjalankan program pada waktu yang ditentukan
Summary(is):	Vixie cron púkinn keyrir skilgreind forrit á ákveðnum tímum
Summary(it):	Vixie: demone di cron per eseguire programmi a orari prestabiliti
Summary(ja):	ÀßÄê¤µ¤ì¤¿»þ´Ö¤ËÆÃÄê¤Î¥×¥í¥°¥é¥à¤ò¼Â¹Ô¤¹¤ë Vixie cron ¥Ç¡¼¥â¥ó
Summary(nb):	Vixie cron-daemon for kjøring av spesifiserte programmer ved bestemte tider
Summary(pl):	Demon Vixie cron uruchamiaj±cy zadane programy w okre¶lonym czasie
Summary(pt):	O 'daemon' cron Vixie para executar programas indicados em alturas definidas
Summary(ru):	Vixie cron - ÄÅÍÏÎ, ÚÁÐÕÓËÁÀÝÉÊ ÐÒÏÃÅÓÓÙ ÐÏ ÒÁÓÐÉÓÁÎÉÀ
Summary(sk):	Vixie cron démon na spú¹»anie daných programov v urèený èas
Summary(sl):	Stre¾nik Vixie cron za izvajanje programov ob doloèenih èasih
Summary(sv):	Vixie-cron-demonen för att köra angivna program vid bestämda tider
Summary(tr):	Vixie cron süreci, periyodik program çalýþtýrma yeteneði
Summary(uk):	Vixie cron - ÄÅÍÏÎ, ÝÏ ÚÁÐÕÓËÁ¤ ÐÒÏÃÅÓÉ ÚÁ ÒÏÚËÌÁÄÏÍ
Summary(zh_CN):	ÓÃÓÚÔÚÔ¤ÉèÊ±¼äÖ´ÐÐÖ¸¶¨³ÌÐòµÄ Vixie cron ºóÌ¨³ÌÐò¡£
Name:		vixie-cron
Version:	4.1
Release:	3
License:	distributable
Group:		Daemons
Source0:	ftp://ftp.isc.org/isc/cron/cron_%{version}.shar
# Source0-md5:	5e1be9dbde66295821ac7899f2e1f561
Source1:	%{name}.init
Source2:	cron.logrotate
Source3:	cron.sysconfig
Source4:	%{name}.crontab
Source5:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source5-md5:	8516dbf0641eb3035d43f18b7ca95c73
Source6:	%{name}.pam
Patch0:		%{name}-pld.patch
Patch1:		%{name}-sprintf.patch
Patch2:		%{name}-sigchld2.patch
Patch3:		%{name}-crond.patch
Patch4:		%{name}-manpages.patch
Patch5:		%{name}-name.patch
Patch6:		%{name}-security3.patch
Patch7:		%{name}-noroot.patch
Patch8:		%{name}-pam.patch
Patch9:		%{name}-sgid-crontab.patch
Patch10:	%{name}-selinux.patch
Patch11:	%{name}-foreground.patch
Patch12:	%{name}-fd0open.patch
Patch13:	%{name}-CAN-2005-1038.patch
Patch14:	%{name}-nodebug.patch
%{?with_selinux:BuildRequires:	libselinux-devel}
BuildRequires:	pam-devel
BuildRequires:	rpmbuild(macros) >= 1.202
PreReq:		rc-scripts
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(post,preun):	/sbin/chkconfig
Requires(post):	fileutils
Requires(postun):	/usr/sbin/groupdel
Requires:	/bin/run-parts
Requires:	psmisc >= 20.1
Provides:	crontabs >= 1.7
Provides:	crondaemon
Provides:	group(crontab)
Obsoletes:	crontabs
Obsoletes:	fcron
Obsoletes:	hc-cron
Obsoletes:	mcron
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The vixie-cron package contains the Vixie version of cron. Cron is a
standard UNIX program that runs user-specified programs at periodic
scheduled times. Vixie cron adds a number of features to the basic
UNIX cron, including better security and more powerful configuration
options.

%description -l cs
Balíèek vixie-cron obsahuje Vixie verzi standardního démona cron. Cron
je standardní unixový program, který spou¹tí u¾ivatelem urèené
programy v periodicky plánovaných intervalech. Vixie cron pøiná¹í
celou øadu funkcí do základního unixového cron vèetnì lep¹ího
zabezpeèení a mocnìj¹ích konfiguraèních voleb.

%description -l de
cron ist ein Standard-UNIX-Programm, das zu vorgegebenen Zeiten vom
Benutzer angegebene Programme ausführt. vixie cron weist mehr
Funktionen auf als cron aus UNIX, u.a. bessere Sicherheit und
leistungsfähigere Konfigurationsoptionen.

%description -l es
El paquete vixie-cron contiene la versión Vixie del cron. Cron es un
demonio UNIX estandard para ejecutar programas a horas específicas.
Vixie cron tiene mayor seguridad y más opciones de configuración que
la version estandar.

%description -l fr
cron est un des programmes UNIX standard qui permet à un utilisateur
donné de lancer des périodiquement des programmes selon un ordre
planifié. vixie cron ajoute de nombreuses fonctionnalités au cron UNIX
de base, dont une plus grande sécurité et des options de configuration
plus puissantes.

%description -l id
Package vixie-cron berisi cron versi Vixie. Cron adalah daemon standar
UNIX yang menjalankan program pada waktu yang ditentukan. Vixie cron
menambahkan keamanan yang lebih baik dan konfigurasi yang lebih baik
dari cron versi standar.

%description -l is
Vixie-cron pakkinn hefur að geyma Vixie útgáfuna af cron. Cron er
staðlaður UNIX púki sem keyrir tilgreind forrit á fyrirfram tilteknum
tíma. Vixie cron bætir auknu öryggi og öflugri stillingarmöguleikum
við stöðluðu útgáfu cron.

%description -l it
Il pacchetto vixie-cron contiene la versione Vixie del programma cron.
Cron è un demone UNIX standard per eseguire programmi specifici a
orari prestabiliti. Vixie-cron aggiunge maggiore sicurezza e opzioni
di configurazione più potenti rispetto alla versione standard di cron.

%description -l ja
vixie-cron ¥Ñ¥Ã¥±¡¼¥¸¤Ë¤Ï Vixie ¥Ð¡¼¥¸¥ç¥ó¤Î cron ¤¬Æþ¤Ã¤Æ¤¤¤Þ¤¹¡£cron
¤Ï¡¢¥¹¥±¥¸¥å¡¼¥ë¤µ¤ì¤¿ »þ´Ö¤ËÆÃÄê¤Î¥×¥í¥°¥é¥à¤ò¼Â¹Ô¤¹¤ëÉ¸½à UNIX
¥Ç¡¼¥â¥ó¤Ç¤¹¡£ vixie-cron ¤Ç¤Ï¡¢É¸½à¥Ð¡¼¥¸¥ç¥ó¤Î cron
¤Î¥»¥­¥å¥ê¥Æ¥£µ¡Ç½¤¬²þÁ±¤µ¤ì¡¢¤Þ¤¿¡¢
¤è¤ê¶¯ÎÏ¤ÊÀßÄê¥ª¥×¥·¥ç¥ó¤¬ÄÉ²Ã¤µ¤ì¤Æ¤¤¤Þ¤¹¡£

%description -l pl
cron to standardowy uniksowy program, który okresowo uruchamia
okre¶lone przez u¿ytkowników programy. vixie cron dodaje mo¿liwo¶ci
podstawowemu uniksowemu cronowi, w tym lepsze bezpieczeñstwo i
bogatsze opcje konfiguracyjne.

%description -l pt
O pacote vixie-cron contém a versão Vixie do cron. O cron é um
'daemon' 'standard' do UNIX que corre programas especificados em horas
escalonadas. O cron Vixie acrescenta melhor segurança e opções de
configuração mais poderosas à versão 'standard' do cron.

%description -l ru
cron - ÜÔÏ ÓÔÁÎÄÁÒÔÎÁÑ ÄÌÑ UNIX ÐÒÏÇÒÁÍÍÁ, ÚÁÐÕÓËÁÀÝÁÑ ÚÁÄÁÎÎÙÅ
ÐÏÌØÚÏ×ÁÔÅÌÅÍ ÐÒÏÇÒÁÍÍÙ ÐÏ ÒÁÓÐÉÓÁÎÉÀ. Vixie cron ÄÏÂÁ×ÌÑÅÔ Ë
ÓÔÁÎÄÁÒÔÎÏÍÕ UNIX cron'Õ ÎÏ×ÙÅ ÏÐÃÉÉ, ×ËÌÀÞÁÑ ÕÓÉÌÅÎÎÕÀ ÂÅÚÏÐÁÓÎÏÓÔØ É
ÂÏÌÅÅ ÍÏÝÎÙÅ ÏÐÃÉÉ ËÏÎÆÉÇÕÒÁÃÉÉ.

%description -l sk
Balík vixie-cron je obsahuje Vixie verziu cronu. Cron je ¹tandardný
démon v UNIXe, ktorý spú¹»a zadaný program v daný èas. Vixie cron
pridáva vy¹¹iu bezpeènos» a lep¹ie mo¾nosti konfigurovania oproti
¹tandardnej verzii cronu.

%description -l sv
Paketet vixie-cron innehåller Vixie-versionen av cron. Cron är en
standarddemon under UNIX som kör angivna program vid bestämta tider.
Vixie cron lägger till utökad säkerhet och kraftfullare
konfigurationsval till standardversionen av cron.

%description -l tr
cron UNIX'de standart olarak belirli zamanlarda bir programý
çalýþtýrmak için kullanýlan daemon'dur. Vixie cron, standart cron'dan
daha güvenlidir ve daha geliþmiþ yapýlandýrma seçenekleri içerir.

%description -l uk
cron - ÃÅ ÓÔÁÎÄÁÒÔÎÁ ÄÌÑ UNIX ÐÒÏÇÒÁÍÁ, ÝÏ ÚÁÐÕÓËÁ¤ ÚÁÄÁÎ¦
ËÏÒÉÓÔÕ×ÁÞÅÍ ÐÒÏÇÒÁÍÉ ÚÁ ÒÏÚËÌÁÄÏÍ. Vixie cron ÄÏÄÁ¤ ÄÏ ÓÔÁÎÄÁÒÔÎÏÇÏ
UNIX cron'Õ ÎÏ×¦ ÏÐÃ¦§, ×ËÌÀÞÁÀÞÉ Â¦ÌØÛÕ ÚÁÈÉÝÅÎ¦ÓÔØ ÔÁ Â¦ÌØÛ ÐÏÔÕÖÎ¦
ÏÐÃ¦§ ËÏÎÆ¦ÇÕÒÁÃ¦§.

%description -l zh_CN
vixie-cron Èí¼þ°ü°üº¬ cron µÄ Vixie °æ±¾¡£Cron ÊÇ±ê×¼µÄ UNIX
ºóÌ¨³ÌÐò£¬ ÓÃÓÚÔÚÔ¤¶¨µÄÊ±¼äÔËÐÐÖ¸¶¨µÄ³ÌÐò¡£ Óë cron
±ê×¼°æ±¾Ïà±È£¬Vixie cron ¾ßÓÐ¸ü¸ßµÄ°²È«ÐÔºÍ¹¦ÄÜ¸üÇ¿µÄÅäÖÃÑ¡Ïî¡£

%prep
%setup -T -c -q -a5
/bin/sh %{SOURCE0}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%{?with_selinux:%patch10 -p1}
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1

%build
%{__make} \
	CC="%{__cc}" \
	RPM_OPT_FLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/var/{log,spool/cron},%{_mandir}} \
	$RPM_BUILD_ROOT/etc/{rc.d/init.d,logrotate.d,sysconfig} \
	$RPM_BUILD_ROOT%{_sysconfdir}/{cron,cron.{d,hourly,daily,weekly,monthly},pam.d}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	DESTMAN=$RPM_BUILD_ROOT%{_mandir}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/crond
install %{SOURCE2} $RPM_BUILD_ROOT/etc/logrotate.d/cron
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/cron
install %{SOURCE4} $RPM_BUILD_ROOT/etc/cron.d/crontab
install %{SOURCE6} $RPM_BUILD_ROOT/etc/pam.d/cron

for a in fi fr id ja ko pl ; do
	if test -f $a/man1/crontab.1 ; then
		install -d $RPM_BUILD_ROOT%{_mandir}/$a/man1
		install $a/man1/crontab.1 $RPM_BUILD_ROOT%{_mandir}/$a/man1
	fi
	if test -f $a/man5/crontab.5 ; then
		install -d $RPM_BUILD_ROOT%{_mandir}/$a/man5
		install $a/man5/crontab.5 $RPM_BUILD_ROOT%{_mandir}/$a/man5
	fi
	if test -f $a/man8/cron.8 ; then
		install -d $RPM_BUILD_ROOT%{_mandir}/$a/man8
		install $a/man8/cron.8 $RPM_BUILD_ROOT%{_mandir}/$a/man8
		echo .so cron.8 > $RPM_BUILD_ROOT%{_mandir}/$a/man8/crond.8
	fi
done

touch $RPM_BUILD_ROOT/var/log/cron

cat > $RPM_BUILD_ROOT%{_sysconfdir}/cron/cron.allow << EOF
# cron.allow	This file describes the names of the users which are
#		allowed to use the local cron daemon
root
EOF

cat > $RPM_BUILD_ROOT%{_sysconfdir}/cron/cron.deny << EOF2
# cron.deny	This file describes the names of the users which are
#		NOT allowed to use the local cron daemon
EOF2

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 117 -r -f crontab

%post
/sbin/chkconfig --add crond
if [ -f /var/lock/subsys/crond ]; then
	/etc/rc.d/init.d/crond restart >&2
else
	echo "Run \"/etc/rc.d/init.d/crond start\" to start cron daemon."
fi
umask 027
touch /var/log/cron
chgrp crontab /var/log/cron
chmod 660 /var/log/cron

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/crond ]; then
		/etc/rc.d/init.d/crond stop >&2
	fi
	/sbin/chkconfig --del crond
fi

%postun
if [ "$1" = "0" ]; then
	%groupremove crontab
fi

%triggerpostun -- vixie-cron <= 3.0.1-85
for i in `/bin/ls /var/spool/cron 2>/dev/null`
do
	chown ${i} /var/spool/cron/${i} 2>/dev/null || :
done
/bin/chmod 660 /var/log/cron
/bin/chgrp crontab /var/log/cron
/bin/chmod 640 /etc/cron/cron.*
/bin/chgrp crontab /etc/cron/cron.*

%triggerpostun -- vixie-cron <= 3.0.1-73
if [ -f /etc/cron.d/cron.allow.rpmsave ]; then
	mv -f /etc/cron.d/cron.allow.rpmsave /etc/cron/cron.allow
fi
if [ -f /etc/cron.d/cron.allow ]; then
	mv -f /etc/cron.d/cron.allow /etc/cron/cron.allow
fi
if [ -f /etc/cron.d/cron.deny.rpmsave ]; then
	mv -f /etc/cron.d/cron.deny.rpmsave /etc/cron/cron.deny
fi
if [ -f /etc/cron.d/cron.deny ]; then
	mv -f /etc/cron.d/cron.deny /etc/cron/cron.deny
fi

%triggerpostun -- vixie-cron <= 3.0.1-70
if [ -f /etc/cron.allow ]; then
	mv -f /etc/cron.allow /etc/cron/cron.allow
fi
if [ -f /etc/cron.deny ]; then
	mv -f /etc/cron.deny /etc/cron/cron.deny
fi

%triggerpostun -- hc-cron
/sbin/chkconfig --del crond
/sbin/chkconfig --add crond

%triggerpostun -- hc-cron <= 0.14-12
for i in `/bin/ls /var/spool/cron 2>/dev/null`
do
	chown ${i} /var/spool/cron/${i} 2>/dev/null || :
done
/bin/chmod 660 /var/log/cron
/bin/chgrp crontab /var/log/cron
/bin/chmod 640 /etc/cron/cron.*
/bin/chgrp crontab /etc/cron/cron.*

%files
%defattr(644,root,root,755)
%doc CHANGES CONVERSION FEATURES MAIL README THANKS
%attr(750,root,crontab) %dir %{_sysconfdir}/cron*
%attr(640,root,crontab) %config(noreplace,missingok) /etc/cron.d/crontab
%attr(640,root,crontab) %config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/cron/cron.allow
%attr(640,root,crontab) %config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/cron/cron.deny
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/cron
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/cron
%attr(754,root,root) /etc/rc.d/init.d/crond
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/cron
%attr(755,root,root) %{_sbindir}/crond
%attr(2755,root,crontab) %{_bindir}/crontab

%{_mandir}/man*/*
%lang(fi) %{_mandir}/fi/man*/*
%lang(fr) %{_mandir}/fr/man*/*
%lang(id) %{_mandir}/id/man*/*
%lang(ja) %{_mandir}/ja/man*/*
%lang(ko) %{_mandir}/ko/man*/*
%lang(pl) %{_mandir}/pl/man*/*

%attr(1730,root,crontab) /var/spool/cron
%attr(660,root,crontab) %ghost /var/log/cron
