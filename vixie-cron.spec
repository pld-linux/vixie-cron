#
# Conditional build:
%bcond_without	selinux		# without SELinux support
#
Summary:	The Vixie cron daemon for executing specified programs at set times
Summary(cs.UTF-8):	Démon pro periodické spouštění zadaných programů v nastaveném čase
Summary(da.UTF-8):	Vixie cron-dæmon for kørsel af specificerede programmer ved bestemte tider
Summary(de.UTF-8):	Der Vixie-cron-Dämon zum Ausführen von Programmen zu bestimmten Zeiten
Summary(es.UTF-8):	Demonio Vixie cron para ejecutar programas a horas específicas
Summary(fr.UTF-8):	Démon vixie cron pour l'exécution de programmes spécifiés à des moments déterminés
Summary(id.UTF-8):	Vixie cron daemon untuk menjalankan program pada waktu yang ditentukan
Summary(is.UTF-8):	Vixie cron púkinn keyrir skilgreind forrit á ákveðnum tímum
Summary(it.UTF-8):	Vixie: demone di cron per eseguire programmi a orari prestabiliti
Summary(ja.UTF-8):	設定された時間に特定のプログラムを実行する Vixie cron デーモン
Summary(nb.UTF-8):	Vixie cron-daemon for kjøring av spesifiserte programmer ved bestemte tider
Summary(pl.UTF-8):	Demon Vixie cron uruchamiający zadane programy w określonym czasie
Summary(pt.UTF-8):	O 'daemon' cron Vixie para executar programas indicados em alturas definidas
Summary(ru.UTF-8):	Vixie cron - демон, запускающий процессы по расписанию
Summary(sk.UTF-8):	Vixie cron démon na spúšťanie daných programov v určený čas
Summary(sl.UTF-8):	Strežnik Vixie cron za izvajanje programov ob določenih časih
Summary(sv.UTF-8):	Vixie-cron-demonen för att köra angivna program vid bestämda tider
Summary(tr.UTF-8):	Vixie cron süreci, periyodik program çalıştırma yeteneği
Summary(uk.UTF-8):	Vixie cron - демон, що запускає процеси за розкладом
Summary(zh_CN.UTF-8):	用于在预设时间执行指定程序的 Vixie cron 后台程序。
Name:		vixie-cron
Version:	4.1
Release:	15
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
Patch3:		%{name}-crontab.patch
Patch4:		%{name}-crond.patch
Patch5:		%{name}-manpages.patch
Patch6:		%{name}-security3.patch
Patch7:		%{name}-noroot.patch
Patch8:		%{name}-pam.patch
Patch9:		%{name}-selinux.patch
Patch10:	%{name}-foreground.patch
Patch11:	%{name}-fd0open.patch
Patch12:	%{name}-CAN-2005-1038.patch
Patch13:	%{name}-nodebug.patch
Patch14:	%{name}-syslog-facility.patch
Patch15:	%{name}-saved-uids.patch
Patch16:	%{name}-setuid_check.patch
Patch17:	%{name}-content_type.patch
%{?with_selinux:BuildRequires:	libselinux-devel}
BuildRequires:	pam-devel
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post):	fileutils
Requires(post,preun):	/sbin/chkconfig
Requires(post,preun):	rc-scripts
Requires(postun):	/usr/sbin/groupdel
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires:	/bin/run-parts
Requires:	/sbin/chkconfig
Requires:	psmisc >= 20.1
Requires:	rc-scripts
Provides:	crondaemon
Provides:	crontabs >= 1.7
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

%description -l cs.UTF-8
Balíček vixie-cron obsahuje Vixie verzi standardního démona cron. Cron
je standardní unixový program, který spouští uživatelem určené
programy v periodicky plánovaných intervalech. Vixie cron přináší
celou řadu funkcí do základního unixového cron včetně lepšího
zabezpečení a mocnějších konfiguračních voleb.

%description -l de.UTF-8
cron ist ein Standard-UNIX-Programm, das zu vorgegebenen Zeiten vom
Benutzer angegebene Programme ausführt. vixie cron weist mehr
Funktionen auf als cron aus UNIX, u.a. bessere Sicherheit und
leistungsfähigere Konfigurationsoptionen.

%description -l es.UTF-8
El paquete vixie-cron contiene la versión Vixie del cron. Cron es un
demonio UNIX estandard para ejecutar programas a horas específicas.
Vixie cron tiene mayor seguridad y más opciones de configuración que
la version estandar.

%description -l fr.UTF-8
cron est un des programmes UNIX standard qui permet à un utilisateur
donné de lancer des périodiquement des programmes selon un ordre
planifié. vixie cron ajoute de nombreuses fonctionnalités au cron UNIX
de base, dont une plus grande sécurité et des options de configuration
plus puissantes.

%description -l id.UTF-8
Package vixie-cron berisi cron versi Vixie. Cron adalah daemon standar
UNIX yang menjalankan program pada waktu yang ditentukan. Vixie cron
menambahkan keamanan yang lebih baik dan konfigurasi yang lebih baik
dari cron versi standar.

%description -l is.UTF-8
Vixie-cron pakkinn hefur að geyma Vixie útgáfuna af cron. Cron er
staðlaður UNIX púki sem keyrir tilgreind forrit á fyrirfram tilteknum
tíma. Vixie cron bætir auknu öryggi og öflugri stillingarmöguleikum
við stöðluðu útgáfu cron.

%description -l it.UTF-8
Il pacchetto vixie-cron contiene la versione Vixie del programma cron.
Cron è un demone UNIX standard per eseguire programmi specifici a
orari prestabiliti. Vixie-cron aggiunge maggiore sicurezza e opzioni
di configurazione più potenti rispetto alla versione standard di cron.

%description -l ja.UTF-8
vixie-cron パッケージには Vixie バージョンの cron が入っています。cron
は、スケジュールされた 時間に特定のプログラムを実行する標準 UNIX
デーモンです。 vixie-cron では、標準バージョンの cron
のセキュリティ機能が改善され、また、
より強力な設定オプションが追加されています。

%description -l pl.UTF-8
cron to standardowy uniksowy program, który okresowo uruchamia
określone przez użytkowników programy. vixie cron dodaje możliwości
podstawowemu uniksowemu cronowi, w tym lepsze bezpieczeństwo i
bogatsze opcje konfiguracyjne.

%description -l pt.UTF-8
O pacote vixie-cron contém a versão Vixie do cron. O cron é um
'daemon' 'standard' do UNIX que corre programas especificados em horas
escalonadas. O cron Vixie acrescenta melhor segurança e opções de
configuração mais poderosas à versão 'standard' do cron.

%description -l ru.UTF-8
cron - это стандартная для UNIX программа, запускающая заданные
пользователем программы по расписанию. Vixie cron добавляет к
стандартному UNIX cron'у новые опции, включая усиленную безопасность и
более мощные опции конфигурации.

%description -l sk.UTF-8
Balík vixie-cron je obsahuje Vixie verziu cronu. Cron je štandardný
démon v UNIXe, ktorý spúšťa zadaný program v daný čas. Vixie cron
pridáva vyššiu bezpečnosť a lepšie možnosti konfigurovania oproti
štandardnej verzii cronu.

%description -l sv.UTF-8
Paketet vixie-cron innehåller Vixie-versionen av cron. Cron är en
standarddemon under UNIX som kör angivna program vid bestämta tider.
Vixie cron lägger till utökad säkerhet och kraftfullare
konfigurationsval till standardversionen av cron.

%description -l tr.UTF-8
cron UNIX'de standart olarak belirli zamanlarda bir programı
çalıştırmak için kullanılan daemon'dur. Vixie cron, standart cron'dan
daha güvenlidir ve daha gelişmiş yapılandırma seçenekleri içerir.

%description -l uk.UTF-8
cron - це стандартна для UNIX програма, що запускає задані
користувачем програми за розкладом. Vixie cron додає до стандартного
UNIX cron'у нові опції, включаючи більшу захищеність та більш потужні
опції конфігурації.

%description -l zh_CN.UTF-8
vixie-cron 软件包包含 cron 的 Vixie 版本。Cron 是标准的 UNIX
后台程序， 用于在预定的时间运行指定的程序。 与 cron
标准版本相比，Vixie cron 具有更高的安全性和功能更强的配置选项。

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
%{?with_selinux:%patch9 -p1}
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p0
%patch15 -p1
%patch16 -p1
%patch17 -p1

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
umask 027
touch /var/log/cron
chgrp crontab /var/log/cron
chmod 660 /var/log/cron
%service crond restart "cron daemon"

%preun
if [ "$1" = "0" ]; then
	%service crond stop
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
