Name: sisu-inject
Version: 0.3.1
Summary: Sisu inject
License: EPL
Url: http://eclipse.org/sisu
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.eclipse.sisu:org.eclipse.sisu.inject) = 0.3.1
Provides: mvn(org.eclipse.sisu:org.eclipse.sisu.inject:pom:) = 0.3.1
Provides: mvn(org.eclipse.sisu:sisu-inject:pom:) = 0.3.1
Provides: sisu-inject = 1:0.3.1-2.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.ow2.asm:asm)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: sisu-inject-0.3.1-2.fc23.cpio

%description
This package contains Sisu inject.

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
* Tue Jan 19 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.3.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

