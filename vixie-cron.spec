Summary:     Vixie cron daemon
Summary(de): Vixie cron daemon 
Summary(fr): Démon Vixie cron
Summary(pl): Demon Vixie cron
Summary(tr): Vixie cron süreci, periyodik program çalýþtýrma yeteneði
Name:        vixie-cron
Version:     3.0.1
Release:     28
Copyright:   distributable
Group:       Daemons
Source0:     ftp://ftp.vix.com/pub/vixie/%{name}-%{version}.tar.gz
Source1:     vixie-cron.init
Source2:     cron.log
Patch0:      vixie-cron-3.0.1-redhat.patch
Patch1:      vixie-cron-3.0.1-security.patch
Patch3:      vixie-cron-3.0.1-badsig.patch
Patch4:      vixie-cron-3.0.1-crontab.patch
Patch5:      vixie-cron-3.0.1-sigchld.patch
Patch6:      vixie-cron-3.0.1-sprintf.patch
Patch7:      vixie-cron-3.0.1-sigchld2.patch
Patch8:      vixie-cron-3.0.1-syscrondir.patch
Prereq:      /sbin/chkconfig
Buildroot:   /tmp/%{name}-%{version}-root

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
install -d $RPM_BUILD_ROOT/usr/{sbin,bin,man/man{1,5,8}} \
	$RPM_BUILD_ROOT/var/spool/cron \
	$RPM_BUILD_ROOT/etc/{crontab.d,rc.d/init.d,logrotate.d}

install -s cron $RPM_BUILD_ROOT/usr/sbin/crond
install -s crontab $RPM_BUILD_ROOT/usr/bin
install crontab.1 $RPM_BUILD_ROOT/usr/man/man1
install crontab.5 $RPM_BUILD_ROOT/usr/man/man5
install cron.8 $RPM_BUILD_ROOT/usr/man/man8
install $RPM_SOURCE_DIR/vixie-cron.init $RPM_BUILD_ROOT/etc/rc.d/init.d/crond
install $RPM_SOURCE_DIR/cron.log $RPM_BUILD_ROOT/etc/logrotate.d/cron

echo ".so cron.8" >$RPM_BUILD_ROOT/usr/man/man8/crond.8

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
%defattr(644, root, root, 755)
%attr(0700, root, root) /usr/sbin/crond
%attr(4755, root, root) /usr/bin/crontab
%attr(0644, root,  man) /usr/man/man*/*
%attr(0700, root, root) /var/spool/cron
%dir /etc/crontab.d
%attr(0744, root, root) %config /etc/rc.d/init.d/crond
%config /etc/logrotate.d/cron

%changelog
* Thu Nov 12 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.0.1-28]
- added %triggerpostun -- hc-cron section (now vixie-cron is full
  alternative for hc-cron).

* Mon Sep 28 1998 Marcin 'Qrczak' Kowalczyk <qrczak@knm.org.pl>
  [3.0.1-27]
- use %{name} and %{version} macros,
- simplified /etc/rc.d/rc?.d/???crond stuff,
- added %setup -q parameter,
- `mkdir -p' replaced with more standard `install -d',
- added full %attr description in %files,
- /usr/sbin/crond permissions changed to 700,
- replaced symlink in man page with .so include,
- added pl translation,
- changed install procedure to allow building from non-root account,
- added patch that reads /etc/crontab.d/* in addition to /etc/crontab,
  simplifying automatic adding of cron jobs by packages.

* Wed Jun 10 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Wed Jun 10 1998 Jeff Johnson <jbj@redhat.com>
- reset SIGCHLD before grandchild execle (problem #732)

* Sat May 02 1998 Cristian Gafton <gafton@redhat.com>
- enhanced initscript

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Dec 11 1997 Cristian Gafton <gafton@redhat.com>
- added a patch to get rid of the dangerous sprintf() calls
- added BuildRoot and Prereq: /sbin/chkconfig

* Sun Nov 09 1997 Michael K. Johnson <johnsonm@redhat.com>
- fixed cron/crond dichotomy in init file.

* Wed Oct 29 1997 Donnie Barnes <djb@redhat.com>
- fixed bad init symlinks

* Thu Oct 23 1997 Erik Troan <ewt@redhat.com>
- force it to use SIGCHLD instead of defunct SIGCLD

* Mon Oct 20 1997 Erik Troan <ewt@redhat.com>
- updated for chkconfig
- added status, restart options to init script

* Tue Jun 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Wed Feb 19 1997 Erik Troan <ewt@redhat.com>
- Swhich conditional from "axp" to "alpha" 
