Url: http://www.altlinux.org/Appliances
Name: appliance-asterisk-gateway
Summary: Simple Asterisk gateway
BuildArch: noarch
Version: 4.0.2
Release: alt2
License: GPL
Group: System/Base

Requires: asterisk1.8
Requires: asterisk1.8-chan_dahdi
Requires: asterisk1.8-chan_sip
Requires: asterisk1.8-chan_iax2
Requires: alterator-asterisk-gateway
Requires: appliance-pbx-hardware

%description
%summary

%files

%changelog
* Sun Jun 16 2013 Denis Smirnov <mithraen@altlinux.ru> 4.0.2-alt2
- add Url tag

* Thu Apr 11 2013 Denis Smirnov <mithraen@altlinux.ru> 4.0.2-alt1
- use asterisk 1.8 

* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus

