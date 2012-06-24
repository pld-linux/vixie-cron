Summary:	Vixie cron daemon
Summary(de):	Vixie cron daemon 
Summary(fr):	D�mon Vixie cron
Summary(pl):	Demon Vixie cron
Summary(tr):	Vixie cron s�reci, periyodik program �al��t�rma yetene�i
Name:		vixie-cron
Version:	3.0.1
Release:	71
License:	distributable
Group:		Daemons
Group(cs):	D�moni
Group(da):	D�moner
Group(de):	Server
Group(es):	Servidores
Group(fr):	Serveurs
Group(is):	P�kar
Group(it):	Demoni
Group(ja):	�ǡ����
Group(no):	Daemoner
Group(pl):	Serwery
Group(pt):	Servidores
Group(ru):	������
Group(sl):	Stre�niki
Group(sv):	Demoner
Group(uk):	������
Source0:	ftp://ftp.vix.com/pub/vixie/%{name}-%{version}.tar.gz
Source1:	%{name}.init
Source2:	cron.logrotate
Source3:	cron.sysconfig
Source4:	%{name}.crontab
Source5:	%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-redhat.patch
Patch1:		%{name}-security.patch
Patch2:		%{name}-pl_man.patch
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
Patch20:	%{name}-noroot.patch
Patch21:	%{name}-allow_location.patch
Provides:	crontabs >= 1.7
Provides:	crondaemon
Obsoletes:	crontabs
Obsoletes:	crondaemon
Obsoletes:	hc-cron
Prereq:		rc-scripts
Prereq:		/sbin/chkconfig
Requires:	/bin/run-parts
Requires:	psmisc >= 20.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The vixie-cron package contains the Vixie version of cron. Cron is a
standard UNIX program that runs user-specified programs at periodic
scheduled times. Vixie cron adds a number of features to the basic
UNIX cron, including better security and more powerful configuration
options.

%description -l de
cron ist ein Standard-UNIX-Programm, das zu vorgegebenen Zeiten vom
Benutzer angegebene Programme ausf�hrt. vixie cron weist mehr
Funktionen auf als cron aus UNIX, u.a. bessere Sicherheit und
leistungsf�higere Konfigurationsoptionen.

%description -l fr
cron est un des programmes UNIX standard qui permet � un utilisateur
donn� de lancer des p�riodiquement des programmes selon un ordre
planifi�. vixie cron ajoute de nombreuses fonctionnalit�s au cron UNIX
de base, dont une plus grande s�curit� et des options de configuration
plus puissantes.

%description -l pl
cron to standardowy uniksowy program, kt�ry okresowo uruchamia
okre�lone przez u�ytkownik�w programy. vixie cron dodaje mo�liwo�ci
podstawowemu uniksowemu cronowi, w tym lepsze bezpiecze�stwo i
bogatsze opcje konfiguracyjne.

%description -l tr
cron UNIX'de standart olarak belirli zamanlarda bir program�
�al��t�rmak i�in kullan�lan daemon'dur. Vixie cron, standart cron'dan
daha g�venlidir ve daha geli�mi� yap�land�rma se�enekleri i�erir.

%prep
%setup -q -a5
%patch0 -p1
%patch1 -p1
%patch2 -p0
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
%patch20 -p1
%patch21 -p1

%build
%{__make} CC=%{__cc} RPM_OPT_FLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/var/{log,spool/cron},%{_mandir}} \
	$RPM_BUILD_ROOT/etc/{rc.d/init.d,logrotate.d,sysconfig} \
	$RPM_BUILD_ROOT%{_sysconfdir}/cron.{d,hourly,daily,weekly,monthly}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	DESTMAN=$RPM_BUILD_ROOT%{_mandir}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/crond
install %{SOURCE2} $RPM_BUILD_ROOT/etc/logrotate.d/cron
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/cron
install %{SOURCE4} $RPM_BUILD_ROOT/etc/cron.d/crontab

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

cat > $RPM_BUILD_ROOT/etc/cron.d/cron.allow << EOF
# hosts.allow   This file describes the names of the users which are
#               allowed to use the local cron daemon
root
EOF

cat > $RPM_BUILD_ROOT/etc/cron.d/cron.deny << EOF2
# hosts.deny    This file describes the names of the users which are
#               NOT allowed to use the local cron daemon
EOF2

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
%attr(0644,root,root) %config(noreplace) /etc/cron.d/crontab
%attr(0644,root,root) %config(noreplace,missingok) %verify(not md5 mtime size) /etc/cron.d/cron.allow
%attr(0644,root,root) %config(noreplace,missingok) %verify(not md5 mtime size) /etc/cron.d/cron.deny
%attr(0754,root,root) /etc/rc.d/init.d/crond
%config /etc/logrotate.d/cron
%attr(0755,root,root) %{_sbindir}/crond
%attr(4755,root,root) %{_bindir}/crontab

%{_mandir}/man*/*
%lang(fi) %{_mandir}/fi/man*/*
%lang(fr) %{_mandir}/fr/man*/*
%lang(id) %{_mandir}/id/man*/*
%lang(ja) %{_mandir}/ja/man*/*
%lang(ko) %{_mandir}/ko/man*/*
%lang(pl) %{_mandir}/pl/man*/*

%attr(0700,root,root) /var/spool/cron
%attr(0600,root,root) %ghost /var/log/cron
