Summary:	Vixie cron daemon
Summary(de):	Vixie cron daemon 
Summary(fr):	Démon Vixie cron
Summary(pl):	Demon Vixie cron
Summary(tr):	Vixie cron süreci, periyodik program çalýþtýrma yeteneði
Name:		vixie-cron
Version:	3.0.1
Release:	28
Copyright:	distributable
Group:		Daemons
Group(pl):	Serwery
Source0:	ftp://ftp.vix.com/pub/vixie/%{name}-%{version}.tar.gz
Source1:	vixie-cron.init
Source2:	cron.log
Patch0:		vixie-cron-3.0.1-redhat.patch
Patch1:		vixie-cron-3.0.1-security.patch
Patch3:		vixie-cron-3.0.1-badsig.patch
Patch4:		vixie-cron-3.0.1-crontab.patch
Patch5:		vixie-cron-3.0.1-sigchld.patch
Patch6:		vixie-cron-3.0.1-sprintf.patch
Patch7:		vixie-cron-3.0.1-sigchld2.patch
Patch8:		vixie-cron-3.0.1-syscrondir.patch
Prereq:		/sbin/chkconfig
Buildroot:	/tmp/%{name}-%{version}-root

%description
cron is a standard UNIX program that runs user-specified programs at
periodic scheduled times. vixie cron adds a number of features to the basic
UNIX cron, including better security and more powerful configuration
options.

%description -l de
cron ist ein Standard-UNIX-Programm, das zu vorgegebenen Zeiten vom Benutzer
angegebene Programme ausführt. vixie cron weist mehr Funktionen auf als cron
aus UNIX, u.a. bessere Sicherheit und leistungsfähigere
Konfigurationsoptionen.

%description -l fr
cron est un des programmes UNIX standard qui permet à un utilisateur donné
de lancer des périodiquement des programmes selon un ordre planifié. vixie
cron ajoute de nombreuses fonctionnalités au cron UNIX de base, dont une
plus grande sécurité et des options de configuration plus puissantes.

%description -l pl
cron to standardowy uniksowy program, który okresowo uruchamia okre¶lone
przez u¿ytkowników programy. vixie cron dodaje mo¿liwo¶ci podstawowemu
uniksowemu cronowi, w tym lepsze bezpieczeñstwo i bogatsze opcje
konfiguracyjne.

%description -l tr
cron UNIX'de standart olarak belirli zamanlarda bir programý çalýþtýrmak
için kullanýlan daemon'dur. Vixie cron, standart cron'dan daha güvenlidir ve
daha geliþmiþ yapýlandýrma seçenekleri içerir.

%prep
%setup -q
%patch0 -p1 -b .norh
%patch1 -p1 -b .nomisc
%patch3 -p1 -b .badsig
%patch4 -p1 -b .crontabhole
%patch5 -p1 -b .sigchld
%patch6 -p1 -b .sprintf
%patch7 -p1 -b .sigchld
%patch8 -p1 -b .syscrondir

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_bindir},%{_mandir}/man{1,5,8}} \
	$RPM_BUILD_ROOT/var/spool/cron \
	$RPM_BUILD_ROOT/etc/{crontab.d,rc.d/init.d,logrotate.d}

install -s cron $RPM_BUILD_ROOT%{_sbindir}/crond
install -s crontab $RPM_BUILD_ROOT%{_bindir}
install crontab.1 $RPM_BUILD_ROOT%{_mandir}/man1
install crontab.5 $RPM_BUILD_ROOT%{_mandir}/man5
install cron.8 $RPM_BUILD_ROOT%{_mandir}/man8
install $RPM_SOURCE_DIR/vixie-cron.init $RPM_BUILD_ROOT/etc/rc.d/init.d/crond
install $RPM_SOURCE_DIR/cron.log $RPM_BUILD_ROOT/etc/logrotate.d/cron

echo ".so cron.8" >$RPM_BUILD_ROOT%{_mandir}/man8/crond.8

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add crond

%postun
if [ $1 = 0 ]; then 
    /sbin/chkconfig --del crond
fi

%triggerpostun -- hc-cron
/sbin/chkconfig --add crond

%files
%defattr(644,root,root,755)
%attr(0700,root,root) %{_sbindir}/crond
%attr(4755,root,root) %{_bindir}/crontab
%{_mandir}/man*/*
%attr(0700,root,root) /var/spool/cron
%dir /etc/crontab.d
%attr(0744,root,root) %config /etc/rc.d/init.d/crond
%config /etc/logrotate.d/cron
