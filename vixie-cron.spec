#
# Conditional build:
%bcond_without	selinux		# without SELinux support
#
Summary:	The Vixie cron daemon for executing specified programs at set times
Summary(cs):	D�mon pro periodick� spou�t�n� zadan�ch program� v nastaven�m �ase
Summary(da):	Vixie cron-d�mon for k�rsel af specificerede programmer ved bestemte tider
Summary(de):	Der Vixie-cron-D�mon zum Ausf�hren von Programmen zu bestimmten Zeiten
Summary(es):	Demonio Vixie cron para ejecutar programas a horas espec�ficas
Summary(fr):	D�mon vixie cron pour l'ex�cution de programmes sp�cifi�s � des moments d�termin�s
Summary(id):	Vixie cron daemon untuk menjalankan program pada waktu yang ditentukan
Summary(is):	Vixie cron p�kinn keyrir skilgreind forrit � �kve�num t�mum
Summary(it):	Vixie: demone di cron per eseguire programmi a orari prestabiliti
Summary(ja):	���ꤵ�줿���֤�����Υץ�����¹Ԥ��� Vixie cron �ǡ����
Summary(nb):	Vixie cron-daemon for kj�ring av spesifiserte programmer ved bestemte tider
Summary(pl):	Demon Vixie cron uruchamiaj�cy zadane programy w okre�lonym czasie
Summary(pt):	O 'daemon' cron Vixie para executar programas indicados em alturas definidas
Summary(ru):	Vixie cron - �����, ����������� �������� �� ����������
Summary(sk):	Vixie cron d�mon na sp���anie dan�ch programov v ur�en� �as
Summary(sl):	Stre�nik Vixie cron za izvajanje programov ob dolo�enih �asih
Summary(sv):	Vixie-cron-demonen f�r att k�ra angivna program vid best�mda tider
Summary(tr):	Vixie cron s�reci, periyodik program �al��t�rma yetene�i
Summary(uk):	Vixie cron - �����, �� �������� ������� �� ���������
Summary(zh_CN):	������Ԥ��ʱ��ִ��ָ������� Vixie cron ��̨����
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
Bal��ek vixie-cron obsahuje Vixie verzi standardn�ho d�mona cron. Cron
je standardn� unixov� program, kter� spou�t� u�ivatelem ur�en�
programy v periodicky pl�novan�ch intervalech. Vixie cron p�in��
celou �adu funkc� do z�kladn�ho unixov�ho cron v�etn� lep��ho
zabezpe�en� a mocn�j��ch konfigura�n�ch voleb.

%description -l de
cron ist ein Standard-UNIX-Programm, das zu vorgegebenen Zeiten vom
Benutzer angegebene Programme ausf�hrt. vixie cron weist mehr
Funktionen auf als cron aus UNIX, u.a. bessere Sicherheit und
leistungsf�higere Konfigurationsoptionen.

%description -l es
El paquete vixie-cron contiene la versi�n Vixie del cron. Cron es un
demonio UNIX estandard para ejecutar programas a horas espec�ficas.
Vixie cron tiene mayor seguridad y m�s opciones de configuraci�n que
la version estandar.

%description -l fr
cron est un des programmes UNIX standard qui permet � un utilisateur
donn� de lancer des p�riodiquement des programmes selon un ordre
planifi�. vixie cron ajoute de nombreuses fonctionnalit�s au cron UNIX
de base, dont une plus grande s�curit� et des options de configuration
plus puissantes.

%description -l id
Package vixie-cron berisi cron versi Vixie. Cron adalah daemon standar
UNIX yang menjalankan program pada waktu yang ditentukan. Vixie cron
menambahkan keamanan yang lebih baik dan konfigurasi yang lebih baik
dari cron versi standar.

%description -l is
Vixie-cron pakkinn hefur a� geyma Vixie �tg�funa af cron. Cron er
sta�la�ur UNIX p�ki sem keyrir tilgreind forrit � fyrirfram tilteknum
t�ma. Vixie cron b�tir auknu �ryggi og �flugri stillingarm�guleikum
vi� st��lu�u �tg�fu cron.

%description -l it
Il pacchetto vixie-cron contiene la versione Vixie del programma cron.
Cron � un demone UNIX standard per eseguire programmi specifici a
orari prestabiliti. Vixie-cron aggiunge maggiore sicurezza e opzioni
di configurazione pi� potenti rispetto alla versione standard di cron.

%description -l ja
vixie-cron �ѥå������ˤ� Vixie �С������� cron �����äƤ��ޤ���cron
�ϡ��������塼�뤵�줿 ���֤�����Υץ�����¹Ԥ���ɸ�� UNIX
�ǡ����Ǥ��� vixie-cron �Ǥϡ�ɸ��С������� cron
�Υ������ƥ���ǽ���������졢�ޤ���
��궯�Ϥ����ꥪ�ץ�����ɲä���Ƥ��ޤ���

%description -l pl
cron to standardowy uniksowy program, kt�ry okresowo uruchamia
okre�lone przez u�ytkownik�w programy. vixie cron dodaje mo�liwo�ci
podstawowemu uniksowemu cronowi, w tym lepsze bezpiecze�stwo i
bogatsze opcje konfiguracyjne.

%description -l pt
O pacote vixie-cron cont�m a vers�o Vixie do cron. O cron � um
'daemon' 'standard' do UNIX que corre programas especificados em horas
escalonadas. O cron Vixie acrescenta melhor seguran�a e op��es de
configura��o mais poderosas � vers�o 'standard' do cron.

%description -l ru
cron - ��� ����������� ��� UNIX ���������, ����������� ��������
������������� ��������� �� ����������. Vixie cron ��������� �
������������ UNIX cron'� ����� �����, ������� ��������� ������������ �
����� ������ ����� ������������.

%description -l sk
Bal�k vixie-cron je obsahuje Vixie verziu cronu. Cron je �tandardn�
d�mon v UNIXe, ktor� sp���a zadan� program v dan� �as. Vixie cron
prid�va vy��iu bezpe�nos� a lep�ie mo�nosti konfigurovania oproti
�tandardnej verzii cronu.

%description -l sv
Paketet vixie-cron inneh�ller Vixie-versionen av cron. Cron �r en
standarddemon under UNIX som k�r angivna program vid best�mta tider.
Vixie cron l�gger till ut�kad s�kerhet och kraftfullare
konfigurationsval till standardversionen av cron.

%description -l tr
cron UNIX'de standart olarak belirli zamanlarda bir program�
�al��t�rmak i�in kullan�lan daemon'dur. Vixie cron, standart cron'dan
daha g�venlidir ve daha geli�mi� yap�land�rma se�enekleri i�erir.

%description -l uk
cron - �� ���������� ��� UNIX ��������, �� �������� ����Φ
������������ �������� �� ���������. Vixie cron ����� �� ������������
UNIX cron'� ��צ ��æ�, ��������� ¦���� ������Φ��� �� ¦��� �����Φ
��æ� ���Ʀ����æ�.

%description -l zh_CN
vixie-cron ��������� cron �� Vixie �汾��Cron �Ǳ�׼�� UNIX
��̨���� ������Ԥ����ʱ������ָ���ĳ��� �� cron
��׼�汾��ȣ�Vixie cron ���и��ߵİ�ȫ�Ժ͹��ܸ�ǿ������ѡ�

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
