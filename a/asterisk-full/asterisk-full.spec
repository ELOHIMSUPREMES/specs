Name: asterisk-full
Summary: Asterisk -- last stable version
Version: 4.0.2
Release: alt1
License: GPL
Group: System/Servers
BuildArch: noarch
Url: http://www.asterisk.org/

%package -n asterisk1.8-full
Summary: Asterisk 1.8 -- full package
Group: System/Servers
BuildArch: noarch
Conflicts: asterisk-full < %version-%release
Provides: asterisk-full = %version-%release
Requires: appliance-asterisk-office
Requires: asterisk1.8-complete
Requires: asterisk1.8-devel-doc
Requires: asterisk1.8-sources
Requires: asterisk1.8-chan_dongle
Requires: asterisk1.8-chan_ss7
Requires: asterisk1.8-app_konference

%description -n asterisk1.8-full
Asterisk 1.8 -- full package

%package -n asterisk11-full
Summary: Asterisk 11 -- full package
Group: System/Servers
BuildArch: noarch
Conflicts: asterisk-full < %version-%release
Requires: appliance-asterisk-office
Requires: asterisk11-sources
Requires: asterisk11-complete
Requires: asterisk11-chan_dongle

%description -n asterisk11-full
Asterisk 11 -- full package

%description
Asterisk -- last stable version

%files -n asterisk1.8-full

%files -n asterisk11-full

%changelog
* Fri Jul 05 2013 Denis Smirnov <mithraen@altlinux.ru> 4.0.2-alt1
- import asterisk11-full and asterisk1.8-full as subpackages
- remove asterisk-full virtual package

* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus

