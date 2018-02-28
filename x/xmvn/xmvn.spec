Name: xmvn
Version: 2.4.0
Summary: Local Extensions for Apache Maven
License: ASL 2.0
Url: http://mizdebsk.fedorapeople.org/xmvn
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: xmvn = 2.4.0-5.fc23
Requires: /bin/sh
Requires: maven
Requires: xmvn-api
Requires: xmvn-connector-aether
Requires: xmvn-core

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: xmvn-2.4.0-5.fc23.cpio

%description
This package provides extensions for Apache Maven that can be used to
manage system artifact repository and use it to resolve Maven
artifacts in offline mode, as well as Maven plugins to help with
creating RPM packages containing Maven artifacts.

# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none
%prep
cpio -idmu --quiet --no-absolute-filenames < %{SOURCE0}

%build
cpio --list < %{SOURCE0} | sed -e 's,^\.,,' > %name-list

%install
mkdir -p $RPM_BUILD_ROOT
for i in usr var etc; do
[ -d $i ] && mv $i $RPM_BUILD_ROOT/
done


%files -f %name-list

%changelog
* Tue Jan 19 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt4_4jpp7
- rebuild to update symlinks

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt3_4jpp7
- fixed bin
- nobootstrap build

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_5jpp7
- nobootstrap build

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu Mar 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

