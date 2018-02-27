%define rname	lightning-ru
%define cid	langpack-ru@lightning.mozilla.org
%define ciddir	%tbird_noarch_extensionsdir/%cid

Name:		thunderbird-%rname
Version:	2.6.2
Release:	alt2
Serial: 	1
Summary:	Russian (RU) Language Pack for Lightning
Packager:	Radik Usupov <radik@altlinux.org>

BuildArch: noarch

License:	GPL
Group:		Networking/Mail
URL:		http://www.mozilla.org/projects/calendar/lightning/

Source0:	lightning-ru-%version.xpi
Patch0:		max-versions.patch

BuildRequires(pre):	rpm-build-thunderbird 
BuildRequires:		unzip
Requires:   thunderbird-lightning

%description
The Mozilla Lightning in Russian.

%install
mkdir -p %buildroot/%ciddir
unzip -qq -d %buildroot/%ciddir %SOURCE0
cd %buildroot/%ciddir
patch -p2 < %PATCH0

%files
%ciddir

%changelog
* Fri Jan 31 2014 Andrey Cherepanov <cas@altlinux.org> 1:2.6.2-alt2
- Increase maxVersion for Thunderbird 24.3.x and Seamonkey 2.23.x support

* Wed Nov 06 2013 Andrey Cherepanov <cas@altlinux.org> 1:2.6.2-alt1
- New version

* Thu Dec 20 2012 Andrey Cherepanov <cas@altlinux.org> 1:1.0-alt3
- Update for thunderbird-lightning-17.0

* Thu Jun 21 2012 Andrey Cherepanov <cas@altlinux.org> 1:1.0-alt2
- Adapt for new version of Thunderbird

* Mon Feb 20 2012 Radik Usupov <radik@altlinux.org> 1:1.0-alt1
- New version (1.0)
- Drop old folders

* Sat Aug 27 2011 Radik Usupov <radik@altlinux.org> 1.0b5pre-alt2
- Rebuild from new version TB

* Mon Aug 01 2011 Radik Usupov <radik@altlinux.org> 1.0b5pre-alt1
- New version (1.0b5pre)

* Tue Feb 08 2011 Radik Usupov <radik@altlinux.org> 1.0b3pre-alt1
- Initial build (Closes: 24993)

