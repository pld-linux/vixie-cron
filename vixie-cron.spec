Summary:	Vixie cron daemon
Summary(de):	Vixie cron daemon 
Summary(fr):	Démon Vixie cron
Summary(pl):	Demon Vixie cron
Summary(tr):	Vixie cron süreci, periyodik program çalýþtýrma yeteneði
Name:		vixie-cron
Version:	3.0.1
Release:	63
License:	Distributable
Group:		Daemons
Group(de):	Server
Group(pl):	Serwery
Source0:	ftp://ftp.vix.com/pub/vixie/%{name}-%{version}.tar.gz
Source1:	%{name}.init
Source2:	cron.logrotate
Source3:	cron.sysconfig
Source4:	%{name}.crontab
Source5:	crontab.1.pl
Source6:	cron.8.pl
Patch0:		%{name}-redhat.patch
Patch1:		%{name}-security.patch
Patch3:		%{name}-badsig.patch
Patch4:		%{name}-crontab.patch
Patch5:		%{name}-sigchld.patch
Patch6:		%{name}-sprintf.patch
Patch7:		%{name}-sigchld2.patch
Patch8:		%{name}-crond.patch
Patch9:		%{name}-dst.patch
Patch10:	%{name}-0days.patch
Patch11:	%{name}-security2.patch
Patch12:	%{name}-DESTDIR.patch
Patch13:	%{name}-linux.patch
Patch14:	%{name}-crontabloc.patch
Patch15:	%{name}-nodot.patch
Patch16:	%{name}-time.h.patch
Patch17:	%{name}-newtime.patch
Patch18:	%{name}-name.patch
Patch19:	%{name}-security3.patch
Provides:	crontabs >= 1.7
Obsoletes:	crontabs
Provides:	crondaemon
Requires:	/bin/run-parts
Prereq:		rc-scripts
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	crondaemon
Obsoletes:	hc-cron

%description
The vixie-cron package contains the Vixie version of cron. Cron is a
standard UNIX program that runs user-specified programs at periodic
scheduled times. Vixie cron adds a number of features to the basic
UNIX cron, including better security and more powerful configuration
options.

%description -l de
cron ist ein Standard-UNIX-Programm, das zu vorgegebenen Zeiten vom
Benutzer angegebene Programme ausführt. vixie cron weist mehr
Funktionen auf als cron aus UNIX, u.a. bessere Sicherheit und
leistungsfähigere Konfigurationsoptionen.

%description -l fr
cron est un des programmes UNIX standard qui permet à un utilisateur
donné de lancer des périodiquement des programmes selon un ordre
planifié. vixie cron ajoute de nombreuses fonctionnalités au cron UNIX
de base, dont une plus grande sécurité et des options de configuration
plus puissantes.

%description -l pl
cron to standardowy uniksowy program, który okresowo uruchamia
okre¶lone przez u¿ytkowników programy. vixie cron dodaje mo¿liwo¶ci
podstawowemu uniksowemu cronowi, w tym lepsze bezpieczeñstwo i
bogatsze opcje konfiguracyjne.

%description -l tr
cron UNIX'de standart olarak belirli zamanlarda bir programý
çalýþtýrmak için kullanýlan daemon'dur. Vixie cron, standart cron'dan
daha güvenlidir ve daha geliþmiþ yapýlandýrma seçenekleri içerir.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1

%build
%{__make} CC=%{__cc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/var/{log,spool/cron},%{_mandir}/pl/man{1,8}} \
	$RPM_BUILD_ROOT/etc/{rc.d/init.d,logrotate.d,sysconfig} \
	$RPM_BUILD_ROOT%{_sysconfdir}/cron.{d,hourly,daily,weekly,monthly}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	DESTMAN=$RPM_BUILD_ROOT%{_mandir}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/crond
install %{SOURCE2} $RPM_BUILD_ROOT/etc/logrotate.d/cron
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/cron
install %{SOURCE4} $RPM_BUILD_ROOT/etc/cron.d/crontab
install %{SOURCE5} $RPM_BUILD_ROOT%{_mandir}/pl/man1/crontab.1
install %{SOURCE6} $RPM_BUILD_ROOT%{_mandir}/pl/man8/cron.8

touch $RPM_BUILD_ROOT/var/log/cron

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add crond
if [ -f /var/lock/subsys/crond ]; then
	/etc/rc.d/init.d/crond restart >&2
else
	echo "Run \"/etc/rc.d/init.d/crond start\" to start cron daemon."
fi
touch /var/log/cron
chmod 600 /var/log/cron

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/crond ]; then
		/etc/rc.d/init.d/crond stop >&2
	fi
	/sbin/chkconfig --del crond
fi

%triggerpostun -- hc-cron
/sbin/chkconfig --del crond
/sbin/chkconfig --add crond

%files
%defattr(644,root,root,755)
%attr(0750,root,root) %dir %{_sysconfdir}/cron.*
/etc/cron.d/crontab
%attr(0754,root,root) /etc/rc.d/init.d/crond
%config /etc/logrotate.d/cron
%attr(0755,root,root) %{_sbindir}/crond
%attr(4755,root,root) %{_bindir}/crontab

%{_mandir}/man*/*
%lang(pl) %{_mandir}/pl/man*/*

%attr(0700,root,root) /var/spool/cron
%attr(0600,root,root) %ghost /var/log/cron
