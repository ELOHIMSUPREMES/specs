%define _altdata_dir %_datadir/alterator

Name: alterator-ports-access
Version: 0.0.3
Release: alt6
Packager: Packager: Andriy Stepanov <stanv@altlinux.ru>
BuildArch: noarch
Source:%name-%version.tar
Summary: alterator module to control ports access
License: %gpl2plus
Group: System/Configuration/Other
Requires: alterator >= 4.10-alt8 alterator-sh-functions >= 0.6-alt5 libshell >= 0.0.1-alt4 gettext
Requires: alterator-l10n >= 2.7-alt10
BuildPreReq: rpm-build-licenses
BuildPreReq: rpm-macros-alterator
BuildRequires: alterator
BuildArch: noarch

%description
Alterator module to control serial/USB ports access

%prep
%setup -q

%build
%make_build

%install
%makeinstall
%find_lang %name

%files -f %name.lang
%_altdata_dir/applications/*
%_altdata_dir/ui/*/*
%_alterator_backend3dir/*
%_altdata_dir/help/*/*
%_sysconfdir/rc.d/rc.serial
%_bindir/%name
/lib/udev/alterator-ports-access

%changelog
* Mon Sep 24 2012 Andriy Stepanov <stanv@altlinux.ru> 0.0.3-alt6
- Fix serial available ports list 2

* Mon Sep 24 2012 Andriy Stepanov <stanv@altlinux.ru> 0.0.3-alt5
- Fix serial available ports list

* Wed Sep 19 2012 Andriy Stepanov <stanv@altlinux.ru> 0.0.3-alt4
- Accepts bad words

* Wed Sep 19 2012 Andriy Stepanov <stanv@altlinux.ru> 0.0.3-alt3
- Add BuildRequires to alterator

* Wed Sep 19 2012 Andriy Stepanov <stanv@altlinux.ru> 0.0.3-alt2
- Fix spec, add rpm-macros-alterator

* Wed Sep 19 2012 Andriy Stepanov <stanv@altlinux.ru> 0.0.3-alt1
- Add serial field in known USB devices, add patch from ua2fgb.

* Fri Aug 31 2012 Andriy Stepanov <stanv@altlinux.ru> 0.0.2-alt1
- List devices, USB HID

* Tue Jul 31 2012 Andriy Stepanov <stanv@altlinux.ru> 0.0.1-alt1
- Initial build
