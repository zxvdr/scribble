Name:           scribble
Version:        0.3
Release:        1%{?dist}
Summary:        Daemon that sends log files to a Scribe log server

Group:          Development/Languages
License:        GPLv3+
URL:            https://github.com/zxvdr/scribble
Source0:        https://github.com/zxvdr/scribble/raw/master/scribble
Source1:        https://github.com/zxvdr/scribble/raw/master/scribble.init
Source2:        https://github.com/zxvdr/scribble/raw/master/logs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
Requires:       python-daemon
Requires:       scribe
Requires(post): chkconfig

%description
Scribble is a daemon that sends log files to a Scribe log server.

%install
rm -rf %{buildroot}
install -D -m 755 %{SOURCE0} %{buildroot}/%{_sbindir}/scribble
install -D -m 755 %{SOURCE1} %{buildroot}/%{_sysconfdir}/rc.d/init.d/scribble
install -D -m 644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/scribed/logs.conf

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/scribed/logs.conf
%{_sysconfdir}/rc.d/init.d/scribble
%{_sbindir}/scribble

%post
/sbin/chkconfig --add scribble

%preun
if [ $1 -eq 0 ] ; then
    /sbin/service scribble stop >/dev/null 2>&1
    /sbin/chkconfig --del scribble
fi

%changelog
* Fri May 27 2011 David Robinson <zxvdr.au@gmail.com> - 0.2-1
- New release

* Mon May 02 2011 David Robinson <zxvdr.au@gmail.com> - 0.1-1
- Initial build
