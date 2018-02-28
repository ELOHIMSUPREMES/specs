Name: xmvn-connector-gradle
Version: 2.4.0
Summary: XMvn Connector for Gradle
License: ASL 2.0
Url: http://mizdebsk.fedorapeople.org/xmvn
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.fedoraproject.xmvn:xmvn-connector-gradle) = 2.4.0
Provides: mvn(org.fedoraproject.xmvn:xmvn-connector-gradle:pom:) = 2.4.0
Provides: xmvn-connector-gradle = 2.4.0-5.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.fedoraproject.xmvn:xmvn-api)
Requires: mvn(org.fedoraproject.xmvn:xmvn-launcher)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: xmvn-connector-gradle-2.4.0-5.fc23.cpio

%description
This package provides XMvn Connector for Gradle, which provides
integration of Gradle with XMvn.  It provides an adapter which allows
XMvn resolver to be used as Gradle resolver.

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
* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

